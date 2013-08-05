'''
Created on 29/07/2013

@author: Danny
'''
from PyQt4.QtGui import QMainWindow
from ui_nuevojuego import Ui_NuevoJuego
from sudoku import Sudoku
import ctypes

class Nuevojuego(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui= Ui_NuevoJuego()
        self.ui.setupUi(self)
        self.ui.pBJugar.clicked.connect(self.onPbjugarClicked)
        self.ui.pBCancelar.clicked.connect(self.onPbcancelarClicked)
        self.MessageBox= ctypes.windll.user32.MessageBoxA
        self.MB_ICONERROR = 0x00000010L #Critical Icon
        
    def onPbjugarClicked(self):
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
            self.n= Sudoku(1,invalida,incorrecta,ayuda)
            self.n.setVisible(True)
            self.close()
        elif medio:
            self.n= Sudoku(1,invalida,incorrecta,ayuda)
            self.n.setVisible(True)
            self.close()
        elif dificil:
            self.n= Sudoku(1,invalida,incorrecta,ayuda)
            self.n.setVisible(True)
            self.close()
        elif experto:
            self.n= Sudoku(1,invalida,incorrecta,ayuda)
            self.n.setVisible(True)
            self.close()
            
    def Regresar(self,p):
        self.r=p
        
    def onPbcancelarClicked(self):
        self.hide()
        self.r.show()