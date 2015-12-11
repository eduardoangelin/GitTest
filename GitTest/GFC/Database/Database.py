# -*- coding: UTF-8 -*-
import pyodbc
import pandas.io.sql as psql
from GFC.Database.Credencias import Credenciais

class Database (object):

	def __init__(self, server="NotAmazon", instance = "MSSQL"):
		self.connection = None
		self.server = server
		self.instance = instance
		self.dictView_InsertProcedureDatabase = {}
		self.dictView_InsertProcedureDatabase['CAIXA'] = 'EXECUTE [dbo].[SP_INSERTCAIXA] @ID, @SUF_COD_CTA, @CTA, @DT_SALDO, @SALDO, @COMANDO'
		self.dictView_InsertProcedureDatabase['BANCO'] = 'EXECUTE [dbo].[SP_INSERTBANCO] @ID, @SUF_COD_CTA, @CTA, @DT_SALDO, @SALDO, @COMANDO'
		self.dictView_InsertProcedureDatabase[u'APLICAÇÃO'] = 'EXECUTE [dbo].[SP_INSERTAPLICACAO] @ID, @SUF_COD_CTA, @CTA, @DT_SALDO, @SALDO, @COMANDO'
		self.dictView_InsertProcedureDatabase['ADIANTAMENTO'] = 'EXECUTE [dbo].[SP_INSERTADIANTAMENTO] @ID, @SUF_COD_CTA, @CTA, @DT_SALDO, @SALDO, @COMANDO'
		
		self.dictView_Table = {'CAIXABANCO':'VW_CAIXABANCO','CAIXA':'VW_CAIXABANCO','BANCO':'VW_CAIXABANCO',u'APLICAÇÃO':'VW_CAIXABANCO','ADIANTAMENTO':'VW_CAIXABANCO'}
		
		
	def ConnectDB(self):
		credenciais = Credenciais(self.server, self.instance)
		print("Conectando Banco de Dados")
		self.connection = pyodbc.connect(credenciais.getDriver()+credenciais.getServer()+credenciais.getDatabase()+credenciais.getUserPass())
		print("Banco de Dados conectado com Sucesso!")
		return self.connection
	
	def GetColumnFromView(self, columnsList, view, IDClause = None):
		if(columnsList == ["*"]):
			columns = "*"
		else:	
			columns = ','.join(columnsList)
		sql = "select {} from {}".format(columns, self.dictView_Table[view.upper()])
		if (IDClause != None):
			sql = sql + " where ID = {}".format(IDClause)
		df = psql.read_sql(sql, self.connection)
		df.rename(columns=lambda x: x.upper(), inplace=True)
		return df
	
	def QueryView(self, columnsList, view, whereDict = None):
		if(columnsList == ["*"] or columnsList is None):
			columns = "*"
		else:	
			columns = ','.join(columnsList)
		sql = "select {} from {}".format(columns, self.dictView_Table[view.upper()])
		if (whereDict != None):
			vFirst = True
			for vKey in whereDict.keys():
				if (vFirst):
					sql = sql + " where {} = {}".format(vKey, whereDict[vKey])
					vFirst = False
				else:
					sql = sql + " AND {} = {}".format(vKey, whereDict[vKey])
		df = psql.read_sql(sql, self.connection)
		df.rename(columns=lambda x: x.upper(), inplace=True)
		return df
	
	def InsertFornecedor(self, vDictInputsDatabase):
		cursor = self.connection.cursor()
		#command = "EXECUTE [dbo].[SP_INSERTCLIENTEFORNECEDOR] @ID,@DT_ALT,@COD_NAT,@IND_CTA,@NIVEL,@COD_CTA,@COD_CTA_SUP,@CTA,@IND_DC,@SALDO,@CLIFOR,@PESSOA,@ENDERECO,@RAZAOSOCIAL,@CPF,@RG,@CNPJ,@INSCR_MUNICIPAL,@INSCR_ESTADUAL,@NUMERO,@COMPLEMENTO,@BAIRRO,@CIDADE,@CEP,@EMAIL,@DDD_FONE,@FONE,@UF,@COMANDO"
		command = "EXECUTE [dbo].[SP_INSERTFORNECEDOR] @ID, @SUF_COD_CTA, @CTA, @SALDO, @PESSOA, @ENDERECO, @RAZAOSOCIAL, @CPF, @RG, @CNPJ, @INSCR_MUNICIPAL, @INSCR_ESTADUAL, @NUMERO, @COMPLEMENTO, @BAIRRO, @CIDADE, @CEP, @EMAIL, @DDD_FONE, @FONE, @UF, @COMANDO"
		for i in vDictInputsDatabase.keys():
			command = command.replace(i, vDictInputsDatabase[i])
		cursor.execute(command)
		cursor.commit()
	
	def InsertView(self, view, vDictInputsDatabase):
		cursor = self.connection.cursor()
		command = self.dictView_InsertProcedureDatabase[view.upper()]
		for i in vDictInputsDatabase.keys():
			command = command.replace(i, vDictInputsDatabase[i])
		cursor.execute(command)	
		cursor.commit()
		
	def DeleteView(self, view, vID):
		cursor = self.connection.cursor()
		command = self.dictView_InsertProcedureDatabase[view.upper()]
		vParam = command.replace(command[:command.find("@")], "").replace(" ", "").split(",")
		for i in vParam:
			if (i == '@ID'):
				command = command.replace(i, str(vID))
			elif (i == '@COMANDO'):
				command = command.replace(i, "'D'")
			else:
				command = command.replace(i, "NULL")
		cursor.execute(command)	
		cursor.commit()
	
	def ConsultaClientesPorNome(self, name):
		sql = "select id, RAZAOSOCIAL, CIDADE, UF from clientefornecedor where RAZAOSOCIAL LIKE '%{}%'".format(name)
		df = psql.read_sql(sql, self.connection)
		tuples = [tuple(x) for x in df.values]
		return tuples


if __name__ == '__main__':
	db = Database()
	db.ConnectDB()
	df = db.GetColumnFromView(["*"], "CAIXABANCO")
	print (df)
	for i in df:
		print (i)
	
	
		