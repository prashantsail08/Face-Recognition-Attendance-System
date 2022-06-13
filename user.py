from tkinter import*
from PIL import Image,ImageTk
from face_recognition import Face_Recognition
from attendance import Attendance
from Qr_code import Qr_Code

class User:     
    def __init__(self,root):
        self.root=root
        self.root.geometry("1000x600+200+50")
        self.root.title("QR Generator")
        
        #====Background Image
        img3=Image.open(r"college_images\bg.jpg")
        img3=img3.resize((1360,768),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=60,width=1360,height=768)
        
        title=Label(self.root,text="Student Attendance",font=("times new roman",40),bg='blue',fg='white').place(x=0,y=0,relwidth=1)
        
        
       
        #====STUDENT BUTTOM========= 
        img4=Image.open(r"college_images\face_rec.jpg")
        img4=img4.resize((300,300),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        

        b1=Button(bg_img,image=self.photoimg4,command=self.face_data,cursor="hand2")
        b1.place(x=150,y=160,width=300,height=300)

        b1_1=Button(bg_img,text="Face Detector",command=self.face_data,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="dark blue")
        b1_1.place(x=150,y=460,width=300,height=40)

        #====DETECT FACE BUTTOM========= 
        img5=Image.open(r"college_images\qr1.jpg")
        img5=img5.resize((300,300),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.open_qr_code)
        b1.place(x=550,y=160,width=300,height=300)

        b1_1=Button(bg_img,text="QR Code",cursor="hand2",command=self.open_qr_code,font=("times new roman",15,"bold"),bg="white",fg="dark blue")
        b1_1.place(x=550,y=460,width=300,height=40)
        
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
        
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    
    def open_qr_code(self):
        self.new_window=Toplevel(self.root)
        self.app=Qr_Code(self.new_window)

        

if __name__ == "__main__":  
    root=Tk()
    obj=User(root)
    root.mainloop()