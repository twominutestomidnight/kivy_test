# -*- coding: utf-8 -*-




from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtCore import pyqtSlot


class Ui_PreviewImage(object):
    currentPC = 1

    def __init__(self, camera_array, prevWindow):
        self.camera_array = camera_array
        self.prevWindow = prevWindow
        self.count_camera = len(camera_array)

    def setup(self, PreviewImage):
        PreviewImage.setObjectName("PreviewImage")
        PreviewImage.resize(1188, 756)
        self.CamName = QtWidgets.QLabel(PreviewImage)
        self.CamName.setGeometry(QtCore.QRect(30, 30, 1071, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.CamName.setFont(font)
        self.CamName.setObjectName("CamName")
        self.OriginImage = QtWidgets.QLabel(PreviewImage)
        self.OriginImage.setGeometry(QtCore.QRect(20, 180, 571, 411))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.OriginImage.setFont(font)
        self.OriginImage.setObjectName("OriginImage")
        self.CameraImage = QtWidgets.QLabel(PreviewImage)
        self.CameraImage.setGeometry(QtCore.QRect(620, 180, 551, 411))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.CameraImage.setFont(font)
        self.CameraImage.setObjectName("CameraImage")
        self.label = QtWidgets.QLabel(PreviewImage)
        self.label.setGeometry(QtCore.QRect(620, 610, 421, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.prev = QtWidgets.QPushButton(PreviewImage)
        self.prev.setGeometry(QtCore.QRect(830, 690, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.prev.setFont(font)
        self.prev.setObjectName("prev")
        self.next = QtWidgets.QPushButton(PreviewImage)
        self.next.setGeometry(QtCore.QRect(1030, 690, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.next.setFont(font)
        self.next.setObjectName("next")
        self.startQuiz = QtWidgets.QPushButton(PreviewImage)
        self.startQuiz.setGeometry(QtCore.QRect(20, 660, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.startQuiz.setFont(font)
        self.startQuiz.setObjectName("startQuiz")
        self.stopQuiz = QtWidgets.QPushButton(PreviewImage)
        self.stopQuiz.setGeometry(QtCore.QRect(180, 660, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.stopQuiz.setFont(font)
        self.stopQuiz.setObjectName("stopQuiz")
        self.loadImage = QtWidgets.QPushButton(PreviewImage)
        self.loadImage.setGeometry(QtCore.QRect(340, 660, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.loadImage.setFont(font)
        self.loadImage.setObjectName("loadImage")

        self.loadImage.clicked.connect(self.load_Image)
        self.startQuiz.clicked.connect(self.start_Prog)
        self.stopQuiz.clicked.connect(self.stop_Prog)


        # def a():
        #     name = QtWidgets.QFileDialog.getOpenFileName(parent=self.prevWindow)
        #     print("a")
        #     print(name)
        #
        # self.loadImage.clicked.connect(a)


        self.ip = QtWidgets.QLineEdit(PreviewImage)
        self.ip.setGeometry(QtCore.QRect(20, 600, 431, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ip.setFont(font)
        self.ip.setObjectName("ip")

        self.ip.textChanged.connect(self.changedValue)

        self.retranslateUi(PreviewImage)
        QtCore.QMetaObject.connectSlotsByName(PreviewImage)

        if self.currentPC == 1:
            self.prev.hide()

    def retranslateUi(self, PreviewImage):
        _translate = QtCore.QCoreApplication.translate
        PreviewImage.setWindowTitle(_translate("PreviewImage", "Form"))
        self.CamName.setText(_translate("PreviewImage", "Computer #1, Username"))
        self.OriginImage.setText(_translate("PreviewImage", "Origin Image #1"))
        self.CameraImage.setText(_translate("PreviewImage", "Image from camera"))
        self.label.setText(_translate("PreviewImage", "Similarity : "))
        self.prev.setText(_translate("PreviewImage", "Prev"))
        self.next.setText(_translate("PreviewImage", "Next"))
        self.startQuiz.setText(_translate("PreviewImage", "Start Quiz"))
        self.stopQuiz.setText(_translate("PreviewImage", "Stop Quiz"))
        self.loadImage.setText(_translate("PreviewImage", "LoadImage"))
        self.ip.setText(_translate("PreviewImage", "Enter username here "))

    def changedValue(self):
        # print(";lkjl",self.ip.text())
        self.CamName.setText("Computer #{}, {}".format(self.currentPC, self.ip.text()))

    def start_Prog(self):
        print(self.ip.text())
        print(self.camera_array[self.currentPC-1])
        self.startQuiz.hide()
        self.loadImage.hide()
        self.ip.setReadOnly(True)
        # TODO : here will be connection to database


    def stop_Prog(self):
        print(self.ip.text())
        print(self.camera_array[self.currentPC-1])
        self.startQuiz.show()
        self.loadImage.show()
        self.ip.setReadOnly(False)
        # TODO : stop connection to database


    # self.CamName.setText(self.ip.text())
    # @pyqtSlot()
    def load_Image(self):
        print("ghfhfd")
        name = QtWidgets.QFileDialog.getOpenFileName(parent=self.prevWindow)
        print("a")
        print(name)
        # pixmap = QtGui.QPixmap("origin.jpg")
        if name[0]:
            # TODO : before load image into label, image should be encoded
            pixmap = QtGui.QPixmap(name[0])
            self.OriginImage.setPixmap(pixmap)
            self.OriginImage.setScaledContents(True)
        # QtWidgets.QFileDialog.__init__(self, QtWidgets.QWidget,parent = None)
        # name = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File')

        # print()

        # q = QMessageBox(self, 'qqq', fname, QMessageBox.NoButton)
#
# if __name__ == '__main__':
#
#     app = QtWidgets.QApplication(sys.argv)
#
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_PreviewImage()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
