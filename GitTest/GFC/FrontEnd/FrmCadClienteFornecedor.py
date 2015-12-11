# -*- coding: UTF-8 -*-
'''
Created on 03/05/2014

@author: jotage
'''
from FrmcadDefault import FrmCadDefault
from PyQt5.QtWidgets import QApplication
from GFC.FrontEnd.Base import *
from GFC.FrontEnd.FrmPesquisaCliente import FrmPesquisaCliente
from GFC.Database.Database import Database
from PyQt5.QtGui import QIntValidator, QDoubleValidator
from PyQt5.QtCore import Qt

class FrmCadClienteFornecedor(FrmCadDefault):
    
    def __init__(self, db):
        super(FrmCadClienteFornecedor, self).__init__()
        
        self.FrmCadClienteCreate()
        #criando um objeto cliente DB ara que fique a disposição para interagir com o módulo de acesso a dados
        self.db = db
        self.dictFields = {}
        
        # conectando os clicks dos botoes as devidas funçoes
        self.btnPesquisar.clicked.connect(self.AbrePesquisa)
        self.btnSalvar.clicked.connect(self.Salvar)
        self.btnExcluir.clicked.connect(self.__Excluir)
    
        
    def FrmCadClienteCreate(self):
        self.setWindowTitle('Cadastro de Clientes')
        self.setWindowState(Qt.WindowMaximized)
        
        # criando os campos de cadastro
        self.AddItemDictInput('CPF', vWidget=TextBox(MaxLength=11, Validator=QIntValidator()))
        self.AddItemDictInput('CNPJ', vWidget=TextBox(MaxLength=14, Validator=QIntValidator()))
        cmbPessoa = ComboBox()
        cmbPessoa.setPessoaForm()
        self.AddItemDictInput('Pessoa', vWidget=cmbPessoa)
        self.AddItemDictInput('RG', vWidget=TextBox(MaxLength=7, Validator=QIntValidator()))
        self.AddItemDictInput(u'Razão Social')
        self.AddItemDictInput(u'Endereço')
        self.AddItemDictInput(u'Número', vWidget=TextBox(MaxLength=5, Validator=QIntValidator()))
        self.AddItemDictInput('Complemento')
        self.AddItemDictInput('CEP', vWidget=TextBox(MaxLength=8, Validator=QIntValidator()))
        self.AddItemDictInput('Bairro')
        self.AddItemDictInput('Cidade')
        cmbUF = ComboBox()
        cmbUF.setUFForm()
        self.AddItemDictInput('UF', vWidget=cmbUF)
        self.AddItemDictInput(u'Inscrição Municípal', vWidget=TextBox(MaxLength=20, Validator=QIntValidator()))
        self.AddItemDictInput(u'Inscrição Estadual', vWidget=TextBox(MaxLength=20, Validator=QIntValidator()))
        self.AddItemDictInput('Email')
        self.AddItemDictInput('DDD', vWidget=TextBox(MaxLength=2, Validator=QIntValidator()))
        self.AddItemDictInput('Fone', vWidget=TextBox(MaxLength=9, Validator=QIntValidator()))
        self.AddItemDictInput(u'Código Analítico', vWidget=TextBox(MaxLength=3, Validator=QIntValidator()))
        self.AddItemDictInput('Nome da Conta')
        self.AddItemDictInput('Saldo', vWidget=TextBox(Validator=QDoubleValidator()))
        
        
    def AbrePesquisa(self):
        #print ("Entrou AbrePesquisa")
        self.frmPesquisa = FrmPesquisaCliente(self.db)
        #FrmPesquisaCliente(self, self.db)
        #print ("Passou FrmPesquisaCliente")
        self.frmPesquisa.setModal(True)
        self.frmPesquisa.show()
        self.frmPesquisa.exec_()
        
    def Salvar(self):
        try:
            #capturando os dados da tela
            #CodAnal = self.txtCodAnal.text()
            
            vDictInputsDatabase = self.GetDictDatabaseInputs()
            "EXECUTE [dbo].[SP_INSERTFORNECEDOR] @ID, @DDD_FONE, @FONE, @UF, @COMANDO"
            vDictInputsDatabase["@ID"] = "NULL"
            vDictInputsDatabase["@SUF_COD_CTA"] = self.dictFields[u'Código Analítico'][4]
            vDictInputsDatabase["@CTA"] = self.dictFields['Nome da Conta'][4]
            vDictInputsDatabase["@INSCR_MUNICIPAL"] = self.dictFields[u'Inscrição Municípal'][4]
            vDictInputsDatabase["@INSCR_ESTADUAL"] = self.dictFields[u'Inscrição Estadual'][4]
            del vDictInputsDatabase["@DDD"]
            vDictInputsDatabase["@DDD_FONE"] = self.dictFields['DDD'][4]
            vDictInputsDatabase["@COMANDO"] = "'I'"
            
            self.db.InsertFornecedor(vDictInputsDatabase)
            msg = MessageBox()
            msg.information(self, 'Cadastro de cliente', 'Cliente salvo com sucesso !!!', MessageBox.Ok)
        except Exception as e:
            msg = MessageBox()
            msg.critical(self, 'Cadastro de clientes', 'Ocorreu o seguinte erro ao tentar inserir o cliente: \n ' + str(e), MessageBox.Ok)
    
    def __inserir(self, id, cpf, nome, logradouro, numero, bairro, cidade, uf):
        '''Método cria um objeto cliente do modulo de acesso a dados, e inclui um novo cliente no banco'''
        
        self.db.Salvar(id, cpf, nome, logradouro, numero, bairro, cidade, uf)

    def __Excluir(self, pId):
        try:
            codigo = int(self.txtCodigo.text())
            self.clientedb.Excluir(codigo)
            
        except Exception as e:
            msg = MessageBox()
            msg.critical(self, 'Cadastro de clientes', 'Ocorreu o seguinte erro ao tentar excluir: \n ' + str(e).decode('utf8'), MessageBox.Ok)


if __name__ == '__main__':
    import sys
    root = QApplication(sys.argv)
    db = Database()
    db.ConnectDB()
    app = FrmCadClienteFornecedor(db)
    app.show()
    root.exec_()