# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindows.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from GFC.FrontEnd.Widgets import Widgets

class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow, db):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(383, 374)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        vWidgets = Widgets(db)
        self.label, self.comboBox = vWidgets.comboBox(self.centralwidget, "PlanoContas", "cta", "Plano de Contas")
        #self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 100, 47, 13))
        #self.label.setObjectName("label")
        #self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(230, 100, 69, 22))
        #self.comboBox.setObjectName("comboBox")
        #self.comboBox.addItem("")
        #self.comboBox.addItem("")
        #self.comboBox.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 383, 21))
        self.menubar.setObjectName("menubar")
        self.menuCadastro = QtWidgets.QMenu(self.menubar)
        self.menuCadastro.setObjectName("menuCadastro")
        self.menuContas = QtWidgets.QMenu(self.menubar)
        self.menuContas.setObjectName("menuContas")
        self.menuMovimentos = QtWidgets.QMenu(self.menubar)
        self.menuMovimentos.setObjectName("menuMovimentos")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuCadastro.menuAction())
        self.menubar.addAction(self.menuContas.menuAction())
        self.menubar.addAction(self.menuMovimentos.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        #self.comboBox.setItemText(0, _translate("MainWindow", "1"))
        #self.comboBox.setItemText(1, _translate("MainWindow", "2"))
        #self.comboBox.setItemText(2, _translate("MainWindow", "3"))
        #self.label.setText(_translate("MainWindow", "TextLabel"))
        self.menuCadastro.setTitle(_translate("MainWindow", "Cadastro"))
        self.menuContas.setTitle(_translate("MainWindow", "Contas"))
        self.menuMovimentos.setTitle(_translate("MainWindow", "Movimentos"))

