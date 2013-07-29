# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'principal.ui'
#
# Created: Sun Jul 28 16:07:01 2013
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_principal(object):
    def setupUi(self, principal):
        principal.setObjectName(_fromUtf8("principal"))
        principal.setWindowModality(QtCore.Qt.NonModal)
        principal.resize(543, 358)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/sudoku1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        principal.setWindowIcon(icon)
        principal.setStyleSheet(_fromUtf8("#centralwidget{background-image: url(:/img/fondoPrinc.png);}\n"
""))
        self.centralwidget = QtGui.QWidget(principal)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.icono = QtGui.QLabel(self.centralwidget)
        self.icono.setGeometry(QtCore.QRect(40, 10, 471, 131))
        self.icono.setStyleSheet(_fromUtf8("#icono{background-image: url(:/img/TituloIco.png);}\n"
""))
        self.icono.setText(_fromUtf8(""))
        self.icono.setObjectName(_fromUtf8("icono"))
        self.nuevoJuego = QtGui.QPushButton(self.centralwidget)
        self.nuevoJuego.setGeometry(QtCore.QRect(70, 170, 75, 61))
        self.nuevoJuego.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/ico Jugar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nuevoJuego.setIcon(icon1)
        self.nuevoJuego.setIconSize(QtCore.QSize(72, 72))
        self.nuevoJuego.setFlat(True)
        self.nuevoJuego.setObjectName(_fromUtf8("nuevoJuego"))
        self.CargaJuego = QtGui.QPushButton(self.centralwidget)
        self.CargaJuego.setGeometry(QtCore.QRect(380, 170, 75, 61))
        self.CargaJuego.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/cargar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CargaJuego.setIcon(icon2)
        self.CargaJuego.setIconSize(QtCore.QSize(52, 52))
        self.CargaJuego.setFlat(True)
        self.CargaJuego.setObjectName(_fromUtf8("CargaJuego"))
        self.Estadisticas = QtGui.QPushButton(self.centralwidget)
        self.Estadisticas.setGeometry(QtCore.QRect(230, 170, 75, 61))
        self.Estadisticas.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/icoEstadisticas.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Estadisticas.setIcon(icon3)
        self.Estadisticas.setIconSize(QtCore.QSize(60, 60))
        self.Estadisticas.setFlat(True)
        self.Estadisticas.setObjectName(_fromUtf8("Estadisticas"))
        self.AcercaDe = QtGui.QPushButton(self.centralwidget)
        self.AcercaDe.setGeometry(QtCore.QRect(150, 240, 75, 61))
        self.AcercaDe.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/about.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AcercaDe.setIcon(icon4)
        self.AcercaDe.setIconSize(QtCore.QSize(60, 60))
        self.AcercaDe.setFlat(True)
        self.AcercaDe.setObjectName(_fromUtf8("AcercaDe"))
        self.salir = QtGui.QPushButton(self.centralwidget)
        self.salir.setGeometry(QtCore.QRect(300, 240, 71, 71))
        self.salir.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/icoSalir.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.salir.setIcon(icon5)
        self.salir.setIconSize(QtCore.QSize(60, 60))
        self.salir.setFlat(True)
        self.salir.setObjectName(_fromUtf8("salir"))
        principal.setCentralWidget(self.centralwidget)

        self.retranslateUi(principal)
        QtCore.QMetaObject.connectSlotsByName(principal)

    def retranslateUi(self, principal):
        principal.setWindowTitle(_translate("principal", "SUDOKU", None))

import img_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    principal = QtGui.QMainWindow()
    ui = Ui_principal()
    ui.setupUi(principal)
    principal.show()
    sys.exit(app.exec_())

