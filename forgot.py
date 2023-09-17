from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import os
import tkinter
from tkinter import messagebox
import mysql.connector

class Forgot:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("forgot password")

        self.bg=ImageTk.PhotoImage(file=r"Images\bg3.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0)

        frame=Frame(self.root,bd=2,background='#BCD4E6')
        frame.place(x=500,y=50,width=650,height=650)

        forgot = Image.open(r"Images\forgot.png")
        forgot = forgot.resize((80, 80), Image.LANCZOS)
        self.forgot_photoimg3 = ImageTk.PhotoImage(forgot)

        f_label2 = Label(frame, image=self.forgot_photoimg3, bg="#BCD4E6", borderwidth=0)
        f_label2.place(x=70, y=35, width=80, height=80)
        
        started=Label(frame,text="Forget Password",font=("times new roman",35,"bold"),fg="Green",bg="#BCD4E6")
        started.place(x=150,y=45)

        #username
        username_label=Label(frame,text="Username:",font=("times new roman",30,"bold"),fg="black",bg="#BCD4E6")
        username_label.place(x=10,y=125)

        self.username=ttk.Entry(frame,width=20,font=("times new roman",20,"bold"))
        self.username.place(x=360,y=130,width=270,height=40)

        #Security Question
        security_label=Label(frame,text="Security Question:",font=("times new roman",30,"bold"),fg="black",bg='#BCD4E6')
        security_label.place(x=10,y=200)

        self.security_combo=ttk.Combobox(frame,font=("times new roman",20," bold"),state="readonly",width=18,background="white")
        self.security_combo["values"]=("Select","Your Birth Place","Your Mother Name","Your Nickname","Your Petname")
        self.security_combo.current(0)
        self.security_combo.place(x=360,y=210,width=270,height=40)

        #Security Question Answer
        S_Q_A_label=Label(frame,text="Security Answer:",font=("times new roman",30,"bold"),bg='#BCD4E6',fg="black")
        S_Q_A_label.place(x=10,y=270)

        self.S_Q_A_entry=ttk.Entry(frame,width=20,font=("times new roman",20,"bold"),background='#BCD4E6',foreground="black")
        self.S_Q_A_entry.place(x=360,y=280,width=270,height=40)

        #Password
        password_label=Label(frame,text="Password:",font=("times new roman",30,"bold"),bg='#BCD4E6',fg="black")
        password_label.place(x=10,y=340)

        self.password_entry=ttk.Entry(frame,width=20,font=("times new roman",20,"bold"),foreground="black",background='#BCD4E6')
        self.password_entry.place(x=360,y=350,width=270,height=40)
        #Confirm Password
        Confirm_label=Label(frame,text="Confirm Password:",font=("times new roman",30,"bold"),bg='#BCD4E6',fg="black")
        Confirm_label.place(x=10,y=410)

        self.Confirm_entry=ttk.Entry(frame,width=20,font=("times new roman",20,"bold"),foreground="black",background='#BCD4E6')
        self.Confirm_entry.place(x=360,y=420,width=270,height=40)

        img = Image.open(r"Images\reset.png")
        img = img.resize((200, 80), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        reset_button = Button(frame, image=self.photoimg,command=self.forgot_pass,cursor="hand2", borderwidth=0,
                                 bg='#bcd4e6', activebackground='#bcd4e6')
        reset_button.place(x=200, y=500)


    def forgot_pass(self):
        if self.username.get() == "":
            messagebox.showerror("Error","Please enter email address to reset password",parent=self.root)
        elif self.security_combo.get() == "Select":
            messagebox.showerror("Error", "Please Select Security Question",parent=self.root)
        elif self.S_Q_A_entry.get() == "":
            messagebox.showerror("Error", "Please Answer Security Question",parent=self.root)
        elif self.password_entry.get() == "":
            messagebox.showerror("Error", "Please Enter Password",parent=self.root)
        elif self.Confirm_entry.get() == "":
            messagebox.showerror("Error", "Please Enter Confirm Password",parent=self.root)
        elif self.Confirm_entry.get() != self.password_entry.get():
            messagebox.showerror("Error", "Entered Password and Confirm Password need to be same",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Nikhil@9664",
                                           database="project")
            my_cursor = conn.cursor()
            query = ("select * from student_registerdata where email=%s and securityq=%s and securitya=%s")
            value = (self.username.get(),self.security_combo.get(),self.S_Q_A_entry.get())
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error","Invalid Username or question and answer",parent=self.root)
            else:
                query1 = 'update student_registerdata set password=%s where email=%s'
                value1 = (self.password_entry.get(),self.username.get(),)
                my_cursor.execute(query1, value1)

                messagebox.showinfo("Success","Your password has been reset,please login new password")
                conn.commit()
                conn.close()




if __name__ == "__main__":
    root=Tk()
    obj=Forgot(root)
    root.mainloop()

