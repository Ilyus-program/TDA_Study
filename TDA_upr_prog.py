from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Win_upr_prog(object):
    def setupUi(self, Win_upr_prog):
        Win_upr_prog.setObjectName("Win_upr_prog")
        Win_upr_prog.resize(1920, 961)
        self.centralwidget = QtWidgets.QWidget(Win_upr_prog)
        self.centralwidget.setObjectName("centralwidget")
        self.bckgrnd = QtWidgets.QLabel(self.centralwidget)
        self.bckgrnd.setGeometry(QtCore.QRect(0, 0, 1920, 961))
        self.bckgrnd.setText("")
        self.bckgrnd.setPixmap(QtGui.QPixmap("images/Upr_prog.png"))
        self.bckgrnd.setObjectName("bckgrnd")
        self.btn_win_main = QtWidgets.QPushButton(self.centralwidget)
        self.btn_win_main.setGeometry(QtCore.QRect(980, 770, 321, 33))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btn_win_main.setFont(font)
        self.btn_win_main.setObjectName("btn_win_main")
        Win_upr_prog.setCentralWidget(self.centralwidget)

        self.retranslateUi(Win_upr_prog)
        QtCore.QMetaObject.connectSlotsByName(Win_upr_prog)

    def retranslateUi(self, Win_upr_prog):
        _translate = QtCore.QCoreApplication.translate
        Win_upr_prog.setWindowTitle(_translate("Win_upr_prog", "MainWindow"))
        self.btn_win_main.setText(_translate("Win_upr_prog", "ТДА 1. Главное окно"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Win_upr_prog = QtWidgets.QMainWindow()
#     ui = Ui_Win_upr_prog()
#     ui.setupUi(Win_upr_prog)
#     Win_upr_prog.show()
#     sys.exit(app.exec_())
