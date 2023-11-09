from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_main_gui(object):
    def setupUi(self, main_gui):
        main_gui.setObjectName("main_gui")
        main_gui.resize(397, 306)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=main_gui)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(259, 229, 131, 61))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.listView = QtWidgets.QListView(parent=main_gui)
        self.listView.setGeometry(QtCore.QRect(10, 10, 371, 211))
        self.listView.setObjectName("listView")
        self.textEdit = QtWidgets.QTextEdit(parent=main_gui)
        self.textEdit.setGeometry(QtCore.QRect(10, 230, 241, 61))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(main_gui)
        QtCore.QMetaObject.connectSlotsByName(main_gui)

    def retranslateUi(self, main_gui):
        _translate = QtCore.QCoreApplication.translate
        main_gui.setWindowTitle(_translate("main_gui", "Form"))
        self.pushButton.setText(_translate("main_gui", "Send"))
        self.pushButton_2.setText(_translate("main_gui", "Receive"))
