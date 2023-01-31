import sys
from random import randrange

from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.count = 0
        self.pushButton.clicked.connect(lambda: self.update())

    def paintEvent(self, event):
        if self.count != 0:
            qp = QPainter()
            qp.begin(self)
            for i in range(5):
                self.draw_circle(qp)
            qp.end()
        else:
            self.count += 1

    def draw_circle(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        dm = randrange(5, 50)
        qp.drawEllipse(randrange(dm, 400 - dm), randrange(dm, 300 - dm), dm, dm)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    ex = Widget()
    ex.show()
    sys.exit(app.exec())
