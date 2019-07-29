# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'quiz.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtCore import pyqtSlot
from Image import getImageFromCamera
import datetime
from facematch import faceCompare
import time

class Ui_Form(QtWidgets.QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1267, 794)
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(30, 30, 331, 41))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 329, 39))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)


        self.label = QtWidgets.QLabel(Form)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(9, 120, 621, 451))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setObjectName("label")
        pixmap = QtGui.QPixmap("origin.jpg")
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)


        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(649, 120, 611, 451))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        pixmap = QtGui.QPixmap("sample.jpg")
        self.label_2.setPixmap(pixmap)
        self.label_2.setScaledContents(True)

        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(50, 590, 321, 71))
        self.textBrowser.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_3 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_3.setGeometry(QtCore.QRect(480, 590, 261, 51))
        self.textBrowser_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textBrowser_3.setObjectName("textBrowser_3")


        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(670, 670, 161, 81))
        self.pushButton.setObjectName("pushButton")


        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(980, 670, 161, 81))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton.clicked.connect(self.on_click1)
        self.pushButton_2.clicked.connect(self.on_click2)




        self.textBrowser_4 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_4.setGeometry(QtCore.QRect(840, 590, 261, 51))
        self.textBrowser_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_5 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_5.setGeometry(QtCore.QRect(50, 700, 321, 61))
        self.textBrowser_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textBrowser_5.setObjectName("textBrowser_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">current system time</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt;\"><br /></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Similarity :</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "PushButton"))
        self.pushButton_2.setText(_translate("Form", "PushButton2"))
        self.textBrowser_4.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Similarity :</span></p></body></html>"))
        self.textBrowser_5.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">time made image</span></p></body></html>"))


    @pyqtSlot()
    def on_click1(self):
        # while True:
        print('PyQt5 button1 click')
            # print(self.textBrowser.setText('AI1524PO'))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.textBrowser.setFont(font)

        self.textBrowser.setText(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        getImageFromCamera()
        pixmap = QtGui.QPixmap("sample2.jpg")
        self.label_2.setPixmap(pixmap)
        self.label_2.setScaledContents(True)
        result, accuracy = faceCompare(imageToCompare='sample2.jpg',
                    imageOrigin='origin.jpg')
        font = QtGui.QFont()
        font.setPointSize(18)
        self.textBrowser_3.setFont(font)

        font = QtGui.QFont()
        font.setPointSize(16)
        self.textBrowser_4.setFont(font)

        if result:
            print('This is origin')
            self.textBrowser_3.setText('This is origin')
        else:
            self.textBrowser_3.setText('This is not origin')

        # self.textBrowser_4.setText('Similarity : '+str(accuracy[0]))
        self.textBrowser_4.setText(str(accuracy[0]))
            # time.sleep(5)




    @pyqtSlot()
    def on_click2(self):
        print('PyQt5 button2 click')

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
