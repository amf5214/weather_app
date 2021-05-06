import requests
import configparser
from PyQt5.QtWidgets import QMainWindow, QFrame, QGridLayout, QMessageBox, QFontDialog, QAction
from visual_elements import *
from PyQt5.QtGui import QImage, QPalette, QBrush, QIcon, QPixmap
import random
from PyQt5.QtCore import QSize
from bs4 import BeautifulSoup



country = 'US'
units = 'F'
unit = 'Imperial'


def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']


def get_weather(zipcode, country_code='US'):
    global weather, local_state
    zip_code = f'{zipcode}, {country_code}'
    payload = {'q': zip_code, 'appid': get_api_key(), 'units': unit}
    weather = requests.get('https://api.openweathermap.org/data/2.5/weather', params=payload)
    # print(weather.status_code)
    if weather.status_code == 200:
        # print(weather.json())
        coordinates = weather.json()['coord']
        loc = requests.get(f'https://www.google.com/maps/place/{coordinates["lat"]},{coordinates["lon"]}')
        loc_data = loc.content
        soup = BeautifulSoup(loc_data, 'lxml')
        local_state = str(soup.find_all('meta', {'itemprop': "description"})[0]).split(sep='"')[1].split(sep=', ')[-1]
        # print(local_state)
    else: return


class WeatherApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.root = QFrame(self)
        self.setCentralWidget(self.root)
        self.primary = QGridLayout(self.root)
        self.setWindowTitle('Weather App')
        self.setWindowIcon(QIcon('sun_icon.png'))
        self.setFixedSize(1400, 700)

        create_elements(self)
        self.add_widgets()
        self.default_text()

        self.menu = self.menuBar()
        self.menu.setFont(QFont('Times', 10))
        self.settings_menu = self.menu.addMenu('Settings')
        self.settings_menu.setFont(QFont('Times', 10))
        self.font_menu = self.settings_menu.addMenu('Font')
        self.font_menu.setFont(QFont('Times', 10))
        self.unit_menu = self.settings_menu.addMenu('Unit')
        self.unit_menu.setFont(QFont('Times', 10))

        self.menu_setup()

        self.show()

    def activate_request(self):
        get_weather(zip_code, country)
        if weather.status_code == 200:
            self.set_text(weather)
            self.set_pic(weather)
            # print(self.size())
        else:
            QMessageBox.warning(self, 'Error', 'Please make sure that your entry is valid')

    def menu_setup(self):
        header_font_btn = QAction('Modify Header Font', self)
        header_font_btn.setFont(QFont('Times', 10))
        header_font_btn.setStatusTip('Modify Header Font')
        header_font_btn.triggered.connect(self.header_font_mod)
        self.font_menu.addAction(header_font_btn)

        text_font_btn = QAction('Modify Text Font', self)
        text_font_btn.setFont(QFont('Times', 10))
        text_font_btn.setStatusTip('Modify Text Font')
        text_font_btn.triggered.connect(self.text_font_mod)
        self.font_menu.addAction(text_font_btn)

        kelvin_btn = QAction('Kelvin', self)
        kelvin_btn.setFont(QFont('Times', 10))
        kelvin_btn.setStatusTip('Kelvin')
        kelvin_btn.triggered.connect(self.kelvin_unit_mod)
        self.unit_menu.addAction(kelvin_btn)

        celsius_btn = QAction('Celsius', self)
        celsius_btn.setFont(QFont('Times', 10))
        celsius_btn.setStatusTip('Celsius')
        celsius_btn.triggered.connect(self.celsius_unit_mod)
        self.unit_menu.addAction(celsius_btn)

        fahrenheit_btn = QAction('Fahrenheit', self)
        fahrenheit_btn.setFont(QFont('Times', 10))
        fahrenheit_btn.setStatusTip('Fahrenheit')
        fahrenheit_btn.triggered.connect(self.fahrenheit_unit_mod)
        self.unit_menu.addAction(fahrenheit_btn)

        help_btn = QAction('Help', self)
        help_btn.setFont(QFont('Times', 10))
        help_btn.setStatusTip('Help')
        help_btn.triggered.connect(self.user_help)
        self.menu.addAction(help_btn)

    def user_help(self):
        QMessageBox.information(self, 'Help', """This is a weather App.
\nThe data that is provided by this app is gathered using OpenWeather.com
\nThis app takes a city name or zipcode in the following format:
\ncity(, country code) \n\nor \n\nzipcode(, country code).
\nIf you do not supply an ISO country code, the default country code of US will be used
\nExample: New York
Example: New York, US
Example: 30334""")

    def header_font_mod(self):
        item = 'headers'
        self.on_click(item)

    def text_font_mod(self):
        item = 'text'
        self.on_click(item)

    def kelvin_unit_mod(self):
        global unit, units
        unit = 'standard'
        units = 'K'

    def celsius_unit_mod(self):
        global unit, units
        unit = 'metric'
        units = 'C'

    def fahrenheit_unit_mod(self):
        global unit, units
        unit = 'imperial'
        units = 'F'


    def on_click(self, objects):
        def openfontdialog():
            global font, ok
            font, ok = QFontDialog.getFont()
            # print(font)
            return font, ok

        openfontdialog()
        if ok:
            if objects == 'headers':
                self.header_col_1.setFont(QFont(font))
                self.header_col_2.setFont(QFont(font))
                self.city.setFont(QFont(font))
                self.description.setFont(QFont(font))
                self.entry.setFont(QFont(font))
                self.activate_app.setFont(QFont(font))
            elif objects == 'text':
                self.actual_temp_data.setFont(QFont(font))
                self.actual_temp.setFont(QFont(font))
                self.feels_like_data.setFont(QFont(font))
                self.feels_like.setFont(QFont(font))
                self.min_temp.setFont(QFont(font))
                self.min_temp_data.setFont(QFont(font))
                self.max_temp.setFont(QFont(font))
                self.max_temp_data.setFont(QFont(font))
                self.humidity.setFont(QFont(font))
                self.humidity_data.setFont(QFont(font))
                self.city_data.setFont(QFont(font))
                self.description_data.setFont(QFont(font))
        else:
            return

    def add_widgets(self):
        self.primary.addWidget(self.header_col_1, 0, 0)
        self.primary.addWidget(self.header_col_2, 0, 1)
        self.primary.addWidget(self.actual_temp, 1, 0)
        self.primary.addWidget(self.actual_temp_data, 1, 1)
        self.primary.addWidget(self.feels_like, 2, 0)
        self.primary.addWidget(self.feels_like_data, 2, 1)
        self.primary.addWidget(self.min_temp, 3, 0)
        self.primary.addWidget(self.min_temp_data, 3, 1)
        self.primary.addWidget(self.max_temp, 4, 0)
        self.primary.addWidget(self.max_temp_data, 4, 1)
        self.primary.addWidget(self.humidity, 5, 0)
        self.primary.addWidget(self.humidity_data, 5, 1)
        self.primary.addWidget(self.city, 0, 2)
        self.primary.addWidget(self.city_data, 1, 2)
        self.primary.addWidget(self.description, 0, 3)
        self.primary.addWidget(self.description_data, 1, 3)
        self.primary.addWidget(self.entry, 4, 2, 1, 2)
        self.primary.addWidget(self.activate_app, 5, 2, 1, 2)
        self.primary.addWidget(self.weather_label, 2, 2, 2, 2)

    def set_text(self, weather_data):
        self.header_col_1.setText('WEATHER INDICATOR')
        self.header_col_2.setText('VALUE')

        self.actual_temp_data.setText(str(round(weather_data.json()['main']['temp']))
                                      + ' ' + units)
        self.actual_temp.setText('Current Temperature:')

        self.feels_like_data.setText(str(round(weather_data.json()['main']['feels_like']))
                                     + ' ' + units)
        self.feels_like.setText('Feels Like Temperature:')

        self.min_temp.setText('Min Temperature:')
        self.min_temp_data.setText(str(round(weather_data.json()['main']['temp_min']))
                                     + ' ' + units)

        self.max_temp.setText('Max Temperature:')
        self.max_temp_data.setText(str(round(weather_data.json()['main']['temp_max']))
                                     + ' ' + units)

        self.humidity.setText('Humidity:')
        self.humidity_data.setText(str(round(weather_data.json()['main']['humidity']))
                                     + ' %')

        self.city.setText('Location')
        # self.city_data.setText(weather_data.json()['name'] + ', ' + weather_data.json()['sys']['country'])
        self.city_data.setText(weather_data.json()['name'] + ', ' + local_state + ', ' + weather_data.json()['sys']['country'])

        self.description.setText('Description')
        self.description_data.setText(str(weather_data.json()['weather'][0]['description']).capitalize())


    def default_text(self):
        self.header_col_1.setText('WEATHER INDICATOR')
        self.header_col_2.setText('VALUE')

        self.actual_temp_data.setText('NA')
        self.actual_temp.setText('Current Temperature:')

        self.feels_like_data.setText('NA')
        self.feels_like.setText('Feels Like Temperature:')

        self.min_temp.setText('Min Temperature:')
        self.min_temp_data.setText('NA')

        self.max_temp.setText('Max Temperature:')
        self.max_temp_data.setText('NA')

        self.humidity.setText('Humidity:')
        self.humidity_data.setText('NA')

        self.city.setText('Location')
        self.city_data.setText('NA')

        self.description.setText('Description')
        self.description_data.setText('NA')

    def set_pic(self, weather_data):
        description = weather_data.json()['weather'][0]['icon']
        pixmap = QPixmap('icons/' + description + '.png')
        self.weather_label.setPixmap(pixmap)
        self.weather_label.resize(self.pixmap.width(),
                            self.pixmap.height())
        # print(pixmap)
        # print(description)
        # print(type(description))

    def set_background(self):
        n = random.randint(0, 3)
        pic_name = 'day_background' + str(n) + '.jpg'
        # self.root.setStyleSheet(f'background-image: url({pic_name}); background-repeat: no-repeat')
        oimage = QImage(pic_name)
        simage = oimage.scaled(QSize(1600, 700))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(simage))
        self.setPalette(palette)

    def set_city(self, text):
        global zip_code, country
        # self.entry.adjustSize()
        if ',' in text:
            city_country = text.split(sep=', ')
            if len(city_country) == 1:
                zip_code = city_country[0]

            elif len(city_country) == 2:
                zip_code = city_country[0]
                country = city_country[1]

            elif len(city_country) > 2:
                QMessageBox.warning(self, 'Input Error', 'Please enter city, country or zipcode, country')
                return
            else:
                return
        else:
            zip_code = text


