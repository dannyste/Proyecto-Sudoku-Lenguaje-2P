'''
Created on 29/07/2013

@author: Danny
'''
from PyQt4.QtGui import QMainWindow
from ui_nuevojuego import Ui_NuevoJuego
from sudoku import Sudoku
import ctypes
MessageBox= ctypes.windll.user32.MessageBoxA
MB_ICONERROR = 0x00000010L #Critical Icon

class Nuevojuego(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui= Ui_NuevoJuego()
        self.ui.setupUi(self)
        self.ui.pBJugar.clicked.connect(self.onPbjugarClicked)
        
    def onPbjugarClicked(self):
        facil=self.ui.rBFacil.isChecked()
        medio=self.ui.rBMedio.isChecked()
        dificil=self.ui.rBDificil.isChecked()
        experto=self.ui.rBExperto.isChecked()
        inc=self.ui.cbIncorrectas.isChecked()
        inv=self.ui.cbInvalidas.isChecked()
        help=self.ui.cbhelp.isChecked()
        
        if facil==False and medio==False and dificil==False and experto==False:
            MessageBox(None,"Seleccione Un Nivel De Dificultad..!","ERROR",MB_ICONERROR)
        elif inc==False and inv==False:
            MessageBox(None,"Seleccione al menos una opcion de alertas..!","ERROR",MB_ICONERROR)
        elif facil:
            self.n= Sudoku()
            self.n.setVisible(True)
            self.close()
            dificultad=1
        elif medio:
            self.n= Sudoku()
            self.n.setVisible(True)
            self.close()
            dificultad=2
        elif dificil:
            self.n= Sudoku()
            self.n.setVisible(True)
            self.close()
            dificultad=3
        elif experto:
            self.n= Sudoku()
            self.n.setVisible(True)
            self.close()
            dificultad=4