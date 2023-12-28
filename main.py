
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