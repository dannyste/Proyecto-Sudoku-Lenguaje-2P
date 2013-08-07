'''
Created on 30/07/2013

@author: Edwin
'''
from PyQt4.QtGui import QMainWindow,QPushButton,QInputDialog,QLineEdit
from PyQt4.QtCore import QSize,SIGNAL,QTime,QTimer
from ui_sudoku import Ui_Sudoku
from validador import Validador
import ctypes
import random

## \brief Clase que maneja el tablero
## \details Aqui se genera el tablero de acuerdo con las especificaciones dadas desde la ventana de nuevo juego como las opciones de alerta, la dificultad y la ayuda.
class Sudoku(QMainWindow):

    def __init__(self,dificultad,invalida,incorrecta,ayuda):
        """Contructor
            *Crea una instancia de Sudoku de acuerdo a las especificaciones dadas por las variables de entrada.
            *Se crea e inicia el cron�metro.
            Parametro:
            - dificultad Dificultad del juego.
            - incorrecta Determina si se realizan o no las validaciones de jugadas incorrectas.
            - invalida Determina si se realizan o no las validaciones de jugadas inv�lidas.
            - ayuda Determina si se activa o no el boton ayuda."""
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
        """Inicia el contador del cronometro"""
        self.tiempo = QTime()
        self.tiempo.setHMS(0,0,0,0)
        self.timer = QTimer()
        self.connect(self.timer, SIGNAL("timeout()"),self.mostrarTiempo)
        self.segundos = 0
        self.text = self.tiempo.toString("hh:mm:ss")
        self.ui.contTiempo.display(self.text)
        self.timer.start(1000)
        
    def mostrarTiempo(self):
        """Controla el aumento de los segundos"""
        self.nuevoTiempo = QTime()
        self.segundos = self.segundos + 1
        self.nuevoTiempo = self.tiempo.addSecs(self.segundos)
        self.cronometro = self.nuevoTiempo.toString("hh:mm:ss")
        self.ui.contTiempo.display(self.cronometro)
        
    def initGui(self):
        """Inicializa la interfaz gr�fica del tablero
            Se inicializa el tablero y luego se lo llena con el numero de fichas de acuerdo a la dificultad."""
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
        """Slot que se ejecuta cada vez que se presione en algun boton dentro del tablero
         Determina que acci�n se realiza al pulsar la ficha en el tablero.
         Controla que tipo de validaci�n se realiza."""
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
                indice=self.ui.gLTablero.indexOf(caja)
                nAct=str(self.numero)
                nAnt=caja.accessibleName()
                caja.setAccessibleName(nAct)
                self.validador.Relacionar()
                if (self.validador.Validaciones()):
                    if self.jugadaIncorrecta(indice):
                        self.MessageBox(None,"Su Jugada Es Incorrecta, Intente Con Otra Ficha","Jugada Incorrecta",self.MB_ICONERROR)
                        caja.setAccessibleName(nAnt)
                        self.validador.Relacionar()
                    else:
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
        """Inicializa el arreglo al principio con fichas vacias"""
        self.posFichas=[]
        for i in range(9):
            self.posFichas.append(QPushButton())
            self.posFichas[i].setIcon(self.imgFichas[0])
            self.posFichas[i].setIconSize(QSize(48, 48))
            self.posFichas[i].setFlat(True)
            
    def muestraPosiblesFichas(self,caja):
        """Muestra las fichas que son validas para esa posici�n.
            Parametro: button Boton en la posicion donde se desea colocar la ficha."""
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
        """Agrega las posibles fichas en la ventana"""
        k=0
        for i in range(3):
            for j in range(3):
                self.ui.glPistas.addWidget(self.posFichas[k],i,j)
                k=k+1
                
    def opcionAyuda(self,caja):
        """Maneja la opci�n cuando el jugador activa la ayuda
            Parametro: b El bot�n que corresponde al lugar del tablero donde el jugador desea se coloque el numero correcto."""
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
        """Llena el tablero que se mostrara al jugador de acuerdo a la dificultad que se eligi�
            Se asigna el numero de fichas de acuerdo con la dificultad en posiciones aleatorias."""
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
        """Lee la dificultad y se asigna el numero de fichas correspondiente a dicha dificultad."""
        if self.dificultad==1:
            self.nroFichas=(81-35)
        elif self.dificultad==2:
            self.nroFichas=(81-50)
        elif self.dificultad==3:
            self.nroFichas=(81-63)
        else:
            self.nroFichas=(81-64)
    
    def convertirInttoImg(self):
        """Convierte el numero que se encuentra el la matriz Modelo a una ficha."""
        for i in range(9):
            for j in range(9):
                self.cajas[i][j].setIcon(self.imgFichas[self.numeros[i][j]])
                self.cajas[i][j].setIconSize(QSize(48, 48))
                self.cajas[i][j].setStyleSheet("*{background-color:rgb(158,209,247)}")
                
    def jugadaIncorrecta(self,indice):
        """Determina si la jugada es Incorrecta
            *Compara el numero que el jugador desea colocar con el numero que est� en esa misma posici�n del tablero solucionado.
            Parametro: ind El indice del boton correspondiente al lugar donde el jugador desea colocar la ficha.
            Retorna: 1 -> Incorrecto , 0 -> Correcto."""
        if not(self.incorrecta):
            return 0
        contador = 0
        for i in range(9):
            for j in range(9):
                if indice==contador:
                    if self.numero==self.resuelto[i][j]:
                        return 0
                    else:
                        return 1
                contador = contador + 1
        return 1
            
    def leerArchivoSudokuResuelto(self):
        """Lee el archivo de texto encriptado y llena el arreglo con el sudoku resuelto"""
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
        self.intercambiarFilas()
        self.intercambiarColumnas()
        self.intercambiarGrupoFilas()
        self.intercambiarGrupoColumnas()

    def intercambiarFilas(self):
        """Realiza un intercambio aleatorio de las filas dentro de las subcuadriculas"""
        inicial=0
        final=2
        for i in range(3):
            i1=random.randint(inicial,final)
            i2=random.randint(inicial,final)
            while i1==i2:
                i2=random.randint(inicial,final)
            for j in range(9):
                numero=self.resuelto[i1][j]
                self.resuelto[i1][j]=self.resuelto[i2][j]
                self.resuelto[i2][j]=numero
            inicial = inicial + 3
            final = final + 3
            
    def intercambiarColumnas(self):
        """Realiza un intercambio aleatorio de las columnas dentro de las subcuadriculas"""
        inicial=0
        final=2
        for j in range(3):
            j1=random.randint(inicial,final)
            j2=random.randint(inicial,final)
            while j1==j2:
                j2=random.randint(inicial,final)
            for i in range(9):
                numero=self.resuelto[i][j1]
                self.resuelto[i][j1]=self.resuelto[i][j2]
                self.resuelto[i][j2]=numero
            inicial = inicial + 3
            final = final + 3
            
    def intercambiarGrupoFilas(self):
        """Realiza un intercambio aleatorio de filas de subcuadriculas dentro del tablero"""
        f1=random.randint(0,2)
        f2=random.randint(0,2)
        while f1==f2:
            f2=random.randint(0,2)
        if ((f1==0 and f2==1) or (f1==1 and f2==0)):
            for i in range(3):
                for j in range(9):
                    numero=self.resuelto[i][j]
                    self.resuelto[i][j]=self.resuelto[i+3][j]
                    self.resuelto[i+3][j]=numero
        elif ((f1==0 and f2==2) or (f1==2 and f2==0)):
            for i in range(3):
                for j in range(9):
                    numero=self.resuelto[i][j]
                    self.resuelto[i][j]=self.resuelto[i+6][j]
                    self.resuelto[i+6][j]=numero
        else:
            for i in range(3,6):
                for j in range(9):
                    numero=self.resuelto[i][j]
                    self.resuelto[i][j]=self.resuelto[i+3][j]
                    self.resuelto[i+3][j]=numero
        
    def intercambiarGrupoColumnas(self):
        """Realiza un intercambio aleatorio de columnas de subcuadriculas dentro del tablero"""
        c1=random.randint(0,2)
        c2=random.randint(0,2)
        while c1==c2:
            c2=random.randint(0,2)
        if ((c1==0 and c2==1) or (c1==1 and c2==0)):
            for i in range(9):
                for j in range(3):
                    numero=self.resuelto[i][j]
                    self.resuelto[i][j]=self.resuelto[i][j+3]
                    self.resuelto[i][j+3]=numero
        elif ((c1==0 and c2==2) or (c1==2 and c2==0)):
            for i in range(9):
                for j in range(3):
                    numero=self.resuelto[i][j]
                    self.resuelto[i][j]=self.resuelto[i][j+6]
                    self.resuelto[i][j+6]=numero
        else:
            for i in range(9):
                for j in range(3,6):
                    numero=self.resuelto[i][j]
                    self.resuelto[i][j]=self.resuelto[i][j+3]
                    self.resuelto[i][j+3]=numero
    
    def onPbf1Clicked(self):
        """Setea el numero 1 siendo �sta ficha la que el jugador quiere colocar en alguna parte del tablero."""
        self.numero = 1
        self.Bmetodo = 1
        
    def onPbf2Clicked(self):
        """Setea el numero 2 siendo �sta ficha la que el jugador quiere colocar en alguna parte del tablero."""
        self.numero = 2
        self.Bmetodo = 1
        
    def onPbf3Clicked(self):
        """Setea el numero 3 siendo �sta ficha la que el jugador quiere colocar en alguna parte del tablero."""
        self.numero = 3
        self.Bmetodo = 1
        
    def onPbf4Clicked(self):
        """Setea el numero 4 siendo �sta ficha la que el jugador quiere colocar en alguna parte del tablero."""
        self.numero = 4
        self.Bmetodo = 1
        
    def onPbf5Clicked(self):
        """Setea el numero 5 siendo �sta ficha la que el jugador quiere colocar en alguna parte del tablero."""
        self.numero = 5
        self.Bmetodo = 1
        
    def onPbf6Clicked(self):
        """Setea el numero 6 siendo �sta ficha la que el jugador quiere colocar en alguna parte del tablero."""
        self.numero = 6
        self.Bmetodo = 1
        
    def onPbf7Clicked(self):
        """Setea el numero 7 siendo �sta ficha la que el jugador quiere colocar en alguna parte del tablero."""
        self.numero = 7
        self.Bmetodo = 1
        
    def onPbf8Clicked(self):
        """Setea el numero 8 siendo �sta ficha la que el jugador quiere colocar en alguna parte del tablero."""
        self.numero = 8
        self.Bmetodo = 1
        
    def onPbf9Clicked(self):
        """Setea el numero 9 siendo �sta ficha la que el jugador quiere colocar en alguna parte del tablero."""
        self.numero = 9
        self.Bmetodo = 1
        
    def onBtHelpClicked(self):
        """Setea el numero 0 que indicar� que se va a colocar el n�mero correcto automaticamente."""
        self.numero = 0
        self.Bmetodo = 1
    
    def onActionnuevo_juegoTriggered(self):
        """Despliega la ventana de nuevo juego"""
        from nuevojuego import Nuevojuego
        self.n= Nuevojuego()
        self.n.setVisible(True)
        self.close()
    
    def onActionguardarTriggered(self):
        """Guarda la partida actual
            Se pide el nombre con el que se desea guardar la partida y luego se procede a grabarla con encriptaci�n."""
        (nombre,ok) = QInputDialog.getText(self, self.tr("Sudoku"), self.tr("Nombre:"),QLineEdit.Normal, self.tr(""))
        if ok==True:
            while str(nombre)=="" and ok==True:
                self.MessageBox(None,"Ingrese Un Nombre..!","ERROR",self.MB_ICONERROR)
                (nombre,ok) = QInputDialog.getText(self, self.tr("Sudoku"), self.tr("Nombre:"),QLineEdit.Normal, self.tr(""))
            if ok==True:
                archivo=open("Partidas.txt","a")
                archivo.write(str(nombre))
                archivo.write(",")
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
        """Salir de la partida actual."""
        self.close()