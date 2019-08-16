# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layer1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtCore import pyqtSlot
from layerWithForm import Ui_Second_Form


class Ui_Form(QtWidgets.QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(506, 260)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(320, 190, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 70, 321, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.spinBox = QtWidgets.QSpinBox(Form)
        self.spinBox.setGeometry(QtCore.QRect(360, 90, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.spinBox.setFont(font)
        self.spinBox.setObjectName("spinBox")

        # self.pushButton.clicked.connect(self.on_click1)
        self.pushButton.clicked.connect(self.openWindow)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Next step"))
        self.label.setText(_translate("Form", "Enter number of workplaces  in class "))


    def openWindow(self):
        # self.window = QtWidgets.QMainWindow()
        # number_of_cameras = self.spinBox.value()
        # print("number_of_cameras : ", number_of_cameras)
        # self.ui = Ui_Second_Form(number_of_cameras)
        # self.ui.setupUi(self.window)
        # MainWindow.hide()
        # self.window.show()
        self.SecondWindow = QtWidgets.QMainWindow()
        number_of_cameras = self.spinBox.value()
        print("number_of_cameras : ", number_of_cameras)
        if number_of_cameras > 0 :
            self.ui = Ui_Second_Form(number_of_cameras,self.SecondWindow)
            self.ui.setupUi(self.SecondWindow)
            MainWindow.hide()
            self.SecondWindow.show()




if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
