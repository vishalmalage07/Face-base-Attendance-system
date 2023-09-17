import re
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import os
import tkinter
import mysql.connector
from tkinter import messagebox



class register:
        def __init__(self, root2):
                self.root2=root2
                self.root2.geometry("1530x790+0+0")
                self.root2.title("Staff Register Page")


        #=======================Variables Declaration============================
                self.var_fname=StringVar()
                self.var_lname=StringVar()
                self.var_email=StringVar()
                self.var_phone=StringVar()
                self.var_SecurityQ=StringVar()
                self.var_SecurityA=StringVar()
                self.var_Pass=StringVar()
                self.var_Cpass=StringVar()
                self.var_check=IntVar()

        #===============background==============================
                self.bg=ImageTk.PhotoImage(file=r"D:\clgproject\web\bg4.jpg")
                lbl_bg=Label(self.root2,image=self.bg)
                lbl_bg.place(x=0,y=0,relheight=1,relwidth=1)
        #===================frame==========================
                frame = Frame(self.root2, bd=2, background='#BCD4E6')
                frame.place(x=200, y=100, width=1050, height=600)
                frame.propagate(0)

                register_label = Label(frame, text=" Staff Register Here", font=("times new roman", 30, "bold"),
                                       fg="green",
                                       bg='#BCD4E6')
                register_label.place(x=25, y=10)

                #===================Labels==========================
                fname_label = Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg='#bcd4e6')
                fname_label.place(x=50, y=100)

                self.fname_entry = ttk.Entry(frame, textvariable=self.var_fname, validate="key",
                                             validatecommand=(frame.register(self.validate_name), '%P'),
                                             width=20, font=("times new roman", 15, "bold"))
                self.fname_entry.place(x=50, y=130, width=350, height=40)

                lname_label = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg='#bcd4e6')
                lname_label.place(x=570, y=100)

                self.lname_entry = ttk.Entry(frame, textvariable=self.var_lname, validate="key",
                                             validatecommand=(frame.register(self.validate_name), '%P'),
                                             width=20, font=("times new roman", 15, "bold"))
                self.lname_entry.place(x=570, y=130, width=350, height=40)

                #Phone No
                Phone_no_label=Label(frame,text="Phone No",font=("times new roman",15,"bold"),bg='#bcd4e6')
                Phone_no_label.place(x=50,y=180)

                self.Phone_no_entry=ttk.Entry(frame,textvariable=self.var_phone,width=20,font=("times new roman",15,"bold"))
                self.Phone_no_entry.place(x=50,y=210,width=350,height=40)
                #Email
                email_label=Label(frame,text="Email",font=("times new roman",15,"bold"),bg='#bcd4e6')
                email_label.place(x=570,y=180)

                self.email_entry=ttk.Entry(frame,width=20,textvariable=self.var_email,font=("times new roman",15,"bold"))
                self.email_entry.place(x=570,y=210,width=350,height=40)



                #Security Question
                security_label=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg='#bcd4e6')
                security_label.place(x=50,y=260)

                self.security_combo=ttk.Combobox(frame,textvariable=self.var_SecurityQ,font=("times new roman",15," bold"),state="readonly",width=18,background="white")
                self.security_combo["values"]=("Select","Your Birth Place","Your Mother Name","Your Nickname","Your Petname")
                self.security_combo.current(0)
                self.security_combo.place(x=50,y=290,width=350,height=40)

                #Security Question Answer
                S_Q_A_label=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg='#bcd4e6')
                S_Q_A_label.place(x=570,y=260)

                self.S_Q_A_entry=ttk.Entry(frame,textvariable=self.var_SecurityA,width=20,font=("times new roman",15,"bold"))
                self.S_Q_A_entry.place(x=570,y=290,width=350,height=40)

                #Password
                password_label=Label(frame,text="Password",font=("times new roman",15,"bold"),bg='#bcd4e6')
                password_label.place(x=50,y=340)

                self.password_entry=ttk.Entry(frame,textvariable=self.var_Pass,width=20,font=("times new roman",15,"bold"),show="*")
                self.password_entry.place(x=50,y=370,width=350,height=40)
                #Confirm Password
                Confirm_label=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg='#bcd4e6')
                Confirm_label.place(x=570,y=340)

                self.Confirm_entry=ttk.Entry(frame,textvariable=self.var_Cpass,width=20,font=("times new roman",15,"bold"))
                self.Confirm_entry.place(x=570,y=370,width=350,height=40)

        #==========================Check Button================================
                checkbtn = Checkbutton(frame, variable=self.var_check, text="I Agree to the terms & conditions",
                                       font=("times new roman", 15, "bold"), bg='#bcd4e6', activebackground='#bcd4e6',
                                       onvalue=1, offvalue=0)
                checkbtn.place(x=50, y=420)

                #============================Buttons========================================
                img=Image.open(r"D:\clgproject\web\register.png")
                img=img.resize((300,120),Image.LANCZOS)
                self.photoimg=ImageTk.PhotoImage(img)

                register_button=Button(frame,image=self.photoimg,command=self.register_data,cursor="hand2",borderwidth=0,bg='#bcd4e6',activebackground='#bcd4e6')
                register_button.place(x=100,y=450)
                
                existing_acc_button=Button(frame,text="Already have an account?", command = self.login_window ,cursor="hand2",borderwidth=0,font=("times new roman",20,"bold"),fg="blue",activebackground='#bcd4e6',bg='#bcd4e6')
                existing_acc_button.place(x=470,y=485)

#==================================Function Declaration==========================

        def register_data(self):
                if self.var_fname.get()=="" or self.var_phone=="" or self.var_email=="" or self.var_SecurityQ=="Select" or self.var_SecurityA=="":
                     messagebox.showerror("Error","All fields need to be fill",parent=self.root2)
                elif self.var_Pass.get()!=self.var_Cpass.get(): 
                     messagebox.showerror("Error","Password and confirm password need to be same",parent=self.root2)
                elif self.var_check.get()==0:
                      messagebox.showerror("Error","You need to agree our terms and conditions",parent=self.root2)
                else:
                        conn=mysql.connector.connect(host="localhost",username="root",password="Nikhil@9664",database="project")
                        my_cursur=conn.cursor()
                        query1=("select * from staff_registerdata where email=%s")
                        value=(self.var_email.get(),)
                        my_cursur.execute(query1,value)
                        row=my_cursur.fetchone()
                        if row!=None:
                               messagebox.showerror("Error","User already exist,please try another email or phone",parent=self.root2)
                        else:
                                my_cursur.execute("insert into staff_registerdata values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                        self.var_fname.get(),
                                                                                                        self.var_lname.get(),
                                                                                                        self.var_phone.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_SecurityQ.get(),
                                                                                                        self.var_SecurityA.get(),
                                                                                                        self.var_Pass.get()
                                                                                                ))
                        conn.commit()
                        conn.close()
                        messagebox.showinfo("Success","Register successfully",parent=self.root2)

        def login_window(self):
                from teacher_login import TLogin
                self.new_windwow=Toplevel(self.root2)
                self.app=TLogin(self.new_windwow)

        def validate_name(self, value):
                # Regular expression pattern to match any digit or space
                pattern = r"[\d\s]"
                if re.search(pattern, value):
                        self.fname_entry.config(style="Invalid.TEntry")
                        return False
                else:
                        self.fname_entry.config(style="TEntry")
                        return True


if __name__ == "__main__":
    root2=Tk()

    # Create a custom style for the invalid entry field
    style = ttk.Style()
    style.configure("Invalid.TEntry", bordercolor="red")

    obj=register(root2)
    root2.mainloop()

