from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import os
import tkinter
from tkinter import messagebox
import mysql.connector
from main import Face_Recognition_System


class Login:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Login Page")

        self.bg=ImageTk.PhotoImage(file=r"web\bg3.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relheight=1,relwidth=1)

        student_frame=Frame(self.root,bd=2,bg="black")
        student_frame.place(x=500,y=100,width=450,height=600)

        student_img1=Image.open(r"web\login.png")
        student_img1=student_img1.resize((120,120),Image.LANCZOS)
        self.student_photoimg1=ImageTk.PhotoImage(student_img1)

        f_label=Label(self.root,image=self.student_photoimg1,bg="black",borderwidth=0)
        f_label.place(x=650,y=105,width=120,height=120)

        started=Label(student_frame,text="Student Log In",font=("times new roman",30,"bold"),fg="red",bg="Black")
        started.place(x=90,y=115)

        def show():
            hide_button=Button(self.root,image=student_hide_pass,command=hide,bd=0,relief=FLAT,background="white",activebackground="white")
            hide_button.place(x=805,y=413)
            self.password.config(show='*')

        def hide():
            show_button=Button(self.root,image=student_show_pass,cursor="hand2",command=show,bd=0,relief=FLAT,background="white",activebackground="white")
            show_button.place(x=805,y=413)
            self.password.config(show='')


        student_show_pass=ImageTk.PhotoImage(file=r"web\eye.jpg")
        student_hide_pass=ImageTk.PhotoImage(file=r"web\hide.jpg")
        
        #username
        username_label=Label(student_frame,text="Username:",font=("times new roman",30,"bold"),fg="White",bg="Black")
        username_label.place(x=95,y=170)

        self.username=ttk.Entry(student_frame,width=20,font=("times new roman",20,"bold"))
        self.username.place(x=70,y=220,width=300,height=40)

        password_label=Label(student_frame,text="Password:",font=("times new roman",30,"bold"),fg="White",bg="Black")
        password_label.place(x=95,y=260)

        self.password=ttk.Entry(student_frame,width=20,font=("times new roman",20,"bold"),show="*")
        self.password.place(x=70,y=310,width=300,height=40)

        hide_button=Button(self.root,image=student_hide_pass,cursor="hand2",command=hide,bd=0,relief=FLAT,background="white",activebackground="white")
        hide_button.place(x=805,y=413)

        student_img2=Image.open(r"web\user.png")
        student_img2=student_img2.resize((40,40),Image.LANCZOS)
        self.student_photoimg2=ImageTk.PhotoImage(student_img2)

        f_label1=Label(self.root,image=self.student_photoimg2,bg="black",borderwidth=0)
        f_label1.place(x=560,y=278,width=40,height=40)

        student_img3=Image.open(r"web\lock.png")
        student_img3=student_img3.resize((40,40),Image.LANCZOS)
        self.student_photoimg3=ImageTk.PhotoImage(student_img3)

        f_label2=Label(self.root,image=self.student_photoimg3,bg="black",borderwidth=0)
        f_label2.place(x=560,y=368,width=40,height=40)

        #buttons
        forget_button=Label(self.root,text="Forget Password?",width=65,cursor="hand2",font=("times new roman",12,"bold"),borderwidth=0,relief=RIDGE,bg="black",fg="blue")
        forget_button.place(x=575,y=465,width=120,height=25)

        login_button=Button(self.root,text="Login",width=75,cursor="hand2",command=self.login,font=("times new roman",12,"bold"),bd=5,relief=RIDGE,bg="red",fg="White",activeforeground="white",activebackground="red")
        login_button.place(x=670,y=500,width=120,height=40)

        new_label=Label(self.root,text="not register yet,",width=75,font=("times new roman",13,"bold"),borderwidth=0,relief=RIDGE,bg="black",fg="White")
        new_label.place(x=575,y=550,width=120,height=25)

        signup_label=Button(self.root,text="Sign up",width=65,cursor="hand2",font=("times new roman",13,"bold"),borderwidth=0, command=self.register_window,activebackground='black', activeforeground='blue',relief=RIDGE,bg="black",fg="blue")
        signup_label.place(x=695,y=550,width=70,height=25)

        




#==================================Define function==================================
        
    def login(self):
        if self.username.get()=="" or self.password.get()=="":
            messagebox.showerror("Error","Fileds can't be blank")

        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Nikhil@9664",
                                                   database="project")
            my_cursur = conn.cursor()
            query = 'select * from student_registerdata where email=%s and password=%s'
            my_cursur.execute(query, (self.username.get(), self.password.get()))
            row = my_cursur.fetchone()
            if row == None:
                messagebox.showerror("Error", "Invalid Username and Password")
            else:
                self.new_windwow = Toplevel(self.root)
                self.app = Face_Recognition_System(self.new_windwow)
                conn.commit()
                conn.close()

    def register_window(self):
        from studentregister import register
        self.new_windwow=Toplevel(self.root)
        self.new_windwow.geometry("700x250")
        self.app=register(self.new_windwow)





if __name__ == "__main__":
    root=Tk()
    obj=Login(root)
    root.mainloop()
