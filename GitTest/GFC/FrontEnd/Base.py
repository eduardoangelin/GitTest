# -*- coding: UTF-8 -*-

'''
Created on 2 de dez de 2015

@author: Angelin
'''

#from PyQt5 import QtCore, QtGui, QtWidgets
import pyodbc
from PyQt5.QtWidgets import QLabel, QLineEdit, QCheckBox, QPushButton, QVBoxLayout, QHBoxLayout, QFormLayout, QWidget, QDialog, QTableWidget, QMessageBox, QAbstractItemView 


class TextBox(QLineEdit):
    
    def __init__(self, parent = None):
        super(TextBox, self).__init__(parent)
        
class Label(QLabel):
    
    def __init__(self, pText= '', parent = None):
        super(Label, self).__init__(parent)
        
        self.setText(pText)
        
class CheckBox(QCheckBox):
    
    def __init__(self,pText= '', parent = None):
        super(CheckBox, self).__init__(parent)
        
        self.setText(pText)
        
class Botao(QPushButton):
    
    def __init__(self,pText= '', parent = None):
        super(Botao, self).__init__(parent)
        
        self.setText(pText)
        
        
class LayoutVertical(QVBoxLayout):
    
    def __init__(self):
        super(LayoutVertical, self).__init__()
        
class LayoutHorizontal(QHBoxLayout):
    
    def __init__(self):
        super(LayoutHorizontal, self).__init__()
        
class FormLayout(QFormLayout):
    
    def __init__(self):
        super(FormLayout, self).__init__()
        
class Widget(QWidget):
    
    def __init__(self, parent = None):
        super(Widget, self).__init__(parent)
        
        
class Diaglog(QDialog):
    
    def __init__(self, parent = None):
        super(Diaglog, self).__init__(parent)
        
class Grid(QTableWidget):
    
    def __init__(self, parent = None , qtde_linhas = 0, qtde_colunas = 0):
        super(Grid, self).__init__(parent)
        
        self.setRowCount(qtde_linhas)
        self.setColumnCount(qtde_colunas)
        
                
        #redimenciona a linha automaticamente
        self.resizeRowsToContents()
        
        #coloca as linhas em cores alternadas
        self.setAlternatingRowColors(True) 
        
        #habilita a ordena��o ao clicar no titulo da coluna
        self.setSortingEnabled(True)
        
        #seleciona toda a linha quando clicado
        self.setSelectionBehavior(QAbstractItemView.SelectRows)

class MessageBox(QMessageBox):
    
    def __init__(self, parent = None):
        super(MessageBox, self).__init__(parent)