# coding=utf-8
import sys
import os
from GFC.FrontEnd.TelaGrid import Ui_MainWindow
from GFC.Report.ReportTest import ReportTest
from GFC.Database.Database import ConnectDB
from PyQt5 import QtWidgets
#from PyQt5 import QtCore, QtGui, QtWidgets
from io import BytesIO
from GFC.pdfdocument.document import PDFDocument
from reportlab.pdfgen import canvas
from reportlab.graphics import renderPDF
from GFC.pdfdocument.svglib import svg2rlg
from reportlab.lib.pagesizes import A4


def runApp():
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


def say_hello():
	f = BytesIO()
	pdf = PDFDocument(f)
	pdf.init_report()
	pdf.h1('Hello World')
	pdf.p('Creating PDFs made easy.')
	myCanvas = canvas.Canvas('myFileTest.pdf', pagesize=A4)
	#keep for later
	pdf.draw_svg(canvas = myCanvas, path= os.getcwd())
	pdf.generate()
	return f.getvalue()




