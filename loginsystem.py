from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from hotel import HotelManagementSystem

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()      

class Login_Window:
    def __init__(self,root):

        self.root=root
        self.root.title("Hotel Management System - Login")
        self.root.state('zoomed')
        #w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        #self.root.geometry("%dx%d+0+0" % (w, h))
        #self.root.geometry("1550x800+0+0")

        self.bg= ImageTk.PhotoImage(file=r"C:\Users\vivek\Desktop\VIVEK\HMS\Hotel Management System\HOTEL MANAGEMENT SYSTEM\images\login back.jpg")  # path for image

        lbl_bg= Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame= Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\vivek\Desktop\VIVEK\HMS\Hotel Management System\HOTEL MANAGEMENT SYSTEM\images\login logo.png")      #path for image
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimage1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimage1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",20,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password = lbl = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=70, y=225)

        self.txtpass = ttk.Entry(frame,show="*",font=("times new roman", 20, "bold"))
        self.txtpass.place(x=40, y=250, width=270)

        # icon images
        img2 = Image.open(r"C:\Users\vivek\Desktop\VIVEK\HMS\Hotel Management System\HOTEL MANAGEMENT SYSTEM\images\user.png")  # path for image
        img2 = img2.resize((25, 25), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg1 = Label(image=self.photoimage2, bg="black", borderwidth=0)
        lblimg1.place(x=650, y=323, width=25, height=25)

        img3 = Image.open(r"C:\Users\vivek\Desktop\VIVEK\HMS\Hotel Management System\HOTEL MANAGEMENT SYSTEM\images\pass.png")  # path for image
        img3 = img3.resize((25, 25), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg1 = Label(image=self.photoimage3, bg="black", borderwidth=0)
        lblimg1.place(x=650, y=395, width=25, height=25)

        #LoginButton
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman", 20, "bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        #registerbutton
        registerbtn = Button(frame, text="New User Register",command=self.register_window,font=("times new roman", 10, "bold"),borderwidth=0, fg="white",
                             bg="black", activeforeground="white", activebackground="black")
        registerbtn.place(x=15, y=350, width=160)

        # forgt btn
        registerbtn = Button(frame, text="Forgot Password",command=self.forgot_password_window,font=("times new roman", 10, "bold"),borderwidth =0, fg="white",bg="black", activeforeground="white", activebackground="black")
        registerbtn.place(x=10, y=370, width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all fields  required")
        elif self.txtuser.get()=="kapu" and self.txtpass.get()=="ashu":
            messagebox.showinfo("success","Welcome")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email = %s and password = %s",(
                                                                        self.txtuser.get(), 
                                                                        self.txtpass.get()         

                                                                        ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password combination")
            else :
                self.new_window=Toplevel(self.root)
                self.app=HotelManagementSystem(self.new_window)
                conn.commit()
                conn.close()

    # ============== reset pass ==============
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select" :
            messagebox.showerror("Error","Select Security Question",parent=self.root2)
        elif self.txt_security.get()=="":
             messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
             messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else :
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="management")
            my_cursor=conn.cursor()
            qury=("select * from register where email = %s and securityQ = %s and securityA =%s")
            vlaue=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get())
            my_cursor.execute(qury,vlaue)
            row=my_cursor.fetchone()
            if row==None:
                 messagebox.showerror("Error","Please enter correct answer",parent=self.root2)
            else :
                query=("update register set password = %s where email = %s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your passwordhas been reset! Please login using new password",parent=self.root2)
                self.root2.destroy()
        


    # ============ foregt pass ==================
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the email address to reset Password")
        else :
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="management")
            my_cursor=conn.cursor()
            query=("Select * from register where email = %s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter valid username and password")
            else :
                conn.close()
                self.root2=Toplevel()
                self.root2.title=("Forgot Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forget password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your BirthPlace","Your Friend Name","Your Pet Name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)


                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_security.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_newpass.place(x=50,y=250,width=250)

                btn=Button(self.root2,command=self.reset_pass,text="Reset",font=("times new roman",15,"bold"),bg="green",fg="white")
                btn.place(x=100,y=290)


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System - Register")
        self.root.state('zoomed')
        #self.root.geometry("1600x900+0+0")

    
        #=========== variables =================================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
         

        # ======= bg image ===========
        self.bg= ImageTk.PhotoImage(file=r"C:\Users\vivek\Desktop\VIVEK\HMS\Hotel Management System\HOTEL MANAGEMENT SYSTEM\images\login back.jpg")  # path for image
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)


         # ======= bg image ===========
        self.bg1= ImageTk.PhotoImage(file=r"C:\Users\vivek\Desktop\VIVEK\HMS\Hotel Management System\HOTEL MANAGEMENT SYSTEM\images\wall.jpg")  # path for image
        bg_lbl=Label(self.root,image=self.bg1)
        bg_lbl.place(x=50,y=100,width=470,height=550)

        #============ main frame =============
        frame=Frame(self.root,bg="White")
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)

        #=================label and entry =======================
        # row 1
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15))
        self.fname_entry.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)

        # row2
        contact=Label(frame,text="Contact No.",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)

        # row 3
        security_Q=Label(frame,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your BirthPlace","Your Friend Name","Your Pet Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)


        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)

        # row4

        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)

        # chck btn_
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The terms & Conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

        #btns
        img=Image.open(r"C:\Users\vivek\Desktop\VIVEK\HMS\Hotel Management System\HOTEL MANAGEMENT SYSTEM\images\register.jpg")
        img=img.resize((200,55),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,borderwidth=0,command=self.register_data,cursor="hand2",font=("times new roman",15),fg="white")
        b1.place(x=10,y=420,width=200)

        img1=Image.open(r"C:\Users\vivek\Desktop\VIVEK\HMS\Hotel Management System\HOTEL MANAGEMENT SYSTEM\images\login.jpg")
        img1=img1.resize((200,45),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,borderwidth=0,command=self.return_login,cursor="hand2",font=("times new roman",15),fg="white")
        b1.place(x=330,y=420,width=200)

    #==== fndclrn =====

    def register_data(self):
        if self.var_fname.get()=="" or self.var_lname.get()=="" or self.var_contact.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select" or self.var_securityA.get()=="" or self.var_pass.get()=="" or self.var_confpass.get()=="":   
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password and confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and conditions")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="management")
            my_cursor=conn.cursor()
            query=("select * from register where email = %s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exists! Please try another email")
            else :
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
            messagebox.showinfo("Success","Registered Succesfully!")

    def return_login(self):
        self.root.destroy()

if __name__ == "__main__":
       main()   