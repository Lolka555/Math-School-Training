import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel
from galera import Work, Work1, Work2
import sqlite3

class Diff(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 100)
        self.setWindowTitle('Difficult')

        self.button_1 = QPushButton(self)
        self.button_1.move(90, 10)
        self.button_1.setText("Easy")
        self.button_1.clicked.connect(self.run)

        self.button_2 = QPushButton(self)
        self.button_2.move(90, 40)
        self.button_2.setText("Medium")
        self.button_2.clicked.connect(self.run2)

        self.button_3 = QPushButton(self)
        self.button_3.move(90, 70)
        self.button_3.setText("Hard")
        self.button_3.clicked.connect(self.run3)
        
        my_file = open('Last.txt', 'r')
        self.lastname = my_file.read()
        my_file.close()
        
        self.base = sqlite3.connect("base.db")
        self.cur = self.base.cursor()        

        self.show()

    def run(self):
        self.cur.execute('UPDATE core SET LVL == ? WHERE Name == ?', (1, self.lastname))
        self.base.commit()
        self.cur.close()
        self.base.close()          
        self.work = Work()
        self.work.show()
        self.hide()
        
    def run2(self):  
        self.cur.execute('UPDATE core SET LVL == ? WHERE Name == ?', (2, self.lastname))
        self.base.commit()
        self.cur.close()
        self.base.close()          
        self.work = Work1()
        self.work.show()
        self.hide()

    def run3(self):    
        self.cur.execute('UPDATE core SET LVL == ? WHERE Name == ?', (3, self.lastname))
        self.base.commit()
        self.cur.close()
        self.base.close()          
        self.work = Work2()
        self.work.show()
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Diff()
    ex.show()
    sys.exit(app.exec())


