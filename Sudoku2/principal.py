'''
Created on 28/07/2013

@author: Danny
'''
from PyQt4.QtGui import QMainWindow
from ui_principal import Ui_principal
from ui_acercade import Ui_acercaDe

class Principal(QMainWindow):

    def __init__(self):
        QMainWindow._init_(self)
        self.ui= Ui_principal()
        self.ui.setupUi(self)
        self.ui.AcercaDe.click.connect(self.mostrar)
        
    def mostrar(self):
        self.setVisible(False)
                
if __name__ == '__main__':
    import sys
    from PyQt4.QtGui import QApplication
    from PyQt4 import QtGui
    app=QApplication(sys.argv)
    p = QtGui.QMainWindow()
    ui = Ui_principal()
    ui.setupUi(p)
    p.show()
    sys.exit(app.exec_())