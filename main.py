from tkinter import *
from tkinter import ttk
#import pymysql
import mysql.connector as mq
from tkinter import messagebox
passwd=''
dtb="school"
chst='utf8'


class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")
        title=Label(self.root,text="Student Management System",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="black",fg="light blue")
        title.pack(side=TOP,fill=X)


        #All variables---------------------
        self.Roll_no_var=StringVar()
        self.Name_var=StringVar()
        self.Email_var=StringVar()
        self.Gender_var=StringVar()
        self.Contact_var=StringVar()
        self.Dob_var=StringVar()


        self.search_by_var=StringVar()
        self.search_value_var=StringVar()


        # -------------------Manage Frame Details---------------------------------
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="black")
        Manage_Frame.place(x=20,y=100,width=450,height=580)
        m_title=Label(Manage_Frame,text="Manage Student",bg="black",fg="light blue",font=("constantia",20,"bold"))
        m_title.grid(row=0,columnspan=2, pady=10,padx=10)
        lbl_rollno=Label(Manage_Frame,bd=4,text="Roll number",font=("constantia",15,"bold"),bg="black",fg="light blue")
        lbl_rollno.grid(row=1,column=0,padx=20,pady=10,sticky="w")
        txt_Rollno=Entry(Manage_Frame,textvariable=self.Roll_no_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Rollno.grid(row=1,column=1,padx=10,pady=10,sticky="w")
        lbl_name=Label(Manage_Frame,text="Name",bd=4,font=("constantia",15,"bold"),bg="black",fg="light blue")
        lbl_name.grid(row=2,column=0,padx=20,pady=10,sticky='w')
        txt_Name=Entry(Manage_Frame,textvariable=self.Name_var,bd=5,font=("times new roman",15,"bold"),relief=GROOVE)
        txt_Name.grid(row=2,column=1,padx=10,pady=10,sticky="w")
        lbl_Email=Label(Manage_Frame,text="Email ID",font=("constantia",15,"bold"),bg="black",fg="light blue")
        lbl_Email.grid(row=3,column=0,padx=20,pady=10,sticky="w")
        txt_Email=Entry(Manage_Frame,textvariable=self.Email_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Email.grid(row=3,column=1,padx=10,pady=10,sticky="w")
        lbl_Gender=Label(Manage_Frame,text="Gender",bd=4,bg="black",fg="light blue",font=("constantia",15,"bold"))
        lbl_Gender.grid(row=4,column=0,padx=20,pady=10,sticky="w")
        combo_Gender=ttk.Combobox(Manage_Frame,textvariable=self.Gender_var,font=("times new roman",13,"bold"),state="readonly")
        combo_Gender["values"]=("Male","Female","Other")
        combo_Gender.grid(row=4,column=1,padx=10,pady=10)
        lbl_Cotact=Label(Manage_Frame,text="Contact",fg="light blue",bg="black",bd=4,font=("constantia",15,"bold"))
        lbl_Cotact.grid(row=5,column=0,padx=20,pady=10,sticky="w")
        txt_Contact=Entry(Manage_Frame,textvariable=self.Contact_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Contact.grid(row=5,column=1,padx=10,pady=10,sticky="w")


        lbl_DOB=Label(Manage_Frame,text="D.O.B",bg="black",fg="light blue",bd=4,font=("constantia",15,"bold"))
        lbl_DOB.grid(row=6,column=0,padx=20,pady=10,sticky="w")
        txt_DOB=Entry(Manage_Frame,textvariable=self.Dob_var,bd=5,font=("times new roman",15,"bold"),relief=GROOVE)
        txt_DOB.grid(row=6,column=1,padx=10,pady=20,sticky="w")
        lbl_Address=Label(Manage_Frame,text="Address",bd=4,bg="black",fg="light blue",font=("constantia",15,"bold"))
        lbl_Address.grid(row=7,column=0,padx=20,pady=10,sticky="w")
        self.txt_Address=Text(Manage_Frame,font=("times new roman",15,"bold"),height=4,width=20)
        self.txt_Address.grid(row=7,column=1,padx=10,pady=10,sticky="w")
        btn_Frame=Frame(Manage_Frame,bd=1,relief=RIDGE,bg="black")
        btn_Frame.place(x=20,y=520,width=370,height=40)
        btn_Add=Button(btn_Frame,text="Add",width=10,command=self.add_student_fun)
        btn_Add.grid(row=0,column=0,padx=5,pady=5,sticky="w")
        btn_Update=Button(btn_Frame,text="Update",width=10,command=self.update_data_fun)
        btn_Update.grid(row=0,column=1,padx=5,pady=5,sticky="w")
        btn_Delete=Button(btn_Frame,text="Delete",width=10,command=self.delete_data_fun)
        btn_Delete.grid(row=0,column=2,padx=5,pady=5,sticky="w")
        btn_Clear=Button(btn_Frame,text="Clear",width=10,command=self.clear)
        btn_Clear.grid(row=0,column=3,padx=5,pady=5,sticky="w")


        # -------------------Details Frame Details---------------------------------
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="black")
        Detail_Frame.place(x=500,y=100,width=830,height=580)
        lbl_Search=Label(Detail_Frame,text="Search",bg="black",fg="lightblue",font=("constantia",20,"bold"),bd=4)
        lbl_Search.grid(row=0,column=0,padx=20,pady=20,sticky="w")
        combo_Search=ttk.Combobox(Detail_Frame,font=("constantia",13,"bold"),state="readonly",width=10,textvariable=self.search_by_var)
        combo_Search['values']=('RollNo','Name','Contact')
        combo_Search.grid(row=0,column=1,padx=10,pady=10,sticky="w")
        txt_Search=Entry(Detail_Frame,bd=5,font=("constantia",13,"bold"),relief=GROOVE,textvariable=self.search_value_var)
        txt_Search.grid(row=0,column=2,padx=10,pady=10,sticky="w")
        btn_Search=Button(Detail_Frame,text="Search",width=10,font=("",10),command=self.search_student_fun)
        btn_Search.grid(row=0,column=3,padx=10,pady=10,sticky="w")
        btn_SearchAll=Button(Detail_Frame,text="Search All",width=10,font=("",10),command=self.fetch_student_fun)
        btn_SearchAll.grid(row=0,column=4,padx=10,pady=10,sticky="w")


        table_Frame=Frame(Detail_Frame,bg="black",relief=RIDGE,bd=4)
        table_Frame.place(x=10,y=80,height=480,width=800)


        scroll_x=Scrollbar(table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_Frame,orient=VERTICAL)
        self.student_Table=ttk.Treeview(table_Frame,columns=("rollno","name","email","gender","contact","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_Table.xview)
        scroll_y.config(command=self.student_Table.yview)
        self.student_Table.heading("rollno",text="Roll No")
        self.student_Table.heading("name",text="Name")
        self.student_Table.heading("email",text="Email ID")
        self.student_Table.heading("gender",text="Gender")
        self.student_Table.heading("contact",text="Contact")
        self.student_Table.heading("dob",text="D.O.B")
        self.student_Table.heading("address",text="Address")
        self.student_Table['show']='headings'
        self.student_Table.column("rollno",width=50)
        self.student_Table.column("name",width=100)
        self.student_Table.column("email",width=150)
        self.student_Table.column("gender",width=50)
        self.student_Table.column("contact",width=150)
        self.student_Table.column("dob",width=50)
        self.student_Table.column("address",width=200)
        self.student_Table.pack(fill=BOTH,expand=1)
        self.student_Table.bind('<ButtonRelease-1>',self.get_cursor)
        self.fetch_student_fun()
    def add_student_fun(self):
        con=mq.connect(host='localhost',user='root',password=passwd,database='school',charset=chst)
        cur=con.cursor()
        cur.execute("insert into student1 values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_no_var.get(),self.Name_var.get(),
                                                                        self.Email_var.get(),
                                                                        self.Gender_var.get(),
                                                                        self.Contact_var.get(),
                                                                        self.Dob_var.get(),
                                                                        self.txt_Address.get('1.0',END)                                                                                                                                               
                                                                        ))
        con.commit()
        self.fetch_student_fun()
        self.clear()
        con.close()
    def fetch_student_fun(self):
        con=mq.connect(host='localhost',user='root',password=passwd,database='school',charset=chst)
        cur=con.cursor()
        cur.execute("select * from student1")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_Table.delete(*self.student_Table.get_children())
            for row in rows:
                self.student_Table.insert('',END,values=row)
            con.commit()
        con.close()
    def clear(self):
        self.Roll_no_var.set("")
        self.Name_var.set("")
        self.Email_var.set("")
        self.Gender_var.set("")
        self.Contact_var.set("")
        self.Dob_var.set("")
        self.txt_Address.delete("1.0",END)
    
    def get_cursor(self,ev):
        
        cursor_row_var=self.student_Table.focus()
        content_var=self.student_Table.item(cursor_row_var)
        row=content_var['values']
        self.Roll_no_var.set(row[0])
        self.Name_var.set(row[1])
        self.Email_var.set(row[2])
        self.Gender_var.set(row[3])
        self.Contact_var.set(row[4])
        self.Dob_var.set(row[5])
        self.txt_Address.delete('1.0',END)
        self.txt_Address.insert(END,row[6])
    def update_data_fun(self):
        con=mq.connect(host='localhost',user='root',password=passwd,database='school',charset=chst)
        cur=con.cursor()
        cur.execute("update student1 set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where rollno=%s",(self.Name_var.get(),
                                                                                                  self.Email_var.get(),
                                                                                                  self.Gender_var.get(),
                                                                                                  self.Contact_var.get(),
                                                                                                  self.Dob_var.get(),
                                                                                                  self.txt_Address.get("1.0",END),
                                                                                                  self.Roll_no_var.get()
                                                                                                  ))
        con.commit()
        self.fetch_student_fun()
        self.clear() 
        con.close()
    def delete_data_fun(self):
        con=mq.connect(host='localhost',user='root',password=passwd,database='school',charset=chst)
        cur=con.cursor()
        str1="delete from student1 where rollno='{}'".format(self.Roll_no_var.get())
        cur.execute(str1)
        con.commit()
        self.fetch_student_fun()
        self.clear()
        con.close()                                                                                                                                                                                                 


    def search_student_fun(self):
        print("Search")
        con=mq.connect(host='localhost',user='root',password=passwd,database='school',charset=chst)
        cur=con.cursor()
        str1="select * from student1 where "+str(self.search_by_var.get())+" LIKE '%"+str(self.search_value_var.get())+"%'"
        print(str1)
        cur.execute(str1)
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_Table.delete(*self.student_Table.get_children())
            for row in rows:
                self.student_Table.insert('',END,values=row)
        con.commit()
        con.close()  
        


root=Tk()
ob=Student(root)
root.mainloop()
