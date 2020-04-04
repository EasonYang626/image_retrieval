import PyQt5
import sys
import numpy
from PyQt5 import QtCore
from PyQt5.QtWidgets import *

import gray_search
import ui
import ui2
import query
import color_search
change = 0
class MainWindow(QMainWindow, ui.Ui_MainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        ui.Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.initUI()

    #加括号会出现child没有定义的问题
    def initUI(self):
        self.pushButton.clicked.connect(self.Upload)
        self.pushButton_2.clicked.connect(self.Search)
        self.pushButton_3.clicked.connect(self.Change)
        print(self.Search)

    def Upload(self):
        child.upload()

    def Search(self):
        child.search()

    def Change(self):
        global change
        change = change + 1
        if((change % 3) == 1):
          QMessageBox.information(self, "提示", "已经转换为颜色直方图算法")
        elif((change % 3) == 2):
          QMessageBox.information(self, "提示", "已经转换为灰度直方图算法")
        else:
          QMessageBox.information(self, "提示", "已经转换为VGG算法")

class Child(QMainWindow, ui2.Ui_ResultWindow):
    openfile_name = ''
    def __init__(self):
        QMainWindow.__init__(self)
        ui2.Ui_ResultWindow.__init__(self)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.back)

    def back(self):
        self.hide()
        md.show()

    def upload(self):
        self.openfile_name = QFileDialog.getOpenFileName(self, '选择文件', '', 'image files(*.jpg , *.png)')
        if self.openfile_name[0] is '':
           QMessageBox.information(self,"警告","请选择一副图片")
        else:
           md.label_2.setText(self.openfile_name[0]+'已上传')
           md.label_2.setStyleSheet("color:white;")

    def search(self):
        global change
        if(change % 3 == 0):
            if self.openfile_name is '':
              QMessageBox.information(self, "警告", "请选择一副图片")
            else:
              result = query.query(self, self.openfile_name[0])
              if (PyQt5.QtGui.QPixmap(self.openfile_name[0]).width()> PyQt5.QtGui.QPixmap(self.openfile_name[0]).height()):
                  self.label_3.setGeometry(QtCore.QRect(20, 240, 150, 150))
                  self.label_4.setGeometry(QtCore.QRect(320, 240, 150, 150))
                  self.label_5.setGeometry(QtCore.QRect(620, 240, 150, 150))
                  self.label_6.setGeometry(QtCore.QRect(920, 240, 150, 150))
                  self.label_7.setGeometry(QtCore.QRect(1220, 240, 150, 150))
                  self.label_8.setGeometry(QtCore.QRect(20, 390, 150, 150))
                  self.label_9.setGeometry(QtCore.QRect(320, 390, 150, 150))
                  self.label_10.setGeometry(QtCore.QRect(20, 210, 81, 31))
                  self.label_11.setGeometry(QtCore.QRect(620, 390, 150, 150))
                  self.label_12.setGeometry(QtCore.QRect(920, 390, 150, 150))
                  self.label_13.setGeometry(QtCore.QRect(1220, 390, 150, 150))
                  self.label_2.setPixmap(PyQt5.QtGui.QPixmap(self.openfile_name[0]))
                  self.label_2.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height()*2.0)
                  self.label_2.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width()*1.8)
                  self.label_2.setScaledContents(True)

                  self.label_3.setPixmap(
                      PyQt5.QtGui.QPixmap(
                          r'E:\graduation\image_retrieval\image_retrieval\database1' + '\\' + result[0].decode()))
                  self.label_3.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                  self.label_3.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                  self.label_3.setScaledContents(True)
                  self.label_4.setPixmap(
                      PyQt5.QtGui.QPixmap(
                          r'E:\graduation\image_retrieval\image_retrieval\database1' + '\\' + result[1].decode()))
                  self.label_4.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                  self.label_4.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                  self.label_4.setScaledContents(True)
                  self.label_5.setPixmap(
                      PyQt5.QtGui.QPixmap(
                          r'E:\graduation\image_retrieval\image_retrieval\database1' + '\\' + result[2].decode()))
                  self.label_5.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                  self.label_5.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                  self.label_5.setScaledContents(True)
                  self.label_6.setPixmap(
                      PyQt5.QtGui.QPixmap(
                          r'E:\graduation\image_retrieval\image_retrieval\database1' + '\\' + result[3].decode()))
                  self.label_6.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                  self.label_6.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                  self.label_6.setScaledContents(True)
                  self.label_7.setPixmap(
                      PyQt5.QtGui.QPixmap(
                          r'E:\graduation\image_retrieval\image_retrieval\database1' + '\\' + result[4].decode()))
                  self.label_7.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                  self.label_7.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                  self.label_7.setScaledContents(True)
                  self.label_8.setPixmap(
                      PyQt5.QtGui.QPixmap(
                          r'E:\graduation\image_retrieval\image_retrieval\database1' + '\\' + result[5].decode()))
                  self.label_8.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                  self.label_8.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                  self.label_8.setScaledContents(True)
                  self.label_9.setPixmap(
                      PyQt5.QtGui.QPixmap(
                          r'E:\graduation\image_retrieval\image_retrieval\database1' + '\\' + result[6].decode()))
                  self.label_9.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                  self.label_9.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                  self.label_9.setScaledContents(True)
                  self.label_11.setPixmap(
                      PyQt5.QtGui.QPixmap(
                          r'E:\graduation\image_retrieval\image_retrieval\database1' + '\\' + result[7].decode()))
                  self.label_11.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                  self.label_11.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                  self.label_11.setScaledContents(True)
                  self.label_12.setPixmap(
                      PyQt5.QtGui.QPixmap(
                          r'E:\graduation\image_retrieval\image_retrieval\database1' + '\\' + result[8].decode()))
                  self.label_12.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                  self.label_12.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                  self.label_12.setScaledContents(True)
                  self.label_13.setPixmap(
                      PyQt5.QtGui.QPixmap(
                          r'E:\graduation\image_retrieval\image_retrieval\database1' + '\\' + result[9].decode()))
                  self.label_13.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                  self.label_13.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                  self.label_13.setScaledContents(True)
                  self.show()
              else:
                  self.label_10.setGeometry(QtCore.QRect(20, 290, 81, 31))
                  self.label_2.setPixmap(PyQt5.QtGui.QPixmap(self.openfile_name[0]))

                  self.label_2.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.8)
                  self.label_2.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.8)
                  self.label_2.setScaledContents(True)

                  self.label_3.setPixmap(
                      PyQt5.QtGui.QPixmap(
                          r'E:\graduation\image_retrieval\image_retrieval\database1' + '\\' + result[0].decode()))
                  self.label_3.setGeometry(QtCore.QRect(20, 320, 150, 150))
                  self.label_3.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                  self.label_3.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                  self.label_3.setScaledContents(True)
                  self.label_4.setPixmap(
                      PyQt5.QtGui.QPixmap(
                          r'E:\graduation\image_retrieval\image_retrieval\database1' + '\\' + result[1].decode()))
                  self.label_4.setGeometry(QtCore.QRect(160, 320, 150, 150))
                  self.label_4.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                  self.label_4.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                  self.label_4.setScaledContents(True)
                  self.label_5.setPixmap(
                      PyQt5.QtGui.QPixmap(
                          r'E:\graduation\image_retrieval\image_retrieval\database1' + '\\' + result[2].decode()))
                  self.label_5.setGeometry(QtCore.QRect(300, 320, 150, 150))
                  self.label_5.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                  self.label_5.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                  self.label_5.setScaledContents(True)
                  self.label_6.setPixmap(
                      PyQt5.QtGui.QPixmap(
                          r'E:\graduation\image_retrieval\image_retrieval\database1' + '\\' + result[3].decode()))
                  self.label_6.setGeometry(QtCore.QRect(440, 320, 150, 150))
                  self.label_6.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                  self.label_6.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                  self.label_6.setScaledContents(True)
                  self.label_7.setPixmap(
                      PyQt5.QtGui.QPixmap(
                          r'E:\graduation\image_retrieval\image_retrieval\database1' + '\\' + result[4].decode()))
                  self.label_7.setGeometry(QtCore.QRect(580, 320, 150, 150))
                  self.label_7.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                  self.label_7.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                  self.label_7.setScaledContents(True)
                  self.label_8.setPixmap(
                      PyQt5.QtGui.QPixmap(
                          r'E:\graduation\image_retrieval\image_retrieval\database1' + '\\' + result[5].decode()))
                  self.label_8.setGeometry(QtCore.QRect(720, 320, 150, 150))
                  self.label_8.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                  self.label_8.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                  self.label_8.setScaledContents(True)
                  self.label_9.setPixmap(
                      PyQt5.QtGui.QPixmap(
                          r'E:\graduation\image_retrieval\image_retrieval\database1' + '\\' + result[6].decode()))
                  self.label_9.setGeometry(QtCore.QRect(860, 320, 150, 150))
                  self.label_9.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                  self.label_9.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                  self.label_9.setScaledContents(True)
                  self.label_11.setPixmap(
                      PyQt5.QtGui.QPixmap(
                          r'E:\graduation\image_retrieval\image_retrieval\database1' + '\\' + result[7].decode()))
                  self.label_11.setGeometry(QtCore.QRect(1000, 320, 150, 150))
                  self.label_11.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                  self.label_11.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                  self.label_11.setScaledContents(True)
                  self.label_12.setPixmap(
                      PyQt5.QtGui.QPixmap(
                          r'E:\graduation\image_retrieval\image_retrieval\database1' + '\\' + result[8].decode()))
                  self.label_12.setGeometry(QtCore.QRect(1140, 320, 150, 150))
                  self.label_12.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                  self.label_12.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                  self.label_12.setScaledContents(True)
                  self.label_13.setPixmap(
                      PyQt5.QtGui.QPixmap(
                          r'E:\graduation\image_retrieval\image_retrieval\database1' + '\\' + result[9].decode()))
                  self.label_13.setGeometry(QtCore.QRect(1280, 320, 150, 150))
                  self.label_13.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                  self.label_13.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                  self.label_13.setScaledContents(True)
                  self.show()

        elif(change % 3 == 1):
            if self.openfile_name is '':
              QMessageBox.information(self, "警告", "请选择一副图片")
            else:
              result = color_search.search(self, self.openfile_name[0])
              if (PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() > PyQt5.QtGui.QPixmap(
                      self.openfile_name[0]).height()):
                  self.label_3.setGeometry(QtCore.QRect(20, 240, 150, 150))
                  self.label_4.setGeometry(QtCore.QRect(320, 240, 150, 150))
                  self.label_5.setGeometry(QtCore.QRect(620, 240, 150, 150))
                  self.label_6.setGeometry(QtCore.QRect(920, 240, 150, 150))
                  self.label_7.setGeometry(QtCore.QRect(1220, 240, 150, 150))
                  self.label_8.setGeometry(QtCore.QRect(20, 390, 150, 150))
                  self.label_9.setGeometry(QtCore.QRect(320, 390, 150, 150))
                  self.label_10.setGeometry(QtCore.QRect(20, 210, 81, 31))
                  self.label_11.setGeometry(QtCore.QRect(620, 390, 150, 150))
                  self.label_12.setGeometry(QtCore.QRect(920, 390, 150, 150))
                  self.label_13.setGeometry(QtCore.QRect(1220, 390, 150, 150))
                  self.label_2.setPixmap(PyQt5.QtGui.QPixmap(self.openfile_name[0]))
                  self.label_2.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 2.0)
                  self.label_2.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.8)
                  self.label_2.setScaledContents(True)

                  self.label_3.setPixmap(
                      PyQt5.QtGui.QPixmap(
                          r'E:\graduation\image_retrieval\image_retrieval' + '\\' + result[0][1]))
                  self.label_3.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                  self.label_3.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                  self.label_3.setScaledContents(True)
                  self.label_4.setPixmap(
                      PyQt5.QtGui.QPixmap(
                          r'E:\graduation\image_retrieval\image_retrieval' + '\\' + result[1][1]))
                  self.label_4.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                  self.label_4.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                  self.label_4.setScaledContents(True)
                  self.label_5.setPixmap(
                      PyQt5.QtGui.QPixmap(
                          r'E:\graduation\image_retrieval\image_retrieval' + '\\' + result[2][1]))
                  self.label_5.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                  self.label_5.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                  self.label_5.setScaledContents(True)
                  self.label_6.setPixmap(
                      PyQt5.QtGui.QPixmap(
                          r'E:\graduation\image_retrieval\image_retrieval' + '\\' + result[3][1]))
                  self.label_6.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                  self.label_6.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                  self.label_6.setScaledContents(True)
                  self.label_7.setPixmap(
                      PyQt5.QtGui.QPixmap(
                          r'E:\graduation\image_retrieval\image_retrieval' + '\\' + result[4][1]))
                  self.label_7.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                  self.label_7.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                  self.label_7.setScaledContents(True)
                  self.label_8.setPixmap(
                      PyQt5.QtGui.QPixmap(
                          r'E:\graduation\image_retrieval\image_retrieval' + '\\' + result[5][1]))
                  self.label_8.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                  self.label_8.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                  self.label_8.setScaledContents(True)
                  self.label_9.setPixmap(
                      PyQt5.QtGui.QPixmap(
                          r'E:\graduation\image_retrieval\image_retrieval' + '\\' + result[6][1]))
                  self.label_9.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                  self.label_9.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                  self.label_9.setScaledContents(True)
                  self.label_11.setPixmap(
                      PyQt5.QtGui.QPixmap(
                          r'E:\graduation\image_retrieval\image_retrieval' + '\\' + result[7][1]))
                  self.label_11.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                  self.label_11.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                  self.label_11.setScaledContents(True)
                  self.label_12.setPixmap(
                      PyQt5.QtGui.QPixmap(
                          r'E:\graduation\image_retrieval\image_retrieval' + '\\' + result[8][1]))
                  self.label_12.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                  self.label_12.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                  self.label_12.setScaledContents(True)
                  self.label_13.setPixmap(
                      PyQt5.QtGui.QPixmap(
                          r'E:\graduation\image_retrieval\image_retrieval' + '\\' + result[9][1]))
                  self.label_13.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                  self.label_13.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                  self.label_13.setScaledContents(True)
                  self.show()
              else:
                  self.label_10.setGeometry(QtCore.QRect(20, 290, 81, 31))
                  self.label_2.setPixmap(PyQt5.QtGui.QPixmap(self.openfile_name[0]))

                  self.label_2.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.8)
                  self.label_2.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.8)
                  self.label_2.setScaledContents(True)

                  self.label_3.setPixmap(
                      PyQt5.QtGui.QPixmap(
                          r'E:\graduation\image_retrieval\image_retrieval' + '\\' + result[0][1]))
                  self.label_3.setGeometry(QtCore.QRect(20, 320, 150, 150))
                  self.label_3.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                  self.label_3.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                  self.label_3.setScaledContents(True)
                  self.label_4.setPixmap(
                      PyQt5.QtGui.QPixmap(
                          r'E:\graduation\image_retrieval\image_retrieval' + '\\' + result[1][1]))
                  self.label_4.setGeometry(QtCore.QRect(160, 320, 150, 150))
                  self.label_4.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                  self.label_4.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                  self.label_4.setScaledContents(True)
                  self.label_5.setPixmap(
                      PyQt5.QtGui.QPixmap(
                          r'E:\graduation\image_retrieval\image_retrieval' + '\\' + result[2][1]))
                  self.label_5.setGeometry(QtCore.QRect(300, 320, 150, 150))
                  self.label_5.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                  self.label_5.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                  self.label_5.setScaledContents(True)
                  self.label_6.setPixmap(
                      PyQt5.QtGui.QPixmap(
                          r'E:\graduation\image_retrieval\image_retrieval' + '\\' + result[3][1]))
                  self.label_6.setGeometry(QtCore.QRect(440, 320, 150, 150))
                  self.label_6.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                  self.label_6.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                  self.label_6.setScaledContents(True)
                  self.label_7.setPixmap(
                      PyQt5.QtGui.QPixmap(
                          r'E:\graduation\image_retrieval\image_retrieval' + '\\' + result[4][1]))
                  self.label_7.setGeometry(QtCore.QRect(580, 320, 150, 150))
                  self.label_7.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                  self.label_7.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                  self.label_7.setScaledContents(True)
                  self.label_8.setPixmap(
                      PyQt5.QtGui.QPixmap(
                          r'E:\graduation\image_retrieval\image_retrieval' + '\\' + result[5][1]))
                  self.label_8.setGeometry(QtCore.QRect(720, 320, 150, 150))
                  self.label_8.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                  self.label_8.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                  self.label_8.setScaledContents(True)
                  self.label_9.setPixmap(
                      PyQt5.QtGui.QPixmap(
                          r'E:\graduation\image_retrieval\image_retrieval' + '\\' + result[6][1]))
                  self.label_9.setGeometry(QtCore.QRect(860, 320, 150, 150))
                  self.label_9.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                  self.label_9.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                  self.label_9.setScaledContents(True)
                  self.label_11.setPixmap(
                      PyQt5.QtGui.QPixmap(
                          r'E:\graduation\image_retrieval\image_retrieval' + '\\' + result[7][1]))
                  self.label_11.setGeometry(QtCore.QRect(1000, 320, 150, 150))
                  self.label_11.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                  self.label_11.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                  self.label_11.setScaledContents(True)
                  self.label_12.setPixmap(
                      PyQt5.QtGui.QPixmap(
                          r'E:\graduation\image_retrieval\image_retrieval' + '\\' + result[8][1]))
                  self.label_12.setGeometry(QtCore.QRect(1140, 320, 150, 150))
                  self.label_12.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                  self.label_12.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                  self.label_12.setScaledContents(True)
                  self.label_13.setPixmap(
                      PyQt5.QtGui.QPixmap(
                          r'E:\graduation\image_retrieval\image_retrieval' + '\\' + result[9][1]))
                  self.label_13.setGeometry(QtCore.QRect(1280, 320, 150, 150))
                  self.label_13.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                  self.label_13.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                  self.label_13.setScaledContents(True)
                  self.show()
        elif (change % 3 == 2):
            if self.openfile_name is '':
                QMessageBox.information(self, "警告", "请选择一副图片")
            else:
                result = gray_search.search(self, self.openfile_name[0])
                if (PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() > PyQt5.QtGui.QPixmap(
                        self.openfile_name[0]).height()):
                    self.label_3.setGeometry(QtCore.QRect(20, 240, 150, 150))
                    self.label_4.setGeometry(QtCore.QRect(320, 240, 150, 150))
                    self.label_5.setGeometry(QtCore.QRect(620, 240, 150, 150))
                    self.label_6.setGeometry(QtCore.QRect(920, 240, 150, 150))
                    self.label_7.setGeometry(QtCore.QRect(1220, 240, 150, 150))
                    self.label_8.setGeometry(QtCore.QRect(20, 390, 150, 150))
                    self.label_9.setGeometry(QtCore.QRect(320, 390, 150, 150))
                    self.label_10.setGeometry(QtCore.QRect(20, 210, 81, 31))
                    self.label_11.setGeometry(QtCore.QRect(620, 390, 150, 150))
                    self.label_12.setGeometry(QtCore.QRect(920, 390, 150, 150))
                    self.label_13.setGeometry(QtCore.QRect(1220, 390, 150, 150))
                    self.label_2.setPixmap(PyQt5.QtGui.QPixmap(self.openfile_name[0]))
                    self.label_2.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 2.0)
                    self.label_2.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.8)
                    self.label_2.setScaledContents(True)

                    self.label_3.setPixmap(
                        PyQt5.QtGui.QPixmap(
                            r'E:\graduation\image_retrieval\image_retrieval' + '\\' + result[0][1]))
                    self.label_3.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                    self.label_3.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                    self.label_3.setScaledContents(True)
                    self.label_4.setPixmap(
                        PyQt5.QtGui.QPixmap(
                            r'E:\graduation\image_retrieval\image_retrieval' + '\\' + result[1][1]))
                    self.label_4.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                    self.label_4.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                    self.label_4.setScaledContents(True)
                    self.label_5.setPixmap(
                        PyQt5.QtGui.QPixmap(
                            r'E:\graduation\image_retrieval\image_retrieval' + '\\' + result[2][1]))
                    self.label_5.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                    self.label_5.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                    self.label_5.setScaledContents(True)
                    self.label_6.setPixmap(
                        PyQt5.QtGui.QPixmap(
                            r'E:\graduation\image_retrieval\image_retrieval' + '\\' + result[3][1]))
                    self.label_6.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                    self.label_6.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                    self.label_6.setScaledContents(True)
                    self.label_7.setPixmap(
                        PyQt5.QtGui.QPixmap(
                            r'E:\graduation\image_retrieval\image_retrieval' + '\\' + result[4][1]))
                    self.label_7.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                    self.label_7.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                    self.label_7.setScaledContents(True)
                    self.label_8.setPixmap(
                        PyQt5.QtGui.QPixmap(
                            r'E:\graduation\image_retrieval\image_retrieval' + '\\' + result[5][1]))
                    self.label_8.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                    self.label_8.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                    self.label_8.setScaledContents(True)
                    self.label_9.setPixmap(
                        PyQt5.QtGui.QPixmap(
                            r'E:\graduation\image_retrieval\image_retrieval' + '\\' + result[6][1]))
                    self.label_9.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                    self.label_9.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                    self.label_9.setScaledContents(True)
                    self.label_11.setPixmap(
                        PyQt5.QtGui.QPixmap(
                            r'E:\graduation\image_retrieval\image_retrieval' + '\\' + result[7][1]))
                    self.label_11.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                    self.label_11.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                    self.label_11.setScaledContents(True)
                    self.label_12.setPixmap(
                        PyQt5.QtGui.QPixmap(
                            r'E:\graduation\image_retrieval\image_retrieval' + '\\' + result[8][1]))
                    self.label_12.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                    self.label_12.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                    self.label_12.setScaledContents(True)
                    self.label_13.setPixmap(
                        PyQt5.QtGui.QPixmap(
                            r'E:\graduation\image_retrieval\image_retrieval' + '\\' + result[9][1]))
                    self.label_13.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                    self.label_13.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                    self.label_13.setScaledContents(True)
                    self.show()
                else:
                    self.label_10.setGeometry(QtCore.QRect(20, 290, 81, 31))
                    self.label_2.setPixmap(PyQt5.QtGui.QPixmap(self.openfile_name[0]))

                    self.label_2.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.8)
                    self.label_2.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.8)
                    self.label_2.setScaledContents(True)

                    self.label_3.setPixmap(
                        PyQt5.QtGui.QPixmap(
                            r'E:\graduation\image_retrieval\image_retrieval' + '\\' + result[0][1]))
                    self.label_3.setGeometry(QtCore.QRect(20, 320, 150, 150))
                    self.label_3.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                    self.label_3.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                    self.label_3.setScaledContents(True)
                    self.label_4.setPixmap(
                        PyQt5.QtGui.QPixmap(
                            r'E:\graduation\image_retrieval\image_retrieval' + '\\' + result[1][1]))
                    self.label_4.setGeometry(QtCore.QRect(160, 320, 150, 150))
                    self.label_4.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                    self.label_4.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                    self.label_4.setScaledContents(True)
                    self.label_5.setPixmap(
                        PyQt5.QtGui.QPixmap(
                            r'E:\graduation\image_retrieval\image_retrieval' + '\\' + result[2][1]))
                    self.label_5.setGeometry(QtCore.QRect(300, 320, 150, 150))
                    self.label_5.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                    self.label_5.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                    self.label_5.setScaledContents(True)
                    self.label_6.setPixmap(
                        PyQt5.QtGui.QPixmap(
                            r'E:\graduation\image_retrieval\image_retrieval' + '\\' + result[3][1]))
                    self.label_6.setGeometry(QtCore.QRect(440, 320, 150, 150))
                    self.label_6.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                    self.label_6.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                    self.label_6.setScaledContents(True)
                    self.label_7.setPixmap(
                        PyQt5.QtGui.QPixmap(
                            r'E:\graduation\image_retrieval\image_retrieval' + '\\' + result[4][1]))
                    self.label_7.setGeometry(QtCore.QRect(580, 320, 150, 150))
                    self.label_7.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                    self.label_7.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                    self.label_7.setScaledContents(True)
                    self.label_8.setPixmap(
                        PyQt5.QtGui.QPixmap(
                            r'E:\graduation\image_retrieval\image_retrieval' + '\\' + result[5][1]))
                    self.label_8.setGeometry(QtCore.QRect(720, 320, 150, 150))
                    self.label_8.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                    self.label_8.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                    self.label_8.setScaledContents(True)
                    self.label_9.setPixmap(
                        PyQt5.QtGui.QPixmap(
                            r'E:\graduation\image_retrieval\image_retrieval' + '\\' + result[6][1]))
                    self.label_9.setGeometry(QtCore.QRect(860, 320, 150, 150))
                    self.label_9.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                    self.label_9.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                    self.label_9.setScaledContents(True)
                    self.label_11.setPixmap(
                        PyQt5.QtGui.QPixmap(
                            r'E:\graduation\image_retrieval\image_retrieval' + '\\' + result[7][1]))
                    self.label_11.setGeometry(QtCore.QRect(1000, 320, 150, 150))
                    self.label_11.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                    self.label_11.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                    self.label_11.setScaledContents(True)
                    self.label_12.setPixmap(
                        PyQt5.QtGui.QPixmap(
                            r'E:\graduation\image_retrieval\image_retrieval' + '\\' + result[8][1]))
                    self.label_12.setGeometry(QtCore.QRect(1140, 320, 150, 150))
                    self.label_12.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                    self.label_12.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                    self.label_12.setScaledContents(True)
                    self.label_13.setPixmap(
                        PyQt5.QtGui.QPixmap(
                            r'E:\graduation\image_retrieval\image_retrieval' + '\\' + result[9][1]))
                    self.label_13.setGeometry(QtCore.QRect(1280, 320, 150, 150))
                    self.label_13.setFixedHeight(PyQt5.QtGui.QPixmap(self.openfile_name[0]).height() * 1.5)
                    self.label_13.setFixedWidth(PyQt5.QtGui.QPixmap(self.openfile_name[0]).width() * 1.5)
                    self.label_13.setScaledContents(True)
                    self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    md = MainWindow()
    child = Child()
    md.show()
    sys.exit(app.exec_())