# coding=utf-8
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from GFC.FrontEnd.MainWindows import Ui_MainWindow
from GFC.Database.Database import Database

if __name__ == "__main__":
    db = Database()
    db.ConnectDB()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, db)
    MainWindow.show()
    sys.exit(app.exec_())