from tkinter import*
from PIL import Image,ImageTk

class Qr_Code:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1000x600+200+50")
        self.root.title("QR Generator")
        
        
        title=Label(self.root,text="Scan QR Code",font=("times new roman",40),bg='blue',fg='white').place(x=0,y=0,relwidth=1)
        
        img2=Image.open(r"QR_codes\qrchimpX1024.png")
        img2=img2.resize((500,400),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=300,y=100,width=500,height=400)
        
if __name__ == "__main__":      
    root=Tk()
    obj=Qr_Code(root)
    root.mainloop()