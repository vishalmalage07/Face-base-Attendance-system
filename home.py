from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk, ImageFont, ImageDraw
from tkinter import messagebox
from student_login import Login
from studentregister import register
from teacher_login import TLogin


class Home:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Home Page")

        first_frame=Frame(self.root,bd=2,bg="#001433")
        first_frame.place(x=0,y=0,width=1550,height=40)

        img=Image.open(r"D:\clgproject\web\phone.png")
        img=img.resize((30,30),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        first_label=Label(first_frame,image=self.photoimg,bg="#001433")
        first_label.place(x=1100,y=10,width=30,height=30 )

        second_label=Label(first_frame,text="8808888657",font=("Algerian",15,"bold"),fg='#0ABAB1',bg="#001433")
        second_label.place(x=1130,y=13)

        img2=Image.open(r"D:\clgproject\web\mail.png")
        img2=img2.resize((30,30),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        third_label=Label(first_frame,image=self.photoimg2,bg="#001433")
        third_label.place(x=1270,y=13,width=30,height=30 )

        fourth_label=Label(first_frame,text="info@ftccoe.ac.in",font=("Algerian",15,"bold"),fg='#0ABAB1',bg="#001433")
        fourth_label.place(x=1300,y=13)

        second_frame=Frame(self.root,bd=2,bg="#001433")
        second_frame.place(x=0,y=40,width=1550,height=130)

        img3=Image.open(r"D:\clgproject\web\fab.png")
        img3=img3.resize((1500,100),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        fifth_label=Label(second_frame,image=self.photoimg3,bg="#001433")
        fifth_label.place(x=35,y=10,width=1500,height=100 )

        third_frame=Frame(self.root,bd=2,bg="#001433")
        third_frame.place(x=0,y=160,width=1550,height=700)

        img4=Image.open(r"D:\clgproject\web\facer.jpg")
        img4=img4.resize((1550,700),Image.LANCZOS)
        pic =ImageTk.PhotoImage(img4)

        canvas=Canvas(third_frame,width=1550,height=700)
        canvas.place(x=0,y=160)

        canvas.create_image(0,0,image=pic, anchor="nw")
        canvas.create_text(1200, 100, text="Face Recognition Based \n Attendance System ", fill="#0ABAB1", font=('Algerian 35 bold'))
        canvas.place(x=0,y=0)
        canvas.img4=pic

        img5=Image.open(r"D:\clgproject\web\sbutton.png")
        img5=img5.resize((150,60),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        staff_button=Button(self.root,image=self.photoimg5,command=self.staff_login_window,cursor="hand2",borderwidth=5,activebackground='#001433',bg='#001433')
        staff_button.place(x=1100,y=400)

        img6=Image.open(r"D:\clgproject\web\stbutton.png")
        img6=img6.resize((150,60),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        student_button=Button(self.root,image=self.photoimg6,command=self.student_login_window,cursor="hand2",borderwidth=5,activeforeground='#001433',activebackground='#001433',bg='#001433')
        student_button.place(x=900,y=400)

        img7=Image.open(r"D:\clgproject\web\rbutton.png")
        img7=img7.resize((150,60),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        register_button=Button(self.root,image=self.photoimg7,command=self.register_window,cursor="hand2",borderwidth=5,activebackground='#001433',bg='#001433')
        register_button.place(x=1300,y=400)

        

#======================================function declaration=====================

    def staff_login_window(self):
        self.new_windwow=Toplevel(self.root)
        self.app=TLogin(self.new_windwow)

    def student_login_window(self):
        self.new_windwow=Toplevel(self.root)
        self.app=Login(self.new_windwow)

    def register_window(self):
        
        self.new_windwow=Toplevel(self.root)
        self.app=register(self.new_windwow)






if __name__ == "__main__":
    root=Tk()
    obj=Home(root)
    root.mainloop()
