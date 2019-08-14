# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layerWithForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtCore import pyqtSlot
from Camera import Camera

array_of_cameras = []

class Ui_Second_Form(object):
    count = 1
    def __init__(self, num_of_cams):
        self.number = num_of_cams


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(614, 429)
        self.computerNumber = QtWidgets.QLabel(Form)
        self.computerNumber.setGeometry(QtCore.QRect(40, 50, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.computerNumber.setFont(font)
        self.computerNumber.setObjectName("computerNumber")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 130, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 190, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(40, 250, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(40, 310, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.nextBtn = QtWidgets.QPushButton(Form)
        self.nextBtn.setGeometry(QtCore.QRect(440, 370, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.nextBtn.setFont(font)
        self.nextBtn.setObjectName("nextBtn")

        self.nextBtn.clicked.connect(self.next_click)

        self.ip = QtWidgets.QLineEdit(Form)
        self.ip.setGeometry(QtCore.QRect(220, 130, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ip.setFont(font)
        self.ip.setObjectName("ip")
        self.port = QtWidgets.QLineEdit(Form)
        self.port.setGeometry(QtCore.QRect(220, 190, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.port.setFont(font)
        self.port.setObjectName("port")
        self.login = QtWidgets.QLineEdit(Form)
        self.login.setGeometry(QtCore.QRect(220, 250, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.login.setFont(font)
        self.login.setObjectName("login")
        self.password = QtWidgets.QLineEdit(Form)
        self.password.setGeometry(QtCore.QRect(220, 310, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.password.setFont(font)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setReadOnly(False)
        self.password.setObjectName("password")
        self.prevBtn = QtWidgets.QPushButton(Form)
        self.prevBtn.setGeometry(QtCore.QRect(10, 370, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.prevBtn.setFont(font)
        self.prevBtn.setObjectName("prevBtn")
        self.statusBtn = QtWidgets.QPushButton(Form)
        self.statusBtn.setGeometry(QtCore.QRect(300, 10, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.statusBtn.setFont(font)
        self.statusBtn.setObjectName("statusBtn")
        self.status = QtWidgets.QLabel(Form)
        self.status.setGeometry(QtCore.QRect(450, 10, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.status.setFont(font)
        self.status.setObjectName("status")


        self.statusBtn.clicked.connect(self.status_click)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    # @pyqtSlot()
    def status_click(self):
        print('PyQt5 button1 click')
        # print(self.ip.text())
        print(Camera(self.ip.text(), self.port.text(), self.login.text(), self.password.text()))
        # TODO: here will be check status of connection, send request to camera, if status = 200, write OK,otherwise write enter correct information or check connection
        status = 2001
        if status == 200:
            self.status.setText("Status : OK")
        else:
            self.status.setText("Status : False")

    def next_click(self):
        print('PyQt5 next_click click')
        array_of_cameras.append(Camera(self.ip.text(), self.port.text(), self.login.text(), self.password.text()))
        self.ip.setText("0.0.0.0")
        self.port.setText("80")
        self.login.setText("login")
        self.password.setText("password")
        self.count += 1
        if self.count<= self.number:
            self.computerNumber.setText("Computer #{}".format(self.count))
        else:
            self.nextBtn.setText("Done.")




    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.computerNumber.setText(_translate("Form", "Computer #{}".format(self.count)))
        self.label_2.setText(_translate("Form", "IP"))
        self.label_3.setText(_translate("Form", "Port"))
        self.label_4.setText(_translate("Form", "Login"))
        self.label_5.setText(_translate("Form", "Password"))
        self.nextBtn.setText(_translate("Form", "Next Workspace"))
        self.ip.setText(_translate("Form", "192.168.30.144"))
        self.port.setText(_translate("Form", "80"))
        self.login.setText(_translate("Form", "192.168.30.144"))
        self.password.setText(_translate("Form", "192.168.30.144"))
        self.prevBtn.setText(_translate("Form", "Previous Workspace"))
        self.statusBtn.setText(_translate("Form", "Check status "))
        self.status.setText(_translate("Form", "Status : "))


#
# if __name__ == '__main__':
#
#     app = QtWidgets.QApplication(sys.argv)
#
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_Second_Form()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
