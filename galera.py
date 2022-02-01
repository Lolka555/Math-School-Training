import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel
from l1 import Start1
from ll1 import Start2
from lll1 import Start3

class Work(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 100)
        self.setWindowTitle('Easy LVL')
        self.button_1 = QPushButton(self)
        self.button_1.move(90, 40)
        self.button_1.setText("Start")
        self.button_1.clicked.connect(self.run1)
        self.show()
        
    def run1(self):
        self.work = Start1()
        self.work.show()
        self.hide()
        
        
        
class Work1(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 100)
        self.setWindowTitle('Medium LVL')
        self.button_1 = QPushButton(self)
        self.button_1.move(90, 40)
        self.button_1.setText("Start")
        self.button_1.clicked.connect(self.run2)            
        self.show()
        
    def run2(self):
        self.work = Start2()
        self.work.show()
        self.hide()        
        
        
class Work2(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 100)
        self.setWindowTitle('Hard LVL')
        self.button_1 = QPushButton(self)
        self.button_1.move(90, 40)
        self.button_1.setText("Start")
        self.button_1.clicked.connect(self.run3)
        self.show()  
        
    def run3(self):
        self.work = Start3()
        self.work.show()
        self.hide()           



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Work()
    ex.show()
    sys.exit(app.exec())
