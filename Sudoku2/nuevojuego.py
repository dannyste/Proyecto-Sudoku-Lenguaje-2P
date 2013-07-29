'''
Created on 29/07/2013

@author: Danny
'''
from PyQt4.QtGui import QMainWindow
from ui_nuevojuego import Ui_NuevoJuego

class Nuevojuego(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui= Ui_NuevoJuego()
        self.ui.setupUi(self)