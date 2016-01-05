# -*- coding: UTF-8 -*-
'''
Created on 5 de dez de 2015

@author: Angelin
'''
from Base import *
from unicodedata import normalize
from GFC.Database.Database import Database

class FrmInsDefault(Diaglog):
    
    def __init__(self, db, view, dictFields, vDictBD, vID, vCommand):
        super(FrmInsDefault, self).__init__()
        self.db = db
        self.view = view
        self.dictFields = dictFields
        self.vDictBD = vDictBD
        self.vID = vID
        self.vCommand = vCommand
        self.FrmInsDefaultCreate()
        
        if (self.vCommand == "'I'"):
            self.btnSalvar.clicked.connect(self.Inserir)
        elif (self.vCommand == "'U'"):
            self.btnSalvar.clicked.connect(self.Atualizar)
        self.btnCancelar.clicked.connect(self.Cancelar)
        
    def FrmInsDefaultCreate(self):
        #=======================================================================
        # CUSTOMIZANDO A JANETA
        #=======================================================================
        if (self.vCommand == "'I'"):
            vTitle = 'Inserir {}'.format(self.view)
        elif (self.vCommand == "'U'"):
            vTitle = 'Atualizar {}'.format(self.view)
        self.setWindowTitle(vTitle)
        
        self.layoutPrincipal = LayoutVertical()
            
        self.fLayout = FormLayout()
        
        # adicionando os campos no form layout da base de cadastro
        #for vKey in self.dictFields.keys():
        
        
        vDictAsListTuple = sorted(list(self.dictFields.items()), key=lambda tup: tup[1][1])
        
        for vKey in [x[0] for x in vDictAsListTuple]:    
            self.fLayout.addRow(vKey, self.dictFields[vKey][3])
        
        #adicionando o form layout ao layout principal
        self.layoutPrincipal.addLayout(self.fLayout)
        
        #=======================================================================
        # CRIANDO OS BOTOES
        #=======================================================================
        self.btnSalvar = Botao('&Salvar', self)
        self.btnCancelar = Botao('&Cancelar', self)
        
        hboxBotoes = LayoutHorizontal()
        hboxBotoes.addStretch(2)
        hboxBotoes.addWidget(self.btnSalvar)
        hboxBotoes.addWidget(self.btnCancelar)
        hboxBotoes.setSpacing(1)
        
        
        #adicionando os botoes ao layout principal
        self.layoutPrincipal.addLayout(hboxBotoes)
        
        self.setLayout(self.layoutPrincipal)
    
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
      
    def Inserir(self):
        ''' Salva no Banco o dicionário padrão, acrescentando os novos termos do dicionário @self.vDictBD'''
        try:
            #capturando os dados da tela
            #CodAnal = self.txtCodAnal.text()
            
            self.vDictInputsDatabase = self.GetDictDatabaseInputs()
            vHasID = False
            for i in self.vDictBD.keys():
                if(i=='@ID'):
                    self.vDictInputsDatabase['@ID'] = self.vID
                    vHasID = True
                else:
                    self.vDictInputsDatabase[i] = self.dictFields[self.vDictBD[i]][4]
            
            if (vHasID == False):
                self.vDictInputsDatabase['@ID'] = self.vID
            self.vDictInputsDatabase["@COMANDO"] = self.vCommand
            
            self.db.InsertView(self.view, self.vDictInputsDatabase)
            w = Widget()
            result = MessageBox().question(w, 'Cadastro de {}'.format(self.view), '{} salvo com sucesso! Deseja limpar a tela e realizar outro cadastro?'.format(self.view), MessageBox.Yes | MessageBox.No, MessageBox.Yes)
            self.ClearInputs()
            if result == QMessageBox.No:
                self.close()
            #w.show()
        except Exception as e:
            w = Widget()
            result = MessageBox().question(w, 'Cadastro de {}'.format(self.view), 'Ocorreu o seguinte erro ao tentar inserir o {}: \n{}\n\nDeseja tentar inserir novamente?'.format(self.view, str(e)), MessageBox.Yes | MessageBox.No, MessageBox.Yes)
            if result == QMessageBox.No:
                self.ClearInputs()
                self.close()
            #w.show()
    
    def Atualizar(self):
        ''' Salva no Banco o dicionário padrão, acrescentando os novos termos do dicionário @self.vDictBD'''
        try:
            #capturando os dados da tela
            #CodAnal = self.txtCodAnal.text()
            
            self.vDictInputsDatabase = self.GetDictDatabaseInputs()
            
            for i in self.vDictBD.keys():
                self.vDictInputsDatabase[i] = self.dictFields[self.vDictBD[i]][4]
            
            self.vDictInputsDatabase["@COMANDO"] = self.vCommand
            
            w = Widget()
            result = MessageBox().question(w, 'Cadastro de {}'.format(self.view), 'Tem certeza que deseja atualizar este registro?', MessageBox.Yes | MessageBox.No, MessageBox.No)
            if result == QMessageBox.Yes:
                self.db.InsertView(self.view, self.vDictInputsDatabase)
                MessageBox.information(self, '', u'Atualização feita com sucesso!', MessageBox.Ok, MessageBox.Ok)
                self.ClearInputs()
                self.close()
            #w.show()
        except Exception as e:
            w = Widget()
            result = MessageBox().question(w, 'Cadastro de {}'.format(self.view), 'Ocorreu o seguinte erro ao tentar inserir o {}: \n{}\n\nDeseja tentar atualizar novamente?'.format(self.view, str(e)), MessageBox.Yes | MessageBox.No, MessageBox.Yes)
            if result == QMessageBox.No:
                self.ClearInputs()
                self.close()
            #w.show()
    
    def Cancelar(self):
        self.ClearInputs()
        self.close()
    
    def GetDictDatabaseInputs(self):
        ''' Retorna dicion�rio do tipo: {@vParamDatabase: @ValueInput}'''
        self.FormatInputRegistry()
        vResultDict = {}
        for i in self.dictFields.keys():
            vResultDict[self.dictFields[i][1]] = self.dictFields[i][4]
        return vResultDict
    
    def ClearInputs(self):
        for vKey in self.dictFields.keys():
            self.dictFields[vKey][3].clear()
    