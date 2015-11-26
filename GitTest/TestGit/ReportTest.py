'''
Created on 26 de nov de 2015

@author: Angelin
'''

from __future__ import print_function
import pandas as pd
import numpy as np
import pandas.io.sql as psql
from jinja2 import Environment, FileSystemLoader
import os.path
from reportlab.pdfgen import canvas


class ReportTest(object):
    
    def __init__(self, conn):
        self.connection = conn
        
    def BalanceteReport(self):
        #cursor = self.connection.cursor()
        #cursor.execute("select * from balancete")
        #rows = cursor.fetchall()
        
        sql = "select * from balancete"
        
        df = psql.frame_query(sql, self.connection)
        #print (df)
        sales_report = pd.pivot_table(df, columns=["codigo", "nomeconta"], values=["saldoanterior", "debitos", "creditos", "saldoatual"],aggfunc=[np.sum, np.sum, np.sum, np.sum], fill_value=0)
        sales_report.head()
        #print (sales_report)
        return sales_report
        
        
    def ReportLayout(self):
        env = Environment(loader=FileSystemLoader('.'))
        template = env.get_template("myReportLayout.html")
        pathHTML = os.path.abspath("/GitTest\\TestGit\\myReportLayout.html")
        
        c = canvas.Canvas("hello.pdf")
        c.drawString(100,750,"Welcome to Reportlab!")
        c.save()
        
        
        
        
        