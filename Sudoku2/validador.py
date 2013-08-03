'''
Created on 02/08/2013

@author: Danny
'''
from graficador import Graficador
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