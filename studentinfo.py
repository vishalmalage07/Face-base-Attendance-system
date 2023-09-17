from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Personal:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recogniton System")

        # =======================Variables Declaration============================
        self.var_StudentID = StringVar()
        self.var_StudentName = StringVar()
        self.var_Roll = StringVar()
        self.var_Gender = StringVar()
        self.var_DOB = StringVar()
        self.var_Email = StringVar()
        self.var_Phone = StringVar()
        self.var_Address = StringVar()
        self.var_Teacher = StringVar()
        self.var_Department = StringVar()
        self.var_Semester = StringVar()
        self.var_Year = StringVar()
        self.var_AcademicYear = StringVar()
        self.var_radio1 = StringVar()

        # first image
        img = Image.open(r"D:\clgproject\web\student.png")
        img = img.resize((600, 120), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        first_label = Label(self.root, image=self.photoimg)
        first_label.place(x=0, y=0, width=600, height=120)

        # Second Image
        img1 = Image.open(r"D:\clgproject\web\student1.png")
        img1 = img1.resize((300, 120), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        first_label = Label(self.root, image=self.photoimg1)
        first_label.place(x=600, y=0, width=300, height=120)

        # Third Image
        img2 = Image.open(r"D:\clgproject\web\students.jpg")
        img2 = img2.resize((700, 120), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        first_label = Label(self.root, image=self.photoimg2)
        first_label.place(x=900, y=0, width=700, height=120)

        # Bg Image
        img3 = Image.open(r"D:\clgproject\web\bg.jpg")
        img3 = img3.resize((1550, 720), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=120, width=1540, height=720)

        title_lbl = Label(bg_img, text="Student Information", font=("Bebas Neue", 35, "bold"), bg="white", fg="Green")
        title_lbl.place(x=0, y=0, width=1540, height=45)

        # Frame
        main_frame = Frame(bg_img, bd=2, bg="#0ABAB5")
        main_frame.place(x=40, y=60, width=1450, height=652)

        # Main label frame
        main_frame = LabelFrame(main_frame, bd=2, bg="white", borderwidth=6, relief=GROOVE, text=" Student Details",
                                font=("times new roman", 12, "bold"))
        main_frame.place(x=10, y=10, width=1430, height=630)

        img_main = Image.open(r"D:\clgproject\web\book.jpg")
        img_main = img_main.resize((1380, 200), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_main)

        f_label = Label(main_frame, image=self.photoimg_left)
        f_label.place(x=5, y=0, width=1380, height=200)

        # Current Course
        current_course_frame = LabelFrame(main_frame, bd=2, bg="white", borderwidth=4, relief=GROOVE,
                                          text=" Current Course", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=700, y=200, width=687, height=150)

        # Department
        dep_label = Label(current_course_frame, text="Department", font=("times new roman", 12, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_Department,
                                 font=("times new roman", 12, " bold"), state="read only")
        dep_combo["values"] = ("Select Department", "CSE", "Civil", "Mechanical", "E&TC", "AI")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Course
        course_label = Label(current_course_frame, text="Year", font=("times new roman", 12, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_Year,
                                    font=("times new roman", 12, " bold"), state="read only")
        course_combo["values"] = ("Select Year of Study", "FE", "SE", "TE", "BE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year
        Sem_label = Label(current_course_frame, text="Academic Year", font=("times new roman", 12, "bold"), bg="white")
        Sem_label.grid(row=1, column=0, padx=10, sticky=W)

        sem_combo = ttk.Combobox(current_course_frame, textvariable=self.var_AcademicYear,
                                 font=("times new roman", 12, " bold"), state="read only")
        sem_combo["values"] = ("Select Year", "20-21", "21-22", "22-23")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semester
        Sem_label = Label(current_course_frame, text="Semester", font=("times new roman", 12, "bold"), bg="white")
        Sem_label.grid(row=1, column=2, padx=10, sticky=W)

        sem_combo = ttk.Combobox(current_course_frame, textvariable=self.var_Semester,
                                 font=("times new roman", 12, " bold"), state="read only")
        sem_combo["values"] = ("Select Semester", "Sem-1", "Sem-2")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        table_frame = LabelFrame(main_frame, bd=2, bg="white", borderwidth=4, relief=GROOVE)
        table_frame.place(x=700, y=350, width=687, height=130)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=(
            "id", "name", "roll", "gender", "DOB", "Email", "phone", "address", "teacher", "Department", "sem", "year",
            "course", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("id", text="StudentId")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("roll", text="Roll")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("DOB", text="DOB")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("Department", text="Department")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("course", text="Academic_Year")
        self.student_table.heading("photo", text="PhotoSample  ")
        self.student_table["show"] = "headings"

        self.student_table.column("id", width=90)
        self.student_table.column("name", width=90)
        self.student_table.column("roll", width=90)
        self.student_table.column("gender", width=90)
        self.student_table.column("DOB", width=90)
        self.student_table.column("Email", width=90)
        self.student_table.column("phone", width=90)
        self.student_table.column("address", width=90)
        self.student_table.column("teacher", width=90)
        self.student_table.column("Department", width=90)
        self.student_table.column("course", width=90)
        self.student_table.column("year", width=90)
        self.student_table.column("sem", width=90)
        self.student_table.column("photo", width=90)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.cursor)
        self.fetch_data()

        # class Student info
        class_student_frame = LabelFrame(main_frame, bd=2, bg="white", relief=GROOVE, text="Class Student information",
                                         borderwidth=4, font=("times new roman", 12, "bold"))
        class_student_frame.place(x=5, y=200, width=687, height=280)

        # Student id
        studentID_label = Label(class_student_frame, text="StudentID", font=("times new roman", 12, "bold"), bg="white")
        studentID_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        studentID_entry = ttk.Entry(class_student_frame, textvariable=self.var_StudentID, width=20,
                                    font=("times new roman", 12, "bold"))
        studentID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Student name
        studentname_label = Label(class_student_frame, text="Student Name", font=("times new roman", 12, "bold"),
                                  bg="white")
        studentname_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        studentname_entry = ttk.Entry(class_student_frame, textvariable=self.var_StudentName, width=20,
                                      font=("times new roman", 12, "bold"))
        studentname_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Roll No
        roll_no_label = Label(class_student_frame, text="Roll No", font=("times new roman", 12, "bold"), bg="white")
        roll_no_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        roll_no_entry = ttk.Entry(class_student_frame, textvariable=self.var_Roll, width=20,
                                  font=("times new roman", 12, "bold"))
        roll_no_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Gender
        gender_label = Label(class_student_frame, text="Gender", font=("times new roman", 12, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_Gender,
                                    font=("times new roman", 12, " bold"), state="read only", width=18)
        gender_combo["values"] = ("Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=10, sticky=W)

        # DOB
        dob_label = Label(class_student_frame, text="DOB", font=("times new roman", 12, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        dob_entry = ttk.Entry(class_student_frame, textvariable=self.var_DOB, width=20,
                              font=("times new roman", 12, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Email
        email_label = Label(class_student_frame, text="Email", font=("times new roman", 12, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(class_student_frame, textvariable=self.var_Email, width=20,
                                font=("times new roman", 12, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Phone No
        Phone_no_label = Label(class_student_frame, text="Phone No", font=("times new roman", 12, "bold"), bg="white")
        Phone_no_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        Phone_no_entry = ttk.Entry(class_student_frame, textvariable=self.var_Phone, width=20,
                                   font=("times new roman", 12, "bold"))
        Phone_no_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Address
        address_label = Label(class_student_frame, text="Address", font=("times new roman", 12, "bold"), bg="white")
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        address_entry = ttk.Entry(class_student_frame, textvariable=self.var_Address, width=20,
                                  font=("times new roman", 12, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Teacher
        TeacherName_label = Label(class_student_frame, text="Class Teacher ", font=("times new roman", 12, "bold"),
                                  bg="white")
        TeacherName_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        TeacherName_entry = ttk.Entry(class_student_frame, textvariable=self.var_Teacher, width=20,
                                      font=("times new roman", 12, "bold"))
        TeacherName_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        # radio Buttons

        radiobutton1 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="Take Photo Sample Now",
                                       value="YES")
        radiobutton1.grid(row=6, column=0)

        radiobutton2 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="Take Photo Sample Later",
                                       value="NO")
        radiobutton2.grid(row=6, column=1)

        # Button Frame
        button_frame = Frame(main_frame, bd=2, borderwidth=4, relief=GROOVE, bg="white")
        button_frame.place(x=5, y=480, width=1380, height=40)

        save_button = Button(button_frame, text="Save", command=self.add_data, width=75, cursor="hand2",
                             font=("times new roman", 12, "bold"), bg="black", fg="White")
        save_button.grid(row=0, column=0)

        Reset_button = Button(button_frame, text="Reset", width=75, command=self.reset_data, cursor="hand2",
                              font=("times new roman", 12, "bold"), bg="black", fg="White")
        Reset_button.grid(row=0, column=3)

        # Second Button Frame
        button2_frame = Frame(main_frame, bd=2, borderwidth=4, relief=GROOVE, bg="white")
        button2_frame.place(x=5, y=520, width=1380, height=40)

        Take_Photo_button = Button(button2_frame, text="Take Photo Sample", command=self.generate_data, width=75,
                                   cursor="hand2", font=("times new roman", 12, "bold"), bg="black", fg="White")
        Take_Photo_button.grid(row=0, column=0)

        Update_Photo_button = Button(button2_frame, text="Update Photo", width=75, cursor="hand2",
                                     font=("times new roman", 12, "bold"), bg="black", fg="White")
        Update_Photo_button.grid(row=0, column=1)

    # ===========================================function declaration=======================================

    def add_data(self):
        if self.var_StudentID.get() == "" or self.var_Department.get() == "Select Department" or self.var_Semester.get() == "Select Semester" or self.var_Address.get() == "" or self.var_Roll.get() == "" or self.var_StudentName.get() == "" or self.var_Teacher.get() == "" or self.var_DOB.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Nikhil@9664",
                                               database="project")
                my_cursur = conn.cursor()
                my_cursur.execute("insert into studentinfo values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_StudentID.get(),
                    self.var_StudentName.get(),
                    self.var_Roll.get(),
                    self.var_Gender.get(),
                    self.var_DOB.get(),
                    self.var_Email.get(),
                    self.var_Phone.get(),
                    self.var_Address.get(),
                    self.var_Teacher.get(),
                    self.var_Department.get(),
                    self.var_Year.get(),
                    self.var_AcademicYear.get(),
                    self.var_Semester.get(),
                    self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Details have added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    # ==================Reset Function==================
    def reset_data(self):
        self.var_StudentID.set(""),
        self.var_StudentName.set(""),
        self.var_Roll.set(""),
        self.var_Gender.set("Male"),
        self.var_DOB.set(""),
        self.var_Email.set(""),
        self.var_Phone.set(""),
        self.var_Address.set(""),
        self.var_Teacher.set(""),
        self.var_Department.set("Select Department"),
        self.var_Year.set("Select Year of Study"),
        self.var_AcademicYear.set("Select Year"),
        self.var_Semester.set("Select Semester"),
        self.var_radio1.set("")

    # ===========================Fetch Data===============================

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Nikhil@9664",
                                       database="project")
        my_cursur = conn.cursor()
        my_cursur.execute("Select * from studentinfo")
        data = my_cursur.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit
        conn.close

    # =============================Cursor=============
    def cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_StudentID.set(data[0]),
        self.var_StudentName.set(data[1]),
        self.var_Roll.set(data[2]),
        self.var_Gender.set(data[3]),
        self.var_DOB.set(data[4]),
        self.var_Email.set(data[5]),
        self.var_Phone.set(data[6]),
        self.var_Address.set(data[7]),
        self.var_Teacher.set(data[8]),
        self.var_Department.set(data[9]),
        self.var_AcademicYear.set(data[10]),
        self.var_Year.set(data[11]),
        self.var_Semester.set(data[12]),
        self.var_radio1.set(data[13])

    # ===========================Generate data set====================================
    def generate_data(self):
        if self.var_StudentID.get() == "" or self.var_Department.get() == "Select Department" or self.var_Semester.get() == "Select Semester" or self.var_Address.get() == "" or self.var_Roll.get() == "" or self.var_StudentName.get() == "" or self.var_Teacher.get() == "" or self.var_DOB.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Nikhil@9664",
                                               database="project")
                my_cursur = conn.cursor()
                my_cursur.execute("select * from studentinfo")
                myresult = my_cursur.fetchall()
                id = 0
                id1 = self.var_StudentID.get()
                for x in myresult:
                    id += 1
                my_cursur.execute(
                    "update studentinfo set Student_Name=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Department=%s,Year=%s,Academic_Year=%s,Semester=%s,Photosample=%s where Student_ID=%s",
                    (
                        self.var_StudentName.get(),
                        self.var_Roll.get(),
                        self.var_Gender.get(),
                        self.var_DOB.get(),
                        self.var_Email.get(),
                        self.var_Phone.get(),
                        self.var_Address.get(),
                        self.var_Teacher.get(),
                        self.var_Department.get(),
                        self.var_Year.get(),
                        self.var_AcademicYear.get(),
                        self.var_Semester.get(),
                        self.var_radio1.get(),
                        self.var_StudentID.get()
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ====================Load Predefined Data========================

                cap = cv2.VideoCapture(0)
                while True:
                    ret, pic_frame = cap.read()
                    file_name = "Stud_data/" + str(id1) + ".jpg"
                    cv2.imwrite(file_name, pic_frame)
                    cv2.imshow("Cropped Face", pic_frame)

                    if cv2.waitKey(1) == 13:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data sets completed!!!!")

            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Personal(root)
    root.mainloop()
