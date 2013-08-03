'''
Created on 30/07/2013

@author: Edwin
'''
from PyQt4.QtGui import QMainWindow,QPushButton
from PyQt4.QtCore import QSize,SIGNAL,QTime,QTimer
from ui_sudoku import Ui_Sudoku
from validador import Validador

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
                qpushbutton.append(QPushButton(self))
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
        if self.Bmetodo==1:
            self.boton=QPushButton(self)
            self.boton=self.sender()
            self.boton.setIcon(self.imgFichas[self.numero])
            self.boton.setIconSize(QSize(48, 48))
            self.Bmetodo=0
        
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