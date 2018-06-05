import design
import sys
from PyQt5 import QtWidgets, QtGui
from math import sqrt

result = 0
decyph = 0

#gsn=(11,19,31,41,59,71,73,79,107,109,113,139,149,163,173,181,191,193,197,211,227,229,241,257,269,277,293,307,317,347)


def simplicity_check(num):
    for i in range(2, int(sqrt(num))):
        if num % i == 0:
            return False
        else:
            return True


def euclid(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


def gcdex(a, b):
    global result
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = gcdex(b, a % b)
        result = y
        return d, y, x - y * (a // b)


class Rsapp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.rsacalculate)
        self.pushButton_2.clicked.connect(self.decyphprint)

    def rsacalculate(self):
        global decyph
        p = self.lineEdit.text()
        q = self.lineEdit_2.text()
        if not simplicity_check(int(p)) or not simplicity_check(int(q)):
            font = QtGui.QFont()
            font.setPointSize(15)
            self.textBrowser_2.setFont(font)
            self.textBrowser_2.setText('Введите простые p, q')
        else:
            font = QtGui.QFont()
            font.setPointSize(30)
            self.textBrowser_2.setFont(font)
            n = int(p) * int(q)
            fi = (int(p)-1)*(int(q)-1)
            for e in range(69, fi):
                if euclid(e, fi) == 1:
                    break
            gcdex(e, fi)
            d = result
            m = int(self.lineEdit_3.text())
            c = (pow(m, e) % n)
            decyph = (pow(c, d) % n)
            self.textBrowser.setText(str(n))
            self.textBrowser_2.setText(str(c))

    def decyphprint(self):
        global decyph
        self.textBrowser_2.setText(str(decyph))


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Rsapp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
