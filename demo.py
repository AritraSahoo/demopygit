import  mysql;
from mysql.connector import connect

mydb = connect(host="localhost", user ="root", password="root");

myCursor = mydb.cursor()
myCursor.execute("use new_schema")
myCursor.execute("select * from new_table")

result = myCursor.fetchmany(2)

for i in result:
    print(i)