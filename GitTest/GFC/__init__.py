# coding=utf-8
import sys
from GFC.Database.Database import *
from GFC.Report.ReportTest import *

if __name__ == "__main__":
    try:
        amazon = True
        #f = say_hello()
        print ('Inicio')
        db = Database()
        connection = db.ConnectDB()
        print ('Conectado')
        reportTest = ReportTest(db.connection)
        reportTest.ReportHTML("fn_BalanceteConsolidadoContabil", ["'2015-01-31'", "'2015-01-01'"])
        print ('Gerando Relatorio')
        sys.exit(0)
    except Exception:
        print ("error({0}): {1}".format(Exception.errno, Exception.strerror))
        sys.exit(0)