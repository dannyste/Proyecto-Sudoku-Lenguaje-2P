'''
Created on 30/07/2013

@author: Edwin
'''
from PyQt4.QtGui import QMainWindow,QPushButton
from PyQt4.QtCore import QSize,SIGNAL,QTime,QTimer
from ui_sudoku import Ui_Sudoku
from validador import Validador
import ctypes
import random

class Sudoku(QMainWindow):

    def __init__(self,dificultad,invalida,incorrecta,ayuda):
        QMainWindow.__init__(self)
        self.ui= Ui_Sudoku()
        self.ui.setupUi(self)        
        self.dificultad=dificultad
        self.invalida=invalida
        self.incorrecta=incorrecta
        self.ayuda=ayuda
        if self.ayuda==False:
            self.ui.btHelp.setEnabled(False)
        else:
            self.ayudas=0
        self.initCronometro()
        self.validador=Validador(self)
        self.validador.graficador.initArregloImgFichas()
        self.initArregloPistas()
        self.initGui()
        self.ui.pBf1.clicked.connect(self.onPbf1Clicked)
        self.ui.pBf2.clicked.connect(self.onPbf2Clicked)
        self.ui.pBf3.clicked.connect(self.onPbf3Clicked)
        self.ui.pBf4.clicked.connect(self.onPbf4Clicked)
        self.ui.pBf5.clicked.connect(self.onPbf5Clicked)
        self.ui.pBf6.clicked.connect(self.onPbf6Clicked)
        self.ui.pBf7.clicked.connect(self.onPbf7Clicked)
        self.ui.pBf8.clicked.connect(self.onPbf8Clicked)
        self.ui.pBf9.clicked.connect(self.onPbf9Clicked)
        self.ui.btHelp.clicked.connect(self.onBtHelpClicked)
        self.ui.actionNuevo_Juego.triggered.connect(self.onActionnuevo_juegoTriggered)
        self.ui.actionGuardar.triggered.connect(self.onActionguardarTriggered)
        self.ui.actionSalir.triggered.connect(self.onActionsalirTriggered)
        self.MessageBox= ctypes.windll.user32.MessageBoxA
        self.MB_ICONERROR = 0x00000010L #Critical Icon
        self.MB_ICONEXCLAMATION= 0x00000030L #Exclamation Icon
    
    def initCronometro(self):
        self.tiempo = QTime()
        self.tiempo.setHMS(0,0,0,0)
        self.timer = QTimer()
        self.connect(self.timer, SIGNAL("timeout()"),self.mostrarTiempo)
        self.segundos = 0
        self.text = self.tiempo.toString("hh:mm:ss")
        self.ui.contTiempo.display(self.text)
        self.timer.start(1000)
        
    def mostrarTiempo(self):
        self.nuevoTiempo = QTime()
        self.segundos = self.segundos + 1
        self.nuevoTiempo = self.tiempo.addSecs(self.segundos)
        self.cronometro = self.nuevoTiempo.toString("hh:mm:ss")
        self.ui.contTiempo.display(self.cronometro)
        
    def initGui(self):
        self.Bmetodo=0
        self.cajas=[]
        for i in range(9):
            qpushbutton=[]
            for j in range(9):
                qpushbutton.append(QPushButton())
            self.cajas.append(qpushbutton)
        for i in range(9):
            for j in range(9):
                self.cajas[i][j].setIcon(self.imgFichas[0])
                self.cajas[i][j].setIconSize(QSize(48, 48))
                self.cajas[i][j].setAccessibleName("0")
                self.cajas[i][j].setStyleSheet("*{background-color:rgb(158,209,247)}")
                self.ui.gLTablero.addWidget(self.cajas[i][j],i,j)
                self.cajas[i][j].clicked.connect(self.onColocarFicha)
        self.validador.Relacionar()
        if self.dificultad!=5:
            self.leerArchivoSudokuResuelto()
            self.llenaTableroDificultad()
        
    def onColocarFicha(self):
        caja=QPushButton()
        caja=self.sender()
        if self.Bmetodo==0:
            for i in range(9):
                self.posFichas[i].setIcon(self.imgFichas[0])
            self.muestraPosiblesFichas(caja)
        else:
            if self.numero==0:
                self.ayudas = self.ayudas + 1
                self.opcionAyuda(caja)
                if self.ayudas==5:
                    self.ui.btHelp.setEnabled(False)
            else:
                nAct=str(self.numero)
                nAnt=caja.accessibleName()
                caja.setAccessibleName(nAct)
                self.validador.Relacionar()
                if (self.validador.Validaciones()):
                    caja.setIcon(self.imgFichas[self.numero])
                    caja.setIconSize(QSize(48, 48))
                    caja.setStyleSheet("*{background-color:rgb(158,209,247)}")
                else:
                    caja.setAccessibleName(nAnt)
                    self.validador.Relacionar()
            if (self.validador.ValidarEspaciosVacios()):
                self.MessageBox(None,"Sudoku Correcto..!","FELICITACIONES",self.MB_ICONEXCLAMATION)
            for i in range(9):
                self.posFichas[i].setIcon(self.imgFichas[0])
            self.Bmetodo=0
        
    def initArregloPistas(self):
        self.posFichas=[]
        for i in range(9):
            self.posFichas.append(QPushButton())
            self.posFichas[i].setIcon(self.imgFichas[0])
            self.posFichas[i].setIconSize(QSize(48, 48))
            self.posFichas[i].setFlat(True)
            
    def muestraPosiblesFichas(self,caja):
        contador=0
        for i in range(1,10):
            nAct=str(i)
            nAnt=caja.accessibleName()
            caja.setAccessibleName(nAct)
            self.validador.Relacionar()
            if (self.validador.ValidarX() and self.validador.ValidarY() and self.validador.SubCuadros()):
                self.posFichas[contador].setIcon(self.imgFichas[i])
                contador = contador + 1
            self.validador.graficador.pintaTablero()
            caja.setAccessibleName(nAnt)
            self.validador.Relacionar()
            self.mostrarPistas()
            
    def mostrarPistas(self):
        k=0
        for i in range(3):
            for j in range(3):
                self.ui.glPistas.addWidget(self.posFichas[k],i,j)
                k=k+1
                
    def opcionAyuda(self,caja):
        indice=self.ui.gLTablero.indexOf(caja)
        contador=0
        for i in range(9):
            for j in range(9):
                if indice==contador:
                    self.numeros[i][j]=self.resuelto[i][j]
                    nAct=str(self.resuelto[i][j])
                    caja.setAccessibleName(nAct)
                    caja.setIcon(self.imgFichas[self.resuelto[i][j]])
                    caja.setIconSize(QSize(48, 48))
                    caja.setStyleSheet("*{background-color:rgb(158,209,247)}")
                contador = contador +1
                
    def llenaTableroDificultad(self):
        self.setDificultad()
        for i in range(self.nroFichas):
            f=random.randint(0, 8)
            c=random.randint(0, 8)
            while (self.numeros[f][c]!=0):
                f=random.randint(0, 8)
                c=random.randint(0, 8)
            self.numeros[f][c]=self.resuelto[f][c]
            self.cajas[f][c].setAccessibleName(str(self.numeros[f][c]))
        self.convertirInttoImg()
    
    def setDificultad(self):
        if self.dificultad==1:
            self.nroFichas=(81-35)
        elif self.dificultad==2:
            self.nroFichas=(81-50)
        elif self.dificultad==3:
            self.nroFichas=(81-63)
        else:
            self.nroFichas=(81-64)
    
    def convertirInttoImg(self):
        for i in range(9):
            for j in range(9):
                self.cajas[i][j].setIcon(self.imgFichas[self.numeros[i][j]])
                self.cajas[i][j].setIconSize(QSize(48, 48))
                self.cajas[i][j].setStyleSheet("*{background-color:rgb(158,209,247)}")
                
    def leerArchivoSudokuResuelto(self):
        archivo=open("Soluciones.txt","r")
        linea=archivo.readline()
        k=0
        self.resuelto=[]
        for i in range(9):
            numeros=[]
            for j in range(9):
                numeros.append(int(linea[k]))
                k=k+1
            self.resuelto.append(numeros)
        archivo.close()
    
    def onPbf1Clicked(self):
        self.numero = 1
        self.Bmetodo = 1
        
    def onPbf2Clicked(self):
        self.numero = 2
        self.Bmetodo = 1
        
    def onPbf3Clicked(self):
        self.numero = 3
        self.Bmetodo = 1
        
    def onPbf4Clicked(self):
        self.numero = 4
        self.Bmetodo = 1
        
    def onPbf5Clicked(self):
        self.numero = 5
        self.Bmetodo = 1
        
    def onPbf6Clicked(self):
        self.numero = 6
        self.Bmetodo = 1
        
    def onPbf7Clicked(self):
        self.numero = 7
        self.Bmetodo = 1
        
    def onPbf8Clicked(self):
        self.numero = 8
        self.Bmetodo = 1
        
    def onPbf9Clicked(self):
        self.numero = 9
        self.Bmetodo = 1
        
    def onBtHelpClicked(self):
        self.numero = 0
        self.Bmetodo = 1
    
    def onActionnuevo_juegoTriggered(self):
        from nuevojuego import Nuevojuego
        self.n= Nuevojuego()
        self.n.setVisible(True)
        self.close()
    
    def onActionguardarTriggered(self):
        archivo=open("Partidas.txt","a")
        for i in range(9):
            for j in range(9):
                archivo.write(str(self.numeros[i][j]))
        archivo.write(",")
        archivo.write(self.cronometro)
        if self.invalida:
            archivo.write(",1")
        else:
            archivo.write(",0")
        if self.incorrecta:
            archivo.write(",1")
        else:
            archivo.write(",0")
        if self.ayuda:
            archivo.write(",1")
        else:
            archivo.write(",0")
        archivo.write("\n")
        archivo.close()
        self.MessageBox(None,"Partida Guardada..!","Sudoku",self.MB_ICONEXCLAMATION)
    
    def onActionsalirTriggered(self):
        self.close()