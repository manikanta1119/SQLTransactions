import pyodbc

#conn= pyodbc.connect('Driver={SQL Server};''Server=US5CD9011ZYR\MSSQLMANI;''Trusted_Connection=yes;')
#conn= pyodbc.connect('Driver={SQL Server};''Server=US5CD9011ZYR\MSSQLMANI;''database= PythonDB;''Trusted_Connection=yes;')
conn= pyodbc.connect('Driver={SQL Server};''Server=US5CD9011ZYR\MSSQLMANI;''Database=PythonDB;''Trusted_Connection=yes;')
cursor= conn.cursor()

Record1 =(1,"EMEA")
Record2=(2,"NA")

Record_list=[]
Record_list.append(Record1)
Record_list.append(Record2)

#cursor.execute("CREATE DATABASE [PythonDB]")

#cursor.execute("CREATE Table Region_tbl(id INTEGER , RegionName varchar(50));")
insert_records = "INSERT INTO Region_tbl(id,RegionName) VALUES(?,?) "
cursor.executemany(insert_records,Record_list)
conn.commit()

cursor.close()

conn.close()