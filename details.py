from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class DetailsRoom:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System - Manage Rooms")
        self.root.geometry("1300x550+225+220")
        #self.root.geometry("1295x550+230+220")

        # ==============title=======================
        lbl_title=Label(self.root,text="Manage Rooms",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)


        # ================logo=======================
        img2=Image.open(r"C:\Users\vivek\Desktop\VIVEK\HMS\Hotel Management System\HOTEL MANAGEMENT SYSTEM\images\hotel_logo.png")
        img2=img2.resize((100,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lbing=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lbing.place(x=5,y=2,width=100,height=40)

        # =================labelFrame=================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",font=("arial",12,"bold"),padx=2,)
        labelframeleft.place(x=5,y=50,width=540,height=350)

        # Floor
        lbl_floor=Label(labelframeleft,text="Floor",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W)

        self.var_floor=StringVar()
        enty_floor=ttk.Entry(labelframeleft,textvariable=self.var_floor,font=("arial",13,"bold"),width=20)
        enty_floor.grid(row=0,column=1,sticky=W)

        # Room No
        lbl_RoomNo=Label(labelframeleft,text="Room No.",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_RoomNo.grid(row=1,column=0,sticky=W)

        self.var_roomNo=StringVar()
        enty_RoomNo=ttk.Entry(labelframeleft,textvariable=self.var_roomNo,font=("arial",13,"bold"),width=20)
        enty_RoomNo.grid(row=1,column=1,sticky=W)

        # Room Type
        lbl_RoomType=Label(labelframeleft,text="Room Type",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_RoomType.grid(row=2,column=0,sticky=W)

        self.var_RoomType=StringVar()
        combo_id=ttk.Combobox(labelframeleft,textvariable=self.var_RoomType,font=("arial",12,"bold"),width=27,state="readonly")
        combo_id["value"]=("Single","Double","Triple","Luxury")
        combo_id.current(0)
        combo_id.grid(row=2,column=1)
        # enty_RoomType=ttk.Entry(labelframeleft,textvariable=self.var_RoomType,font=("arial",13,"bold"),width=20)
        # enty_RoomType.grid(row=2,column=1,sticky=W)

        # ========================Buttons==========================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnReset.grid(row=0,column=3,padx=1)

        # ===================table frame search system===============
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Details Panel",font=("arial",12,"bold"),padx=2,pady=6)
        Table_Frame.place(x=600,y=55,width=600,height=350)

        scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)
        self.room_table=ttk.Treeview(Table_Frame,column=("floor","roomno","roomType"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("floor",text="Floor")
        self.room_table.heading("roomno",text="Room No")
        self.room_table.heading("roomType",text="Room Type")
        
        self.room_table["show"]="headings"

        self.room_table.column("floor",width=100)
        self.room_table.column("roomno",width=100)
        self.room_table.column("roomType",width=100)
        
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_floor.get() == "" or self.var_RoomType.get() == "" or self.var_roomNo.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="", database="management")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)", (
                                                                            self.var_floor.get(),
                                                                            self.var_roomNo.get(),
                                                                            self.var_RoomType.get()
                                                                            


                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                conn = mysql.connector.connect(host="localhost", username="root", password="", database="management")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into roomavail values(%s,%s)", (
                                                                            self.var_roomNo.get(),
                                                                            self.var_RoomType.get()
                                                                            


                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "New room added successfully", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went Wrong:{str(es)}", parent=self.root)

    #fetch data
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from details")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    #getcursor
    def get_cursor(self, event=""):
            cursor_row = self.room_table.focus()
            content = self.room_table.item(cursor_row)
            row = content["values"]
            
            self.var_floor.set(row[0]),
            self.var_roomNo.set(row[1]),
            self.var_RoomType.set(row[2])

    # update function
    def update(self):
            if self.var_floor.get() == "" or self.var_RoomType.get() == "" or self.var_roomNo.get()=="":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
            else:
                conn = mysql.connector.connect(host="localhost", username="root", password="", database="management")
                my_cursor = conn.cursor()
                my_cursor.execute("update details set Floor=%s,RoomType=%s where RoomNo=%s",(
                                        self.var_floor.get(),
                                        self.var_RoomType.get(),
                                        self.var_roomNo.get()
                                        ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Update", "New room details have been updated successfully", parent=self.root)
                conn = mysql.connector.connect(host="localhost", username="root", password="", database="management")
                my_cursor = conn.cursor()
                my_cursor.execute("update roomavail set RoomType=%s where RoomNo=%s",(
                                        self.var_RoomType.get(),
                                        self.var_roomNo.get()
                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()

    def mDelete(self):
                    mDelete = messagebox.askyesno("Hotel management System", "Do you want to delete these room details?", parent=self.root)
                    if mDelete > 0:
                        conn = mysql.connector.connect(host="localhost", username="root", password="", database="management")
                        my_cursor = conn.cursor()
                        query = "delete from details where RoomNo=%s"
                        value = (self.var_roomNo.get(),)
                        my_cursor.execute(query, value)
                        query = "delete from roomavail where RoomNo=%s"
                        value = (self.var_roomNo.get(),)
                        my_cursor.execute(query, value)
                    else:
                        if not mDelete:
                            return
                    conn.commit()
                    self.fetch_data()
                    conn.close()

    def reset_data(self):
        self.var_floor.set(""),
        self.var_roomNo.set(""),
        self.var_RoomType.set("")

if __name__=="__main__":
    root=Tk()
    obj=DetailsRoom(root)
    root.mainloop()