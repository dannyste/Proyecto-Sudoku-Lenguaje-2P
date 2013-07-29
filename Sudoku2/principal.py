'''
Created on 28/07/2013

@author: Danny
'''
from PyQt4.QtGui import QMainWindow
from ui_principal import Ui_principal
from acercade import Acercade

class Principal(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui= Ui_principal()
        self.ui.setupUi(self)
        self.show()
        self.ui.AcercaDe.clicked.connect(self.onAcercadeClicked)
        self.ui.salir.clicked.connect(self.onSalirClicked)
    
    def onAcercadeClicked(self):        
        self.w = Acercade()
        self.w.setVisible(True)        
        self.close()
        
    def onSalirClicked(self):
        self.close()
        
if __name__ == '__main__':
    import sys
    from PyQt4.QtGui import QApplication
    app = QApplication(sys.argv)
    p = Principal()
    sys.exit(app.exec_())