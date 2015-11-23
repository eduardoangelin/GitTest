import pyodbc
import socket

def ConnectDB(amazon=True):
	hostname = socket.gethostname()
	if (hostname == "DoSoft01"):
		driver = "DRIVER=PostgreSQL ANSI(x64);"
	elif(hostname == "mbp-de-eduardo"):
		driver = "DRIVER=/usr/local/lib/psqlodbcw.so;"

	if (amazon):
	    server="SERVER=testdb.c3rdj3prlvky.us-east-1.rds.amazonaws.com;"
	    database="DATABASE=testGFC;"
	    userPass="UID=testuser;PWD=testuser;"
	else:
	    server="SERVER=localhost;"
	    database="DATABASE=GFC;"
	    userPass="UID=postgres;PWD=admin"

	connection = pyodbc.connect(driver+server+database+userPass)
	return connection
	