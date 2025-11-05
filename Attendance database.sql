CREATE DATABASE Attendance;
USE Attendance;


CREATE TABLE Employees(
	emp_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(50),
    mobile_no BIGINT,
    shift_start TIME,
    shift_end TIME
)AUTO_INCREMENT = 101;

CREATE TABLE Attendance(
	emp_id INT,
    login_date DATE,
    in_time TIME,
    FOREIGN KEY (emp_id) REFERENCES Employees(emp_id)
);

CREATE TABLE Log_out(
	emp_id INT,
    logout_date DATE,
    out_time TIME,
    FOREIGN KEY (emp_id) REFERENCES Employees(emp_id)
);

CREATE VIEW Attendance_data
AS
SELECT a.emp_id as "Employee ID", a.login_date as "Check in date", a.in_time as "Check in time",  L.logout_date as "Check out date", L.out_time as "Check out time" 
FROM Attendance as a JOIN Log_out as L 
ON a.emp_id = L.emp_id;

SELECT * FROM Attendance_data;
select * from Attendance_data where `Employee ID`=107;
SELECT * FROM Attendance_data WHERE Date(`Check in date`) BETWEEN '2025-10-01' AND '2025-10-20';



drop view attendance_data;
-- delimiter \\
-- CREATE TRIGGER 
select * from Employees
select Emp_ID from employees
select * from attendance

DROP TABLE ATTENDANCE;
DROP TABLE Log_out;
DROP TABLE Employees;
DROP VIEW Attendance_data

Delete from attendance where emp_id >110;
Delete from Employees where emp_id <110;