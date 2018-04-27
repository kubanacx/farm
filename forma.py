# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import paho.mqtt.client as mqtt
import json
import time
from datetime import datetime
import threading

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

class Ui_MainWindow(object):

    def __init__(self):
        self.flag = 1
        self.mqttc = mqtt.Client()
        self.mqttc.on_message = self.on_message
        self.mqttc.connect("localhost", 1883, 60)
        self.mqttc.subscribe("test", 0)


    def collector(self):
        while(self.flag == 1):
            self.mqttc.loop(0.1)

    def killer(self):
        self.flag = 0
        return 0

    def on_message(self, mqttc, obj, msg):
        payload = json.loads(msg.payload.decode('utf-8'))
        print(payload, datetime.now().time().replace(microsecond = 0))
        self.lineEdit.setText(str(payload['tem']) + u"\u2103")
        self.lineEdit_2.setText(str(payload['hum'])+'%')
        self.lineEdit_3.setText(str(payload['ovf']))
        self.lineEdit_4.setText(str(payload['prx']))
        self.lineEdit_5.setText(str(payload['dyl']))
        self.lineEdit_6.setText(str(payload['ph']))


    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 168)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 127);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setText('/')
        self.lineEdit.setGeometry(QtCore.QRect(40, 70, 113, 29))
        self.lineEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border: solid 1px ;\n"
"border-color: rgb(0, 0, 0);"))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setText('/')
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 70, 113, 29))
        self.lineEdit_2.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border: solid 1px ;\n"
"border-color: rgb(0, 0, 0);"))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setText('/')
        self.lineEdit_3.setGeometry(QtCore.QRect(520, 70, 113, 29))
        self.lineEdit_3.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border: solid 1px ;\n"
"border-color: rgb(0, 0, 0);"))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_4.setText('/')
        self.lineEdit_4.setGeometry(QtCore.QRect(640, 70, 113, 29))
        self.lineEdit_4.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border: solid 1px ;\n"
"border-color: rgb(0, 0, 0);"))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_5 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_5.setEnabled(False)
        self.lineEdit_5.setText('/')
        self.lineEdit_5.setGeometry(QtCore.QRect(400, 70, 113, 29))
        self.lineEdit_5.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border: solid 1px ;\n"
"border-color: rgb(0, 0, 0);"))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.lineEdit_6 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_6.setEnabled(False)
        self.lineEdit_6.setText('/')
        self.lineEdit_6.setGeometry(QtCore.QRect(280, 70, 113, 29))
        self.lineEdit_6.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border: solid 1px ;\n"
"border-color: rgb(0, 0, 0);"))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 40, 91, 17))
        self.label.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 40, 68, 17))
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(660, 40, 68, 17))
        self.label_3.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(540, 40, 81, 17))
        self.label_4.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(290, 40, 81, 17))
        self.label_5.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(410, 40, 101, 17))
        self.label_6.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Temperatura", None))
        self.label_2.setText(_translate("MainWindow", "Vlaznost", None))
        self.label_3.setText(_translate("MainWindow", "Blizina", None))
        self.label_4.setText(_translate("MainWindow", "Pretek vode", None))
        self.label_5.setText(_translate("MainWindow", "pH vrednost", None))
        self.label_6.setText(_translate("MainWindow", "Dnevno svetlo", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    t = threading.Thread(target = ui.collector)
    t.start()
    sys.exit([app.exec_(), ui.killer()])

    sys.exit(0)
