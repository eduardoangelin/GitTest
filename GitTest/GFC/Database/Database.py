# coding=utf-8
import pyodbc
import pandas.io.sql as psql
from GFC.Database.Credencias import Credenciais

class Database (object):

	def __init__(self, server="Amazon", db = "MSSQL"):
		self.connection = None
		self.server = server
		self.db = db
		
		
	def ConnectDB(self):
		credenciais = Credenciais(self.server, self.db)
		print("Conectando Banco de Dados")
		self.connection = pyodbc.connect(credenciais.getDriver()+credenciais.getServer()+credenciais.getDatabase()+credenciais.getUserPass())
		print("Banco de Dados conectado com Sucesso!")
		return self.connection
	
	def GetColumnFromView(self, columnsList, view):
		columns = ','.join(columnsList)
		sql = "select {} from {}".format(columns, view)
		df = psql.read_sql(sql, self.connection)
		return df
		
		