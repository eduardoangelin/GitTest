# -*- coding: UTF-8 -*-
'''
Created on 10 de dez de 2015

@author: Angelin
'''

class Util(object):
    '''Classe de metodos gerericos'''


    def __init__(self, params):
        pass
        
    def IdentifyParamProcedure(self, vCommand):
        vCommand = vCommand.replace("EXECUTE", "").replace(" ", "").split(",")
        return vCommand
                
            
        
        