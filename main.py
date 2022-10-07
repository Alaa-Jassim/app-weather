import json
import sys
import urllib.request

import requests
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from style import StyleWindow
import threading


class Main:
    def __init__(self, root):
        self.root = root
        self.class_style = StyleWindow(self.root)

        self.URL = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
        self.API = '06051f3cad0ad7ba821ba795bf6d124f'
        self.list_country = list()
        self.check = ""
        self.is_guide_shown = True


        self.add_search_field()
        self.add_search_button()
        self.read_country()

    def add_search_field(self):
        """ Add QLineEdit """
        self.search_field = QLineEdit(self.root)
        self.search_field.move(200, 70)
        self.search_field.resize(500, 50)
        self.search_field.setStyleSheet("font-size:24px; background-color:white; padding: 0 15px; border:2px solid gray; border-radius:23px 23px;")
        self.search_field.returnPressed.connect(self.check_connection)

    def add_search_button(self):
        self.search_button = QPushButton(self.root)
        self.search_button.move(645, 75)
        self.search_button.resize(40, 40)
        self.search_button.setStyleSheet("background-color:white; border:0px;")
        self.search_button.setIcon(QIcon("images//get_data.png"))
        self.search_button.setIconSize(QSize(40, 40))
        self.search_button.setToolTip("Click search to get weather")
        self.search_button.clicked.connect(self.check_connection)

    def read_country(self):
        """ Read All Data """
        with open('country.json', mode='r') as self.data:
            self.data = json.loads(self.data.read())

            for self.section in self.data['countries']:
                for self.city_name in self.section['states']:
                    self.list_country.append(self.city_name)

        self.completer = QCompleter(self.list_country)
        self.completer.setCaseSensitivity(0)
        self.search_field.setCompleter(self.completer)

    def check_connection(self):
        """Verify the device is connected to the Internet"""
        self.weather_api_url = 'https://openweathermap.org/'
        self.timeout = 5
        try:
            request = requests.get(self.weather_api_url, timeout=self.timeout)
            if request:
                if self.search_field.text() == "":
                    return QMessageBox.warning(self.root, "Error", "You can't leave this field empty!", QMessageBox.Yes)
                #self.get_data()
                self.thread_get_data = threading.Thread(target=self.get_data,args=()).start()

        except (requests.ConnectionError, requests.Timeout) as exception:
            self.message_connection = QMessageBox.warning(self.root, "Error", "Please check your network!", QMessageBox.Yes)

    

    def get_data(self):
        """The Function Get Data And , Verify the device is connected to the Internet"""

        self.weather_api_data = requests.get(self.URL.format(self.search_field.text(), self.API))

        if self.weather_api_data:
            self.jsonData = self.weather_api_data.json()
            self.city = self.jsonData['name']
            self.country = self.jsonData['sys']['country']
            self.temp_klv = self.jsonData['main']['temp']
            self.temp_celcuis = (self.temp_klv - 273.15)
            self.temp_fehr = (self.temp_klv - 273.15) * 9 / 5 + 32
            self.weather = self.jsonData['weather'][0]['main']
            self.pressure = self.jsonData['main']['pressure']
            self.description = self.jsonData['weather'][0]['description']
            self.humidity = self.jsonData['main']['humidity']
            self.wind = self.jsonData['wind']['speed']

            self.final_result = (
                self.city, self.country, self.temp_klv, self.temp_celcuis,
                self.temp_fehr, self.weather, self.pressure, self.wind, self.humidity,
                self.description
            )

            if self.final_result:
               self.thread_show_data = threading.Thread(target=self.show_data,args=()).start()

    

    def show_data(self):
        if self.is_guide_shown:
            self.class_style.label_guide.deleteLater()
            self.is_guide_shown = False

        self.class_style.location.setText(self.final_result[0] + '-' + self.final_result[1])
        self.class_style.temperature.setText(('{:.0f}°C , {:.0f}°F'.format(self.final_result[3], self.final_result[4])))
        self.class_style.pressure.setText(str(self.final_result[6]))
        self.class_style.humidity.setText(str(self.final_result[7]) + '%')
        self.class_style.wind.setText(str(self.final_result[8]))

        self.class_style.label_weather_now.setText('{:.0f}°C'.format(self.final_result[3]))
        self.class_style.label_weather_now.setStyleSheet("background-color:#333; color:cyan; font-size:22px")
        self.class_style.label_weather_now.move(580, 340)
        self.class_style.label_weather_now.resize(55, 22)
        self.class_style.description.setText(str(self.final_result[9]))

    
        self.thread_get_icon = threading.Thread(target=self.get_icon,args=()).start()

    def get_icon(self):
        """Get Icon Current Weather!"""

        self.data = requests.get(self.URL.format(self.search_field.text(), self.API))
        self.file_josn = self.data.json()
        self.icon = self.file_josn['weather'][0]['icon']
        urllib.request.urlretrieve(f'http://openweathermap.org/img/wn/{self.icon}.png', 'images\\image_weather.png')

        self.pixmap = QPixmap("images\\image_weather.png").scaled(160, 160)
        self.class_style.label_icon.setPixmap(self.pixmap)
        self.class_style.label_icon.move(450, 340)
        self.class_style.label_icon.resize(220, 120)


if __name__ == '__main__':
    application = QApplication(sys.argv)
    window = QWidget()
    class_style = Main(window)
    window.show()
    sys.exit(application.exec_())