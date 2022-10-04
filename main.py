

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PIL import Image
from datetime import datetime
from style import StyleWindow
import sys
import requests 
import json 
import urllib.request



class Main:
    def __init__(self,root):
        self.root = root
        self.class_style = StyleWindow(self.root)

        self.URL = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
        self.API = '06051f3cad0ad7ba821ba795bf6d124f'
        self.list_country = list()
        self.check = ""
       

        self.add_search()
        self.add_button()
        self.read_country()

    def add_search(self):
        """ Add QLineEdit """
        self.search_city = QLineEdit(self.root)
        self.search_city.move(230,70)
        self.search_city.resize(500,50)
        self.search_city.setStyleSheet("font-size:30px; background-color:white ;color:black; border: 2px solid red; border-radius: 23px 23px;")
        self.search_city.setAlignment(Qt.AlignCenter)


    def add_button(self):
        self.button_data = QPushButton(self.root)
        self.button_data.move(650,75)
        self.button_data.resize(40,40)
        self.button_data.setStyleSheet("background-color:white;border:0px;")

        self.button_data.setIcon(QIcon("images//get_data.png"))
        self.button_data.setIconSize(QSize(90,90))
        self.button_data.setToolTip("أنقر لجلب معلومات الطقس") 

        self.button_data.clicked.connect(self.check_connection)



    def read_country(self):
        """ Read All Data Coun """
        with open('country.json',mode='r') as self.data :
            self.data = json.loads(self.data.read())

            for self.section in self.data['countries']:
                for self.city_name in self.section['states']:
                    self.list_country.append(self.city_name)

        self.completer = QCompleter(self.list_country)
        self.search_city.setCompleter(self.completer)



    def check_connection(self):
        """Verify the device is connected to the Internet"""
        self.url_website = 'https://openweathermap.org/'
        self.timeout = 5
        try :
            request = requests.get(self.url_website, timeout=self.timeout)
            if request :
                if self.search_city.text() == "":
                    return QMessageBox.warning(self.root,"خطأ","لا يمكن ترك الحقل فارغاً",QMessageBox.Yes)
                self.get_data()
               
        except (requests.ConnectionError, requests.Timeout) as exception:
            self.message_connection = QMessageBox.warning(self.root,"خطأ","الرجاء التحقق من شبكة الإنترنت",QMessageBox.Yes)


    def get_data(self):
        """The Function Get Data And , Verify the device is connected to the Internet"""

        self.url_api = requests.get(self.URL.format(self.search_city.text(),self.API))

        if self.url_api :
            self.jsonData = self.url_api.json()
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
                self.temp_fehr, self.weather, self.pressure, self.description, self.humidity,
                self.wind 
            )

            if self.final_result :
                self.show_data()
                


    def show_data(self):
        self.class_style.label_1.setText(self.final_result[0] + '-' + self.final_result[1]) 
        self.class_style.label_2.setText(('{:.0f}°C , {:.0f}°F'.format(self.final_result[3],self.final_result[4])))
        self.class_style.label_3.setText(str(self.final_result[6]))
        self.class_style.label_4.setText(str(self.final_result[7]))
        self.class_style.label_5.setText(str(self.final_result[8]))

        self.class_style.label_weather_now.setText('{:.0f}°C'.format(self.final_result[3]))
        self.class_style.label_weather_now.setStyleSheet("background-color:#1b1b1b; color:red; font-size:22px")
        self.class_style.label_weather_now.move(700,250)
        self.class_style.label_weather_now.resize(55,22)
        self.class_style.label_6.setText(str(self.final_result[9]))


        self.class_style.label_weather.setText("WEATHER TODAY")
        self.class_style.label_weather.move(120,300)
        self.class_style.label_weather.resize(220,44)
        self.class_style.label_weather.setStyleSheet("background-color:#1b1b1b; color:white;font-size:22px")



        self.get_icon()



    def get_icon(self):
        """Get Icon Current Weather!"""

        self.data = requests.get(self.URL.format(self.search_city.text(),self.API))
        self.file_josn = self.data.json()
        self.icon = self.file_josn['weather'][0]['icon']
        urllib.request.urlretrieve(f'http://openweathermap.org/img/wn/{self.icon}.png', 'images\\image_weather.png')

        self.pixmap = QPixmap("images\\image_weather.png").scaled(160,160)
        self.class_style.label_icon.setPixmap(self.pixmap)
        self.class_style.label_icon.move(550,250)
        self.class_style.label_icon.resize(220,120)
        

if __name__ == '__main__':
    appliaction = QApplication(sys.argv)
    window = QWidget()
    class_style = Main(window)
    window.show()
    sys.exit(appliaction.exec_())
