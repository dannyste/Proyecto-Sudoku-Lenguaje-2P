'''
Created on 06/08/2013

@author: Edwin
'''
from PyQt4.QtGui import QMainWindow,QTableWidget, QTableWidgetItem
from ui_estadisticas import Ui_estadisticas
from sudoku import Sudoku

class estadisticas(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui= Ui_estadisticas()
        self.ui.setupUi(self)
        self.ui.pBCancelar.clicked.connect(self.onPushbuttonClicked)
        self.ui.twEstadisticas.setColumnCount(2)
        headers=["Jugadores","Tiempo"]
        self.ui.twEstadisticas.setHorizontalHeaderLabels(headers)
        archivo=open("Partidas.txt","r")
        linea=archivo.readline()
        partida=linea.split(",")
        nombreG=partida[0]
        cronometro=partida[2]
        j=0
        while linea!="": 
            self.ui.twEstadisticas.insertRow( self.ui.twEstadisticas.rowCount() )
            partida=linea.split(",")
            nombreG=partida[0]
            cronometro=partida[2] 
            item1 = QTableWidgetItem()
            item2 = QTableWidgetItem()  
            item1.setText("%s" % nombreG )
            item2.setText("%s" % cronometro) 
            self.ui.twEstadisticas.setItem(j,0, item1)
            self.ui.twEstadisticas.setItem(j,1, item2)
            j=j+1
            linea=archivo.readline()        

    def onPushbuttonClicked(self):   
        """maneja evento click boton ok """       
        from principal import Principal
        self.n= Principal()
        self.n.setVisible(True) 
        self.close()
