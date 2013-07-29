# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'acercade.ui'
#
# Created: Sun Jul 28 16:07:30 2013
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

class Ui_acercaDe(object):
    def setupUi(self, acercaDe):
        acercaDe.setObjectName(_fromUtf8("acercaDe"))
        acercaDe.resize(560, 394)
        acercaDe.setStyleSheet(_fromUtf8("#centralwidget{background-image: url(:/img/fondo4.jpg);}\n"
""))
        self.centralwidget = QtGui.QWidget(acercaDe)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 471, 131))
        self.label.setStyleSheet(_fromUtf8("#label{    background-image: url(:/img/TituloIco.png);}"))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 160, 431, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("GrilledCheese BTN Toasted"))
        font.setPointSize(17)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 200, 401, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe Print"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(170, 250, 161, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe Print"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(170, 280, 161, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe Print"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(170, 310, 171, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe Print"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(430, 310, 101, 71))
        self.pushButton.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/ok.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(52, 52))
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        acercaDe.setCentralWidget(self.centralwidget)

        self.retranslateUi(acercaDe)
        QtCore.QMetaObject.connectSlotsByName(acercaDe)

    def retranslateUi(self, acercaDe):
        acercaDe.setWindowTitle(_translate("acercaDe", "MainWindow", None))
        self.label_2.setText(_translate("acercaDe", "Proyecto de Lenguajes de Programación", None))
        self.label_3.setText(_translate("acercaDe", "Grupo:", None))
        self.label_4.setText(_translate("acercaDe", "Kevin Silva", None))
        self.label_5.setText(_translate("acercaDe", "Danny Ponce", None))
        self.label_6.setText(_translate("acercaDe", "Edwin Hermenejildo", None))

import img_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    acercaDe = QtGui.QMainWindow()
    ui = Ui_acercaDe()
    ui.setupUi(acercaDe)
    acercaDe.show()
    sys.exit(app.exec_())

