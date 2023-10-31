from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(295, 354)
        self.bckgrd = QtWidgets.QLabel(Dialog)
        self.bckgrd.setGeometry(QtCore.QRect(0, 0, 295, 354))
        self.bckgrd.setText("")
        self.bckgrd.setPixmap(QtGui.QPixmap("images/KN_fp.png"))
        self.bckgrd.setObjectName("bckgrd")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Ui_Dialog()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec_())
