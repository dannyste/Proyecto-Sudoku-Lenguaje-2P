'''
Created on 01/08/2013

@author: Danny
'''
from PyQt4.QtGui import QIcon,QPixmap
class Graficador:

    def __init__(self,Sudoku):
        self.sudoku=Sudoku
        
    def initArregloImgFichas(self):
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
        for j in range(9):
            self.sudoku.cajas[i][j].setStyleSheet("*{background-color: rgb(255, 255, 127)}");
            
    def pintaY(self,j):
        for i in range(9):
            self.sudoku.cajas[i][j].setStyleSheet("*{background-color: rgb(255, 255, 127)}");
    
    def pintaSub(self,x,y):
        for i in range(x,x+3):
            for j in range(y,y+3):
                self.sudoku.cajas[i][j].setStyleSheet("*{background-color: rgb(255, 255, 127)}");
                
    def pintaTablero(self):
        for i in range(9):
            for j in range(9):
                self.sudoku.cajas[i][j].setStyleSheet("*{background-color:rgb(158,209,247)}")