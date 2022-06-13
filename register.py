from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

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
        img=Image.open(r"college_images\fiber-background-1024x533.jpg")
        img=img.resize((1360,768),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1360,height=768)
        
        #=====main frame=====
        frame=Frame(self.root,bg="black")
        frame.place(x=300,y=100,width=800,height=550)
        
        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roamn",20,"bold"),fg="white",bg="black")
        register_lbl.place(x=20,y=20)
        
        #====label and entry===
        fname=Label(frame,text="First Name",font=("times new roamn",15,"bold"),fg="white",bg="black")
        fname.place(x=50,y=100)
        
        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roamn",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)
        
        l_name=Label(frame,text="Last Name",font=("times new roamn",15,"bold"),fg="white",bg="black")
        l_name.place(x=370,y=100)
        
        self.txt_l_name=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roamn",15,"bold"))
        self.txt_l_name.place(x=370,y=130,width=250)
        #row 2
        contact=Label(frame,text="Contact No",font=("times new roamn",15,"bold"),fg="white",bg="black")
        contact.place(x=50,y=170)
        
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roamn",15,"bold"))
        self.txt_contact.place(x=50,y=200,width=250)
        
        email=Label(frame,text="Email",font=("times new roamn",15,"bold"),fg="white",bg="black")
        email.place(x=370,y=170)
        
        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roamn",15,"bold"))
        self.txt_email.place(x=370,y=200,width=250)
        
        #row3
        security=Label(frame,text="Select Security Question",font=("times new roamn",15,"bold"),fg="white",bg="black")
        security.place(x=50,y=240)
        
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roamn",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Girlfriend name","Your Pet Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)
        
        security_A=Label(frame,text="Security Answer",font=("times new roamn",15,"bold"),fg="white",bg="black")
        security_A.place(x=370,y=240)
        
        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roamn",15,"bold"))
        self.txt_security.place(x=370,y=270,width=250)
        
        #row 4
        pswd=Label(frame,text="Password",font=("times new roamn",15,"bold"),fg="white",bg="black")
        pswd.place(x=50,y=310)
        
        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roamn",15,"bold"))
        self.txt_pswd.place(x=50,y=340,width=250)
        
        confirm=Label(frame,text="Password",font=("times new roamn",15,"bold"),fg="white",bg="black")
        confirm.place(x=370,y=310)
        
        self.txt_confirm=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roamn",15,"bold"))
        self.txt_confirm.place(x=370,y=340,width=250)
        
        #=======checkbuttons===
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditon",font=("times new roamn",12,"bold"),fg="white",bg="black",onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)
        
        #===buttons==
        img1=Image.open(r"college_images\R.png")
        img1=img1.resize((200,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage,command=self.register_data,bg="black",borderwidth=0,cursor="hand2")
        b1.place(x=40,y=420,width=200)
        
        img2=Image.open(r"college_images\loginpng.png")
        img2=img2.resize((200,50),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img2)
        b1=Button(frame,image=self.photoimage1,fg="white",bg="black",borderwidth=0,cursor="hand2")
        b1.place(x=330,y=420,width=200)
    
    #=======function declaration
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password & confirm Password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please Agree our Terms & Condition")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="student_attendance_system")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist please try another email")
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
            messagebox.showinfo("Success","Register Succesfuly")
        
            
            
            
        
        
        
        
if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()    