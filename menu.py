import sys
import requests

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui, QtCore
from menu_design import Ui_MainWindow


# Наследуемся от виджета из PyQt5.QtWidgets и от класса с интерфейсом
class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.pushButton.clicked.connect()
        self.lon = "37.530887"
        self.lan = "55.703118"
        self.delta = 0
        self.size = "450"
        self.zooms = ['10', '5', '3', '2', '1', '0.7', '0.4', '0.2', '0.1', '0.05', '0.03', '0.02']
        self.update_pic(self.lon, self.lan, self.delta, self.size)

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_PageUp:
            if int(self.delta) < 21:
                self.delta = str(int(self.delta) + 1)
                self.update_pic(self.lon, self.lan, self.delta, self.size)
        if e.key() == QtCore.Qt.Key_PageDown:
            if int(self.delta) > 0:
                self.delta = str(int(self.delta) - 1)
                self.update_pic(self.lon, self.lan, self.delta, self.size)

    def update_pic(self, lon, lan, delta, size):
        api_server = "http://static-maps.yandex.ru/1.x/"
        print(delta)
        params = {
            "ll": ",".join([lon, lan]),
            "z": delta,
            "l": "map",
            "size": ",".join([size, size])
        }
        response = requests.get(api_server, params=params)
        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)
        pixmap = QtGui.QPixmap('map.png')
        self.map_pic.setPixmap(pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())