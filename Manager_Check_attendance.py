from tkinter import *
from tkinter import messagebox
from datetime import datetime

import pymysql
conn = pymysql.connect(
    host = "localhost",
    user = "root",
    password = , # Enter your database password
    db = "Attendance"
)
cursor = conn.cursor()

database = Tk()
database.geometry("1650x1000")
heading = Label(database, text="Data",font=('Arial',30))

def New_employee():
    New = Tk()
    New.geometry("1650x1000")
    L1 = Label(New, text="Enter New Employee Name",font=('Arial',20))
    L2 = Label(New, text="Enter Department",font=('Arial',20))
    L3 = Label(New, text="Enter mobile number",font=('Arial',20))
    L4 = Label(New, text="Shift start timing",font=('Arial',20))
    L5 = Label(New, text="Shift end timing",font=('Arial',20))
    name = Entry(New,font=('Arial',20))
    department = Entry(New,font=('Arial',20))
    mobile_no = Entry(New,font=('Arial',20))
    shift_start = Entry(New,font=('Arial',20))
    shift_end = Entry(New,font=('Arial',20))

    
    
    def Confirm():
        Name = name.get()
        Department = department.get()
        Mobile_no = mobile_no.get()
        Shift_start = shift_start.get()
        Shift_end = shift_end.get()
        if Name=="" or Department=="" or Mobile_no=="" or Shift_start=="" or Shift_end=="":
            messagebox.showinfo("Warning","Please Enter all details")
            New.destroy()
        else:
            Query = "INSERT INTO Employees(name, department, mobile_no, shift_start, shift_end) VALUES('"+Name+"','"+Department+"','"+Mobile_no+"','"+Shift_start+"','"+Shift_end+"')"
            cursor.execute(Query)
            conn.commit()
            
            Id = Tk()
            Id.geometry("500x300")
            Query = "SELECT emp_id FROM Employees WHERE mobile_no='"+Mobile_no+"'"
            cursor.execute(Query)
            empid = cursor.fetchall()
            for x in empid:
                L = Label(Id,text="Your Employee Id is ",font=('Arial',20))
                L1 = Label(Id,text=str(x[0]),font=('Arial',20))
        
            def ok():
                messagebox.showinfo("Registration","Thank you")
                New.destroy()
                Id.destroy()
            B1 = Button(Id,text="OK",font=('Aria',20),command=ok)
            L.pack(side=TOP,anchor='sw',fill=X)
            L1.place(x=200,y=50)
            B1.place(x=200,y=150)
            Id.mainloop()
    
    def cancel():
        messagebox.showinfo(" " ,"Cancelled")
        New.destroy()
    
    b1 = Button(New,text="Confirm",font=('Arial',30),width=15,height=2,command=Confirm)
    b2 = Button(New,text="Cancel",font=('Arial',30),width=15,height=2,command=cancel)
    L1.place(x=320,y=100)
    name.place(x=820,y=105)
    
    L2.place(x=320,y=200)
    department.place(x=820,y=205)
    
    L3.place(x=320,y=310)
    mobile_no.place(x=820,y=315)
    
    L4.place(x=320,y=430)
    shift_start.place(x=820,y=435)
    
    L5.place(x=320,y=540)
    shift_end.place(x=820,y=545)
    
    
    b1.place(x=300,y=650)
    b2.place(x=750,y=650)
    New.mainloop()

def check_id():
    showdata = Toplevel()
    showdata.geometry("700x500")
    showdata.title("Accounts")
    l = Label(showdata,text="Employee Data",font=('Arial',30))
    l1 = Label(showdata,text="Enter Employee ID",font=('Arial',20))
    t1 = Entry(showdata,font=('Arial',15))

    def data():
        emp_id = t1.get()
        Query = "select emp_id from Employees where emp_id = '"+emp_id+"'"
        cur = conn.cursor()
        cur.execute(Query)
        ids = cur.fetchall()
        if ids:
            showdata2 = Toplevel()
            showdata2.geometry("1650x1000")
            Query = "select * from Employees where emp_id = '"+emp_id+"'"
            cur = conn.cursor()
            cur.execute(Query)
            row = cur.fetchall()
            l1 = Label(showdata2,text="Employee Id :",font=('Arial',30))
            l2 = Label(showdata2,text="Employee Name :",font=('Arial',30))
            l3 = Label(showdata2,text="Department :",font=('Arial',30))
            l4 = Label(showdata2,text="Mobile Number :",font=('Arial',30))
            l5 = Label(showdata2,text="Shift Start Time :",font=('Arial',30))
            l6 = Label(showdata2,text="Shift End Time :",font=('Arial',30))
            
            for Employees in row:
                l7 = Label(showdata2,text=str(Employees[0]),font=('Arial',30))
                l8 = Label(showdata2,text=str(Employees[1]),font=('Arial',30))
                l9 = Label(showdata2,text=str(Employees[2]),font=('Arial',30))
                l10 = Label(showdata2,text=str(Employees[3]),font=('Arial',30))
                l11 = Label(showdata2,text=str(Employees[4]),font=('Arial',30))
                l12 = Label(showdata2,text=str(Employees[5]),font=('Arial',30))
    
            def end():
                messagebox.showinfo("Done","Thank you")
                showdata.destroy()
                showdata2.destroy()
            b1 = Button(showdata2,text="Exit",font=('Arial',25),command=end)
            l1.place(x=320,y=50)
            l7.place(x=820,y=50)
    
            l2.place(x=320,y=150)
            l8.place(x=820,y=150)
    
            l3.place(x=320,y=250)
            l9.place(x=820,y=250)
    
            l4.place(x=320,y=350)
            l10.place(x=820,y=350)
    
            l5.place(x=320,y=450)
            l11.place(x=820,y=450)
    
            l6.place(x=320,y=550)
            l12.place(x=820,y=550)
            
            b1.place(x=570,y=700)
            showdata2.mainloop()

        else:
            messagebox.showinfo('Error',"Employee Id not available")
            showdata.destroy()
                                

    def cancel():
        messagebox.showinfo("Cancelled","Thank You")
        showdata.destroy()

    b1 = Button(showdata,text="Press for Details",font=('Arial',15),width=20,height=1,command=data)
    b2 = Button(showdata,text="Cancel",font=('Arial',15),width=20,height=1,command=cancel)

    l.pack(side=TOP,anchor='sw',fill=X)
    l1.place(x=50,y=150)
    t1.place(x=325,y=155)
    b1.place(x=100,y=250)
    b2.place(x=400,y=250)
    showdata.mainloop()

def check_attendance():
    attendance = Tk()
    attendance.geometry("700x500")
    L1 = Label(attendance,text="Enter Employee ID",font=("Arial",30))
    L2 = Label(attendance,text="Enter Date 'Y-M-D'",font=("Arial",30))
    ID = Entry(attendance,font=('Arial',18))
    Date = Entry(attendance,font=('Arial',18))

    def output():
        emp_id = ID.get()
        login_date = Date.get()
        Query = "SELECT `Employee ID` FROM Attendance_data WHERE `Employee ID` = '"+emp_id+"' AND `Check in date` = '"+login_date+"'"
        cursor.execute(Query)
        data = cursor.fetchall()
        
        if data:
            showdata2 = Toplevel()
            showdata2.geometry("1650x1000")
            Query = "SELECT * FROM Attendance_data WHERE `Employee ID` = '"+emp_id+"' AND `Check in date` = '"+login_date+"'"
            cur = conn.cursor()
            cur.execute(Query)
            row = cur.fetchall()
            l1 = Label(showdata2,text="Employee Id :",font=('Arial',30))
            l2 = Label(showdata2,text="Check in date :",font=('Arial',30))
            l3 = Label(showdata2,text="Check in time :",font=('Arial',30))
            l4 = Label(showdata2,text="Check out date :",font=('Arial',30))
            l5 = Label(showdata2,text="Check out time :",font=('Arial',30))
            
            for Employees in row:
                l6 = Label(showdata2,text=str(Employees[0]),font=('Arial',30))
                l7 = Label(showdata2,text=str(Employees[1]),font=('Arial',30))
                l8 = Label(showdata2,text=str(Employees[2]),font=('Arial',30))
                l9 = Label(showdata2,text=str(Employees[3]),font=('Arial',30))
                l10 = Label(showdata2,text=str(Employees[4]),font=('Arial',30))
    
            def end():
                messagebox.showinfo("Done","Thank you")
                attendance.destroy()
                showdata2.destroy()
            b1 = Button(showdata2,text="Exit",font=('Arial',25),command=end)
            l1.place(x=320,y=50)
            l6.place(x=820,y=50)
    
            l2.place(x=320,y=150)
            l7.place(x=820,y=150)
    
            l3.place(x=320,y=250)
            l8.place(x=820,y=250)
    
            l4.place(x=320,y=350)
            l9.place(x=820,y=350)
    
            l5.place(x=320,y=450)
            l10.place(x=820,y=450)
            
            b1.place(x=570,y=700)
            showdata2.mainloop()


        else:
            messagebox.showinfo('Error',"Employee Id not available")
            attendance.destroy()

    def cancel():
        messagebox.showinfo("Cancelled","Thank You")
        attendance.destroy()

    b1 = Button(attendance,text="Press for Details",font=('Arial',15),width=20,height=1,command=output)
    b2 = Button(attendance,text="Cancel",font=('Arial',15),width=20,height=1,command=cancel)

    L1.place(x=50,y=75)
    L2.place(x=50,y=150)
    ID.place(x=400,y=80)
    Date.place(x=400,y=155)
    b1.place(x=100,y=290)
    b2.place(x=400,y=290)
            
    attendance.mainloop()

B1 = Button(database, text="Add New Employee",font=('Arial',30),width=20, height=2,command=New_employee)
B2 = Button(database, text="Check by ID", font=('Arial',30),width=20, height=2,command=check_id)
B3 = Button(database, text="Check attendance", font=('Arial',30),width=20, height=2,command=check_attendance)
B1.place(x=520,y=200)
B2.place(x=520,y=350)
B3.place(x=520,y=500)
heading.place(x=700,y=50)
database.mainloop()
