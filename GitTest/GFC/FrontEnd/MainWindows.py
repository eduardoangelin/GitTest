# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindows.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from GFC.FrontEnd.ContasAPagar import FormContasAPagar

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(457, 472)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 457, 21))
        self.menubar.setObjectName("menubar")
        self.menuCadastro = QtWidgets.QMenu(self.menubar)
        self.menuCadastro.setObjectName("menuCadastro")
        self.menuContas = QtWidgets.QMenu(self.menubar)
        self.menuContas.setObjectName("menuContas")
        self.menuMovimentos = QtWidgets.QMenu(self.menubar)
        self.menuMovimentos.setObjectName("menuMovimentos")
        MainWindow.setMenuBar(self.menubar)
        self.actionContas_a_Pagar = QtWidgets.QAction(MainWindow)
        self.actionContas_a_Pagar.setObjectName("actionContas_a_Pagar")
        #self.actionContas_a_Pagar.
        self.actionContas_a_Receber = QtWidgets.QAction(MainWindow)
        self.actionContas_a_Receber.setObjectName("actionContas_a_Receber")
        self.actionBanco = QtWidgets.QAction(MainWindow)
        self.actionBanco.setObjectName("actionBanco")
        self.actionClientes = QtWidgets.QAction(MainWindow)
        self.actionClientes.setObjectName("actionClientes")
        self.actionFornecedores = QtWidgets.QAction(MainWindow)
        self.actionFornecedores.setObjectName("actionFornecedores")
        self.actionReceitas = QtWidgets.QAction(MainWindow)
        self.actionReceitas.setObjectName("actionReceitas")
        self.actionDespesas = QtWidgets.QAction(MainWindow)
        self.actionDespesas.setObjectName("actionDespesas")
        self.actionDepositos = QtWidgets.QAction(MainWindow)
        self.actionDepositos.setObjectName("actionDepositos")
        self.actionSaques = QtWidgets.QAction(MainWindow)
        self.actionSaques.setObjectName("actionSaques")
        self.actionTransferencias_Banc_rias = QtWidgets.QAction(MainWindow)
        self.actionTransferencias_Banc_rias.setObjectName("actionTransferencias_Banc_rias")
        self.menuCadastro.addAction(self.actionBanco)
        self.menuCadastro.addAction(self.actionClientes)
        self.menuCadastro.addAction(self.actionFornecedores)
        self.menuContas.addAction(self.actionContas_a_Pagar)
        self.menuContas.addAction(self.actionContas_a_Receber)
        self.menuMovimentos.addAction(self.actionDepositos)
        self.menuMovimentos.addAction(self.actionSaques)
        self.menuMovimentos.addAction(self.actionTransferencias_Banc_rias)
        self.menubar.addAction(self.menuCadastro.menuAction())
        self.menubar.addAction(self.menuContas.menuAction())
        self.menubar.addAction(self.menuMovimentos.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GFC"))
        self.menuCadastro.setTitle(_translate("MainWindow", "Cadastro"))
        self.menuContas.setTitle(_translate("MainWindow", "Contas"))
        self.menuMovimentos.setTitle(_translate("MainWindow", "Movimentos"))
        self.actionContas_a_Pagar.setText(_translate("MainWindow", "Contas a Pagar"))
        self.actionContas_a_Receber.setText(_translate("MainWindow", "Contas a Receber"))
        self.actionBanco.setText(_translate("MainWindow", "Caixa e Banco"))
        self.actionClientes.setText(_translate("MainWindow", "Clientes e Fornecedores"))
        self.actionFornecedores.setText(_translate("MainWindow", "Receitas e Despesas"))
        self.actionReceitas.setText(_translate("MainWindow", "Receitas"))
        self.actionDespesas.setText(_translate("MainWindow", "Despesas"))
        self.actionDepositos.setText(_translate("MainWindow", "Depositos"))
        self.actionSaques.setText(_translate("MainWindow", "Saques"))
        self.actionTransferencias_Banc_rias.setText(_translate("MainWindow", "Transferencias Bancárias"))

    #@pyqtSignature("")
    
    def on_button_released(self):
        """
        Slot documentation goes here.
        """
        FT = FormContasAPagar()
        FT.show()   