from operator import is_
import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtMultimedia import QSoundEffect
import random

class Obstacle:
    def __init__(self):
        self.image = QPixmap("images/spike.png") 
        self.x = 500
        self.y = 300
        self.w = 40
        self.h = 40
        self.speed = 5

    def draw(self, p):
        p.drawPixmap(QRect(self.x, self.y, self.w, self.h), self.image)

    def move(self):
        self.x -= self.speed
        if self.x < -self.w:
            self.x = 550  # Reposition off-screen

class GameWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.game_area = GameArea()
        layout = QVBoxLayout()
        layout.addWidget(self.game_area)
        self.setLayout(layout)
        self.setMinimumSize(600, 400)


def main():
    app = QApplication(sys.argv)
    w = GameWindow()
    w.show()
    return app.exec_()


if __name__ == "__main__":
    sys.exit(main())