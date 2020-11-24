import sys
from PyQt5 import uic
from random import randint
from PyQt5.QtGui import QPainter, QColor, QPolygon, QPolygonF
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(618, 466)
        self.btn = QtWidgets.QPushButton(Form)
        self.btn.setGeometry(QtCore.QRect(190, 430, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.btn.setFont(font)
        self.btn.setObjectName("btn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Желтые jrhe;yjcnb"))
        self.btn.setText(_translate("Form", "ₐ"))


class Example(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn.clicked.connect(self.a)
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
        qp.setBrush(QColor(QColor(randint(1, 255), randint(1, 255), randint(1, 255))))
        qp.setPen(QColor(QColor(randint(1, 255), randint(1, 255), randint(1, 255))))
        qp.drawEllipse(self.x - (size // 2), self.y - (size // 2), size, size)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())