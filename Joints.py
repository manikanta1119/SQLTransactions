import pyodbc

def main():
    conn=pyodbc.connect('Driver={SQL Server};''Server=US5CD9011ZYR\MSSQLMANI;''Database=PythonDB;''Trusted_Connection=yes;')
    GetJoints(conn)

def GetJoints(conn):
    cursor=conn.cursor()
    cursor.execute("Select customer.id, customer.CustomerName, Region_tbl.RegionName from dbo.Customer with (NOLOCK) inner join dbo.Region_tbl on Customer.Region=Region_tbl.id")    
    Custdata=cursor.fetchall()
    print(Custdata)
    

if __name__ == "__main__":
    main()    