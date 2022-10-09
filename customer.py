from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox

class Cust_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System - Customer Details")
        self.root.geometry("1300x550+225+220")
        #self.root.geometry("1295x550+230+220")

        #======Variables====
        self.var_ref=StringVar()
       
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="management")
        my_cursor=conn.cursor()

        my_cursor.execute("SELECT MAX(Ref) AS maximum FROM customer")
        rows=my_cursor.fetchall()
        for i in rows:
            j=int(0 if i[0] is None else i[0])
            x=j+1
            conn.commit()
        conn.close()

        # x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_surname=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_address=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()

        # ================== TITLE  =============
        lbl_title=Label(self.root,text="Manage Customer Details",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)


        # ==================== logo =======================
        img2=Image.open(r"C:\Users\vivek\Desktop\VIVEK\HMS\Hotel Management System\HOTEL MANAGEMENT SYSTEM\images\hotel_logo.png")
        img2=img2.resize((100,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

        # ==================== label frame =======================
        lableframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("arial",12,"bold"),padx=2)
        lableframeleft.place(x=5,y=50,width=425,height=490)

        # ==================== labels and entries =================
        lbl_cust_ref=Label(lableframeleft,text="Customer Ref",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)


        entry_ref=ttk.Entry(lableframeleft,textvariable=self.var_ref,width=29,font=("arial",13,"bold"),state="readonly")
        entry_ref.grid(row=0,column=1)


        # ================== cust name =======
        cname=Label(lableframeleft,font=("arial",12,"bold"),text="Customer Name:",padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)
        txtcname=ttk.Entry(lableframeleft,textvariable=self.var_cust_name,font=("arial",13,"bold"),width=29)
        txtcname.grid(row=1,column=1)

         # ===============surname name =======
        lblmname=Label(lableframeleft,font=("arial",12,"bold"),text="Surname:",padx=2,pady=6)
        lblmname.grid(row=2,column=0,sticky=W)
        txtmname=ttk.Entry(lableframeleft,textvariable=self.var_surname,font=("arial",13,"bold"),width=29)
        txtmname.grid(row=2,column=1)

        # gender combobox
        label_gender=Label(lableframeleft,font=("arial",12,"bold"),text="Gender :",padx=2,pady=6)
        label_gender.grid(row=3,column=0,sticky=W)

        combo_gender=ttk.Combobox(lableframeleft,textvariable=self.var_gender,font=("arial",12,"bold"),width=27,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)

        # postcode
        lblPostCode=Label(lableframeleft,font=("arial",12,"bold"),text="PostCode :",padx=2,pady=6)
        lblPostCode.grid(row=4,column=0,sticky=W) 
        txtPostCode=ttk.Entry(lableframeleft,textvariable=self.var_post,font=("arial",13,"bold"),width=29)
        txtPostCode.grid(row=4,column=1)

        # mobile num
        lblMobile=Label(lableframeleft,font=("arial",12,"bold"),text="Mobile Number :",padx=2,pady=6)
        lblMobile.grid(row=5,column=0,sticky=W) 
        txtMobile=ttk.Entry(lableframeleft,textvariable=self.var_mobile,font=("arial",13,"bold"),width=29)
        txtMobile.grid(row=5,column=1)

        # email address
        lblEmail=Label(lableframeleft,font=("arial",12,"bold"),text="Email ID :",padx=2,pady=6)
        lblEmail.grid(row=6,column=0,sticky=W) 
        txtEmail=ttk.Entry(lableframeleft,textvariable=self.var_email,font=("arial",13,"bold"),width=29)
        txtEmail.grid(row=6,column=1)

        # nationality 
        lblNationality=Label(lableframeleft,font=("arial",12,"bold"),text="Nationality :",padx=2,pady=6)
        lblNationality.grid(row=7,column=0,sticky=W)

        combo_Nationality=ttk.Entry(lableframeleft,textvariable=self.var_nationality,font=("arial",12,"bold"),width=29)
        #combo_Nationality["value"]=("Indian","American","British")
        #combo_Nationality.current(0)
        combo_Nationality.grid(row=7,column=1)

        # idproof
        lblIdProof=Label(lableframeleft,font=("arial",12,"bold"),text="ID Proof Type :",padx=2,pady=6)
        lblIdProof.grid(row=8,column=0,sticky=W)

        combo_id=ttk.Combobox(lableframeleft,textvariable=self.var_id_proof,font=("arial",12,"bold"),width=27,state="readonly")
        combo_id["value"]=("Aadhar Card","Passport","International Driving Licence")
        combo_id.current(0)
        combo_id.grid(row=8,column=1)

        # id number
        lblIdNumber=Label(lableframeleft,font=("arial",12,"bold"),text="ID Number :",padx=2,pady=6)
        lblIdNumber.grid(row=9,column=0,sticky=W) 
        txtIdNumber=ttk.Entry(lableframeleft,textvariable=self.var_id_number,font=("arial",13,"bold"),width=29)
        txtIdNumber.grid(row=9,column=1)

        # address
        lblAddress=Label(lableframeleft,font=("arial",12,"bold"),text="Address :",padx=2,pady=6)
        lblAddress.grid(row=10,column=0,sticky=W) 
        txtAddress=ttk.Entry(lableframeleft,textvariable=self.var_address,font=("arial",13,"bold"),width=29)
        txtAddress.grid(row=10,column=1)

        # btns
        btn_frame=Frame(lableframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.Update,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnReset.grid(row=0,column=3,padx=1)

        # ==================== label frame =======================
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search Panel",font=("arial",12,"bold"),padx=2)
        Table_Frame.place(x=435,y=50,width=860,height=490)

        lblSearchBy=Label(Table_Frame,font=("arial",12,"bold"),text="Search By:",bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        
        self.search_var=StringVar()
        combo_Search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("arial",12,"bold"),width=24,state="readonly")
        combo_Search["value"]=("Ref","Name","Surname","Mobile")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_Frame,textvariable=self.txt_search,font=("arial",13,"bold"),width=24)
        txtSearch.grid(row=0,column=2,padx=2)
        
        btnSearch=Button(Table_Frame,command=self.search,text="Search",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Table_Frame,command=self.fetch_data,text="Show All",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnShowAll.grid(row=0,column=4,padx=1)

        ##### 44:50 v 2

        # Show data table
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=350)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(details_table,column=("ref","name","surname","gender","post","mobile","email",
                    "nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)


        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref",text="Ref Number")
        self.Cust_Details_Table.heading("name",text="Name")
        self.Cust_Details_Table.heading("surname",text="Surname")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("post",text="PostCode")
        self.Cust_Details_Table.heading("mobile",text="Mobile")
        self.Cust_Details_Table.heading("email",text="Email")
        self.Cust_Details_Table.heading("nationality",text="Nationality")
        self.Cust_Details_Table.heading("idproof",text="Id Proof")
        self.Cust_Details_Table.heading("idnumber",text="Id Number")
        self.Cust_Details_Table.heading("address",text="Address")

        self.Cust_Details_Table["show"]="headings"
        self.Cust_Details_Table.column("ref",width=100)
        self.Cust_Details_Table.column("name",width=100)
        self.Cust_Details_Table.column("surname",width=100)
        self.Cust_Details_Table.column("gender",width=100)
        self.Cust_Details_Table.column("post",width=100)
        self.Cust_Details_Table.column("mobile",width=100)
        self.Cust_Details_Table.column("email",width=100)
        self.Cust_Details_Table.column("nationality",width=100)
        self.Cust_Details_Table.column("idproof",width=100)
        self.Cust_Details_Table.column("idnumber",width=100)
        self.Cust_Details_Table.column("address",width=100)

        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_mobile.get()=="" or self.var_surname.get()=="" or self.var_address.get()=="" or self.var_cust_name.get()=="" or self.var_gender.get()=="" or self.var_id_number.get()=="" or self.var_post.get()=="" or self.var_nationality.get()=="" or self.var_email.get()=="" or self.var_id_proof.get()=="" or self.var_ref.get()=="":   
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.var_nationality.get()=="Indian" and len(self.var_mobile.get())!=10:
            messagebox.showerror("Error","For Indian nationality, mobile number must be of 10 digits only'",parent=self.root)
        elif self.var_nationality.get()!="Indian" and self.var_id_proof.get()=="Aadhar Card":
            messagebox.showerror("Error",f"Aadhar Card is not valid for this country. Please try Passport or International Driving Licence")
        elif self.var_id_proof.get()=="Aadhar Card" and len(self.var_id_number.get())!=12:
            messagebox.showerror("Error","Aadhar Number must be of 12 digits",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                            self.var_ref.get(),
                                                                            self.var_cust_name.get(),
                                                                            self.var_surname.get(),
                                                                            self.var_gender.get(),
                                                                            self.var_post.get(),
                                                                            self.var_mobile.get(),
                                                                            self.var_email.get(), 
                                                                            self.var_nationality.get(),
                                                                            self.var_id_proof.get(),
                                                                            self.var_id_number.get(),
                                                                            self.var_address.get()          

                                                                            ))
                conn.commit()
                self.fetch_data() 
                conn.close()                                                         
                messagebox.showinfo("Success","Customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went Wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
         conn=mysql.connector.connect(host="localhost",username="root",password="",database="management")
         my_cursor=conn.cursor()
         my_cursor.execute("select * from customer")
         rows=my_cursor.fetchall() 
         if len(rows)!=0:
                self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
                for i in rows:
                    self.Cust_Details_Table.insert("",END,values=i)
                conn.commit()
         conn.close()
#28:36

    def get_cursor(self,event=""):
        cursor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cursor_row)
        row=content["values"]

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_surname.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_id_proof.set(row[8]),
        self.var_id_number.set(row[9]),
        self.var_address.set(row[10])   

    def Update(self):
        if self.var_mobile.get()=="" or self.var_surname.get()=="" or self.var_address.get()=="" or self.var_cust_name.get()=="" or self.var_gender.get()=="" or self.var_id_number.get()=="" or self.var_post.get()=="" or self.var_nationality.get()=="" or self.var_email.get()=="" or self.var_id_proof.get()=="" or self.var_ref.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.var_nationality.get()=="Indian" and len(self.var_mobile.get())!=10:
            messagebox.showerror("Error","For Indian nationality, mobile number must be of 10 digits only'",parent=self.root)
        elif self.var_nationality.get()!="Indian" and self.var_id_proof.get()=="Aadhar Card":
            messagebox.showerror("Error",f"Aadhar Card is not valid for this country. Please try Passport or International Driving Licence")
        elif self.var_id_proof.get()=="Aadhar Card" and len(self.var_id_number.get())!=12:
            messagebox.showerror("Error","Aadhar Number must be of 12 digits",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update customer set Name=%s,Surname=%s,Gender=%s,PostCode=%s,Mobile=%s,Email=%s,Nationality=%s,Idproof=%s,Idnumber=%s,Address=%s where Ref=%s",(
                                                                         
                                self.var_cust_name.get(),
                                self.var_surname.get(),
                                self.var_gender.get(),
                                self.var_post.get(),
                                self.var_mobile.get(),
                                self.var_email.get(), 
                                self.var_nationality.get(),
                                self.var_id_proof.get(),
                                self.var_id_number.get(),
                                self.var_address.get(),   
                                self.var_ref.get()
            ))                                                          
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer details has been updated Successfully",parent=self.root)

    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel management System","Do you want to delete this customer?",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="management")
            my_cursor=conn.cursor()
            query="delete from customer where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        #self.var_ref.set("")
        self.var_cust_name.set(""),
        self.var_surname.set(""),
        #self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        #self.var_nationality.set(""),
        #self.var_id_proof.set(""),
        self.var_id_number.set(""),
        self.var_address.set(""),
       
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="management")
        my_cursor=conn.cursor()

        my_cursor.execute("SELECT MAX(Ref) AS maximum FROM customer")
        rows=my_cursor.fetchall()
        for i in rows:
            j=int(0 if i[0] is None else i[0])
            x=j+1
            conn.commit()
        conn.close()

        # x=random.randint(1000,9999)
        self.var_ref.set(str(x))

    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="management")
        my_cursor=conn.cursor()

        my_cursor.execute("select * from customer where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()

if __name__ == "__main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()