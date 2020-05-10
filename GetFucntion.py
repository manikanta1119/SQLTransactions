import pyodbc

#Function Order Insert,select,delete,select from same table
def GetData(conn,ID):
   
    
    cursor= conn.cursor()
    cursor.execute("Select * from Customer where Id=?",ID)
    CustomerData =cursor.fetchall()

    for Customer in CustomerData:
        print(Customer)

def main():
    
    conn= pyodbc.connect('Driver={SQL Server};''Server=US5CD9011ZYR\MSSQLMANI;''Database=PythonDB;''Trusted_Connection=yes;')
   
    ID= input("Please Enter the Unique ID: ")
    CustomerName=input("Please enter the customer Name: ")
    Region =input("Please enter the RegionId: ")

    Record=(ID,CustomerName,Region)
    recrodlist=[]
    recrodlist.append(Record)

    with conn:
        InsertData(conn,recrodlist)
        GetData(conn,ID)
        


    
def InsertData(conn,recrodlist):
    cursor= conn.cursor()
    insert_records=("Insert into Customer (ID,CustomerName,Region) values(?,?,?)")
    cursor.executemany(insert_records,recrodlist)

if __name__ == "__main__":
    main()
    

    

