from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(object):
    
    def __init__(self, conn):
        self.connection = conn

    def fillTableWidget(self, _translate):
        cursor = self.connection.cursor()
        cursor.execute("select id, codigo, planocontas  from teste")
        rows = cursor.fetchall()
        print (len(rows))
        self.tableWidget.setRowCount(len(rows))
        
        for i in range(len(rows)):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(i, item)
            item = self.tableWidget.verticalHeaderItem(i)
            item.setText(_translate("MainWindow", str(rows[i].id)))

            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(i, 0, item)
            item = self.tableWidget.item(i, 0)
            item.setText(_translate("MainWindow", str(rows[i].id)))
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(i, 1, item)
            item = self.tableWidget.item(i, 1)
            item.setText(_translate("MainWindow", str(rows[i].codigo)))
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(i, 2, item)
            item = self.tableWidget.item(i, 2)
            item.setText(_translate("MainWindow", str(rows[i].planocontas)))
        cursor.close()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setProperty("ID", 1)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(180, 60, 341, 161))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        #self.tableWidget.setRowCount(4)
        #item = QtWidgets.QTableWidgetItem()
        #self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        #item = QtWidgets.QTableWidgetItem()
        #self.tableWidget.setItem(0, 0, item)
        #item = QtWidgets.QTableWidgetItem()
        #self.tableWidget.setItem(0, 1, item)
        #item = QtWidgets.QTableWidgetItem()
        #self.tableWidget.setItem(0, 2, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setProperty("PlanoContas", _translate("MainWindow", "Ativo"))
        #item = self.tableWidget.verticalHeaderItem(0)
        #item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Codigo"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Plano Contas"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget
        self.fillTableWidget(_translate)
        self.tableWidget.setSortingEnabled(__sortingEnabled)

