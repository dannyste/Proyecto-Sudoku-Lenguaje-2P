'''
Created on 29/07/2013

@author: Danny
'''
from PyQt4.QtGui import QMainWindow
from ui_acercade import Ui_acercaDe

##   \brief     Clase que corresponde a la ventana acerca de.
##   \details   Aqui se mostrara la informacion de los integrantes del grupo desarrollador del juego.
class Acercade(QMainWindow): 
        
    def __init__(self):   
        """Constructor"""     
        QMainWindow.__init__(self)
        self.ui= Ui_acercaDe()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.onPushbuttonClicked)
        
    def onPushbuttonClicked(self):   
        """maneja evento click boton ok """       
        from principal import Principal
        self.p= Principal()
        self.p.setVisible(True)
        self.close()