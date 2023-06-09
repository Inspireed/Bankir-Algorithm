from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSvg import QSvgWidget, QSvgRenderer

from bankir import bankir
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtSvg
import json
import GraphDrawer
import time
from PyQt5.QtCore import QTimer, QEventLoop
from PyQt5.QtGui import QPixmap

processes = 4
resources = 4
max_resources = [1, 1, 1, 1]
label = 'Безопасная последовательность:'
sequence = ""
with open("config.json") as f:
    config = json.load(f)

lst_of_sec = []


class Ui_mainWindow(object):
    def __init__(self):
        self._current_step = 0
        self._step_count = 0
        self._lst = []
        self.lst_of_sec = []
        self.rest = 0
        self.err = 0

    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(900, 800)
        mainWindow.setGeometry(400, 120, 1020, 800)
        mainWindow.setLayoutDirection(QtCore.Qt.RightToLeft)
        mainWindow.setStyleSheet("background-color: rgb(51, 153, 153);")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #self.img = QtWidgets.QLabel(self.centralwidget)
        #self.img.setGeometry(1010, 540, 410, 380)

        #self.pixmap = QPixmap("logoX2.png")
        #self.pixmap1 = self.pixmap.scaledToWidth(70)
        #self.pixmap2 = self.pixmap.scaledToHeight(70)
        #self.img.setPixmap(self.pixmap2)

        self.svg_widget = QSvgWidget(self.centralwidget)

        self.svg_widget.setGeometry(470, 350, 500, 450)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.svg_widget)



        # self.svgWidget = QtSvg.QSvgWidget()
        # self.svgWidget.setGeometry(1010, 540, 410, 380)
        # self.svgWidget.setWindowTitle("Граф")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(740, 20, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(600, 340, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setGeometry(QtCore.QRect(20, 440, 470, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setGeometry(QtCore.QRect(20, 480, 450, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")

        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(320, 360, 100, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.nextButton.setFont(font)
        self.nextButton.setStyleSheet("background-color: rgb(0, 102, 255);"
                                       "border-style: outset;"
                                       "border-width: 2px;"
                                       "border-radius: 10px;"
                                       "border-color: rgb(0, 0, 0);")
        self.nextButton.setObjectName("nextButton")
        self.nextButton.setVisible(False)
        self.nextButton.clicked.connect(self.next_click)

        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(220, 360, 100, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.backButton.setFont(font)
        self.backButton.setStyleSheet("background-color: rgb(0, 102, 255);"
                                      "border-style: outset;"
                                      "border-width: 2px;"
                                      "border-radius: 10px;"
                                      "border-color: rgb(0, 0, 0);")
        self.backButton.setObjectName("backButton")
        self.backButton.setVisible(False)
        self.backButton.clicked.connect(self.prev_click)

        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(60, 360, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.startButton.clicked.connect(self.start)
        self.startButton.setFont(font)
        self.startButton.setStyleSheet("background-color: rgb(152, 251, 152);"
                                       "border-style: outset;"
                                       "border-width: 2px;"
                                       "border-radius: 10px;"
                                       "border-color: rgb(0, 0, 0);")
        #self.startButton.setStyleSheet("border-width: 2px; border-radius: 10px")
        self.startButton.setObjectName("startButton")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(400, 20, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_34 = QtWidgets.QLabel(self.centralwidget)
        self.label_34.setGeometry(QtCore.QRect(200, 70, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(20, 280, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_35 = QtWidgets.QLabel(self.centralwidget)
        self.label_35.setGeometry(QtCore.QRect(260, 70, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(20, 180, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(20, 230, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_36 = QtWidgets.QLabel(self.centralwidget)
        self.label_36.setGeometry(QtCore.QRect(80, 70, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.centralwidget)
        self.label_37.setGeometry(QtCore.QRect(140, 70, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(60, 110, 238, 211))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layoutWidget_2.sizePolicy().hasHeightForWidth())
        self.layoutWidget_2.setSizePolicy(sizePolicy)
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.allButton_03 = QtWidgets.QPushButton(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.allButton_03.sizePolicy().hasHeightForWidth())
        self.allButton_03.setSizePolicy(sizePolicy)
        self.allButton_03.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.allButton_03.setObjectName("allButton_03")
        self.gridLayout_3.addWidget(self.allButton_03, 0, 0, 1, 1)
        self.allButton_02 = QtWidgets.QPushButton(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.allButton_02.sizePolicy().hasHeightForWidth())
        self.allButton_02.setSizePolicy(sizePolicy)
        self.allButton_02.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.allButton_02.setObjectName("allButton_02")
        self.gridLayout_3.addWidget(self.allButton_02, 0, 1, 1, 1)
        self.allButton_01 = QtWidgets.QPushButton(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.allButton_01.sizePolicy().hasHeightForWidth())
        self.allButton_01.setSizePolicy(sizePolicy)
        self.allButton_01.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.allButton_01.setObjectName("allButton_01")
        self.gridLayout_3.addWidget(self.allButton_01, 0, 2, 1, 1)
        self.allButton_00 = QtWidgets.QPushButton(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.allButton_00.sizePolicy().hasHeightForWidth())
        self.allButton_00.setSizePolicy(sizePolicy)
        self.allButton_00.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.allButton_00.setObjectName("allButton_00")
        self.gridLayout_3.addWidget(self.allButton_00, 0, 3, 1, 1)
        self.allButton_13 = QtWidgets.QPushButton(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.allButton_13.sizePolicy().hasHeightForWidth())
        self.allButton_13.setSizePolicy(sizePolicy)
        self.allButton_13.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.allButton_13.setObjectName("allButton_13")
        self.gridLayout_3.addWidget(self.allButton_13, 1, 0, 1, 1)
        self.allButton_12 = QtWidgets.QPushButton(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.allButton_12.sizePolicy().hasHeightForWidth())
        self.allButton_12.setSizePolicy(sizePolicy)
        self.allButton_12.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.allButton_12.setObjectName("allButton_12")
        self.gridLayout_3.addWidget(self.allButton_12, 1, 1, 1, 1)
        self.allButton_11 = QtWidgets.QPushButton(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.allButton_11.sizePolicy().hasHeightForWidth())
        self.allButton_11.setSizePolicy(sizePolicy)
        self.allButton_11.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.allButton_11.setObjectName("allButton_11")
        self.gridLayout_3.addWidget(self.allButton_11, 1, 2, 1, 1)
        self.allButton_10 = QtWidgets.QPushButton(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.allButton_10.sizePolicy().hasHeightForWidth())
        self.allButton_10.setSizePolicy(sizePolicy)
        self.allButton_10.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.allButton_10.setObjectName("allButton_10")
        self.gridLayout_3.addWidget(self.allButton_10, 1, 3, 1, 1)
        self.allButton_23 = QtWidgets.QPushButton(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.allButton_23.sizePolicy().hasHeightForWidth())
        self.allButton_23.setSizePolicy(sizePolicy)
        self.allButton_23.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.allButton_23.setObjectName("Button_23")
        self.gridLayout_3.addWidget(self.allButton_23, 2, 0, 1, 1)
        self.allButton_22 = QtWidgets.QPushButton(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.allButton_22.sizePolicy().hasHeightForWidth())
        self.allButton_22.setSizePolicy(sizePolicy)
        self.allButton_22.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.allButton_22.setObjectName("allButton_22")
        self.gridLayout_3.addWidget(self.allButton_22, 2, 1, 1, 1)
        self.allButton_21 = QtWidgets.QPushButton(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.allButton_21.sizePolicy().hasHeightForWidth())
        self.allButton_21.setSizePolicy(sizePolicy)
        self.allButton_21.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.allButton_21.setObjectName("allButton_21")
        self.gridLayout_3.addWidget(self.allButton_21, 2, 2, 1, 1)
        self.allButton_20 = QtWidgets.QPushButton(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.allButton_20.sizePolicy().hasHeightForWidth())
        self.allButton_20.setSizePolicy(sizePolicy)
        self.allButton_20.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.allButton_20.setObjectName("allButton_20")
        self.gridLayout_3.addWidget(self.allButton_20, 2, 3, 1, 1)
        self.allButton_33 = QtWidgets.QPushButton(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.allButton_33.sizePolicy().hasHeightForWidth())
        self.allButton_33.setSizePolicy(sizePolicy)
        self.allButton_33.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.allButton_33.setObjectName("allButton_33")
        self.gridLayout_3.addWidget(self.allButton_33, 3, 0, 1, 1)
        self.allButton_32 = QtWidgets.QPushButton(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.allButton_32.sizePolicy().hasHeightForWidth())
        self.allButton_32.setSizePolicy(sizePolicy)
        self.allButton_32.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.allButton_32.setObjectName("Button_32")
        self.gridLayout_3.addWidget(self.allButton_32, 3, 1, 1, 1)
        self.allButton_31 = QtWidgets.QPushButton(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.allButton_31.sizePolicy().hasHeightForWidth())
        self.allButton_31.setSizePolicy(sizePolicy)
        self.allButton_31.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.allButton_31.setObjectName("Button_31")
        self.gridLayout_3.addWidget(self.allButton_31, 3, 2, 1, 1)
        self.allButton_30 = QtWidgets.QPushButton(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.allButton_30.sizePolicy().hasHeightForWidth())
        self.allButton_30.setSizePolicy(sizePolicy)
        self.allButton_30.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.allButton_30.setObjectName("allButton_30")
        self.gridLayout_3.addWidget(self.allButton_30, 3, 3, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(20, 130, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(80, 20, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_38 = QtWidgets.QLabel(self.centralwidget)
        self.label_38.setGeometry(QtCore.QRect(600, 70, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_38.setFont(font)
        self.label_38.setObjectName("label_38")
        self.layoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_3.setGeometry(QtCore.QRect(400, 110, 238, 211))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layoutWidget_3.sizePolicy().hasHeightForWidth())
        self.layoutWidget_3.setSizePolicy(sizePolicy)
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget_3)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.maxButton_03 = QtWidgets.QPushButton(self.layoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maxButton_03.sizePolicy().hasHeightForWidth())
        self.maxButton_03.setSizePolicy(sizePolicy)
        self.maxButton_03.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.maxButton_03.setObjectName("maxButton_03")
        self.gridLayout_4.addWidget(self.maxButton_03, 0, 0, 1, 1)
        self.maxButton_02 = QtWidgets.QPushButton(self.layoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maxButton_02.sizePolicy().hasHeightForWidth())
        self.maxButton_02.setSizePolicy(sizePolicy)
        self.maxButton_02.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.maxButton_02.setObjectName("maxButton_02")
        self.gridLayout_4.addWidget(self.maxButton_02, 0, 1, 1, 1)
        self.maxButton_01 = QtWidgets.QPushButton(self.layoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maxButton_01.sizePolicy().hasHeightForWidth())
        self.maxButton_01.setSizePolicy(sizePolicy)
        self.maxButton_01.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.maxButton_01.setObjectName("maxButton_01")
        self.gridLayout_4.addWidget(self.maxButton_01, 0, 2, 1, 1)
        self.maxButton_00 = QtWidgets.QPushButton(self.layoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maxButton_00.sizePolicy().hasHeightForWidth())
        self.maxButton_00.setSizePolicy(sizePolicy)
        self.maxButton_00.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.maxButton_00.setObjectName("maxButton_00")
        self.gridLayout_4.addWidget(self.maxButton_00, 0, 3, 1, 1)
        self.maxButton_13 = QtWidgets.QPushButton(self.layoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maxButton_13.sizePolicy().hasHeightForWidth())
        self.maxButton_13.setSizePolicy(sizePolicy)
        self.maxButton_13.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.maxButton_13.setObjectName("maxButton_13")
        self.gridLayout_4.addWidget(self.maxButton_13, 1, 0, 1, 1)
        self.maxButton_12 = QtWidgets.QPushButton(self.layoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maxButton_12.sizePolicy().hasHeightForWidth())
        self.maxButton_12.setSizePolicy(sizePolicy)
        self.maxButton_12.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.maxButton_12.setObjectName("maxButton_12")
        self.gridLayout_4.addWidget(self.maxButton_12, 1, 1, 1, 1)
        self.maxButton_11 = QtWidgets.QPushButton(self.layoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maxButton_11.sizePolicy().hasHeightForWidth())
        self.maxButton_11.setSizePolicy(sizePolicy)
        self.maxButton_11.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.maxButton_11.setObjectName("maxButton_11")
        self.gridLayout_4.addWidget(self.maxButton_11, 1, 2, 1, 1)
        self.maxButton_10 = QtWidgets.QPushButton(self.layoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maxButton_10.sizePolicy().hasHeightForWidth())
        self.maxButton_10.setSizePolicy(sizePolicy)
        self.maxButton_10.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.maxButton_10.setObjectName("pushButton_10")
        self.gridLayout_4.addWidget(self.maxButton_10, 1, 3, 1, 1)
        self.maxButton_23 = QtWidgets.QPushButton(self.layoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maxButton_23.sizePolicy().hasHeightForWidth())
        self.maxButton_23.setSizePolicy(sizePolicy)
        self.maxButton_23.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.maxButton_23.setObjectName("maxButton_23")
        self.gridLayout_4.addWidget(self.maxButton_23, 2, 0, 1, 1)
        self.maxButton_22 = QtWidgets.QPushButton(self.layoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maxButton_22.sizePolicy().hasHeightForWidth())
        self.maxButton_22.setSizePolicy(sizePolicy)
        self.maxButton_22.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.maxButton_22.setObjectName("maxButton_22")
        self.gridLayout_4.addWidget(self.maxButton_22, 2, 1, 1, 1)
        self.maxButton_21 = QtWidgets.QPushButton(self.layoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maxButton_21.sizePolicy().hasHeightForWidth())
        self.maxButton_21.setSizePolicy(sizePolicy)
        self.maxButton_21.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.maxButton_21.setObjectName("maxButton_21")
        self.gridLayout_4.addWidget(self.maxButton_21, 2, 2, 1, 1)
        self.maxButton_20 = QtWidgets.QPushButton(self.layoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maxButton_20.sizePolicy().hasHeightForWidth())
        self.maxButton_20.setSizePolicy(sizePolicy)
        self.maxButton_20.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.maxButton_20.setObjectName("maxButton_20")
        self.gridLayout_4.addWidget(self.maxButton_20, 2, 3, 1, 1)
        self.maxButton_33 = QtWidgets.QPushButton(self.layoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maxButton_33.sizePolicy().hasHeightForWidth())
        self.maxButton_33.setSizePolicy(sizePolicy)
        self.maxButton_33.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.maxButton_33.setObjectName("maxButton_33")
        self.gridLayout_4.addWidget(self.maxButton_33, 3, 0, 1, 1)
        self.maxButton_32 = QtWidgets.QPushButton(self.layoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maxButton_32.sizePolicy().hasHeightForWidth())
        self.maxButton_32.setSizePolicy(sizePolicy)
        self.maxButton_32.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.maxButton_32.setObjectName("maxButton_32")
        self.gridLayout_4.addWidget(self.maxButton_32, 3, 1, 1, 1)
        self.maxButton_31 = QtWidgets.QPushButton(self.layoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maxButton_31.sizePolicy().hasHeightForWidth())
        self.maxButton_31.setSizePolicy(sizePolicy)
        self.maxButton_31.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.maxButton_31.setObjectName("maxButton_31")
        self.gridLayout_4.addWidget(self.maxButton_31, 3, 2, 1, 1)
        self.maxButton_30 = QtWidgets.QPushButton(self.layoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maxButton_30.sizePolicy().hasHeightForWidth())
        self.maxButton_30.setSizePolicy(sizePolicy)
        self.maxButton_30.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.maxButton_30.setObjectName("maxButton_30")
        self.gridLayout_4.addWidget(self.maxButton_30, 3, 3, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(360, 180, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_39 = QtWidgets.QLabel(self.centralwidget)
        self.label_39.setGeometry(QtCore.QRect(480, 70, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(self.centralwidget)
        self.label_40.setGeometry(QtCore.QRect(540, 70, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_40.setFont(font)
        self.label_40.setObjectName("label_40")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(360, 130, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(360, 230, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(360, 280, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_41 = QtWidgets.QLabel(self.centralwidget)
        self.label_41.setGeometry(QtCore.QRect(420, 70, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_41.setFont(font)
        self.label_41.setObjectName("label_41")
        self.label_42 = QtWidgets.QLabel(self.centralwidget)
        self.label_42.setGeometry(QtCore.QRect(930, 70, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_42.setFont(font)
        self.label_42.setObjectName("label_42")
        self.layoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_4.setGeometry(QtCore.QRect(730, 110, 238, 211))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layoutWidget_4.sizePolicy().hasHeightForWidth())
        self.layoutWidget_4.setSizePolicy(sizePolicy)
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.layoutWidget_4)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.reqButton_03 = QtWidgets.QPushButton(self.layoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reqButton_03.sizePolicy().hasHeightForWidth())
        self.reqButton_03.setSizePolicy(sizePolicy)
        self.reqButton_03.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.reqButton_03.setObjectName("reqButton_03")
        self.gridLayout_5.addWidget(self.reqButton_03, 0, 0, 1, 1)
        self.reqButton_02 = QtWidgets.QPushButton(self.layoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reqButton_02.sizePolicy().hasHeightForWidth())
        self.reqButton_02.setSizePolicy(sizePolicy)
        self.reqButton_02.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.reqButton_02.setObjectName("reqButton_02")
        self.gridLayout_5.addWidget(self.reqButton_02, 0, 1, 1, 1)
        self.reqButton_01 = QtWidgets.QPushButton(self.layoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reqButton_01.sizePolicy().hasHeightForWidth())
        self.reqButton_01.setSizePolicy(sizePolicy)
        self.reqButton_01.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.reqButton_01.setObjectName("reqButton_01")
        self.gridLayout_5.addWidget(self.reqButton_01, 0, 2, 1, 1)
        self.reqButton_00 = QtWidgets.QPushButton(self.layoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reqButton_00.sizePolicy().hasHeightForWidth())
        self.reqButton_00.setSizePolicy(sizePolicy)
        self.reqButton_00.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.reqButton_00.setObjectName("reqButton_00")
        self.gridLayout_5.addWidget(self.reqButton_00, 0, 3, 1, 1)
        self.reqButton_13 = QtWidgets.QPushButton(self.layoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reqButton_13.sizePolicy().hasHeightForWidth())
        self.reqButton_13.setSizePolicy(sizePolicy)
        self.reqButton_13.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.reqButton_13.setObjectName("reqButton_13")
        self.gridLayout_5.addWidget(self.reqButton_13, 1, 0, 1, 1)
        self.reqButton_12 = QtWidgets.QPushButton(self.layoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reqButton_12.sizePolicy().hasHeightForWidth())
        self.reqButton_12.setSizePolicy(sizePolicy)
        self.reqButton_12.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.reqButton_12.setObjectName("reqButton_12")
        self.gridLayout_5.addWidget(self.reqButton_12, 1, 1, 1, 1)
        self.reqButton_11 = QtWidgets.QPushButton(self.layoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reqButton_11.sizePolicy().hasHeightForWidth())
        self.reqButton_11.setSizePolicy(sizePolicy)
        self.reqButton_11.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.reqButton_11.setObjectName("reqButton_11")
        self.gridLayout_5.addWidget(self.reqButton_11, 1, 2, 1, 1)
        self.reqButton_10 = QtWidgets.QPushButton(self.layoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reqButton_10.sizePolicy().hasHeightForWidth())
        self.reqButton_10.setSizePolicy(sizePolicy)
        self.reqButton_10.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.reqButton_10.setObjectName("reqButton_10")
        self.gridLayout_5.addWidget(self.reqButton_10, 1, 3, 1, 1)
        self.reqButton_23 = QtWidgets.QPushButton(self.layoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reqButton_23.sizePolicy().hasHeightForWidth())
        self.reqButton_23.setSizePolicy(sizePolicy)
        self.reqButton_23.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.reqButton_23.setObjectName("reqButton_23")
        self.gridLayout_5.addWidget(self.reqButton_23, 2, 0, 1, 1)
        self.reqButton_22 = QtWidgets.QPushButton(self.layoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reqButton_22.sizePolicy().hasHeightForWidth())
        self.reqButton_22.setSizePolicy(sizePolicy)
        self.reqButton_22.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.reqButton_22.setObjectName("reqButton_22")
        self.gridLayout_5.addWidget(self.reqButton_22, 2, 1, 1, 1)
        self.reqButton_21 = QtWidgets.QPushButton(self.layoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reqButton_21.sizePolicy().hasHeightForWidth())
        self.reqButton_21.setSizePolicy(sizePolicy)
        self.reqButton_21.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.reqButton_21.setObjectName("reqButton_21")
        self.gridLayout_5.addWidget(self.reqButton_21, 2, 2, 1, 1)
        self.reqButton_20 = QtWidgets.QPushButton(self.layoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reqButton_20.sizePolicy().hasHeightForWidth())
        self.reqButton_20.setSizePolicy(sizePolicy)
        self.reqButton_20.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.reqButton_20.setObjectName("reqButton_20")
        self.gridLayout_5.addWidget(self.reqButton_20, 2, 3, 1, 1)
        self.reqButton_33 = QtWidgets.QPushButton(self.layoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reqButton_33.sizePolicy().hasHeightForWidth())
        self.reqButton_33.setSizePolicy(sizePolicy)
        self.reqButton_33.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.reqButton_33.setObjectName("reqButton_33")
        self.gridLayout_5.addWidget(self.reqButton_33, 3, 0, 1, 1)
        self.reqButton_32 = QtWidgets.QPushButton(self.layoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reqButton_32.sizePolicy().hasHeightForWidth())
        self.reqButton_32.setSizePolicy(sizePolicy)
        self.reqButton_32.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.reqButton_32.setObjectName("reqButton_32")
        self.gridLayout_5.addWidget(self.reqButton_32, 3, 1, 1, 1)
        self.reqButton_31 = QtWidgets.QPushButton(self.layoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reqButton_31.sizePolicy().hasHeightForWidth())
        self.reqButton_31.setSizePolicy(sizePolicy)
        self.reqButton_31.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.reqButton_31.setObjectName("reqButton_31")
        self.gridLayout_5.addWidget(self.reqButton_31, 3, 2, 1, 1)
        self.reqButton_30 = QtWidgets.QPushButton(self.layoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reqButton_30.sizePolicy().hasHeightForWidth())
        self.reqButton_30.setSizePolicy(sizePolicy)
        self.reqButton_30.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.reqButton_30.setObjectName("reqButton_30")
        self.gridLayout_5.addWidget(self.reqButton_30, 3, 3, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(690, 180, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_43 = QtWidgets.QLabel(self.centralwidget)
        self.label_43.setGeometry(QtCore.QRect(810, 70, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_43.setFont(font)
        self.label_43.setObjectName("label_43")
        self.label_44 = QtWidgets.QLabel(self.centralwidget)
        self.label_44.setGeometry(QtCore.QRect(870, 70, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_44.setFont(font)
        self.label_44.setObjectName("label_44")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(690, 130, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(690, 230, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(690, 280, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.label_45 = QtWidgets.QLabel(self.centralwidget)
        self.label_45.setGeometry(QtCore.QRect(750, 70, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_45.setFont(font)
        self.label_45.setObjectName("label_45")
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.cur_alloc = [
            [self.allButton_00, self.allButton_01, self.allButton_02, self.allButton_03],
            [self.allButton_10, self.allButton_11, self.allButton_12, self.allButton_13],
            [self.allButton_20, self.allButton_21, self.allButton_22, self.allButton_23],
            [self.allButton_30, self.allButton_31, self.allButton_32, self.allButton_33],
        ]

        self.mx_nd = [
            [self.maxButton_00, self.maxButton_01, self.maxButton_02, self.maxButton_03],
            [self.maxButton_10, self.maxButton_11, self.maxButton_12, self.maxButton_13],
            [self.maxButton_20, self.maxButton_21, self.maxButton_22, self.maxButton_23],
            [self.maxButton_30, self.maxButton_31, self.maxButton_32, self.maxButton_33],
        ]

        self.cur_req = [
            [self.reqButton_00, self.reqButton_01, self.reqButton_02, self.reqButton_03],
            [self.reqButton_10, self.reqButton_11, self.reqButton_12, self.reqButton_13],
            [self.reqButton_20, self.reqButton_21, self.reqButton_22, self.reqButton_23],
            [self.reqButton_30, self.reqButton_31, self.reqButton_32, self.reqButton_33],
        ]

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

        for lst1 in self.cur_alloc:
            for j in range(4):
                lst1[j].clicked.connect(lambda ch, btn=lst1[j]: self.click_me(btn))

        for lst2 in self.mx_nd:
            for j in range(4):
                lst2[j].clicked.connect(lambda ch, btn=lst2[j]: self.click_me(btn))

        for lst3 in self.cur_req:
            for j in range(4):
                lst3[j].clicked.connect(lambda ch, btn=lst3[j]: self.click_me(btn))

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "BankirAlgorithm"))
        self.label_29.setStyleSheet("color: rgb(51, 0, 51); font: bold")
        self.label_30.setStyleSheet("color: rgb(51, 0, 51)")

        self.label_3.setText(_translate("mainWindow", "Запрос на ресурсы"))
        self.label_3.setStyleSheet("color: rgb(51, 0, 51)")

        self.nextButton.setText(_translate("mainWindow", "next ▶"))
        self.backButton.setText(_translate("mainWindow", "◀ back"))

        self.startButton.setText(_translate("mainWindow", "START"))
        self.label_6.setText(_translate("mainWindow", "Максимальная потребность"))
        self.label_6.setStyleSheet("color: rgb(51, 0, 51)")
        self.label_34.setText(_translate("mainWindow", "R3"))
        self.label_16.setText(_translate("mainWindow", "P4"))
        self.label_35.setText(_translate("mainWindow", "R4"))
        self.label_13.setText(_translate("mainWindow", "P2"))
        self.label_17.setText(_translate("mainWindow", "P3"))
        self.label_36.setText(_translate("mainWindow", "R1"))
        self.label_37.setText(_translate("mainWindow", "R2"))
        self.allButton_03.setText(_translate("mainWindow", "0"))
        self.allButton_02.setText(_translate("mainWindow", "0"))
        self.allButton_01.setText(_translate("mainWindow", "0"))
        self.allButton_00.setText(_translate("mainWindow", "0"))
        self.allButton_13.setText(_translate("mainWindow", "0"))
        self.allButton_12.setText(_translate("mainWindow", "0"))
        self.allButton_11.setText(_translate("mainWindow", "0"))
        self.allButton_10.setText(_translate("mainWindow", "0"))
        self.allButton_23.setText(_translate("mainWindow", "0"))
        self.allButton_22.setText(_translate("mainWindow", "0"))
        self.allButton_21.setText(_translate("mainWindow", "0"))
        self.allButton_20.setText(_translate("mainWindow", "0"))
        self.allButton_33.setText(_translate("mainWindow", "0"))
        self.allButton_32.setText(_translate("mainWindow", "0"))
        self.allButton_31.setText(_translate("mainWindow", "0"))
        self.allButton_30.setText(_translate("mainWindow", "0"))
        self.label_18.setText(_translate("mainWindow", "P1"))
        self.label_4.setText(_translate("mainWindow", "Выделено ресурсов"))
        self.label_4.setStyleSheet("color: rgb(51, 0, 51)")
        self.label_38.setText(_translate("mainWindow", "R4"))
        self.maxButton_03.setText(_translate("mainWindow", "0"))
        self.maxButton_02.setText(_translate("mainWindow", "0"))
        self.maxButton_01.setText(_translate("mainWindow", "0"))
        self.maxButton_00.setText(_translate("mainWindow", "0"))
        self.maxButton_13.setText(_translate("mainWindow", "0"))
        self.maxButton_12.setText(_translate("mainWindow", "0"))
        self.maxButton_11.setText(_translate("mainWindow", "0"))
        self.maxButton_10.setText(_translate("mainWindow", "0"))
        self.maxButton_23.setText(_translate("mainWindow", "0"))
        self.maxButton_22.setText(_translate("mainWindow", "0"))
        self.maxButton_21.setText(_translate("mainWindow", "0"))
        self.maxButton_20.setText(_translate("mainWindow", "0"))
        self.maxButton_33.setText(_translate("mainWindow", "0"))
        self.maxButton_32.setText(_translate("mainWindow", "0"))
        self.maxButton_31.setText(_translate("mainWindow", "0"))
        self.maxButton_30.setText(_translate("mainWindow", "0"))
        self.label_14.setText(_translate("mainWindow", "P2"))
        self.label_39.setText(_translate("mainWindow", "R2"))
        self.label_40.setText(_translate("mainWindow", "R3"))
        self.label_19.setText(_translate("mainWindow", "P1"))
        self.label_20.setText(_translate("mainWindow", "P3"))
        self.label_21.setText(_translate("mainWindow", "P4"))
        self.label_41.setText(_translate("mainWindow", "R1"))
        self.label_42.setText(_translate("mainWindow", "R4"))
        self.reqButton_03.setText(_translate("mainWindow", "0"))
        self.reqButton_02.setText(_translate("mainWindow", "0"))
        self.reqButton_01.setText(_translate("mainWindow", "0"))
        self.reqButton_00.setText(_translate("mainWindow", "0"))
        self.reqButton_13.setText(_translate("mainWindow", "0"))
        self.reqButton_12.setText(_translate("mainWindow", "0"))
        self.reqButton_11.setText(_translate("mainWindow", "0"))
        self.reqButton_10.setText(_translate("mainWindow", "0"))
        self.reqButton_23.setText(_translate("mainWindow", "0"))
        self.reqButton_22.setText(_translate("mainWindow", "0"))
        self.reqButton_21.setText(_translate("mainWindow", "0"))
        self.reqButton_20.setText(_translate("mainWindow", "0"))
        self.reqButton_33.setText(_translate("mainWindow", "0"))
        self.reqButton_32.setText(_translate("mainWindow", "0"))
        self.reqButton_31.setText(_translate("mainWindow", "0"))
        self.reqButton_30.setText(_translate("mainWindow", "0"))
        self.label_15.setText(_translate("mainWindow", "P2"))
        self.label_43.setText(_translate("mainWindow", "R2"))
        self.label_44.setText(_translate("mainWindow", "R3"))
        self.label_22.setText(_translate("mainWindow", "P1"))
        self.label_23.setText(_translate("mainWindow", "P3"))
        self.label_24.setText(_translate("mainWindow", "P4"))
        self.label_45.setText(_translate("mainWindow", "R1"))

    def click_me(self, btn):
        if btn.text() == '0':
            btn.setText('1')
            btn.setStyleSheet("background-color: gray; color: white;")
        else:
            btn.setText('0')
            btn.setStyleSheet("background-color: lightgray;")

    def read_buttons(self) -> tuple[list[list[int]], list[list[int]], list[list[int]]]:
        def to_int(matrix: list[list[str]]) -> list[list[int]]:
            return list(map(lambda l: list(map(int, l)), matrix))

        currently_allocated = [
            [self.allButton_00.text(), self.allButton_01.text(), self.allButton_02.text(), self.allButton_03.text()],
            [self.allButton_10.text(), self.allButton_11.text(), self.allButton_12.text(), self.allButton_13.text()],
            [self.allButton_20.text(), self.allButton_21.text(), self.allButton_22.text(), self.allButton_23.text()],
            [self.allButton_30.text(), self.allButton_31.text(), self.allButton_32.text(), self.allButton_33.text()],
        ]

        max_need = [
            [self.maxButton_00.text(), self.maxButton_01.text(), self.maxButton_02.text(), self.maxButton_03.text()],
            [self.maxButton_10.text(), self.maxButton_11.text(), self.maxButton_12.text(), self.maxButton_13.text()],
            [self.maxButton_20.text(), self.maxButton_21.text(), self.maxButton_22.text(), self.maxButton_23.text()],
            [self.maxButton_30.text(), self.maxButton_31.text(), self.maxButton_32.text(), self.maxButton_33.text()],
        ]

        currently_request = [
            [self.reqButton_00.text(), self.reqButton_01.text(), self.reqButton_02.text(), self.reqButton_03.text()],
            [self.reqButton_10.text(), self.reqButton_11.text(), self.reqButton_12.text(), self.reqButton_13.text()],
            [self.reqButton_20.text(), self.reqButton_21.text(), self.reqButton_22.text(), self.reqButton_23.text()],
            [self.reqButton_30.text(), self.reqButton_31.text(), self.reqButton_32.text(), self.reqButton_33.text()],
        ]

        return to_int(currently_allocated), to_int(max_need), to_int(currently_request)

    def start(self):
        if self.startButton.text() == "START":
            self.currently_allocated, self.max_need, self.currently_request = self.read_buttons()
            allocated = [0] * resources
            for i in range(processes):
                for j in range(resources):
                    allocated[j] += self.currently_allocated[i][j]
            available = [max_resources[i] - allocated[i] for i in range(resources)]

            self.err, self.for_prev_all, self.for_prev_req, self.for_prev_max, self._lst, lab, seq, draw1, draw2, self.rest, self.lst_of_sec = bankir(self.err, processes, resources, max_resources, self.max_need, self.currently_allocated,
                                                       self.currently_request, available, allocated, sequence, label, lst_of_sec)
            drawer = GraphDrawer.GraphDrawer(config)

            for x in range(self.rest):
                dwg = drawer.draw(draw1[x], draw2[x])
                dwg.saveas(f"Pictures/graph{x}.svg")

            self._step_count = self.rest
            self._current_step = 0
            self.update_step()
            self.label_29.setText(lab)
            self.label_30.setText(seq)
            self.startButton.setStyleSheet("background-color: rgb(191, 10, 78);"
                                            "border-style: outset;"
                                            "border-width: 2px;"
                                            "border-radius: 10px;"
                                            "border-color: rgb(0, 0, 0);")

            # кнопки в красный
            print(self.err)
            if self.err:
                for x in range(4):
                    self.cur_alloc[self.err - 1][x].setStyleSheet("background-color: rgb(204, 51, 51);")
                    self.cur_req[self.err - 1][x].setStyleSheet("background-color: rgb(204, 51, 51);")
                    self.mx_nd[self.err - 1][x].setStyleSheet("background-color: rgb(204, 51, 51);")

                # Появление кнопки next, back (если 1, то нет смысла)
            if self.rest == 5:
                self.nextButton.setVisible(True)
                self.backButton.setVisible(True)

            # self.label_29.setText(lab)
            # self.label_30.setText(seq)
            # self.startButton.setStyleSheet("background-color: rgb(191, 10, 78);"
            #                                "border-style: outset;"
            #                                "border-width: 2px;"
            #                                "border-radius: 10px;"
            #                                "border-color: rgb(0, 0, 0);")
            self.startButton.setText('RESET')

        else:
            self._current_step = 0
            self._step_count = 0
            self.svg_widget.load("")

            for lst1 in self.cur_alloc:
                for j in range(4):
                    lst1[j].setText("0")
                    lst1[j].setStyleSheet("background-color: rgb(214, 214, 214)")

            for lst2 in self.mx_nd:
                for j in range(4):
                    lst2[j].setText("0")
                    lst2[j].setStyleSheet("background-color: rgb(214, 214, 214)")

            for lst3 in self.cur_req:
                for j in range(4):
                    lst3[j].setText("0")
                    lst3[j].setStyleSheet("background-color: rgb(214, 214, 214)")


            self.label_29.setText("")
            self.label_30.setText("")
            self.startButton.setStyleSheet("background-color: rgb(152, 251, 152);"
                                        "border-style: outset;"
                                        "border-width: 2px;"
                                        "border-radius: 10px;"
                                        "border-color: rgb(0, 0, 0);")
            self.rest = 0
            self.err = 0
            self.lst_of_sec = []
            self.startButton.setText('START')
            self.nextButton.setVisible(False)
            self.backButton.setVisible(False)
        # if self.startButton.text() == "START" and self.err:
        #     self.currently_allocated, self.max_need, self.currently_request = self.read_buttons()
        #     allocated = [0] * resources
        #     for i in range(processes):
        #         for j in range(resources):
        #             allocated[j] += self.currently_allocated[i][j]
        #     available = [max_resources[i] - allocated[i] for i in range(resources)]
        #
        #     self.err, self.for_prev_all, self.for_prev_req, self.for_prev_max, self._lst, lab, seq, draw1, draw2, self.rest, self.lst_of_sec = bankir(
        #         self.err, processes, resources, max_resources, self.max_need, self.currently_allocated,
        #         self.currently_request, available, allocated, sequence, label, lst_of_sec)
        #     print(self.err)
        #     self.label_29.setText(lab)
        #     self.label_30.setText(seq)
        #     self.startButton.setStyleSheet("background-color: rgb(191, 10, 78);"
        #                                    "border-style: outset;"
        #                                    "border-width: 2px;"
        #                                    "border-radius: 10px;"
        #                                    "border-color: rgb(0, 0, 0);")
        #
        #     for x in range(4):
        #         self.cur_alloc[self.err - 1][x].setStyleSheet("background-color: rgb(204, 51, 51);")
        #         self.cur_req[self.err - 1][x].setStyleSheet("background-color: rgb(204, 51, 51);")
        #         self.mx_nd[self.err - 1][x].setStyleSheet("background-color: rgb(204, 51, 51);")
        #     self.startButton.setText('RESET')
        # elif self.startButton.text() == "RESET" and self.err:
        #     for lst1 in self.cur_alloc:
        #         for j in range(4):
        #             lst1[j].setText("0")
        #             lst1[j].setStyleSheet("background-color: rgb(214, 214, 214)")
        #
        #     for lst2 in self.mx_nd:
        #         for j in range(4):
        #             lst2[j].setText("0")
        #             lst2[j].setStyleSheet("background-color: rgb(214, 214, 214)")
        #
        #     for lst3 in self.cur_req:
        #         for j in range(4):
        #             lst3[j].setText("0")
        #             lst3[j].setStyleSheet("background-color: rgb(214, 214, 214)")
        #     self.label_29.setText("")
        #     self.label_30.setText("")
        #     self.startButton.setStyleSheet("background-color: rgb(152, 251, 152);"
        #                                    "border-style: outset;"
        #                                    "border-width: 2px;"
        #                                    "border-radius: 10px;"
        #                                    "border-color: rgb(0, 0, 0);")
        #
        #     self.lst_of_sec = []
        #     self.rest = 0
        #     self.err = 0
        #     self.startButton.setText('START')
            #self.nextButton.setVisible(False)
            #self.backButton.setVisible(False)

    def update_step(self):

        # Типа Clamp
        self._current_step = self._step_count - 1 if self._current_step >= self._step_count else \
            (0 if self._current_step < 0 else self._current_step)

        self.nextButton.setVisible(self._current_step < self._step_count - 1)
        self.backButton.setVisible(self._current_step > 0 and self._step_count > 0)

        if self._current_step >= self._step_count or self._current_step < 0:
            return
        # if self.rest == 5 and self._current_step != 0:
        #     for but in range(4):
        #         lst_all[self.lst_of_sec[self.lst_of_sec[self._current_step - 1]]][but].setStyleSheet("background-color: green; color: white;")

        # if self.rest == 5 and self._current_step != 0:
        #     for but in range(4):
        #         lst_all[self.lst_of_sec[self._current_step - 1]][but].setText('0')
        #         lst_all[self.lst_of_sec[self._current_step - 1]][but].setStyleSheet("background-color: green; color: white;")
        #         lst_req[self.lst_of_sec[self._current_step - 1]][but].setText('0')
        #         lst_req[self.lst_of_sec[self._current_step - 1]][but].setStyleSheet("background-color: green; color: white;")
        self.svg_widget.load(f"Pictures/graph{self._current_step}.svg")

        # У вас оптимизация повесилась


    def next_click(self):
        self._current_step += 1
        self.update_step()
        if self.rest == 5 and self._current_step != 0:
            for but in range(4):
                self.cur_alloc[self.lst_of_sec[self._current_step - 1] - 1][but].setText('0')
                self.cur_alloc[self.lst_of_sec[self._current_step - 1] - 1][but].setStyleSheet("background-color: green; color: white;")
                self.cur_req[self.lst_of_sec[self._current_step - 1] - 1][but].setText('0')
                self.cur_req[self.lst_of_sec[self._current_step - 1] - 1][but].setStyleSheet("background-color: green; color: white;")
                self.mx_nd[self.lst_of_sec[self._current_step - 1] - 1][but].setText('0')
                self.mx_nd[self.lst_of_sec[self._current_step - 1] - 1][but].setStyleSheet("background-color: green; color: white;")
    def prev_click(self):
        if self.rest == 5 and self._current_step != 0:
            for but in range(4):
                self.cur_alloc[self.lst_of_sec[self._current_step - 1] - 1][but].setText(f'{self.for_prev_all[self.lst_of_sec[self._current_step - 1] - 1][but]}')
                self.cur_alloc[self.lst_of_sec[self._current_step - 1] - 1][but].setStyleSheet("background-color: lightgray;" if self.for_prev_all[self.lst_of_sec[self._current_step - 1] - 1][but] == 0 else "background-color: gray; color: white;")
                self.cur_req[self.lst_of_sec[self._current_step - 1] - 1][but].setText(f'{self.for_prev_req[self.lst_of_sec[self._current_step - 1] - 1][but]}')
                self.cur_req[self.lst_of_sec[self._current_step - 1] - 1][but].setStyleSheet("background-color: lightgray;" if self.for_prev_req[self.lst_of_sec[self._current_step - 1] - 1][but] == 0 else "background-color: gray; color: white;")
                self.mx_nd[self.lst_of_sec[self._current_step - 1] - 1][but].setText(f'{self.for_prev_max[self.lst_of_sec[self._current_step - 1] - 1][but]}')
                self.mx_nd[self.lst_of_sec[self._current_step - 1] - 1][but].setStyleSheet("background-color: lightgray;" if self.for_prev_max[self.lst_of_sec[self._current_step - 1] - 1][but] == 0 else "background-color: gray; color: white;")
        self._current_step -= 1
        self.update_step()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
