from PyQt5.QtWidgets import QApplication
from weather_app import *
import sys


def run():
    app = QApplication(sys.argv)

    window = WeatherApp()

    sys.exit(app.exec_())


if __name__ == '__main__':
    run()
