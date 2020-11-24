import sys
from PyQt5 import uic
from random import randint
from PyQt5.QtGui import QPainter, QColor, QPolygon, QPolygonF
from PyQt5.QtWidgets import QWidget, QApplication, QLabel

class Example(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        super().__init__()
        uic.loadUi('UI.ui', self)

        self.pushButton.clicked.connect(self.a)
        self.x = 250
        self.y = 175
        self.da = False

    def a(self):
        self.da = True
        self.repaint()

    def paintEvent(self, event):
        if self.da:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()
            self.da = False

    def draw(self, qp):
        size = randint(10, 350)
        qp.setBrush(QColor('yellow'))
        qp.setPen(QColor('yellow'))
        qp.drawEllipse(self.x - (size // 2), self.y - (size // 2), size, size)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
