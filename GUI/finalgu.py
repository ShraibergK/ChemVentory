# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, list, size):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(840, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(840, 800))
        MainWindow.setToolTip("")
        MainWindow.setStatusTip("")
        MainWindow.setWhatsThis("")
        MainWindow.setAccessibleName("")
        MainWindow.setAccessibleDescription("")
        MainWindow.setWindowFilePath("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(500, 500))
        self.centralwidget.setSizeIncrement(QtCore.QSize(0, 0))
        self.centralwidget.setStatusTip("")
        self.centralwidget.setWhatsThis("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.chemtabs = QtWidgets.QTabWidget(self.centralwidget)
        self.chemtabs.setObjectName("chemtabs")
        self.Main = QtWidgets.QWidget()
        self.Main.setStatusTip("")
        self.Main.setWhatsThis("")
        self.Main.setAccessibleName("")
        self.Main.setAccessibleDescription("")
        self.Main.setObjectName("Main")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Main)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(self.Main)
        self.frame.setStatusTip("")
        self.frame.setWhatsThis("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(101, 250))
        self.frame_2.setMaximumSize(QtCore.QSize(150, 800))
        self.frame_2.setSizeIncrement(QtCore.QSize(0, 0))
        self.frame_2.setBaseSize(QtCore.QSize(0, 0))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setLineWidth(1)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.listWidget = QtWidgets.QListWidget(self.frame_2)
        self.listWidget.setMinimumSize(QtCore.QSize(100, 250))
        self.listWidget.setMaximumSize(QtCore.QSize(150, 800))
        self.listWidget.setMouseTracking(True)
        self.listWidget.setTabletTracking(True)
        self.listWidget.setIconSize(QtCore.QSize(0, 0))
        self.listWidget.setGridSize(QtCore.QSize(0, 0))
        self.listWidget.setModelColumn(0)
        self.listWidget.setUniformItemSizes(True)
        self.listWidget.setItemAlignment(QtCore.Qt.AlignLeading)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        self.horizontalLayout_4.addWidget(self.frame_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setMinimumSize(QtCore.QSize(175, 0))
        self.lineEdit.setToolTip("")
        self.lineEdit.setStatusTip("")
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton.setMaximumSize(QtCore.QSize(500, 50))
        self.pushButton.setToolTip("")
        self.pushButton.setIconSize(QtCore.QSize(20, 20))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_3.setToolTip("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_2.setToolTip("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setMinimumSize(QtCore.QSize(150, 50))
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_3.addWidget(self.pushButton_5)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_3.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_5.addWidget(self.pushButton_8)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        self.chemtabs.addTab(self.Main, "")
        self.Addnewchem = QtWidgets.QWidget()
        self.Addnewchem.setObjectName("Addnewchem")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.Addnewchem)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame_3 = QtWidgets.QFrame(self.Addnewchem)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_6.addWidget(self.lineEdit_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.label_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_7.addWidget(self.lineEdit_4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_8.addWidget(self.label_4)
        self.comboBox = QtWidgets.QComboBox(self.frame_3)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_8.addWidget(self.comboBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_9.addWidget(self.label_5)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_9.addWidget(self.lineEdit_5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_11.addWidget(self.label_6)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_11.addWidget(self.lineEdit_6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_12.addWidget(self.pushButton_4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_12)
        self.gridLayout_4.addWidget(self.frame_3, 0, 0, 1, 1)
        self.chemtabs.addTab(self.Addnewchem, "")
        self.EditChem = QtWidgets.QWidget()
        self.EditChem.setObjectName("EditChem")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.EditChem)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame_4 = QtWidgets.QFrame(self.EditChem)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_7 = QtWidgets.QLabel(self.frame_4)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_14.addWidget(self.label_7)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_14.addWidget(self.lineEdit_7)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_14.addWidget(self.pushButton_6)
        self.gridLayout_6.addLayout(self.horizontalLayout_14, 0, 0, 1, 1)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.textEdit = QtWidgets.QTextEdit(self.frame_4)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_16.addWidget(self.textEdit)
        self.gridLayout_6.addLayout(self.horizontalLayout_16, 1, 0, 1, 1)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_17.setSpacing(10)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout_17.addWidget(self.pushButton_11)
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_17.addWidget(self.pushButton_10)
        self.gridLayout_6.addLayout(self.horizontalLayout_17, 2, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame_4, 0, 1, 1, 1)
        self.chemtabs.addTab(self.EditChem, "")
        self.gridLayout.addWidget(self.chemtabs, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.additems(list, size)
        self.chemtabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Chemventory MainWindow"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("MainWindow", "Search"))
        self.pushButton_3.setText(_translate("MainWindow", "Check out"))
        self.pushButton_2.setText(_translate("MainWindow", "Check In"))
        self.pushButton_5.setText(_translate("MainWindow", "Create Output File"))
        self.pushButton_8.setText(_translate("MainWindow", "Delete Entry"))
        self.chemtabs.setTabText(self.chemtabs.indexOf(self.Main), _translate("MainWindow", "Main"))
        self.label.setText(_translate("MainWindow", "Name of Chemical:"))
        self.label_2.setText(_translate("MainWindow", "Mass in grams:"))
        self.label_3.setText(_translate("MainWindow", "Date Received:"))
        self.label_4.setText(_translate("MainWindow", "Type of Chemical"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Acid"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Base"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Oxidizer"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Metals"))
        self.label_5.setText(_translate("MainWindow", "Chemical Formula:"))
        self.label_6.setText(_translate("MainWindow", "Supplier:"))
        self.pushButton_4.setText(_translate("MainWindow", "Save"))
        self.chemtabs.setTabText(self.chemtabs.indexOf(self.Addnewchem), _translate("MainWindow", "Add New"))
        self.label_7.setText(_translate("MainWindow", "Chemical:"))
        self.pushButton_6.setText(_translate("MainWindow", "Search"))
        self.pushButton_11.setText(_translate("MainWindow", "Edit Entry"))
        self.pushButton_10.setText(_translate("MainWindow", "Save Entry"))
        self.chemtabs.setTabText(self.chemtabs.indexOf(self.EditChem), _translate("MainWindow", "Edit"))

    def additems(self, list, size):
        index = 0
        namelist = []
        for i in range(size):
            namelist.append(list[i].name)

        print(namelist)
        item = QtWidgets.QListWidget()
        item.addItems(namelist)
