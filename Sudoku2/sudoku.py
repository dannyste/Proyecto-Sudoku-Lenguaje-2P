'''
Created on 30/07/2013

@author: Edwin
'''
from PyQt4.QtGui import QMainWindow
from ui_sudoku import Ui_Sudoku

class Sudoku(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui= Ui_Sudoku()
        self.ui.setupUi(self)
        self.ui.pBf1.clicked.connect(self.onPbf1Clicked)
        self.ui.pBf2.clicked.connect(self.onPbf2Clicked)
        self.ui.pBf3.clicked.connect(self.onPbf3Clicked)
        self.ui.pBf4.clicked.connect(self.onPbf4Clicked)
        self.ui.pBf5.clicked.connect(self.onPbf5Clicked)
        self.ui.pBf6.clicked.connect(self.onPbf6Clicked)
        self.ui.pBf7.clicked.connect(self.onPbf7Clicked)
        self.ui.pBf8.clicked.connect(self.onPbf8Clicked)
        self.ui.pBf9.clicked.connect(self.onPbf9Clicked)
        self.ui.btHelp.clicked.connect(self.onBtHelpClicked)
        
    def onPbf1Clicked(self):
        self.numero = 1
        self.Bmetodo = 1
        
    def onPbf2Clicked(self):
        self.numero = 2
        self.Bmetodo = 1
        
    def onPbf3Clicked(self):
        self.numero = 3
        self.Bmetodo = 1
        
    def onPbf4Clicked(self):
        self.numero = 4
        self.Bmetodo = 1
        
    def onPbf5Clicked(self):
        self.numero = 5
        self.Bmetodo = 1
        
    def onPbf6Clicked(self):
        self.numero = 6
        self.Bmetodo = 1
        
    def onPbf7Clicked(self):
        self.numero = 7
        self.Bmetodo = 1
        
    def onPbf8Clicked(self):
        self.numero = 8
        self.Bmetodo = 1
        
    def onPbf9Clicked(self):
        self.numero = 9
        self.Bmetodo = 1
        
    def onBtHelpClicked(self):
        self.numero = 0
        self.Bmetodo = 1
        
    
    
