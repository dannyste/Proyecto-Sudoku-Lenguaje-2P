# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'estadisticas.ui'
#
# Created: Tue Aug 06 15:15:33 2013
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

class Ui_estadisticas(object):
    def setupUi(self, estadisticas):
        estadisticas.setObjectName(_fromUtf8("estadisticas"))
        estadisticas.resize(633, 438)
        estadisticas.setStyleSheet(_fromUtf8("#centralwidget{background-image: url(:/img/fondo3.jpg)}"))
        self.centralwidget = QtGui.QWidget(estadisticas)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.twEstadisticas = QtGui.QTableWidget(self.centralwidget)
        self.twEstadisticas.setGeometry(QtCore.QRect(190, 190, 256, 192))
        self.twEstadisticas.setObjectName(_fromUtf8("twEstadisticas"))
        self.twEstadisticas.setColumnCount(0)
        self.twEstadisticas.setRowCount(0)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 20, 471, 131))
        self.label.setStyleSheet(_fromUtf8("#label{background-image:  url(:/img/TituloIco.png);}"))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        estadisticas.setCentralWidget(self.centralwidget)

        self.retranslateUi(estadisticas)
        QtCore.QMetaObject.connectSlotsByName(estadisticas)

    def retranslateUi(self, estadisticas):
        estadisticas.setWindowTitle(_translate("estadisticas", "MainWindow", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    estadisticas = QtGui.QMainWindow()
    ui = Ui_estadisticas()
    ui.setupUi(estadisticas)
    estadisticas.show()
    sys.exit(app.exec_())

