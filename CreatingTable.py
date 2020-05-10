import pyodbc

#conn= pyodbc.connect('Driver={SQL Server};''Server=US5CD9011ZYR\MSSQLMANI;''Trusted_Connection=yes;')

#conn= pyodbc.connect('Driver={SQL Server};''Server=US5CD9011ZYR\MSSQLMANI;''database= PythonDB;''Trusted_Connection=yes;')
conn= pyodbc.connect('Driver={SQL Server};''Server=US5CD9011ZYR\MSSQLMANI;''Database=PythonDB;''Trusted_Connection=yes;')
cursor= conn.cursor()

Record1 =(1,"Manikanta",1)
Record2=(2,"Parupally",1)

Record_list=[]
Record_list.append(Record1)
Record_list.append(Record2)

#cursor.execute("CREATE DATABASE [PythonDB]")

#cursor.execute("CREATE Table Customer(id INTEGER , CustomerName varchar(50), Region integer);")
insert_records = "INSERT INTO Customer(id,CustomerName,Region) VALUES(?,?,?) "
cursor.executemany(insert_records,Record_list)
conn.commit()

cursor.close()

conn.close()