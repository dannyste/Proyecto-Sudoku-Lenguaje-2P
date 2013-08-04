'''
Created on 29/07/2013

@author: Danny
'''
from PyQt4.QtGui import QMainWindow
from ui_acercade import Ui_acercaDe

class Acercade(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui= Ui_acercaDe()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.onPushbuttonClicked)
        
    def Regresar(self,p):
        self.r = p
        
    def onPushbuttonClicked(self):
        self.close()
        self.r.show()