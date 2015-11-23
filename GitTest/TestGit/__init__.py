import pyodbc

#pyodbc.connect("")
driver="DRIVER=/usr/local/lib/psqlodbcw.so;"
amazon = True
if (amazon):
    server="SERVER=testdb.c3rdj3prlvky.us-east-1.rds.amazonaws.com;"
    database="DATABASE=testGFC;"
    userPass="UID=testuser;PWD=testuser;"
else:
    server="SERVER=localhost;"
    database="DATABASE=GFC;"
    userPass="UID=postgres;PWD=admin"

connection = pyodbc.connect(driver+server+database+userPass)
cursor = connection.cursor()


cursor.execute("select id from teste")
rows = cursor.fetchall()
for row in rows:
    print row.id
cursor.close()

