import sys
import pygame
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QWidget, QHBoxLayout, QVBoxLayout,
                             QGridLayout, QPushButton)

from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # window
        self.setWindowTitle("First Excercise")
        self.setGeometry(700, 300, 700, 500)
        self.setWindowIcon(QIcon("pic.ico"))

        # widget
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        # LayOut(s)
        self.layout = QVBoxLayout(self.centralWidget)

        # Object(s)
        self.text = QLabel("Ready?")

        self.pic = QPixmap("pic.ico")

        self.button = QPushButton("Start")
        self.button.clicked.connect(self.on_clicked)

        pygame.mixer.init()

       # UI
        self.initUI()

    def initUI(self):

        self.centralWidget.setStyleSheet("background-color: #131117;")

        self.text.setFont(QFont("Tahoma",))
        self.text.setStyleSheet(
            "font: 15px;"
            "color: gray;"
            "padding: 10px;"
            "border-radius: 10px;"
            "border: none;"
            "font-weight: bold;"
        )
        self.text.setAlignment(Qt.AlignCenter)

        self.button.setFont(QFont("Tahoma",))
        self.button.setStyleSheet(
            "font: 30px;"
            "background-color: #4400ff;"
            "padding: 10px;"
            "font-weight: bold;"
            "border-radius: 10px;"
            "border: 2px solid #ffffff;"
            "color: white;"
            "border-bottom: 4px solid #2a0099;"
        )

        self.image_lable = QLabel()
        self.image_lable.setPixmap(self.pic)

        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.image_lable)

        self.layout.setAlignment(Qt.AlignCenter)

    def on_clicked(self):
        print("Button Clicked")
        self.sound = "D:/Coding/PYTHON/Exercisses/Gemini-mini-projects/Change_status/audio.wav"

        pygame.mixer.music.load(self.sound)
        pygame.mixer.music.play()

        if self.button.text() == "Start":
            self.text.setText("YOHAHA")
            self.text.setStyleSheet(
                "color: orange; font-size: 20px; font-weight: bold;")
            self.button.setText("HEHEHE")
            self.button.setStyleSheet(
                "background-color: #e74c3c; color: white; border-radius: 10px; font: 30px;")
        else:
            self.text.setText("Ready?")
            self.text.setStyleSheet(
                "color: gray; font-size: 15px; font-weight: bold;")
            self.button.setText("Start")
            self.button.setStyleSheet(
                "background-color: #4400ff; color: white; border-radius: 10px; font: 30px;")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
