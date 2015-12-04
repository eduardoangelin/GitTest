# -*- coding: UTF-8 -*-

'''
Created on 03/05/2014

@author: jotage
'''
from Base import *
import pyodbc
from PyQt5.QtWidgets import QApplication
from unicodedata import normalize

class FrmCadDefault(Widget):
    
    def __init__(self):
        super(FrmCadDefault, self).__init__()
        self.FrmCadDefaultCreate()
        self.dictFields = {}
        
    def FrmCadDefaultCreate(self):
        #=======================================================================
        # CUSTOMIZANDO A JANETA
        #=======================================================================
        self.setWindowTitle(u'Cadastro padrão')
        
        self.layoutPrincipal = LayoutVertical()
            
        #self.txtCodigo = TextBox(self)
        #self.txtCodigo.setReadOnly(True)
        #self.txtCodigo.setFixedWidth(170)
        
        #self.ckAtivo = CheckBox('Ativo', self)
        #self.ckAtivo.setChecked(True)
        
        #hboxcodigo = LayoutHorizontal()
        #hboxcodigo.addWidget(self.txtCodigo)
        #hboxcodigo.addWidget(self.ckAtivo)
        #hboxcodigo.addStretch(2)
        
        self.fLayout = FormLayout()
        #self.fLayout.addRow(u'Código', hboxcodigo)
        
        #adicionando o form layout ao layout rincipal
        self.layoutPrincipal.addLayout(self.fLayout)
        
        #=======================================================================
        # CRIANDO OS BOTOES
        #=======================================================================
        self.btnNovo = Botao('&Novo', self)
        self.btnSalvar = Botao('&Salvar', self)
        self.btnExcluir = Botao('&Excluir', self)
        self.btnPesquisar = Botao('&Pesquisar', self)
        
        hboxBotoes = LayoutHorizontal()
        hboxBotoes.addStretch(2)
        hboxBotoes.addWidget(self.btnNovo)
        hboxBotoes.addWidget(self.btnSalvar)
        hboxBotoes.addWidget(self.btnExcluir)
        hboxBotoes.addWidget(self.btnPesquisar)
        hboxBotoes.setSpacing(1)
        
        
        #adicionando os botoes ao layout principal
        self.layoutPrincipal.addLayout(hboxBotoes)
        
        self.setLayout(self.layoutPrincipal)
    
    def AddItemDictInput(self, vKey, vOrdem=None, vParamDatabase=None, vDataType=None, vWidget=None):
        vInputRegistry = None
        if(vOrdem is None):
            if(len(self.dictFields.values()) == 0):
                vOrdem = 1
            else:
                vOrdem = max([x[0] for x in self.dictFields.values()])+1
        if(vParamDatabase is None):
            vParamDatabase = normalize('NFKD', vKey).encode('ASCII','ignore').decode("utf-8")
            vParamDatabase = "@"+vParamDatabase.replace(" ", "").upper()
        if(vDataType is None):
            vDataType = "STRING"
        vDataType = str(vDataType).upper()
        if(vWidget is None):
            vWidget = TextBox()
            
        self.dictFields[vKey] = [vOrdem, vParamDatabase, vDataType, vWidget, vInputRegistry]
        
        # adicionando os campos no form layout da base de cadastro
        self.fLayout.addRow(vKey, vWidget)
    
    def FormatInputRegistry(self):
        for i in self.dictFields.keys():
            if(self.dictFields[i][2] == "STRING"):
                self.dictFields[i][4] = "'{}'".format(self.dictFields[i][3].text())
            elif(self.dictFields[i][2] == "INT"):
                self.dictFields[i][4] = "{}".format(self.dictFields[i][3].text())
            elif(self.dictFields[i][2] == "MONEY"):
                self.dictFields[i][4] = "{}".format(self.dictFields[i][3].text())
            elif(self.dictFields[i][2] == "DATE"):
                self.dictFields[i][4] = "'{}'".format(self.dictFields[i][3].text())
    
    def GetDictDatabaseInputs(self):
        self.FormatInputRegistry()
        vResultDict = {}
        for i in self.dictFields.keys():
            vResultDict[self.dictFields[i][1]] = self.dictFields[i][4]
        return vResultDict

if __name__ == '__main__':
    import sys
    root = QApplication(sys.argv)
    app = FrmCadDefault(None)
    app.show()
    root.exec_()