import pickle
from cvzone import cornerRect
import numpy as np
import cv2
import os
import face_recognition
from datetime import datetime, date
import csv
import mysql.connector
import time
from tkinter import messagebox

# Constants
CAPTURE_WIDTH = 640
CAPTURE_HEIGHT = 480
MODE_FOLDER_PATH = 'Resources/Modes'
BACKGROUND_IMAGE_PATH = 'Resources/background.png'
ENCODE_FILE_PATH = 'Encode.xml'
DATABASE_HOST = "localhost"
DATABASE_USERNAME = "root"
DATABASE_PASSWORD = "Nikhil@9664"
DATABASE_NAME = "project"
ATTENDANCE_CSV_FILENAME = f"{date.today()}.csv"
FACE_DETECTION_TIMEOUT = 5  # Adjust the timeout duration as needed (in seconds)

# Initialize capture
cap = cv2.VideoCapture(0)
cap.set(3, CAPTURE_WIDTH)
cap.set(4, CAPTURE_HEIGHT)

# Load background image
imgbg = cv2.imread(BACKGROUND_IMAGE_PATH)

# Load mode images
imgmode = [cv2.imread(os.path.join(MODE_FOLDER_PATH, path)) for path in os.listdir(MODE_FOLDER_PATH)]
modtype = 1

# Load known face encodings and student IDs
with open(ENCODE_FILE_PATH, 'rb') as file:
    encodelistknownwithIds = pickle.load(file)

encodelistknown, studentIds = encodelistknownwithIds

# Get current date and time
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")
current_time = now.strftime("%H:%M:%S")

# Create a connection to the database
try:
    conn = mysql.connector.connect(
        host=DATABASE_HOST,
        username=DATABASE_USERNAME,
        password=DATABASE_PASSWORD,
        database=DATABASE_NAME
    )
    my_cursor = conn.cursor()
except mysql.connector.Error as e:
    print(f"Database connection error: {e}")
    exit(1)

# Create a CSV file with the current date in the filename
csv_filename = ATTENDANCE_CSV_FILENAME

# Set to keep track of processed student IDs
processed_ids = set()

# Set to keep track of unidentified faces
unidentified_faces = set()

# Variables for motion detection and face detection timeout
last_frame = None
motion_detected = False
motion_start_time = None
last_face_detected_time = time.time()

# Function to handle duplicate entry
def handle_duplicate_entry():
    """
        Handle duplicate entry in the attendance record.
        Sets the mode to 3 (duplicate entry).
        """
    global modtype
    modtype = 3

# Function to insert attendance record
def insert_attendance_record(student_id, student_name, roll_number, department):
    """
        Insert the attendance record into the database and CSV file.
        """
    try:
        global modtype
        # Insert record into the database
        my_cursor.execute(
            "INSERT INTO attendance (date, student_id, student_name, roll, department, time) "
            "VALUES (%s, %s, %s, %s, %s, %s)",
            (current_date, student_id, student_name, roll_number, department, current_time))
        conn.commit()
        # Append record to the CSV file
        with open(csv_filename, mode="a", newline="") as file:
            fieldnames = ["Date", "Student ID", "Student Name", "Roll Number", "Department", "Time"]
            attendance = csv.DictWriter(file, fieldnames=fieldnames)
            attendance.writerow({
                "Date": current_date,
                "Student ID": student_id,
                "Student Name": student_name,
                "Roll Number": roll_number,
                "Department": department,
                "Time": current_time
            })
    except mysql.connector.Error as e:
        print(f"Error inserting attendance record: {e}")
        messagebox.showerror("Database Error", "Failed to insert attendance record. Please try again.")

while True:
    # Read frame from the camera
    success, img = cap.read()


    # Resize the frame and convert to RGB
    imgs = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgs = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Perform face detection on the frame
    faceframe = face_recognition.face_locations(imgs)
    encodecurframe = face_recognition.face_encodings(imgs, faceframe)

    # Update the background image with the current frame
    imgbg[162:162 + 480, 55:55 + 640] = img
    imgbg[44:44 + 633, 808:808 + 414] = imgmode[modtype]

    # Convert current frame to grayscale for motion detection
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if last_frame is None:
        last_frame = gray
        continue

    frame_delta = cv2.absdiff(last_frame, gray)
    thresh = cv2.threshold(frame_delta, 30, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)
    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    motion_detected = False

    for contour in contours:
        if cv2.contourArea(contour) < 500:
            continue
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        motion_detected = True

    if motion_detected:
        motion_start_time = time.time()

    if motion_start_time is not None and time.time() - motion_start_time >= FACE_DETECTION_TIMEOUT:
        modtype = 1  # Reset mode to normal when face detection timeout occurs

    if time.time() - last_face_detected_time >= FACE_DETECTION_TIMEOUT:
        modtype = 1  # Reset mode to normal when no face is detected for a certain period of time

    if modtype == 1:  # Normal mode, perform face recognition
        for encodeface, faceloc in zip(encodecurframe, faceframe):
            match = face_recognition.compare_faces(encodelistknown, encodeface)
            facedis = face_recognition.face_distance(encodelistknown, encodeface)

            matchindex = np.argmin(facedis)
            if match[matchindex]:
                St_id = studentIds[matchindex]
                if St_id not in processed_ids:
                    y1, x2, y2, x1 = faceloc
                    bbox = 55 + x1, 162 + y1, x2 - x1, y2 - y1
                    imgbg = cornerRect(imgbg, bbox, rt=0)

                    my_cursor.execute("SELECT student_Name FROM studentinfo WHERE student_ID=%s", (str(St_id),))
                    n = my_cursor.fetchone()
                    na = str(n)
                    n = "".join(n)

                    my_cursor.execute("SELECT Roll FROM studentinfo WHERE student_ID=%s", (str(St_id),))
                    r = my_cursor.fetchone()
                    ro = str(r)
                    r = "".join(r)

                    my_cursor.execute("SELECT Department FROM studentinfo WHERE student_ID=%s", (str(St_id),))
                    d = my_cursor.fetchone()
                    dept = str(d)
                    d = "".join(d)

                    my_cursor.execute("SELECT * FROM attendance WHERE date=%s AND student_id=%s",
                                      (str(current_date), str(St_id)))
                    row = my_cursor.fetchall()

                    if len(row) == 0:
                        insert_attendance_record(St_id, n, r, d)
                    else:
                        handle_duplicate_entry()

                    processed_ids.add(St_id)
                    last_face_detected_time = time.time()
            else:
                unidentified_faces.add(tuple(faceloc))  # Add unidentified face location to set
    else:
        # Custom mode handling goes here (if any)
        pass

    # Set mode to 4 if unidentified faces are found
    if modtype != 4 and len(unidentified_faces) > 0:
        modtype = 5

    # Draw rectangles around unidentified faces in mode 4
    if modtype == 5:
        for face_loc in unidentified_faces:
            y1, x2, y2, x1 = face_loc
            bbox = 55 + x1, 162 + y1, x2 - x1, y2 - y1
            imgbg = cornerRect(imgbg, bbox, rt=0)
            break

    cv2.imshow('Webcam', imgbg)
    cv2.waitKey(1)
