from chemical_class import *
from finalgu import *
from listops import *
import sys
from PyQt5 import QtGui, uic


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWin = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()

    listthing = listloader()
    size = len(listthing)

    ui.setupUi(MainWin, size, listthing)
    MainWin.show()

    sys.exit(app.exec_())
