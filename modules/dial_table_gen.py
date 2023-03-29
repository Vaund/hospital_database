from PyQt5.QtWidgets import QDialog, QApplication, QTableWidgetItem
from PyQt5.QtCore import Qt
from table import Ui_Dialog
import sys


def create_table(col_names, rows, table):
    table.setRowCount(rows)
    table.setColumnCount(len(col_names))
    table.setHorizontalHeaderLabels(col_names)

    for row in range(rows):
        for column in range(len(col_names)):
            item = QTableWidgetItem("")
            item.setFlags(item.flags() & ~Qt.ItemIsEditable)
            table.setItem(row, column, QTableWidgetItem(""))




class MainWindow(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        col_names = ["name", "cabinet","salary"]
        create_table(col_names, 5, self.tableWidget)

        self.pushButton_add.clicked.connect(self.pushButton_add_clicked)
        self.pushButton_edit.clicked.connect(self.pushButton_edit_clicked)
        self.pushButton_delete.clicked.connect(self.pushButton_delete_clicked)

    def pushButton_add_clicked(self):
        print("[+] Добавить pressed")
        selected_index = self.tableWidget.selectedItems()
        if len(selected_index) == 1:
            print(selected_index)
            text_to_place_in_item = self.textEdit.toPlainText()
            selected_index[0].setText(text_to_place_in_item)

    def pushButton_edit_clicked(self):
        print("[+] Изменить pressed")

    def pushButton_delete_clicked(self):
        print("[+] Удалить pressed")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())
