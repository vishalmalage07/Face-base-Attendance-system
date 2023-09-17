import pickle
import sys
from tkinter import *
from tkinter import ttk, messagebox

import cv2
from PIL import Image, ImageTk
import os
import face_recognition
import tkinter
from tkinter.messagebox import askyesno
from subprocess import call
from cvzone import cornerRect

from studentinfo import Personal

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recogniton System")

        # first image
        img = Image.open(r"D:\clgproject\web\face3.png")
        img = img.resize((600, 120), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        first_label = Label(self.root, image=self.photoimg)
        first_label.place(x=0, y=0, width=600, height=120)

        # Second Image
        img1 = Image.open(r"D:\clgproject\web\face2.png")
        img1 = img1.resize((300, 120), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        first_label = Label(self.root, image=self.photoimg1)
        first_label.place(x=600, y=0, width=300, height=120)

        # Third Image
        img2 = Image.open(r"D:\clgproject\web\college.png")
        img2 = img2.resize((700, 120), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        first_label = Label(self.root, image=self.photoimg2)
        first_label.place(x=900, y=0, width=700, height=120)

        # Bg Image
        img3 = Image.open(r"D:\clgproject\web\bg.jpg")
        img3 = img3.resize((1550, 720), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=120, width=1550, height=720)

        title_lbl = Label(bg_img, text="Face Recognition Based Attendance System", font=("Bebas Neue", 35, "bold"),
                          bg="lightblue", fg="red")
        title_lbl.place(x=0, y=0, width=1550, height=45)

        # student button
        img4 = Image.open(r"D:\clgproject\web\info.png")
        img4 = img4.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Label(bg_img, image=self.photoimg4, cursor="hand2", )
        b1.place(x=100, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Student Info", cursor="hand2", command=self.info, font=("Bebas Neue", 15, "bold"), bg="blue",
                      fg="white")
        b1_1.place(x=100, y=300, width=220, height=40)

        # Identifying button
        img9 = Image.open(r"D:\clgproject\web\facer.png")
        img9 = img9.resize((220, 200), Image.Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        b2 = Label(bg_img, image=self.photoimg9, cursor="hand2")
        b2.place(x=450, y=100, width=220, height=200)

        b2_1 = Button(bg_img, text="Train Data", command=self.train, cursor="hand2", font=("Bebas Neue", 15, "bold"), bg="blue",
                      fg="white")
        b2_1.place(x=450, y=300, width=220, height=40)

        # Attendance button
        img5 = Image.open(r"D:\clgproject\web\attendance.png")
        img5 = img5.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b3 = Label(bg_img, image=self.photoimg5, cursor="hand2")
        b3.place(x=800, y=100, width=220, height=220)

        b3_1 = Button(bg_img, text="Attendance", cursor="hand2", command=self.open, font=("Bebas Neue", 15, "bold"), bg="blue", fg="white")
        b3_1.place(x=800, y=300, width=220, height=40)

        # # Photo button
        # img6 = Image.open(r"D:\clgproject\web\photo.png")
        # img6 = img6.resize((220, 220), Image.Resampling.LANCZOS)
        # self.photoimg6 = ImageTk.PhotoImage(img6)
        #
        # b1 = Label(bg_img, image=self.photoimg6, cursor="hand2")
        # b1.place(x=600, y=380, width=220, height=220)
        #
        # b1_1 = Button(bg_img, text="Photos", cursor="hand2", command=self.open_photo, font=("Bebas Neue", 15, "bold"), bg="blue", fg="white")
        # b1_1.place(x=600, y=580, width=220, height=40)
        #
        # # Help Desk button
        # img7 = Image.open(r"D:\clgproject\web\help.png")
        # img7 = img7.resize((220, 220), Image.Resampling.LANCZOS)
        # self.photoimg7 = ImageTk.PhotoImage(img7)
        #
        # b1 = Label(bg_img, image=self.photoimg7, cursor="hand2")
        # b1.place(x=1100, y=100, width=220, height=220)
        #
        # b1_1 = Button(bg_img, text="Help Desk", cursor="hand2", font=("Bebas Neue", 15, "bold"), bg="blue", fg="white")
        # b1_1.place(x=1100, y=300, width=220, height=40)

        #  Exit button
        img8 = Image.open(r"D:\clgproject\web\exit.png")
        img8 = img8.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b4 = Label(bg_img, image=self.photoimg8, cursor="hand2")
        b4.place(x=1150, y=100, width=220, height=220)

        b4_1 = Button(bg_img, text="Exit", command=self.exit, cursor="hand2", font=("Bebas Neue", 15, "bold"), bg="blue", fg="white")
        b4_1.place(x=1150, y=300, width=220, height=40)



    # ================================ Function Button=====================================
    def exit(self):
        self.root.destroy()


    def info(self):
        self.new_window=Toplevel(self.root)
        self.app=Personal(self.new_window)

    def train(self):
        import cv2
        import face_recognition
        import pickle
        import os

        def find_encodings(images_list):
            encodings_list = []
            for img in images_list:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                face_locations = face_recognition.face_locations(img)
                if len(face_locations) > 0:
                    encode = face_recognition.face_encodings(img, face_locations)[0]
                    encodings_list.append(encode)
            return encodings_list

        folder_path = 'Stud_data'
        path_list = os.listdir(folder_path)
        print(path_list)

        image_list = []
        student_ids = []

        for path in path_list:
            image_list.append(cv2.imread(os.path.join(folder_path, path)))
            student_ids.append(os.path.splitext(path)[0])

        print(student_ids)

        print("Encoding started............")
        encodings_known = find_encodings(image_list)
        encodings_known_with_ids = [encodings_known, student_ids]
        print("Encoding ended...........")

        file_path = "Encode.xml"
        with open(file_path, 'wb') as file:
            pickle.dump(encodings_known_with_ids, file)

        print("File saved: " + file_path)
        messagebox.showinfo("Success", "Trained Your Data successfully", parent=self.root)

    def open(self):
        try:
            # Execute the 'testing.py' script
            call([sys.executable, 'testing.py'])
        except Exception as e:
            messagebox.showerror("Error", str(e), parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
