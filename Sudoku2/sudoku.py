'''
Created on 30/07/2013

@author: Edwin
'''
from PyQt4.QtGui import QMainWindow,QPushButton
from PyQt4.QtCore import QSize,SIGNAL,QTime,QTimer
from ui_sudoku import Ui_Sudoku
from validador import Validador
import ctypes

class Sudoku(QMainWindow):

    def __init__(self,dificultad,incorrecta,invalida,ayuda):
        QMainWindow.__init__(self)
        self.ui= Ui_Sudoku()
        self.ui.setupUi(self)        
        self.dificultad=dificultad
        self.incorrecta=incorrecta
        self.invalida=invalida
        if ayuda==False:
            self.ui.btHelp.setEnabled(False)
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
        self.MessageBox= ctypes.windll.user32.MessageBoxA
        self.MB_ICONERROR = 0x00000010L #Critical Icon
    
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
        
    def onColocarFicha(self):
        caja=QPushButton()
        caja=self.sender()
        if self.Bmetodo==0:
            for i in range(9):
                self.posFichas[i].setIcon(self.imgFichas[0])
            self.muestraPosiblesFichas(caja)
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