'''
Created on 28/07/2013

@author: Danny
'''
from PyQt4.QtGui import QMainWindow
from ui_principal import Ui_principal
from nuevojuego import Nuevojuego
from acercade import Acercade

class Principal(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui= Ui_principal()
        self.ui.setupUi(self)
        self.show()
        self.ui.nuevoJuego.clicked.connect(self.onNuevojuegoClicked)
        self.ui.AcercaDe.clicked.connect(self.onAcercadeClicked)
        self.ui.salir.clicked.connect(self.onSalirClicked)
    
    def onNuevojuegoClicked(self):
        self.n= Nuevojuego()
        self.n.Regresar(self)
        self.n.setVisible(True)
        self.close()
    
    def onAcercadeClicked(self):        
        self.a = Acercade()
        self.a.Regresar(self)
        self.a.setVisible(True)        
        self.close()
        
    def onSalirClicked(self):
        self.close()
        
if __name__ == '__main__':
    import sys
    from PyQt4.QtGui import QApplication
    app = QApplication(sys.argv)
    p = Principal()
    sys.exit(app.exec_())