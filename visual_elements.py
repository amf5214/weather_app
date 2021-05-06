from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QSizePolicy
from PyQt5.QtGui import QFont, QPixmap
import PyQt5.QtCore as Qtc


def create_elements(self):
    self.header_col_1 = QLabel(self)
    self.header_col_1.setFont(QFont('Times', 15))
    self.header_col_1.setAlignment(Qtc.Qt.AlignCenter)
    self.header_col_1.setStyleSheet('''background-color: orange; 
                                        color: white;
                                        padding-top:15px;
                                        padding-bottom: 15px;
                                        padding-right: 15px;
                                        padding-left: 15px''')


    self.header_col_2 = QLabel(self)
    self.header_col_2.setFont(QFont('Times', 15))
    self.header_col_2.setAlignment(Qtc.Qt.AlignCenter)
    self.header_col_2.setStyleSheet('''background-color: orange; 
                                        color: white;
                                        padding-top: 15px;
                                        padding-bottom: 15px;
                                        padding-right: 15px;
                                        padding-left: 15px''')

    self.feels_like = QLabel(self)
    self.feels_like.setAlignment(Qtc.Qt.AlignCenter)
    self.feels_like.setFont(QFont('Times', 15))
    self.feels_like_data = QLabel(self)
    self.feels_like_data.setAlignment(Qtc.Qt.AlignCenter)
    self.feels_like_data.setFont(QFont('Times', 15))

    self.actual_temp = QLabel(self)
    self.actual_temp.setAlignment(Qtc.Qt.AlignCenter)
    self.actual_temp.setFont(QFont('Times', 15))
    self.actual_temp_data = QLabel(self)
    self.actual_temp_data.setAlignment(Qtc.Qt.AlignCenter)
    self.actual_temp_data.setFont(QFont('Times', 15))

    self.min_temp = QLabel(self)
    self.min_temp.setAlignment(Qtc.Qt.AlignCenter)
    self.min_temp.setFont(QFont('Times', 15))
    self.min_temp_data = QLabel(self)
    self.min_temp_data.setFont(QFont('Times', 15))
    self.min_temp_data.setAlignment(Qtc.Qt.AlignCenter)

    self.max_temp = QLabel(self)
    self.max_temp.setFont(QFont('Times', 15))
    self.max_temp.setAlignment(Qtc.Qt.AlignCenter)
    self.max_temp_data = QLabel(self)
    self.max_temp_data.setFont(QFont('Times', 15))
    self.max_temp_data.setAlignment(Qtc.Qt.AlignCenter)

    self.humidity = QLabel(self)
    self.humidity.setFont(QFont('Times', 15))
    self.humidity.setAlignment(Qtc.Qt.AlignCenter)
    self.humidity_data = QLabel(self)
    self.humidity_data.setFont(QFont('Times', 15))
    self.humidity_data.setAlignment(Qtc.Qt.AlignCenter)

    self.city = QLabel(self)
    self.city.setFont(QFont('Times', 15))
    self.city.setAlignment(Qtc.Qt.AlignCenter)
    self.city.setStyleSheet('''background-color: orange; 
                                        color: white;
                                        padding-top: 15px;
                                        padding-bottom: 15px;
                                        padding-right: 15px;
                                        padding-left: 15px''')
    self.city_data = QLabel(self)
    self.city_data.setFont(QFont('Times', 15))
    self.city_data.setAlignment(Qtc.Qt.AlignCenter)

    self.description = QLabel(self)
    self.description.setFont(QFont('Times', 15))
    self.description.setAlignment(Qtc.Qt.AlignCenter)
    self.description.setStyleSheet('''background-color: orange; 
                                        color: white;
                                        padding-top: 15px;
                                        padding-bottom: 15px;
                                        padding-right: 15px;
                                        padding-left: 15px''')
    self.description_data = QLabel(self)
    self.description_data.setFont(QFont('Times', 15))
    self.description_data.setAlignment(Qtc.Qt.AlignCenter)

    self.entry = QLineEdit()
    self.entry.setFont(QFont('Times', 15))
    self.entry.setText('City Name')
    self.entry.textChanged.connect(self.set_city)
    self.entry.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
    # self.entry.setMinimumWidth(50)
    self.entry.setAlignment(Qtc.Qt.AlignCenter)
    self.entry.setStyleSheet('''
                                        padding-top: 15px;
                                        padding-bottom: 15px;
                                        padding-right: 15px;
                                        padding-left: 15px''')

    self.activate_app = QPushButton('Check Weather')
    self.activate_app.setFont(QFont('Times', 15))
    self.activate_app.clicked.connect(self.activate_request)
    self.activate_app.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
    self.activate_app.setStyleSheet('''background-color: orange; 
                                        color: white;
                                        padding-top: 15px;
                                        padding-bottom: 15px;
                                        padding-right: 15px;
                                        padding-left: 15px''')

    self.weather_label = QLabel()
    self.pixmap = QPixmap('icons/unknown.png')
    self.weather_label.setPixmap(self.pixmap)
    self.weather_label.setAlignment(Qtc.Qt.AlignCenter)
