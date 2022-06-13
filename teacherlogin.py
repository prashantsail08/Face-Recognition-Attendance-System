from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from attendance import Attendance
from main import Face_Attendance_System
from face_recognition import Face_Recognition
from user import User

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1350x700+0+0")

       #====Background Image
        img3=Image.open(r"college_images\bg2.jpg")
        img3=img3.resize((1360,768),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1360,height=768)
        
        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)
        
        img1=Image.open(r"college_images\LoginIconAppl.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)
#label
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)
        
        self.txtuser=StringVar()
        self.txtpass=StringVar()
        
        self.txtuser=ttk.Entry(frame,textvariable=self.txtuser,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)
        
        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)
        
        self.txtpass=ttk.Entry(frame,textvariable=self.txtpass,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)
        
        #===icon images===
        img2=Image.open(r"college_images\LoginIconAppl.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=323,width=25,height=25)
        
        img3=Image.open(r"college_images\lock-512.png")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=395,width=25,height=25)
        
        #button
        loginbtn=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=160)
        
        registerbtn=Button(frame,text="New User Register?",command=self.register_window,font=("times new roman",12,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=350,width=160)

        registerbtn=Button(frame,text="Forgot Password?",command=self.forgot_password_window,font=("times new roman",12,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=10,y=370,width=160)
      
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
      
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All field required",parent=self.root)
        elif self.txtuser.get()=="admin" and self.txtpass.get()=="admin":
            self.new_window=Toplevel(self.root)
            self.app=Face_Attendance_System(self.new_window)
        elif self.txtuser.get()=="teacher" and self.txtpass.get()=="teacher":
            self.new_window=Toplevel(self.root)
            self.app=Attendance(self.new_window)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="student_attendance_system")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                    self.txtuser.get(),
                                                                                    self.txtpass.get()                 
                                                                                ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid userame & Password",parent=self.root)
            else:
                open_main=messagebox.showinfo("YesNo","Student Login")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Attendance_System(self.new_window)
                else:
                    if not open_main:
                        self.new_window=Toplevel(self.root)
                        self.app=Login_Window(self.new_window)
                    return
            conn.commit()
            conn.close()
           
    def clear(self):
        self.txtuser.set("")
        self.txtpass.set("")
    
    #========reset Password======
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select security Question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="student_attendance_system")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct security question",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)
       
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Your password has been reset Succesfully",parent=self.root2)
                self.root2.destroy()
        
    #=====forget password=======
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="student_attendance_system")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            
            if row==None:
                messagebox.showerror("My Error","Please enter the valid username",parent=self.root2)
            else:
                conn.close()
                self.root2=Toplevel()
                self.root.title("Forget Password")
                self.root2.geometry("340x450+610+170")
                
                l=Label(self.root2,text="Forget Password",font=("times new roman",15,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)
                
                security=Label(self.root2,text="Select Security Question",font=("times new roamn",15,"bold"),bg="white")
                security.place(x=50,y=80)
        
                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roamn",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your Girlfriend name","Your Pet Name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)
        
                security_A=Label(self.root2,text="Security Answer",font=("times new roamn",15,"bold"),bg="white")
                security_A.place(x=50,y=150)
        
                self.txt_security=ttk.Entry(self.root2,font=("times new roamn",15,"bold"))
                self.txt_security.place(x=50,y=180,width=250)
                
                
                new_password=Label(self.root2,text="New Password",font=("times new roamn",15,"bold"),bg="white")
                new_password.place(x=50,y=220)
        
                self.txt_newpass=ttk.Entry(self.root2,font=("times new roamn",15,"bold"))
                self.txt_newpass.place(x=50,y=250,width=250)
                
                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roamn",15,"bold"),fg="white",bg="green")
                btn.place(x=100,y=290)
                
                
 
           
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1350x700+0+0")
        
        #====variables=====
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        self.var_check=IntVar()
        
        #====Background Image
        img=Image.open(r"college_images\bg2.jpg")
        img=img.resize((1360,768),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1360,height=768)
        
        #=====main frame=====
        frame=Frame(self.root,bg="white")
        frame.place(x=300,y=100,width=800,height=550)
        
        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roamn",20,"bold"),fg="Black",bg="white")
        register_lbl.place(x=20,y=20)
        
        #====label and entry===
        fname=Label(frame,text="First Name",font=("times new roamn",15,"bold"),bg="white")
        fname.place(x=50,y=100)
        
        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roamn",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)
        
        l_name=Label(frame,text="Last Name",font=("times new roamn",15,"bold"),bg="white")
        l_name.place(x=370,y=100)
        
        self.txt_l_name=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roamn",15,"bold"))
        self.txt_l_name.place(x=370,y=130,width=250)
        #row 2
        contact=Label(frame,text="Contact No",font=("times new roamn",15,"bold"),bg="white")
        contact.place(x=50,y=170)
        
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roamn",15,"bold"))
        self.txt_contact.place(x=50,y=200,width=250)
        
        email=Label(frame,text="Email",font=("times new roamn",15,"bold"),bg="white")
        email.place(x=370,y=170)
        
        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roamn",15,"bold"))
        self.txt_email.place(x=370,y=200,width=250)
        
        #row3
        security=Label(frame,text="Select Security Question",font=("times new roamn",15,"bold"),bg="white")
        security.place(x=50,y=240)
        
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roamn",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Girlfriend name","Your Pet Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)
        
        security_A=Label(frame,text="Security Answer",font=("times new roamn",15,"bold"),bg="white")
        security_A.place(x=370,y=240)
        
        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roamn",15,"bold"))
        self.txt_security.place(x=370,y=270,width=250)
        
        #row 4
        pswd=Label(frame,text="Password",font=("times new roamn",15,"bold"),bg="white")
        pswd.place(x=50,y=310)
        
        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roamn",15,"bold"))
        self.txt_pswd.place(x=50,y=340,width=250)
        
        confirm=Label(frame,text="Password",font=("times new roamn",15,"bold"),bg="white")
        confirm.place(x=370,y=310)
        
        self.txt_confirm=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roamn",15,"bold"))
        self.txt_confirm.place(x=370,y=340,width=250)
        
        #=======checkbuttons===
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditon",font=("times new roamn",12,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)
        
        #===buttons==
        img1=Image.open(r"college_images\register-now-button1.jpg")
        img1=img1.resize((200,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=10,y=420,width=200)
        
        img2=Image.open(r"college_images\loginpng.png")
        img2=img2.resize((200,50),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img2)
        b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2")
        b1.place(x=330,y=420,width=200)
    
    #=======function declaration
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password & confirm Password must be same",parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please Agree our Terms & Condition",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="student_attendance_system")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist please try another email",parent=self.root)
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get()
                                                                             ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Succesfuly",parent=self.root)
    
    
    def return_login(self):
        self.root.destroy()

        
        
        
        
        
if __name__=="__main__":
    root=Tk()
    app=Login_Window(root)
    root.mainloop()