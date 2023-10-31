import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from TDA_st import Ui_MainWindow
from TDA_upr_prog import Ui_Win_upr_prog
from ZD_panel import Ui_Dialog

app = QtWidgets.QApplication(sys.argv)

MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
Win_Upr = Ui_Win_upr_prog()

def OpenWinUprProg():
    global Win_upr_prog
    Win_upr_prog = QtWidgets.QMainWindow()
    ui = Ui_Win_upr_prog()
    ui.setupUi(Win_upr_prog)
    Win_upr_prog.show()
    MainWindow.close()

    def ReturnToMain():
        Win_upr_prog.close()
        MainWindow.show()

    ui.btn_win_main.clicked.connect(ReturnToMain)

def KN160_open():
    global Dialog
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()

ui.btn_win_upr.clicked.connect(OpenWinUprProg)
ui.KN160.clicked.connect(KN160_open)


sys.exit(app.exec_())