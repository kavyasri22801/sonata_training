import pyodbc
server='HYDTRNG12\SQLEXPRESS'
database='kavya1'
username='sa'
password='kavya@801'
cxcn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)


mycursor=cxcn.cursor()
res=mycursor.execute("select empno,sal,comm,(sal+comm) as salary from emp")
myrecs=res.fetchall();
print(myrecs)
