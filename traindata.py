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
