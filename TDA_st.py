from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 961)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Bkgrnd = QtWidgets.QLabel(self.centralwidget)
        self.Bkgrnd.setGeometry(QtCore.QRect(0, 0, 1920, 961))
        self.Bkgrnd.setText("")
        self.Bkgrnd.setPixmap(QtGui.QPixmap("images/Main.png"))
        self.Bkgrnd.setObjectName("Bkgrnd")
        self.btn_win_upr = QtWidgets.QPushButton(self.centralwidget)
        self.btn_win_upr.setGeometry(QtCore.QRect(26, 76, 321, 33))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btn_win_upr.setFont(font)
        self.btn_win_upr.setObjectName("btn_win_upr")
        self.KN160 = QtWidgets.QPushButton(self.centralwidget)
        self.KN160.setGeometry(QtCore.QRect(1060, 220, 65, 50))
        self.KN160.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/ZD_closen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.KN160.setIcon(icon)
        self.KN160.setIconSize(QtCore.QSize(65, 50))
        self.KN160.setObjectName("KN160")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_win_upr.setText(_translate("MainWindow", "ТДА 1. Управление программами"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

# to GitHub