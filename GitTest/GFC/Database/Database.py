# coding=utf-8
import pyodbc
import pandas.io.sql as psql
from GFC.Database.Credencias import Credenciais

class Database (object):

	def __init__(self, server="Amazon", instance = "MSSQL"):
		self.connection = None
		self.server = server
		self.instance = instance
		
		
	def ConnectDB(self):
		credenciais = Credenciais(self.server, self.instance)
		print("Conectando Banco de Dados")
		self.connection = pyodbc.connect(credenciais.getDriver()+credenciais.getServer()+credenciais.getDatabase()+credenciais.getUserPass())
		print("Banco de Dados conectado com Sucesso!")
		return self.connection
	
	def GetColumnFromView(self, columnsList, view):
		columns = ','.join(columnsList)
		sql = "select {} from {}".format(columns, view)
		df = psql.read_sql(sql, self.connection)
		return df
	
	
	def ConsultaClientesPorNome(self, name):
		sql = "select id, RAZAOSOCIAL, CIDADE, UF from clientefornecedor where RAZAOSOCIAL LIKE '%{}%'".format(name)
		df = psql.read_sql(sql, self.connection)
		tuples = [tuple(x) for x in df.values]
		return tuples
		
		