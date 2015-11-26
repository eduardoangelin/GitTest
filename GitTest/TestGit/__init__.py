import sys
from TelaGrid import Ui_MainWindow
from ReportTest import ReportTest
from ConnectDB import ConnectDB
from PyQt5 import QtWidgets
#from PyQt5 import QtCore, QtGui, QtWidgets



if __name__ == "__main__":
	amazon = True
	connection = ConnectDB()
	reportTest = ReportTest(connection)
	bla = reportTest.BalanceteReport()
	reportTest.ReportLayout()
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow(connection)
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
	sys.exit(0)

