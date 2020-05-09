#install pyodbc in Pip Module 
#pyodbc for SQL Transactions
#py -m pip install pyodbc

import pyodbc

conn= pyodbc.connect('Driver={SQL Server};''Server=US5CD9011ZYR\MSSQLMANI;''Database=Demo;''Trusted_Connection=yes;')

cursor= conn.cursor()

cursor.execute('Select id, ADGroupName from Temp_tbl')


for row in cursor:
    
    ID= row.id
    ADGroupName =row.ADGroupName
    AdGroupSPlit= ADGroupName.split("|")
    
    print(AdGroupSPlit)

    for group in AdGroupSPlit:
        print(group)

conn.close()

