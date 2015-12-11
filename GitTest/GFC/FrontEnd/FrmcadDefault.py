# -*- coding: UTF-8 -*-

'''
Created on 03/05/2014

@author: jotage
'''
from Base import *
import pyodbc
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QWidget
from unicodedata import normalize
from PyQt5.Qt import QDesktopWidget, QWidget
from GFC.FrontEnd.Base import ComboBox
from GFC.FrontEnd.FrmInsDefault import FrmInsDefault
from GFC.Database.Database import Database
from PyQt5.QtCore import Qt

class FrmCadDefault(Widget):
    
    def __init__(self, db, view, vHeaderList, vDictBD):
        super(FrmCadDefault, self).__init__()
        self.db = db
        self.view = view
        self.header_grid = [i[0] for i in vHeaderList]
        self.headerList = vHeaderList
        self.dictFields = {}
        self.vDictBD = vDictBD
        self.limit = 50
        self.PesquisarGridDict = None
        self.FrmCadDefaultCreate()
        self.CenterOnScreen()
        self.btnBuscar.clicked.connect(self.PesquisarGrid)
        self.btnInserir.clicked.connect(self.__inserir)
        self.btnAtualizar.clicked.connect(self.__atualizar)
        self.btnExcluir.clicked.connect(self.__deletar)
        self.grdPesquisaCliente.doubleClicked.connect(self.__atualizar)
        self.cmbField.currentIndexChanged.connect(self.UpdateTxtBusca)
        
    def FrmCadDefaultCreate(self):
        #=======================================================================
        # CUSTOMIZANDO A JANETA
        #=======================================================================
        
        self.setWindowTitle('Pesquisa {}'.format(self.view))
        self.setWindowState(Qt.WindowMaximized)
        #self.resize(800, 300)
        
        self.layoutPrincipal = LayoutVertical()
        self.CreateFilterLayout()
        
        # criando o grid da pesquisa
        len_header_grid = len(self.header_grid)
        self.dict_grid = dict(zip(range(len_header_grid), self.header_grid))
        self.grdPesquisaCliente = Grid(self, 0, len_header_grid)     
        self.grdPesquisaCliente.setHorizontalHeaderLabels(self.header_grid)

        #desativando edição do grid de pesquisa
        self.grdPesquisaCliente.setEditTriggers(QAbstractItemView.NoEditTriggers)

        #recidimencionando as colunas do grid
        self.grdPesquisaCliente.setColumnWidth(1,300)
        self.grdPesquisaCliente.setColumnWidth(2, 200)

        self.layoutPrincipal.addWidget(self.grdPesquisaCliente)
        
        self.fLayout = FormLayout()
        
        #adicionando o form layout ao layout Principal
        self.layoutPrincipal.addLayout(self.fLayout)
        
        #=======================================================================
        # CRIANDO OS BOTOES
        #=======================================================================
        self.btnInserir = Botao('&Inserir', self)
        self.btnAtualizar = Botao('&Atualizar', self)
        self.btnExcluir = Botao('&Excluir', self)
        
        hboxBotoes = LayoutHorizontal()
        hboxBotoes.addStretch(2)
        hboxBotoes.addWidget(self.btnInserir)
        hboxBotoes.addWidget(self.btnAtualizar)
        hboxBotoes.addWidget(self.btnExcluir)
        hboxBotoes.setSpacing(1)
        
        
        #adicionando os botoes ao layout principal
        self.layoutPrincipal.addLayout(hboxBotoes)
        
        self.setLayout(self.layoutPrincipal)
        self.PesquisarGrid()
    
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
        
    def CreateFilterLayout(self):
        self.lblBusca = Label('Campo:', self)
        self.cmbField = ComboBox(self)
        self.cmbField.addItems(self.header_grid)
        self.cmbField.setCurrentIndex(0)
        if(self.headerList[0][1] == 'TextBox'):
            self.txtBusca = TextBox(self)
        elif(self.headerList[0][1] == 'DateBox'):
            self.txtBusca = DateBox(self)
        
        self.btnBuscar = Botao('&Buscar', self)
        
        hboxBusca = LayoutHorizontal()
        hboxBusca.addWidget(self.lblBusca)
        hboxBusca.addWidget(self.cmbField)
        hboxBusca.addWidget(self.txtBusca)
        hboxBusca.addWidget(self.btnBuscar)
        self.layoutPrincipal.addLayout(hboxBusca)
        
        return hboxBusca
    
    def UpdateTxtBusca(self):
        index = self.cmbField.currentIndex()
        
        if(self.headerList[index][1] == 'TextBox'):
            novoTxtBusca = TextBox(self)
            self.layoutPrincipal.replaceWidget(self.txtBusca, novoTxtBusca)
            self.txtBusca.close()
            self.txtBusca = novoTxtBusca
        elif(self.headerList[index][1] == 'DateBox'):
            self.layoutPrincipal.replaceWidget(self.txtBusca, DateBox(self))
        else:
            novoTxtBusca = TextBox(self)
            self.layoutPrincipal.replaceWidget(self.txtBusca, novoTxtBusca)
            self.txtBusca.close()
            self.txtBusca = novoTxtBusca
    
    
    def CenterOnScreen(self):
        '''alinhando a o formulario no centro da tela'''
        resolucao = QDesktopWidget().screenGeometry()
        self.move((resolucao.width() / 2) - (self.frameSize().width() / 2), (resolucao.height() / 2) - (self.frameSize().height() / 2))
        
    def PesquisarGrid(self):
        '''Método faz uma busca de clientes no banco de dados, e cria uma lista de tuplas'''
        # faz a consulta no banco e recebe uma lista de tuplas
        #texto_busca = str(self.txtBusca.text())
        #lista_dados_cliente = self.db.ConsultaClientesPorNome(texto_busca)
        df = self.db.GetColumnFromView(["*"], self.view)
        #df = self.db.QueryView(None, self.view, self.PesquisarGridDict)
        # setando no grid a qtde de linhas, com a mesma qtde de registros da lista
        #qtde_registros = len(lista_dados_cliente)
        qtde_registros = len(df)
        if(qtde_registros > self.limit):
            qtde_registros = self.limit
        self.grdPesquisaCliente.clearContents()
        self.grdPesquisaCliente.setRowCount(qtde_registros)
        
        for linha in range(qtde_registros):
            for col_index in self.dict_grid.keys():
                #preenchendo o grid de pesquisa
                col = self.dict_grid[col_index]
                self.grdPesquisaCliente.setItem(linha, col_index, QTableWidgetItem(str(df[col][linha])))
        
        
        
        if(qtde_registros > 0):
            self.grdPesquisaCliente.selectRow(0)
        
    def __inserir(self):
        #print ("Entrou AbrePesquisa")
        self.frmInserir = FrmInsDefault(self.db, self.view, self.dictFields, self.vDictBD, 'NULL', "'I'")
        #FrmPesquisaCliente(self, self.db)
        #print ("Passou FrmPesquisaCliente")
        self.frmInserir.setModal(True)
        self.frmInserir.show()
        self.frmInserir.exec_()
        self.PesquisarGrid()
    
    def __atualizar(self):
        vID = self.GetColumnValueFromCurrentItem('ID')
        df = self.db.GetColumnFromView(['*'], self.view, vID)
        #vDictAsListTuple = sorted(list(self.dictFields.items()), key=lambda tup: tup[1][1])
        #for vKey in [x[0] for x in vDictAsListTuple]:    
        #    self.fLayout.addRow(vKey, self.dictFields[vKey][3])
        for vKey in self.dictFields.keys():
            col = self.dictFields[vKey][1].replace("@", "")
            self.dictFields[vKey][3].setText(str(df[col][0]))
        
        self.frmInserir = FrmInsDefault(self.db, self.view, self.dictFields, self.vDictBD, vID, "'U'")
        self.frmInserir.setModal(True)
        self.frmInserir.show()
        self.frmInserir.exec_()
        self.PesquisarGrid()
    
    def __deletar(self):
        
        try:
            vID = self.GetColumnValueFromCurrentItem('ID')
            
            w = Widget()
            result = MessageBox().question(w, 'Cadastro de {}'.format(self.view), 'Tem certeza que deseja excluir este registro?', MessageBox.Yes | MessageBox.No, MessageBox.No)
            if result == QMessageBox.Yes:
                self.db.DeleteView(self.view, vID)
                MessageBox.information(self, '', u'exclusão feita com sucesso!', MessageBox.Ok, MessageBox.Ok)
                
        except Exception as e:
            w = Widget()
            MessageBox.information(self, '', 'Ocorreu o seguinte erro ao tentar excluir o {}: \n{}'.format(self.view, str(e)), MessageBox.Ok, MessageBox.Ok)
        
        self.PesquisarGrid()
    
    def GetColumnValueFromCurrentItem(self,columnname):
    
        row = self.grdPesquisaCliente.currentItem().row()
        #col = widget.currentItem().column()
        
        #loop through headers and find column number for given column name
        headercount = self.grdPesquisaCliente.columnCount()
        for x in range(0,headercount,1):
            headertext = self.grdPesquisaCliente.horizontalHeaderItem(x).text()
            if columnname == headertext:
                matchcol = x
                break
        
        cell = self.grdPesquisaCliente.item(row,matchcol).text ()   # get cell at row, col
        
        return cell

if __name__ == '__main__':
    import sys
    root = QApplication(sys.argv)
    db = Database()
    db.ConnectDB()
    vHeaderList = ['ID', 'IDPLANOCONTAS', 'COD_CTA', 'CTA']
    app = FrmCadDefault(db, 'VW_CAIXABANCO', vHeaderList)
    #app = FrmInsDefault(db)
    app.show()
    root.exec_()