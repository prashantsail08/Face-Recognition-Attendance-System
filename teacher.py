from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from time import strftime
from datetime import datetime
from student import Student
import os
from face_recognition import Face_Recognition
from attendance import Attendance
from Qr_code import Qr_Code

class Face_Attendance_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1000x600+200+50")
        self.root.title("TEACHER SIDE")
        
         #====Background Image
        img3=Image.open(r"college_images\bg.jpg")
        img3=img3.resize((1360,768),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=60,width=1360,height=768)
        
        title=Label(self.root,text="Teacher Module",font=("times new roman",40),bg='blue',fg='white').place(x=0,y=0,relwidth=1)

        #======first Image top left
        #img=img.resize((500,130),Image.ANTIALIAS)
        #img=Image.open(r"college_images\un.jpg")
        #self.photoimg=ImageTk.PhotoImage(img)

        #f_lbl=Label(self.root,image=self.photoimg)
        #f_lbl.place(x=0,y=0,width=500,height=130)

        #====second Image Middle
        #img1=Image.open(r"college_images\facialrecognition.png")
        #img1=img1.resize((500,130),Image.ANTIALIAS)
        #self.photoimg1=ImageTk.PhotoImage(img1)

        #f_lbl=Label(self.root,image=self.photoimg1)
        #f_lbl.place(x=500,y=0,width=500,height=130)

        #====third Image Top Right
        #img2=Image.open(r"college_images\university.jpg")
        #img2=img2.resize((500,130),Image.ANTIALIAS)
        #self.photoimg2=ImageTk.PhotoImage(img2)

        #f_lbl=Label(self.root,image=self.photoimg2)
        #f_lbl.place(x=1000,y=0,width=500,height=130)

        #====Background Image
        #img3=Image.open(r"college_images\backgroung.jpg")
        #img3=img3.resize((1360,768),Image.ANTIALIAS)
        #self.photoimg3=ImageTk.PhotoImage(img3)

        #bg_img=Label(self.root,image=self.photoimg3)
        #bg_img.place(x=0,y=0,width=1360,height=768)

        #=====Title====
        #title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",30,"bold"),bg="white",fg="red")
        #title_lbl.place(x=0,y=0,width=1360,height=45)
        
        #=====time=====
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
            
        lbl=Label(bg_img,font=('times new roman',14,'bold'),bg='white',fg='blue')
        lbl.place(x=0,y=0,width=110,height=30)
        time()


        #====STUDENT BUTTOM========= 
        img4=Image.open(r"college_images\student_details.jpg")
        img4=img4.resize((200,200),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=20,y=60,width=300,height=200)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="dark blue")
        b1_1.place(x=20,y=240,width=300,height=40)

        

        #====ATTENDANCE BUTTOM========= 
        img6=Image.open(r"college_images\atten.jpg")
        img6=img6.resize((200,200),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=730,y=60,width=260,height=200)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="white",fg="dark blue")
        b1_1.place(x=730,y=240,width=260,height=40)


        #====PHOTO BUTTOM========= 
        img9=Image.open(r"college_images\photo.jpg")
        img9=img9.resize((200,250),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=400,y=60,width=260,height=200)

        b1_1=Button(bg_img,text="Photo",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="white",fg="dark blue")
        b1_1.place(x=400,y=240,width=260,height=40)

        
    
    def open_img(self):
        os.startfile("data")
        
    def exit(self):
        self.exit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this software",parent=self.root)
        if self.exit >0:
            self.root.destroy()
        else:
            return

        #======Function Buttons========
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
        
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
        
    def open_qr_code(self):
        self.new_window=Toplevel(self.root)
        self.app=Qr_Code(self.new_window)
        
        
    









if __name__=="__main__":
    root=Tk()
    obj=Face_Attendance_System(root)
    root.mainloop()