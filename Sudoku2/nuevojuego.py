'''
Created on 29/07/2013

@author: Danny
'''
from PyQt4.QtGui import QMainWindow
from ui_nuevojuego import Ui_NuevoJuego
from sudoku import Sudoku
import ctypes

##  \brief     Clase que corresponde a la ventana de configuracion de opciones para un nuevo juego
##  \details   Aqui se mostraran 3 secciones:
##  \details   ----->Dificultad. Se escogen la dificultad deseada.
##  \details   ----->Opciones de Alerta. Se escoge que tipos de alerta queremos que nos de la aplicacion al momento de jugar.
##  \details   ----->Ayuda. Activamos o desactivamos el boton de ayuda.
class Nuevojuego(QMainWindow):

    def __init__(self):
        """Contructor
            Setea uno de los dos checkbox de alertas en true y anade el fondo a la ventana."""
        QMainWindow.__init__(self)
        self.ui= Ui_NuevoJuego()
        self.ui.setupUi(self)
        self.ui.pBJugar.clicked.connect(self.onPbjugarClicked)
        self.ui.pBCancelar.clicked.connect(self.onPbcancelarClicked)
        self.MessageBox= ctypes.windll.user32.MessageBoxA
        self.MB_ICONERROR = 0x00000010L #Critical Icon
        
    def onPbjugarClicked(self):
        """Despliega la ventana con el tablero para empezar el juego
            *Crea una instancia de la clase Sudoku y la muestra.
            *Verificara que se halla escogido un solo nivel de dificultad.
            *Verificara que halla escogido al menos una opcion de alerta."""
        facil=self.ui.rBFacil.isChecked()
        medio=self.ui.rBMedio.isChecked()
        dificil=self.ui.rBDificil.isChecked()
        experto=self.ui.rBExperto.isChecked()
        invalida=self.ui.cbInvalidas.isChecked()
        incorrecta=self.ui.cbIncorrectas.isChecked()
        ayuda=self.ui.cbhelp.isChecked()
        if facil==False and medio==False and dificil==False and experto==False:
            self.MessageBox(None,"Seleccione Un Nivel De Dificultad..!","ERROR",self.MB_ICONERROR)
        elif invalida==False and incorrecta==False:
            self.MessageBox(None,"Seleccione al menos una opcion de alertas..!","ERROR",self.MB_ICONERROR)
        elif facil:
            self.n= Sudoku(1,invalida,incorrecta,ayuda,"")
            self.n.setVisible(True)
            self.close()
        elif medio:
            self.n= Sudoku(2,invalida,incorrecta,ayuda,"")
            self.n.setVisible(True)
            self.close()
        elif dificil:
            self.n= Sudoku(3,invalida,incorrecta,ayuda,"")
            self.n.setVisible(True)
            self.close()
        elif experto:
            self.n= Sudoku(4,invalida,incorrecta,ayuda,"")
            self.n.setVisible(True)
            self.close()
        
    def onPbcancelarClicked(self):
        """Despliega la ventana anterior
            Crea una instancia de la ventana principal y la muestra"""
        from principal import Principal
        self.p= Principal()
        self.p.setVisible(True)
        self.close()