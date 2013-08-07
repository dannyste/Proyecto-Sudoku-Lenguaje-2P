'''
Created on 01/08/2013

@author: Danny
'''
from PyQt4.QtGui import QIcon,QPixmap

## \brief clase que se encarga de manejar el color en las fichas en caso de error.
## \details Es utilizada por la clase Sudoku para colorear las fichas cuando existe error en X, en Y, o en la Subcuadricula.
class Graficador:

    def __init__(self,Sudoku):
        """Constructor
           parametro:
            s - Nos da la referencia al objeto Sudoku que la crea, para poder acceder a sus variables"""
        self.sudoku=Sudoku
        
    def initArregloImgFichas(self):
        """Inicializa un arreglo de Iconos del 1 - 9
            Se asigna a cada elemento del arreglo la imagen de la ficha correspondiente al indice del arreglo."""
        self.sudoku.imgFichas=[]
        vacia = QIcon()
        vacia.addPixmap(QPixmap(":/img/vacia2.png"),QIcon.Normal,QIcon.Off)
        self.sudoku.imgFichas.append(vacia)
        uno = QIcon()
        uno.addPixmap(QPixmap(":/img/1.png"),QIcon.Normal,QIcon.Off)
        self.sudoku.imgFichas.append(uno)
        dos = QIcon()
        dos.addPixmap(QPixmap(":/img/2.png"),QIcon.Normal,QIcon.Off)
        self.sudoku.imgFichas.append(dos)
        tres = QIcon()
        tres.addPixmap(QPixmap(":/img/3.png"),QIcon.Normal,QIcon.Off)
        self.sudoku.imgFichas.append(tres)
        cuatro = QIcon()
        cuatro.addPixmap(QPixmap(":/img/4.png"),QIcon.Normal,QIcon.Off)
        self.sudoku.imgFichas.append(cuatro)
        cinco = QIcon()
        cinco.addPixmap(QPixmap(":/img/5.png"),QIcon.Normal,QIcon.Off)
        self.sudoku.imgFichas.append(cinco)
        seis = QIcon()
        seis.addPixmap(QPixmap(":/img/6.png"),QIcon.Normal,QIcon.Off)
        self.sudoku.imgFichas.append(seis)
        siete = QIcon()
        siete.addPixmap(QPixmap(":/img/7.png"),QIcon.Normal,QIcon.Off)
        self.sudoku.imgFichas.append(siete)
        ocho = QIcon()
        ocho.addPixmap(QPixmap(":/img/8.png"),QIcon.Normal,QIcon.Off)
        self.sudoku.imgFichas.append(ocho)
        nueve = QIcon()
        nueve.addPixmap(QPixmap(":/img/9.png"),QIcon.Normal,QIcon.Off)
        self.sudoku.imgFichas.append(nueve)
        
    def pintaX(self,i):
        """Pinta una fila determinada del tablero cuando hay un error
           parametro:
           i La fila en la que se quiere colocar una ficha invalida o incorrecta"""
        for j in range(9):
            self.sudoku.cajas[i][j].setStyleSheet("*{background-color: rgb(255, 255, 127)}");
            
    def pintaY(self,j):
        """Pinta una columna determinada del tablero cuando hay un error
           parametro:
               j La columna en la que se quiere colocar una ficha invalida o incorrecta"""
        for i in range(9):
            self.sudoku.cajas[i][j].setStyleSheet("*{background-color: rgb(255, 255, 127)}");
    
    def pintaSub(self,x,y):
        """Pinta una subcuadricula determinada del tablero cuando hay un error
            Parametro:
                x La fila desde donde empieza la subccuadricula en la que se quiere colocar una ficha invalida o incorrecta.
                y La columna desde donde empieza la subccuadricula en la que se quiere colocar una ficha invalida o incorrecta"""
        for i in range(x,x+3):
            for j in range(y,y+3):
                self.sudoku.cajas[i][j].setStyleSheet("*{background-color: rgb(255, 255, 127)}");
                
    def pintaTablero(self):
        """Pinta completamente tablero"""
        for i in range(9):
            for j in range(9):
                self.sudoku.cajas[i][j].setStyleSheet("*{background-color:rgb(158,209,247)}")