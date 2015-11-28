# coding=utf-8
import pyodbc

from GFC.Database.Credencias import Credenciais

def ConnectDB(amazon=True, db='MSSQL'):
	
	credenciais = Credenciais(amazon, db)
	connection = pyodbc.connect(credenciais.getDriver()+credenciais.getServer()+credenciais.getDatabase()+credenciais.getUserPass())
	return connection
	