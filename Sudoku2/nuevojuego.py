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
        incorrecta=self.ui.cbIncorrectas.isChecked()
        invalida=self.ui.cbInvalidas.isChecked()
        ayuda=self.ui.cbhelp.isChecked()
        
        if facil==False and medio==False and dificil==False and experto==False:
            MessageBox(None,"Seleccione Un Nivel De Dificultad..!","ERROR",MB_ICONERROR)
        elif incorrecta==False and invalida==False:
            MessageBox(None,"Seleccione al menos una opcion de alertas..!","ERROR",MB_ICONERROR)
        elif facil:
            self.n= Sudoku(1,incorrecta,invalida,ayuda)
            self.n.setVisible(True)
            self.close()
        elif medio:
            self.n= Sudoku(1,incorrecta,invalida,ayuda)
            self.n.setVisible(True)
            self.close()
        elif dificil:
            self.n= Sudoku(1,incorrecta,invalida,ayuda)
            self.n.setVisible(True)
            self.close()
        elif experto:
            self.n= Sudoku(1,incorrecta,invalida,ayuda)
            self.n.setVisible(True)
            self.close()