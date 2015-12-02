'''
Created on 1 de dez de 2015

@author: Angelin
'''
from PyQt5 import QtCore, QtWidgets
import pandas as pd
from GFC.Database.Database import Database
from PyQt5.QtCore import QVariant


class Widgets(object):
    
    def __init__(self, db):
        self.db = db
    
    def comboBox(self, Form, view, column, labelText = None):
        _translate = QtCore.QCoreApplication.translate
        
        #Create Elements
        labelText = view if labelText is None else labelText
        vLabel = QtWidgets.QLabel(Form)
        vLabel.setObjectName("lbl_{}".format(view))
        vLabel.setText(labelText)
        vComboBox = QtWidgets.QComboBox(Form)
        vComboBox.setObjectName("cmb_{}".format(view))
        
        #Fill with Data
        columnsList = ["id"]+[column]
        vDataFrame = self.db.GetColumnFromView(columnsList, view)
        vLenDataFrame = len(vDataFrame)
        for i in range(vLenDataFrame):
            vId = vDataFrame['id'].iloc[i]
            vValue = vDataFrame[column].iloc[i]
            vComboBox.addItem(vValue, QVariant(vId))
        return vLabel, vComboBox
    
    def comboBox(self, Form, view, column, labelText = None):
        _translate = QtCore.QCoreApplication.translate
        
        #Create Elements
        labelText = view if labelText is None else labelText
        vLabel = QtWidgets.QLabel(Form)
        vLabel.setObjectName("lbl_{}".format(view))
        vLabel.setText(labelText)
        vComboBox = QtWidgets.QComboBox(Form)
        vComboBox.setObjectName("cmb_{}".format(view))
        
        #Fill with Data
        columnsList = ["id"]+[column]
        vDataFrame = self.db.GetColumnFromView(columnsList, view)
        vLenDataFrame = len(vDataFrame)
        for i in range(vLenDataFrame):
            vId = vDataFrame['id'].iloc[i]
            vValue = vDataFrame[column].iloc[i]
            vComboBox.addItem(vValue, QVariant(vId))
        return vLabel, vComboBox
            
        