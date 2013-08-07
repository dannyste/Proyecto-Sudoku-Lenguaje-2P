'''
Created on 28/07/2013

@author: Danny
'''
from PyQt4.QtGui import QMainWindow
from ui_principal import Ui_principal
from nuevojuego import Nuevojuego
from acercade import Acercade

##  \brief     Clase que corresponde a la ventana Inicial
##  \details   Aquí se mostrarán 5 diferentes opciones:
##  \details           *Nuevo Juego
##  \details           *Cargar Juego
##  \details           *Estadisticas
##  \details           *Acerca de
##  \details           *Salir
class Principal(QMainWindow):

    def __init__(self):
        """Costructor"""
        QMainWindow.__init__(self)
        self.ui= Ui_principal()
        self.ui.setupUi(self)
        self.show()
        self.ui.nuevoJuego.clicked.connect(self.onNuevojuegoClicked)
        self.ui.AcercaDe.clicked.connect(self.onAcercadeClicked)
        self.ui.salir.clicked.connect(self.onSalirClicked)
    
    def onNuevojuegoClicked(self):
        """Inicia un nuevo juego
            Crea una instancia de la clase NuevoJuego y la muestra para poder escoger las opciones de juego."""
        self.n= Nuevojuego()
        self.n.Regresar(self)
        self.n.setVisible(True)
        self.close()
    
    def onAcercadeClicked(self):  
        """Muestra información del grupo desarrollador"""      
        self.a = Acercade()
        self.a.Regresar(self)
        self.a.setVisible(True)        
        self.close()
        
    def onSalirClicked(self):
        """Nos permite cerrar la aplicación"""
        self.close()
        
if __name__ == '__main__':
    import sys
    from PyQt4.QtGui import QApplication
    app = QApplication(sys.argv)
    p = Principal()
    sys.exit(app.exec_())