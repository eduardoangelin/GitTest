'''
Created on 26 de nov de 2015

@author: Angelin
'''

# coding=utf-8
from __future__ import print_function
import pandas as pd
import numpy as np
import pandas.io.sql as psql
from jinja2 import Environment, FileSystemLoader
import os.path
import webbrowser
from reportlab.pdfgen import canvas


class ReportTest(object):
    
    def __init__(self, conn):
        self.connection = conn
        
    def ReportHTML(self, vFunction, vInputs=['']):
        
        #vStrInputs = bytes(str.join(', ', vInputs), 'UTF-8')
        vStrInputs = str.join(', ', vInputs)
        sql = "select * from {}({})".format(vFunction, vStrInputs)
        
        df = psql.read_sql(sql, self.connection)
        
        df_html = df.to_html(index=False)
        filename = 'Report_{}.html'.format(vFunction)
        f = open(filename, 'wb')
        f.write(bytes(df_html, 'UTF-8'))
        f.close()
        path = os.getcwd()+'\\'+filename
        print (path)
        webbrowser.open(path)
        
        return df_html
        
        
    def ReportLayout(self):
        env = Environment(loader=FileSystemLoader('.'))
        #template = env.get_template("myReportLayout.html")
        #pathHTML = os.path.abspath("/GitTest\\TestGit\\myReportLayout.html")
        
        c = canvas.Canvas("hello.pdf")
        c.drawString(100,750,"Welcome to Reportlab!")
        c.save()
        
        
        
        
        