from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class StyleWindow:
    def __init__(self, root):
        self.root = root
        self.root.setWindowTitle('Weather App')
        self.root.setStyleSheet('background-color:#333;')
        self.root.setGeometry(500, 200, 900, 700)
        self.root.setWindowIcon(QIcon('images\\icon_app.ico'))
        self.root.setFixedWidth(900)
        self.root.setFixedHeight(700)


        self.add_logo()
        self.add_box()
        self.add_titles()


    def add_logo(self):
        self.label_image_logo = QLabel(self.root)
        self.pixmap_logo = QPixmap("images\\logo.png")
        self.label_image_logo.setPixmap(self.pixmap_logo)
        self.label_image_logo.move(240, 250)

    def add_box(self):
        self.label_titles = QLabel("", self.root)
        self.label_titles.setStyleSheet("font-size:18px; background-color:#1ab5ef; color:white; border-radius: 14px;")
        self.label_titles.move(30, 570)
        self.label_titles.resize(840, 80)

    def add_titles(self):

        title_style = "font-size:19px; background-color:#1ab5ef; color:white; font-weight: bold;"
        value_style = "font-size:16px; background-color:#1ab5ef; color:black; font-weight: bold;"
        value_empty = "......."

        self.label_location = QLabel("Location", self.root)
        self.label_location.move(60, 578)
        self.label_location.setStyleSheet(title_style)

        self.label_temperature = QLabel("Temperature", self.root)
        self.label_temperature.setStyleSheet(title_style)
        self.label_temperature.move(190, 578)

        self.label_description = QLabel("Description", self.root)
        self.label_description.setStyleSheet(title_style)
        self.label_description.move(360, 578)

        self.label_wind = QLabel("Wind", self.root)
        self.label_wind.setStyleSheet(title_style)
        self.label_wind.move(520, 578)

        self.label_humidity = QLabel("Humidity", self.root)
        self.label_humidity.move(625, 578)
        self.label_humidity.setStyleSheet(title_style)

        self.label_pressure = QLabel("Pressure", self.root)
        self.label_pressure.move(760, 578)
        self.label_pressure.setStyleSheet(title_style)

        self.location = QLabel(value_empty, self.root)
        self.location.setStyleSheet(value_style)
        self.location.move(60, 610)
        self.location.resize(130, 28)

        self.temperature = QLabel(value_empty, self.root)
        self.temperature.setStyleSheet(value_style)
        self.temperature.move(190, 610)
        self.temperature.resize(140, 28)

        self.description = QLabel(value_empty, self.root)
        self.description.setStyleSheet(value_style)
        self.description.move(360, 610)
        self.description.resize(140, 28)

        self.humidity = QLabel(value_empty, self.root)
        self.humidity.setStyleSheet(value_style)
        self.humidity.move(625, 610)
        self.humidity.resize(125, 28)

        self.wind = QLabel(value_empty, self.root)
        self.wind.setStyleSheet(value_style)
        self.wind.move(520, 610)
        self.wind.resize(100, 28)

        self.pressure = QLabel(value_empty, self.root)
        self.pressure.setStyleSheet(value_style)
        self.pressure.move(760, 610)
        self.pressure.resize(110, 28)

        self.label_icon = QLabel(self.root)
        self.label_weather_now = QLabel(self.root)
        self.label_weather = QLabel(self.root)

        self.label_weather = QLabel("TODAY'S WEATHER", self.root)
        self.label_weather.move(460, 270)
        self.label_weather.resize(220, 44)
        self.label_weather.setStyleSheet("background-color:#333; color:white; font-size:22px")

        self.label_guide = QLabel("Enter country or city..", self.root)
        self.label_guide.move(460, 320)
        self.label_guide.resize(220, 44)
        self.label_guide.setStyleSheet("background-color:#333; color:gray; font-size:18px")