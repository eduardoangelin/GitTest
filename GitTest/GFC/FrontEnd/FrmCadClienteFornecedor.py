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
        #self.dictFields = {}
        
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
        
        
    def FrmCadClienteCreate3(self):
        self.setWindowTitle('Cadastro de Clientes')
        self.setWindowState(Qt.WindowMaximized)
        
        vOrder = 0
        # criando os campos de cadastro
        self.txtCPF = TextBox(self)
        self.txtCPF.setFixedWidth(170)
        self.txtCPF.setValidator(QIntValidator())
        self.dictFields[vOrder] = ('CPF', self.txtCPF)
        vOrder = vOrder+1
        
        self.txtCNPJ = TextBox(self)
        self.txtCNPJ.setFixedWidth(170)
        self.txtCNPJ.setValidator(QIntValidator())
        self.dictFields[vOrder] = ('CNPJ', self.txtCNPJ)
        vOrder = vOrder+1
        
        self.txtRG = TextBox(self)
        self.txtRG.setFixedWidth(170)  
        self.txtRG.setValidator(QIntValidator())
        self.dictFields[vOrder] = ('RG', self.txtRG)
        vOrder = vOrder+1          
        
        self.txtRazaoSocial = TextBox(self)
        self.dictFields[vOrder] = (u'Razão Social', self.txtRazaoSocial)
        vOrder = vOrder+1
        self.txtEndereco = TextBox(self)
        self.dictFields[vOrder] = (u'Endereço', self.txtEndereco)
        vOrder = vOrder+1
        
        self.txtNumero = TextBox(self)
        self.txtNumero.setValidator(QIntValidator()) # validando o campo de texto para aceitar somnte inteiros
        self.dictFields[vOrder] = (u'Número', self.txtNumero)
        vOrder = vOrder+1

        self.txtComplemento = TextBox(self)
        self.dictFields[vOrder] = ('Complemento', self.txtComplemento)
        vOrder = vOrder+1
        self.txtBairro = TextBox(self)
        self.dictFields[vOrder] = ('Bairro', self.txtBairro)
        vOrder = vOrder+1
        self.txtCidade = TextBox(self)
        self.dictFields[vOrder] = ('Cidade', self.txtCidade)
        vOrder = vOrder+1
        
        self.cmbUF = ComboBox(self)
        self.cmbUF.setFixedWidth(170)
        self.cmbUF.setUFForm()
        self.dictFields[vOrder] = ('UF', self.cmbUF)
        vOrder = vOrder+1
        
        self.txtInscMun = TextBox(self)
        self.txtInscMun.setFixedWidth(170)  
        self.txtInscMun.setValidator(QIntValidator())
        self.dictFields[vOrder] = (u'Inscrição Municípal', self.txtInscMun)
        vOrder = vOrder+1
        
        self.txtInscEst = TextBox(self)
        self.txtInscEst.setFixedWidth(170)  
        self.txtInscEst.setValidator(QIntValidator()) 
        self.dictFields[vOrder] = (u'Inscrição Estadual', self.txtInscEst)
        vOrder = vOrder+1
        
        self.txtEmail = TextBox(self)
        self.txtEmail.setFixedWidth(500)  
        self.dictFields[vOrder] = ('Email', self.txtEmail)
        vOrder = vOrder+1
        
        self.txtDDD = TextBox(self)
        self.txtDDD.setFixedWidth(70)  
        self.txtDDD.setMaxLength(2)   
        self.txtDDD.setValidator(QIntValidator()) 
        self.dictFields[vOrder] = ('DDD', self.txtDDD)
        vOrder = vOrder+1
        
        self.txtFone = TextBox(self)
        self.txtFone.setFixedWidth(170)  
        self.txtFone.setMaxLength(9)
        self.txtFone.setValidator(QIntValidator())
        self.dictFields[vOrder] = ('Fone', self.txtFone)
        vOrder = vOrder+1
        
        self.txtCodAnal = TextBox(self)
        self.txtCodAnal.setFixedWidth(70)  
        self.txtCodAnal.setMaxLength(3)
        self.txtCodAnal.setValidator(QIntValidator()) 
        self.dictFields[vOrder] = (u'Código Analítico', self.txtCodAnal)
        vOrder = vOrder+1
        
        self.txtNomeConta = TextBox(self)
        self.txtNomeConta.setFixedWidth(170)  
        self.txtNomeConta.setMaxLength(100)
        self.dictFields[vOrder] = ('Nome da Conta', self.txtNomeConta)
        vOrder = vOrder+1
        
        self.txtSaldoInicial = TextBox(self)
        self.txtSaldoInicial.setFixedWidth(70)  
        self.txtSaldoInicial.setMaxLength(3)
        self.txtSaldoInicial.setValidator(QDoubleValidator()) 
        self.dictFields[vOrder] = ('Saldo Inicial', self.txtSaldoInicial)
        vOrder = vOrder+1
        #self.txtSaldoInicial.setValidator(QDoubleValidator().setRange(0, None, 2)) 
        
        # adicionando os campos no form layout da base de cadastro
        for i in range(len(self.dictFields)):
            self.fLayout.addRow(self.dictFields[i][0], self.dictFields[i][1])
            
        
    def FrmCadClienteCreate2(self):
        self.setWindowTitle('Cadastro de Clientes')
        self.setWindowState(Qt.WindowMaximized)
        self.dictFields = {}
        # criando os campos de cadastro
        self.txtCPF = TextBox(self)
        self.txtCPF.setFixedWidth(170)
        self.txtCPF.setValidator(QIntValidator())
        
        self.txtCNPJ = TextBox(self)
        self.txtCNPJ.setFixedWidth(170)
        self.txtCNPJ.setValidator(QIntValidator())
        
        self.txtRG = TextBox(self)
        self.txtRG.setFixedWidth(170)  
        self.txtRG.setValidator(QIntValidator())           
        
        self.txtRazaoSocial = TextBox(self)
        self.txtEndereco = TextBox(self)
        
        self.txtNumero = TextBox(self)
        self.txtNumero.setValidator(QIntValidator()) # validando o campo de texto para aceitar somnte inteiros

        self.txtComplemento = TextBox(self)
        self.txtBairro = TextBox(self)
        self.txtCidade = TextBox(self)
        
        self.cmbUF = ComboBox(self)
        self.cmbUF.setFixedWidth(170)
        self.cmbUF.setUFForm()
        
        self.txtInscMun = TextBox(self)
        self.txtInscMun.setFixedWidth(170)  
        self.txtInscMun.setValidator(QIntValidator()) 
        
        self.txtInscEst = TextBox(self)
        self.txtInscEst.setFixedWidth(170)  
        self.txtInscEst.setValidator(QIntValidator()) 
        
        self.txtEmail = TextBox(self)
        self.txtEmail.setFixedWidth(500)  
        
        self.txtDDD = TextBox(self)
        self.txtDDD.setFixedWidth(70)  
        self.txtDDD.setMaxLength(2)   
        self.txtDDD.setValidator(QIntValidator()) 
        
        self.txtFone = TextBox(self)
        self.txtFone.setFixedWidth(170)  
        self.txtFone.setMaxLength(9)
        self.txtFone.setValidator(QIntValidator()) 
        
        self.txtCodAnal = TextBox(self)
        self.txtCodAnal.setFixedWidth(70)  
        self.txtCodAnal.setMaxLength(3)
        self.txtCodAnal.setValidator(QIntValidator())  
        
        self.txtNomeConta = TextBox(self)
        self.txtNomeConta.setFixedWidth(170)  
        self.txtNomeConta.setMaxLength(100)
        
        self.txtSaldoInicial = TextBox(self)
        self.txtSaldoInicial.setFixedWidth(70)  
        self.txtSaldoInicial.setMaxLength(3)
        self.txtSaldoInicial.setValidator(QDoubleValidator()) 
        #self.txtSaldoInicial.setValidator(QDoubleValidator().setRange(0, None, 2)) 
        
        # adicionando os campos no form layout da base de cadastro
        self.fLayout.addRow('CPF', self.txtCPF)
        self.fLayout.addRow('CNPJ', self.txtCNPJ)
        self.fLayout.addRow('RG', self.txtRG)
        self.fLayout.addRow(u'Razão Social', self.txtRazaoSocial)
        self.fLayout.addRow(u'Endereço', self.txtEndereco)
        self.fLayout.addRow(u'Número', self.txtNumero)
        self.fLayout.addRow('Complemento', self.txtComplemento)
        self.fLayout.addRow('Bairro', self.txtBairro)
        self.fLayout.addRow('Cidade', self.txtCidade)
        self.fLayout.addRow('UF', self.cmbUF)
        self.fLayout.addRow(u'Inscrição Municípal', self.txtInscMun)
        self.fLayout.addRow(u'Inscrição Estadual', self.txtInscEst)
        self.fLayout.addRow('Email', self.txtEmail)
        self.fLayout.addRow('DDD', self.txtDDD)
        self.fLayout.addRow('Fone', self.txtFone)
        self.fLayout.addRow(u'Código Analítico', self.txtCodAnal)
        self.fLayout.addRow('Nome Conta', self.txtNomeConta)
        self.fLayout.addRow('Saldo Inicial', self.txtSaldoInicial)
        
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
            msg.information(self, 'Cadastro de clientes', 'CListe salvo com sucesso !!!', MessageBox.Ok)
        except Exception as e:
            msg = MessageBox()
            msg.critical(self, 'Cadastro de clientes', 'Ocorreu o seguinte erro ao tentar inserir o cliente: \n ' + str(e), MessageBox.Ok)
    
    def Salvar2(self):
        try:
            #capturando os dados da tela
            CodAnal = self.txtCodAnal.text()
            NomeConta = self.txtNomeConta.text()
            SaldoInicial = self.txtSaldoInicial.text()
            CPF = self.txtCPF.text()
            CNPJ = self.txtCNPJ.text()
            RG = self.txtRG.text()
            RazaoSocial = self.txtRazaoSocial.text()
            Endereco = self.txtEndereco.text()
            Numero = self.txtNumero.text()
            Complemento = self.txtComplemento.text()
            Bairro =self.txtBairro.text()
            Cidade = self.txtCidade.text()
            UF = self.cmbUF.currentText()
            InscMun = self.txtInscMun.text()
            InscEst = self.txtInscEst.text()
            Email = self.txtEmail.text()
            DDD = self.txtDDD.text()
            Fone = self.txtFone.text()
            
            
            
            listInputsTuple = [("@ID", "NULL"), ("@DT_ALT", "'2014-05-27'"), ("@COD_NAT", "'02'"), ("@IND_CTA", "'A'"), 
                               ("@NIVEL", "5"), ("@COD_CTA", "'2.1.01.01.{}'".format(str(CodAnal))), ("@COD_CTA_SUP", "'2.1.01.01'"), 
                               ("@CTA", "'{}'".format(str(NomeConta))), ("@IND_DC", "'C'"), ("@SALDO", SaldoInicial), ("@CLIFOR", "'F'"), 
                               ("@PESSOA", "'PJ'"), ("@ENDERECO", Endereco), ("@RAZAOSOCIAL", RazaoSocial), ("@CPF", CPF), ("@RG", RG), ("@CNPJ", "value"), ("@INSCR_MUNICIPAL", "value"), ("@INSCR_ESTADUAL", "value"), ("@NUMERO", "value"), ("@COMPLEMENTO", "value"), ("@BAIRRO", "value"), ("@CIDADE", "value"), ("@CEP", "value"), ("@EMAIL", "value"), ("@DDD_FONE", "value"), ("@FONE", "value"), ("@UF", "value"), ("@COMANDO", "value")]            
            
            self.__inserir(CodAnal, CPF, NomeConta, Endereco, Numero, Bairro, Cidade, UF)
            msg = MessageBox()
            msg.information(self, 'Cadastro de clientes', 'CListe salvo com sucesso !!!', MessageBox.Ok)
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