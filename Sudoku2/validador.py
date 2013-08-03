'''
Created on 02/08/2013

@author: Danny
'''
from PyQt4.QtGui import QMainWindow
from graficador import Graficador
import ctypes
MessageBox= ctypes.windll.user32.MessageBoxA
MB_ICONERROR = 0x00000010L #Critical Icon
class Validador:

    def __init__(self,Sudoku):
        self.sudoku=Sudoku
        self.graficador=Graficador(self.sudoku)
        
    def Relacionar(self):
        self.sudoku.numeros=[]
        for i in range(9):
            n=[]
            for j in range(9):
                n.append(int(self.sudoku.cajas[i][j].accessibleName()))
            self.sudoku.numeros.append(n)
            
    def ValidarEspaciosVacios(self):
        for i in range(9):
            for j in range(9):
                if self.sudoku.numeros[i][j] == 0:
                    return 0
        return 1
    
    def Subcuadros(self):
        self.contador = 0
        #primerSubcuadro
        for i in range(3):
            for j in  range(3):
                self.sudoku.subnumeros[i][j] = self.sudoku.numeros[i][j]
        self.contador = self.contador + self.VerificarSubcuadro()
        if not(self.VerificarSubcuadro()):
            self.graficador.pintaSub(0, 0)
        #SegundoSubcuadro
        for i in range(3):
            for j in  range(3,6):
                self.sudoku.subnumeros[i][j-3] = self.sudoku.numeros[i][j]
        self.contador = self.contador + self.VerificarSubcuadro()
        if not(self.VerificarSubcuadro()):
            self.graficador.pintaSub(0, 3)
        #TercerSubcuadro
        for i in range(3):
            for j in  range(6,9):
                self.sudoku.subnumeros[i][j-6] = self.sudoku.numeros[i][j]
        self.contador = self.contador + self.VerificarSubcuadro()
        if not(self.VerificarSubcuadro()):
            self.graficador.pintaSub(0, 6)
        #CuartoSubcuadro
        for i in range(3,6):
            for j in  range(3):
                self.sudoku.subnumeros[i-3][j] = self.sudoku.numeros[i][j]
        self.contador = self.contador + self.VerificarSubcuadro()
        if not(self.VerificarSubcuadro()):
            self.graficador.pintaSub(3, 0)
        #QuintoSubcuadro
        for i in range(3,6):
            for j in  range(3,6):
                self.sudoku.subnumeros[i-3][j-3] = self.sudoku.numeros[i][j]
        self.contador = self.contador + self.VerificarSubcuadro()
        if not(self.VerificarSubcuadro()):
            self.graficador.pintaSub(3, 3)
        #SextoSubcuadro
        for i in range(3,6):
            for j in  range(6,9):
                self.sudoku.subnumeros[i-3][j-6] = self.sudoku.numeros[i][j]
        self.contador = self.contador + self.VerificarSubcuadro()
        if not(self.VerificarSubcuadro()):
            self.graficador.pintaSub(3, 6)
        #SeptimoSubcuadro
        for i in range(6,9):
            for j in  range(3):
                self.sudoku.subnumeros[i-6][j] = self.sudoku.numeros[i][j]
        self.contador = self.contador + self.VerificarSubcuadro()
        if not(self.VerificarSubcuadro()):
            self.graficador.pintaSub(6, 0)
        #OctavoSubcuadro
        for i in range(6,9):
            for j in  range(3,6):
                self.sudoku.subnumeros[i-6][j-3] = self.sudoku.numeros[i][j]
        self.contador = self.contador + self.VerificarSubcuadro()
        if not(self.VerificarSubcuadro()):
            self.graficador.pintaSub(6, 3)
        #NovenoSubcuadro
        for i in range(6,9):
            for j in range(6,9):
                self.sudoku.subnumeros[i-6][j-6] = self.sudoku.numeros[i][j]
        self.contador = self.contador + self.VerificarSubcuadro()
        if not(self.VerificarSubcuadro()):
            self.graficador.pintaSub(6, 6)
        if self.contador == 9:
            return 1
        return 0
                   
    def VerificarSubcuadro(self):
        for i in range(3):
            for j in range(3):
                self.numero = self.sudoku.subnumeros[i][j]
                if self.numero != 0:
                    for k in range(3):
                        for l in range(3):
                            if i != k or j != l:
                                if self.numero == self.subnumero[k][l]:
                                    return 0
        return 1
    
    def ValidarX(self):
        self.b = 1
        for i in range(9):
            self.b = self.ValidaLinea(i)
            if self.b == 0:
                self.graficador.pintaX(i)
                return 0
        return 1
            
    def ValidaLinea(self,i):
        self.fichas[10] = {0}
        for j in range(9):
            self.ind = self.sudoku.numeros[i][j]
            self.fichas[self.ind] = self.fichas[self.ind] + 1
        return self.verificaArregloIndices(self.fichas)
    
    def ValidarY(self):
        self.b = 1
        for j in range(9):
            self.b = self.ValidaColumna(j)
            if self.b == 0:
                self.graficador.pintaY(j)
                return 0
        return 1
            
    def ValidaColumna(self,j):
        self.fichas[10] = {0}
        self.ind
        for i in range(9):
            self.ind = self.sudoku.numeros[i][j]
            self.fichas[self.ind] = self.fichas[self.ind] + 1
        return self.verificaArregloIndices(self.fichas)
    
    def verificaArregloIndices(self):
        for i in range(10):
            if self.arreglo[i] > 1:
                return 0
        return 1
    
    def Validaciones(self):
        self.b = 1
        if not(self.sudoku.inva):
            return 1
        
        if not(self.ValidarX()):
            self.sudoku.botonObj.setFlat(True)
            MessageBox(None,"Existen Números Repetidos En Las Filas..!","ERROR",MB_ICONERROR)
            self.graficador.pintaTablero()
            self.sudoku.botonObj.setFlat(False)
            self.b = 0
        if not(self.Subcuadros()):
            self.sudoku.botonObj.setFlat(True)
            MessageBox(None,"Existen Números Repetidos En Las Sub-Cuadrículas..!","ERROR",MB_ICONERROR)
            self.graficador.pintaTablero()
            self.sudoku.botonObj.selFlat(False)
            self.b = 0
        return self.b
    
            
            