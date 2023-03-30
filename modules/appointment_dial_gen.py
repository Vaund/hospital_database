from PyQt5.QtWidgets import QDialog, QApplication
from appointment_dial import Ui_Dialog_appointment
import sys


class AppointmentWindow(QDialog, Ui_Dialog_appointment):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.pushButton_clicked)

        # тестовый текст в кнопках
        clients = ["Джейсон Стетим", "Иван Махалов", "Ян Глина", "Геннадий Жмот", "Иван Зяблик"]

        doctors = {"Пеппер": ["Осмотр", "Первичный приём"],
                   "Хаус": ["Первичный осмотр", "Удаление гланд"],
                   "Дрэ": ["Операция по голове", "Вставка"],
                   "Кто": ["Пересадка волос", "Смена пола"]}

        self.comboBox_3.addItems(clients)
        self.comboBox.addItems(doctors.keys())
        self.comboBox.currentIndexChanged.connect(self.comboBox_changed)

    def comboBox_changed(self):
        doctors = {"Пеппер": ["Осмотр", "Первичный приём"],
                   "Хаус": ["Первичный осмотр", "Удаление гланд"],
                   "Дрэ": ["Операция по голове", "Вставка"],
                   "Кто": ["Пересадка волос", "Смена пола"]}

        self.comboBox_2.clear()
        self.comboBox_2.addItems(doctors[self.comboBox.currentText()])

    def pushButton_clicked(self):
        print("[+] Click Записать")
        # Вывод выбранных параметров
        output = ("Пациент:", self.comboBox_3.currentText(), "\n",
                  "Доктор:", self.comboBox.currentText(), "\n",
                  "Манипуляция:", self.comboBox_2.currentText(), "\n",
                  "Начало сеанса:", self.timeEdit.text())

        print(output)
        # Вывод статуса в информационное окно
        try:
            if self.timeEdit.text() != "00:00":
                self.plainTextEdit.setPlainText(str(f"{self.comboBox_3.currentText()} записан на приём! \n"
                                                    f"Лечащий врач: {self.comboBox.currentText()} \n"
                                                    f"Процедура: {self.comboBox_2.currentText()}\n"
                                                    f"Время: {self.timeEdit.text()}"))
                return True
        except Exception as e:
            self.plainTextEdit.setPlainText(str(e))
            return e
        else:
            self.plainTextEdit.setPlainText("Укажите время!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = AppointmentWindow()
    main_window.show()
    sys.exit(app.exec_())
