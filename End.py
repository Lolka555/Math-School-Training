import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel
from os import remove
import sqlite3


class End1(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        my_file = open('Last.txt', 'r')
        lastname = my_file.read()
        my_file.close()
        
        base = sqlite3.connect("base.db")
        cur = base.cursor()         
        score1 = cur.execute('SELECT Score1 FROM core WHERE Name == ?', (lastname,)).fetchone()
        score2 = cur.execute('SELECT Score2 FROM core WHERE Name == ?', (lastname,)).fetchone()
        score3 = cur.execute('SELECT Score3 FROM core WHERE Name == ?', (lastname,)).fetchone()
        score4 = cur.execute('SELECT Score4 FROM core WHERE Name == ?', (lastname,)).fetchone()
        score = int(score1[0]) + int(score2[0]) + int(score3[0]) + int(score4[0])
        
        self.name_label = QLabel(self)
        self.name_label.setText('{}/4'.format(score))
        self.name_label.move(120, 20)
        
        self.setGeometry(300, 300, 250, 100)
        self.setWindowTitle('Easy LVL: Result')
        self.button_1 = QPushButton(self)
        self.button_1.move(100, 40)
        self.button_1.setText("Ok")
        self.button_1.clicked.connect(self.run1)
        self.show()

    def run1(self):
        exit()
        remove('Last.txt')



class End2(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        my_file = open('Last.txt', 'r')
        lastname = my_file.read()
        my_file.close()
        
        base = sqlite3.connect("base.db")
        cur = base.cursor()         
        score1 = cur.execute('SELECT Score1 FROM core WHERE Name == ?', (lastname,)).fetchone()
        score2 = cur.execute('SELECT Score2 FROM core WHERE Name == ?', (lastname,)).fetchone()
        score3 = cur.execute('SELECT Score3 FROM core WHERE Name == ?', (lastname,)).fetchone()
        score4 = cur.execute('SELECT Score4 FROM core WHERE Name == ?', (lastname,)).fetchone()
        score = int(score1[0]) + int(score2[0]) + int(score3[0]) + int(score4[0])        
        
        self.name_label = QLabel(self)
        self.name_label.setText('{}/4'.format(score))
        self.name_label.move(120, 20)
        
        self.setGeometry(300, 300, 250, 100)
        self.setWindowTitle('Medium LVL: Result')
        self.button_1 = QPushButton(self)
        self.button_1.move(100, 40)
        self.button_1.setText("Ok")
        self.button_1.clicked.connect(self.run2)            
        self.show()

    def run2(self):
        exit()
        remove('Last.txt')


class End3(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        my_file = open('Last.txt', 'r')
        lastname = my_file.read()
        my_file.close()
        
        base = sqlite3.connect("base.db")
        cur = base.cursor()         
        score1 = cur.execute('SELECT Score1 FROM core WHERE Name == ?', (lastname,)).fetchone()
        score2 = cur.execute('SELECT Score2 FROM core WHERE Name == ?', (lastname,)).fetchone()
        score3 = cur.execute('SELECT Score3 FROM core WHERE Name == ?', (lastname,)).fetchone()
        score4 = cur.execute('SELECT Score4 FROM core WHERE Name == ?', (lastname,)).fetchone()
        score = int(score1[0]) + int(score2[0]) + int(score3[0]) + int(score4[0])        
        
        self.name_label = QLabel(self)
        self.name_label.setText('{}/4'.format(score))
        self.name_label.move(120, 20)
        
        self.setGeometry(300, 300, 250, 100)
        self.setWindowTitle('Hard LVL: Result')
        self.button_1 = QPushButton(self)
        self.button_1.move(100, 40)
        self.button_1.setText("Ok")
        self.button_1.clicked.connect(self.run3)
        self.show()  

    def run3(self):
        exit()
        remove('Last.txt')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Work()
    ex.show()
    sys.exit(app.exec())