# Libraries 

from tkinter import *
from tkinter import messagebox
from datetime import datetime


# Connect with database (mysql)
import pymysql
conn = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "taruns22",
    db = "Attendance"
)


# GUI 
main = Tk()
main.geometry("1650x1000")
l1 = Label(main,text="Attendance Management System",font=('Arial',30))
def Attendance():
    Attend = Tk()
    Attend.geometry('1650x1000')
    Emp_id = Label(Attend,text="Enter Employee Id",font=('Arial',35))
    Id = Entry(Attend,font=('Arial',30))

    def Confirm():
        emp_id = Id.get()
        Query = "SELECT emp_id FROM Employees WHERE emp_id ='"+emp_id+"'"
        cursor = conn.cursor()
        cursor.execute(Query)
        data = cursor.fetchall()

        if data:
            data = Tk()
            data.geometry('1650x1000')
            emp_id = Id.get()
            Query = "SELECT emp_id, name, department FROM employees where emp_id = '"+emp_id+"'"
            cur = conn.cursor()
            cur.execute(Query)
            entry = cur.fetchall()
            for x in entry:
                l1 = Label(data, text=str(x[0]),font=('Arial',30))
                l2 = Label(data, text=str(x[1]),font=('Arial',30))
                l3 = Label(data, text=str(x[2]),font=('Arial',30))

            def Attendance_done():
                emp_id = Id.get()
                login = datetime.now()
                login_date = login.strftime('%Y-%m-%d')
                in_time = login.strftime('%H:%M:%S')
                Query = "INSERT INTO Attendance VALUES('"+emp_id+"','"+login_date+"','"+in_time+"')"
                cur = conn.cursor()
                cur.execute(Query)
                conn.commit()
                messagebox.showinfo(" ","Present")
                Attend.destroy()
                data.destroy()
                
            def cancel():
                messagebox.showinfo(" ","Thank you")
                Attend.destroy()
                data.destroy()

            yes = Button(data,text="YES",font=('Arial',30),command=Attendance_done)
            no = Button(data,text="NO",font=('Arial',30), command=cancel)
            

            l1.place(x=320,y=100)
            l2.place(x=320,y=150)
            l3.place(x=320,y=200)
            yes.place(x=200,y=400)
            no.place(x=500,y=400)
            
            data.mainloop()
        else:
            messagebox.showinfo(' ',"Employee ID not available")
            Attend.destroy()
    
    def cancel():
        messagebox.showinfo(" ","Thank you")
        Attend.destroy()
    Confirm = Button(Attend, text="Confirm",font=('Arial',20),width=20,height=2,command=Confirm)
    Cancel = Button(Attend, text="Cancel",font=('Arail',20),width=20,height=2,command=cancel)

    
    Emp_id.place(x=520,y=200)
    Id.place(x=520,y=300)
    Confirm.place(x=400,y=500)
    Cancel.place(x=750,y=500)
    Attend.mainloop()

# l3 = Label(main,text="Enter 

def log_out():
    logout = Tk()
    logout.geometry("1650x1000")
    l1 = Label(logout,text="Enter Employee ID",font=('Arial',35))
    Id = Entry(logout,font=('Arial',30))
    
    

    def Confirm2():
        emp_id = Id.get()
        Query = "SELECT * FROM Attendance WHERE emp_id = '"+emp_id+"' AND login_date = CURDATE()"
        cur = conn.cursor()
        cur.execute(Query)
        att = cur.fetchall()
        if att:
        
            Query = "SELECT emp_id FROM employees WHERE emp_id ='"+emp_id+"'"
            cursor = conn.cursor()
            cursor.execute(Query)
            data = cursor.fetchall()
        
            if data:
                data = Tk()
                data.geometry('1650x1000')
                emp_id = Id.get()
                Query = "SELECT emp_id, name, department FROM employees where emp_id = '"+emp_id+"'"
                cur = conn.cursor()
                cur.execute(Query)
                entry = cur.fetchall()
                for x in entry:
                    l1 = Label(data, text=str(x[0]),font=('Arial',30))
                    l2 = Label(data, text=str(x[1]),font=('Arial',30))
                    l3 = Label(data, text=str(x[2]),font=('Arial',30))
        
                def Logout_done():
                    emp_id = Id.get()
                    logout_com = datetime.now()
                    logout_date = logout_com.strftime('%Y-%m-%d')
                    out_time = logout_com.strftime('%H:%M:%S')
                    Query = "INSERT INTO Log_out VALUES('"+emp_id+"','"+logout_date+"','"+out_time+"')"
                    cur = conn.cursor()
                    cur.execute(Query)
                    conn.commit()
                    messagebox.showinfo(" ","LOG OUT")
                    logout.destroy()
                    data.destroy()
                        
                def cancel():
                    messagebox.showinfo(" ","Thank you")
                    logout.destroy()
                    data.destroy()
        
                yes = Button(data,text="YES",font=('Arial',30),command=Logout_done)
                no = Button(data,text="NO",font=('Arial',30), command=cancel)
                    
        
                l1.place(x=320,y=100)
                l2.place(x=320,y=150)
                l3.place(x=320,y=200)
                yes.place(x=200,y=400)
                no.place(x=500,y=400)
                    
                data.mainloop()
            else:
                messagebox.showinfo(' ',"not available")
                logout.destroy()

        else:
            messagebox.showinfo("Error","Please Mark first your attendance")
            logout.destroy()

    def cancel():
        messagebox.showinfo(" ","Thank you")
        logout.destroy()
    Confirm = Button(logout,text="Confirm",font=('Arial',20),width=20,height=2,command=Confirm2)
    Cancel = Button(logout,text="Cancel",font=('Arial',20),width=20,height=2,command=cancel)

    l1.place(x=520,y=200)
    Id.place(x=520,y=300)
    Confirm.place(x=400,y=500)
    Cancel.place(x=750,y=500)
    logout.mainloop()






b1 = Button(main,text="Mark Attendance",font=('Arial',30),width=20,height=2,command=Attendance)
b2 = Button(main,text="Log Out", font=('Arial',30),width=20,height=2,command=log_out)




l1.pack()
b1.place(x=520,y=250)
b2.place(x=520,y=400)


main.mainloop()
