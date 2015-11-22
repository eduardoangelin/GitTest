import pyodbc

#pyodbc.connect("")
connection = pyodbc.connect("DRIVER=/usr/local/lib/psqlodbcw.so;SERVER=localhost;DATABASE=GFC;UID=postgres;PWD=admin")
cursor = connection.cursor()

cursor.execute("select id from teste")
rows = cursor.fetchall()
for row in rows:
    print row.id


