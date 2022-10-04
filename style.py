


from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PIL import Image
from datetime import datetime
import sys

class StyleWindow:
    def __init__(self,root):
        self.root = root
        self.root.setWindowTitle('تنبؤ حالة الطقس')
        self.root.setStyleSheet('background-color:#1b1b1b;')
        self.root.setGeometry(500,200,900,700)
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
        self.label_image_logo.move(340,250)

    def add_box(self):
        self.label_titles = QLabel("",self.root)
        self.label_titles.setStyleSheet("font-size:18px; background-color:#1ab5ef;color:white;  border-radius: 33px;"


                )

        self.label_titles.move(30,570)
        self.label_titles.resize(835,80)




    def add_titles(self):

        self.label_location = QLabel("الموقع",self.root)
        self.label_location.move(60,578)
        self.label_location.setStyleSheet("font-size:18px; background-color:#1ab5ef; color:white;")



        self.label_temperature = QLabel("درجة الحرارة",self.root)
        self.label_temperature.setStyleSheet("font-size:18px; background-color:#1ab5ef; color:white;")
        self.label_temperature.move(180,578)


        self.label_pressure = QLabel("الضغط الجوي",self.root)
        self.label_pressure.setStyleSheet("font-size:18px; background-color:#1ab5ef; color:white;")
        self.label_pressure.move(340,578)


        self.label_descriptaion = QLabel("الوصف",self.root)
        self.label_descriptaion.setStyleSheet("font-size:18px; background-color:#1ab5ef; color:white;")
        self.label_descriptaion.move(730,578)


        self.label_rtooba = QLabel("الرطوبة",self.root)
        self.label_rtooba.move(500,578)
        self.label_rtooba.setStyleSheet("font-size:18px; background-color:#1ab5ef; color:white;")

        self.label_wind = QLabel("الرياح",self.root)
        self.label_wind.move(620,578)
        self.label_wind.setStyleSheet("font-size:18px; background-color:#1ab5ef; color:white;")




        self.label_1 = QLabel(".......",self.root)
        self.label_1.setStyleSheet("font-size:17px; background-color:#1ab5ef; color:black;")
        self.label_1.move(60,614)
        self.label_1.resize(70,20)


        self.label_2 = QLabel(".......",self.root)
        self.label_2.setStyleSheet("font-size:17px; background-color:#1ab5ef; color:black;")
        self.label_2.move(190,610)
        self.label_2.resize(90,28)



        self.label_3 = QLabel(".......",self.root)
        self.label_3.setStyleSheet("font-size:17px; background-color:#1ab5ef; color:black;")
        self.label_3.move(370,610)
        self.label_3.resize(35,28)




        self.label_4 = QLabel(".........",self.root)
        self.label_4.setStyleSheet("font-size:17px; background-color:#1ab5ef; color:black;")
        self.label_4.move(730,610)
        self.label_4.resize(115,28)


        self.label_5 = QLabel(".......",self.root)
        self.label_5.setStyleSheet("font-size:17px; background-color:#1ab5ef; color:black;")
        self.label_5.move(510,610)
        self.label_5.resize(35,28)


        self.label_6 = QLabel(".......",self.root)
        self.label_6.setStyleSheet("font-size:17px; background-color:#1ab5ef; color:black;")
        self.label_6.move(620,610)
        self.label_6.resize(35,28)


        self.label_icon = QLabel(self.root)
        self.label_weather_now = QLabel(self.root)

        self.label_weather = QLabel(self.root)
