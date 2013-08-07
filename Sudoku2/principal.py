'''
Created on 28/07/2013

@author: Danny
'''
from PyQt4.QtGui import QMainWindow,QInputDialog,QLineEdit
from ui_principal import Ui_principal
from nuevojuego import Nuevojuego
from acercade import Acercade
from sudoku import Sudoku
import ctypes

##  \brief     Clase que corresponde a la ventana Inicial
##  \details   Aqui se mostraran 5 diferentes opciones:
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
        self.ui.CargaJuego.clicked.connect(self.onCargajuegoClicked)
        self.MessageBox= ctypes.windll.user32.MessageBoxA
        self.MB_ICONERROR = 0x00000010L #Critical Icon
    
    def onNuevojuegoClicked(self):
        """Inicia un nuevo juego
            Crea una instancia de la clase NuevoJuego y la muestra para poder escoger las opciones de juego."""
        self.n= Nuevojuego()
        self.n.setVisible(True)
        self.close()
    
    def onAcercadeClicked(self):  
        """Muestra informacion del grupo desarrollador"""      
        self.a = Acercade()
        self.a.setVisible(True)        
        self.close()
        
    def onSalirClicked(self):
        """Nos permite cerrar la aplicacion"""
        self.close()
        
    def onCargajuegoClicked(self):
        (nombre,ok) = QInputDialog.getText(self, self.tr("Sudoku"), self.tr("Nombre:"),QLineEdit.Normal, self.tr(""))
        if ok==True:
            while str(nombre)=="" and ok==True:
                self.MessageBox(None,"Ingrese Un Nombre..!","ERROR",self.MB_ICONERROR)
                (nombre,ok) = QInputDialog.getText(self, self.tr("Sudoku"), self.tr("Nombre:"),QLineEdit.Normal, self.tr(""))
            if ok==True:
                archivo=open("Partidas.txt","r")
                linea=archivo.readline()
                Existe=0
                while linea!="":
                    partida=linea.split(",")
                    nombreG=partida[0]
                    if str(nombre)==nombreG:
                        Existe=1
                        break
                    linea=archivo.readline()
                if Existe==1:
                    invalida=partida[3]
                    incorrecta=partida[4]
                    ayuda=partida[5]
                    self.n= Sudoku(5,invalida,incorrecta,ayuda,partida)
                    self.n.setVisible(True)
                    self.close()
                else:
                    self.MessageBox(None,"No Se Encontro El Archivo..!","ERROR",self.MB_ICONERROR)
                archivo.close()
        
if __name__ == '__main__':
    import sys
    from PyQt4.QtGui import QApplication
    app = QApplication(sys.argv)
    p = Principal()
    sys.exit(app.exec_())