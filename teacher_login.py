from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import os
import tkinter
from tkinter import messagebox
import mysql.connector
from main import Face_Recognition_System
from register import register



class TLogin:
    def __init__(self, root1):
        self.root1=root1
        self.root1.geometry("1530x790+0+0")
        self.root1.title("Login Page")

        self.bg=ImageTk.PhotoImage(file=r"D:\clgproject\web\bg3.jpg")
        lbl_bg=Label(self.root1,image=self.bg)
        lbl_bg.place(x=0,y=0)

        frame=Frame(self.root1,bd=2,background='black')
        frame.place(x=500,y=100,width=450,height=600)

        img1=Image.open(r"D:\clgproject\web\staff.png")
        img1=img1.resize((120,120),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_label=Label(self.root1,image=self.photoimg1,bg="black",borderwidth=0)
        f_label.place(x=660,y=105,width=120,height=120)

        started=Label(frame,text="Staff Log In",font=("times new roman",30,"bold"),fg="red",bg="Black")
        started.place(x=115,y=115)

        def show():
            hide_button = Button(self.root1,image=hide_pass,command=hide,bd=0,relief=FLAT,background="white",activebackground="white")
            hide_button.place(x=805,y=413)
            self.password.config(show='*')

        def hide():
            show_button=Button(self.root1,image=show_pass,cursor="hand2",command=show,bd=0,relief=FLAT,background="white",activebackground="white")
            show_button.place(x=805,y=413)
            self.password.config(show='')


        show_pass=ImageTk.PhotoImage(file=r"D:\clgproject\web\eye.jpg")
        hide_pass=ImageTk.PhotoImage(file=r"D:\clgproject\web\hide.jpg")
        
        #username
        username_label=Label(frame,text="Username:",font=("times new roman",30,"bold"),fg="White",bg="Black")
        username_label.place(x=95,y=170)

        self.username=ttk.Entry(frame,width=20,font=("times new roman",20,"bold"))
        self.username.place(x=70,y=220,width=300,height=40)

        password_label=Label(frame,text="Password:",font=("times new roman",30,"bold"),fg="White",bg="Black")
        password_label.place(x=95,y=260)

        self.password=ttk.Entry(frame,width=20,font=("times new roman",20,"bold"),show="*")
        self.password.place(x=70,y=310,width=300,height=40)

        hide_button=Button(self.root1,image=hide_pass,cursor="hand2",command=hide,bd=0,relief=FLAT,background="white",activebackground="white")
        hide_button.place(x=805,y=413)

        img2=Image.open(r"D:\clgproject\web\user.png")
        img2=img2.resize((40,40),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_label1=Label(self.root1,image=self.photoimg2,bg="black",borderwidth=0)
        f_label1.place(x=560,y=278,width=40,height=40)

        img3=Image.open(r"D:\clgproject\web\lock.png")
        img3=img3.resize((40,40),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_label2=Label(self.root1,image=self.photoimg3,bg="black",borderwidth=0)
        f_label2.place(x=560,y=368,width=40,height=40)

        #buttons
        forget_button=Button(self.root1,text="Forget Password?", command=self.forgot_window,width=65,cursor="hand2",font=("times new roman",12,"bold"),borderwidth=0,relief=RIDGE,bg="black",fg="blue",activeforeground="blue",activebackground="black")
        forget_button.place(x=575,y=465,width=120,height=25)

        login_button=Button(self.root1,text="Login",width=75,cursor="hand2",command=self.login,font=("times new roman",12,"bold"),bd=5,relief=RIDGE,bg="red",fg="White",activeforeground="white",activebackground="red")
        login_button.place(x=670,y=500,width=120,height=40)

        new_label=Label(self.root1,text="not register yet,",width=75,font=("times new roman",13,"bold"),borderwidth=0,relief=RIDGE,bg="black",fg="White")
        new_label.place(x=575,y=550,width=120,height=25)

        signup_label=Button(self.root1,text="Sign up",width=65,command=self.register_window,cursor="hand2",font=("times new roman",13,"bold"),borderwidth=0,relief=RIDGE,bg="black",fg="blue",activeforeground="blue",activebackground="black")
        signup_label.place(x=695,y=550,width=70,height=25)

        




#==================================Define function==================================
    


    def login(self):
        if self.username.get()=="" or self.password.get()=="":
            messagebox.showerror("Error","Fileds can't be blank")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Nikhil@9664",database="project")
            my_cursur=conn.cursor()
            query = 'select * from staff_registerdata where email=%s and password=%s'
            my_cursur.execute(query,(self.username.get(),self.password.get()))
            row=my_cursur.fetchone()
            if row==None:
                  messagebox.showerror("Error","Invalid Username and Password")
            else:
                 self.new_windwow=Toplevel(self.root1)
                 self.app=Face_Recognition_System(self.new_windwow)
            conn.commit()
            conn.close()

    
    def register_window(self):
        self.new_windwow=Toplevel(self.root1)
        self.new_windwow.geometry("700x250")
        self.app=register(self.new_windwow)

    def forgot_window(self):
        self.root=Toplevel()
        self.root.title("Forgot password")
        self.root.geometry("1530x790+0+0")

        self.bg1 = ImageTk.PhotoImage(file=r"Images\bg2.jpg")
        lbl_bg1 = Label(self.root, image=self.bg1)
        lbl_bg1.place(x=0, y=0)

        frame1 = Frame(self.root, bd=2, background='#BCD4E6')
        frame1.place(x=500, y=50, width=650, height=650)

        forgot = Image.open(r"Images\forgot.png")
        forgot = forgot.resize((80, 80), Image.LANCZOS)
        self.forgot_photoimg3 = ImageTk.PhotoImage(forgot)

        f_label2 = Label(frame1, image=self.forgot_photoimg3, bg="#BCD4E6", borderwidth=0)
        f_label2.place(x=70, y=35, width=80, height=80)

        started = Label(frame1, text="Forget Password", font=("times new roman", 35, "bold"), fg="Green", bg="#BCD4E6")
        started.place(x=150, y=45)

        # username
        username_label = Label(frame1, text="Username:", font=("times new roman", 30, "bold"), fg="black", bg="#BCD4E6")
        username_label.place(x=10, y=125)

        self.username = ttk.Entry(frame1, width=20, font=("times new roman", 20, "bold"))
        self.username.place(x=360, y=130, width=270, height=40)

        # Security Question
        security_label = Label(frame1, text="Security Question:", font=("times new roman", 30, "bold"), fg="black",
                               bg='#BCD4E6')
        security_label.place(x=10, y=200)

        self.security_combo = ttk.Combobox(frame1, font=("times new roman", 20, " bold"), state="readonly", width=18,
                                           background="white")
        self.security_combo["values"] = (
        "Select", "Your Birth Place", "Your Mother Name", "Your Nickname", "Your Petname")
        self.security_combo.current(0)
        self.security_combo.place(x=360, y=210, width=270, height=40)

        # Security Question Answer
        S_Q_A_label = Label(frame1, text="Security Answer:", font=("times new roman", 30, "bold"), bg='#BCD4E6',
                            fg="black")
        S_Q_A_label.place(x=10, y=270)

        self.S_Q_A_entry = ttk.Entry(frame1, width=20, font=("times new roman", 20, "bold"), background='#BCD4E6',
                                     foreground="black")
        self.S_Q_A_entry.place(x=360, y=280, width=270, height=40)

        # Password
        password_label = Label(frame1, text="Password:", font=("times new roman", 30, "bold"), bg='#BCD4E6', fg="black")
        password_label.place(x=10, y=340)

        self.password_entry = ttk.Entry(frame1, width=20, font=("times new roman", 20, "bold"), foreground="black",
                                        background='#BCD4E6')
        self.password_entry.place(x=360, y=350, width=270, height=40)
        # Confirm Password
        Confirm_label = Label(frame1, text="Confirm Password:", font=("times new roman", 30, "bold"), bg='#BCD4E6',
                              fg="black")
        Confirm_label.place(x=10, y=410)

        self.Confirm_entry = ttk.Entry(frame1, width=20, font=("times new roman", 20, "bold"), foreground="black",
                                       background='#BCD4E6')
        self.Confirm_entry.place(x=360, y=420, width=270, height=40)

        img = Image.open(r"Images\reset.png")
        img = img.resize((200, 80), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        reset_button = Button(frame1, image=self.photoimg, command=self.forgot_pass, cursor="hand2", borderwidth=0,
                              bg='#bcd4e6', activebackground='#bcd4e6')
        reset_button.place(x=200, y=500)

    def forgot_pass(self):
        if self.username.get() == "":
            messagebox.showerror("Error", "Please enter email address to reset password", parent=self.root)
        elif self.security_combo.get() == "Select":
            messagebox.showerror("Error", "Please Select Security Question", parent=self.root)
        elif self.S_Q_A_entry.get() == "":
            messagebox.showerror("Error", "Please Answer Security Question", parent=self.root)
        elif self.password_entry.get() == "":
            messagebox.showerror("Error", "Please Enter Password", parent=self.root)
        elif self.Confirm_entry.get() == "":
            messagebox.showerror("Error", "Please Enter Confirm Password", parent=self.root)
        elif self.Confirm_entry.get() != self.password_entry.get():
            messagebox.showerror("Error", "Entered Password and Confirm Password need to be same", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Nikhil@9664",
                                           database="project")
            my_cursor = conn.cursor()
            query = ("select * from staff_registerdata where email=%s and securityq=%s and securitya=%s")
            value = (self.username.get(), self.security_combo.get(), self.S_Q_A_entry.get())
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Invalid Username or question and answer", parent=self.root)
            else:
                query1 = 'update staff_registerdata set password=%s where email=%s'
                value1 = (self.password_entry.get(), self.username.get(),)
                my_cursor.execute(query1, value1)

                messagebox.showinfo("Success", "Your password has been reset,please login new password",parent=self.root)
                conn.commit()
                conn.close()

if __name__ == "__main__":
    root1=Tk()
    obj=TLogin(root1)
    root1.mainloop()
