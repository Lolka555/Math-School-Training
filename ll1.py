# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit
from random import randint
from ll2 import Work
import sqlite3

class Start2(QWidget):
    
    def var(self):
        self.variant = '+'
        self.firstchis = randint(100, 3000)
        self.secondchis = randint(1000, 2000)
        self.text = [str(self.firstchis), '+', str(self.secondchis)]
        return self.text, int(self.secondchis), int(self.firstchis)

    def __init__(self):
        super().__init__()

        self.setGeometry(300, 300, 270, 150)
        self.setWindowTitle('Do:')

        self.spis = self.var()
        self.text = ' '.join(self.spis[0])
        self.label = QLabel(self)
        self.label.setText(self.text)
        self.label.move(120, 25)

        self.btn = QPushButton('Answer', self)
        self.btn.move(100, 70)
        self.btn.clicked.connect(self.schet)
        
        self.name_input = QLineEdit(self)
        self.name_input.move(90, 45)        

        my_file = open('Last.txt', 'r')
        self.lastname = my_file.read()
        my_file.close()
        
        self.base = sqlite3.connect("base.db")
        self.cur = self.base.cursor()         

    def schet(self):
        self.name = self.name_input.text()
        if self.name.isdigit() is True:
            if int(self.name) == self.spis[2] + self.spis[1]:
                self.cur.execute('UPDATE core SET Score1 == ? WHERE Name == ?', (1, self.lastname))               
            else:
                self.cur.execute('UPDATE core SET Score1 == ? WHERE Name == ?', (0, self.lastname))
        else:
            self.cur.execute('UPDATE core SET Score1 == ? WHERE Name == ?', (0, self.lastname))
        self.base.commit()
        self.cur.close()
        self.base.close()             
        self.ex = Work()
        self.ex.show()
        self.hide()                   
                
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Work()
    ex.show()
    sys.exit(app.exec())
