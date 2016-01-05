# -*- coding: UTF-8 -*-
'''
Created on 5 de dez de 2015

@author: Angelin
'''

from GFC.FrontEnd.FrmcadDefault import FrmCadDefault
from GFC.FrontEnd.FrmInsDefault import FrmInsDefault
from PyQt5.QtWidgets import QApplication
from GFC.FrontEnd.Base import *
from GFC.Database.Database import Database
from PyQt5.QtGui import QIntValidator, QDoubleValidator
from PyQt5.QtCore import Qt


class FrmCaixaBanco(FrmCadDefault):
    
    def __init__(self, db):
        view = "Caixa"
        vHeaderList = [('ID', 'TextBox'), ('IDPLANOCONTAS', 'TextBox'), ('COD_CTA', 'TextBox'), ('CTA', 'TextBox')]
        vDictBD = {"@SUF_COD_CTA":u'Código Analítico',"@CTA":'Nome da Conta',"@DT_SALDO":'Data Saldo'}
        #self.view = "CaixaBanco"
        #self.header_grid = ['ID', 'IDPLANOCONTAS', 'COD_CTA', 'CTA']
        self.db = db
        
        super(FrmCaixaBanco, self).__init__(db, view, vHeaderList, vDictBD)
        self.FrmCadClienteCreate()

    
    def FrmCadClienteCreate(self):
        # criando os campos de cadastro
        vIDWidget = TextBox(Validator=QIntValidator())
        vIDWidget.setReadOnly(True)
        vIDWidget.setEnabled(False)
        self.AddItemDictInput('ID', vDataType="INT", vWidget=vIDWidget)
        self.AddItemDictInput(u'Código Analítico', vWidget=TextBox(MaxLength=3, Validator=QIntValidator()))
        self.AddItemDictInput('Nome da Conta')
        self.AddItemDictInput('Data Saldo', vDataType="DATE", vWidget=DateBox())
        self.AddItemDictInput('Saldo', vDataType="MONEY", vWidget=TextBox(Validator=QDoubleValidator()))
        
        #self.vDictParamDatabase["@ID"] = "NULL"
        #self.vDictParamDatabase["@SUF_COD_CTA"] = self.dictFields[u'Código Analítico'][4]
        #self.vDictParamDatabase["@CTA"] = self.dictFields['Nome da Conta'][4]
        #self.vDictParamDatabase["@COMANDO"] = "'I'"
        
    
if __name__ == '__main__':
    import sys
    root = QApplication(sys.argv)
    db = Database()
    db.ConnectDB()
    app = FrmCaixaBanco(db)
    app.show()
    root.exec_()