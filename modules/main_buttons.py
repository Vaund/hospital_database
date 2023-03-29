# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets
from dial_table_gen import MainWindow as MW
from appointment_dial_gen import AppointmentWindow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(775, 573)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(30, 30, 721, 491))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.pushButton_services = QtWidgets.QPushButton(self.splitter)
        self.pushButton_services.setObjectName("pushButton_services")
        self.pushButton_doctors = QtWidgets.QPushButton(self.splitter)
        self.pushButton_doctors.setObjectName("pushButton_doctors")
        self.pushButton_clients = QtWidgets.QPushButton(self.splitter)
        self.pushButton_clients.setObjectName("pushButton_clients")
        self.pushButton_add_client = QtWidgets.QPushButton(self.splitter)
        self.pushButton_add_client.setObjectName("pushButton_add_client")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 775, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # услуги врачи клиенты
        self.pushButton_services.clicked.connect(self.open_table)
        self.pushButton_doctors.clicked.connect(self.open_table)
        self.pushButton_clients.clicked.connect(self.open_table)

        # запись
        self.pushButton_add_client.clicked.connect(self.open_appointment)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_services.setText(_translate("MainWindow", "УСЛУГИ"))
        self.pushButton_doctors.setText(_translate("MainWindow", "ВРАЧИ"))
        self.pushButton_clients.setText(_translate("MainWindow", "КЛИЕНТЫ"))
        self.pushButton_add_client.setText(_translate("MainWindow", "ЗАПИСЬ"))

    def open_table(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = MW()
        MW().setupUi(dialog)
        dialog.exec_()
        dialog.show()

    def open_appointment(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = AppointmentWindow
        dialog.ui().setupUi(dialog)
        dialog.exec_()
        dialog.show()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())