import sys
from diff import Diff
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):      
        self.setGeometry(300, 200, 300, 180)
        self.setWindowTitle('VArifmetika')
        
        
        self.label = QLabel(self)
        self.label.setText("Welcom to VA")
        self.label.move(40, 30)

        self.name_label = QLabel(self)
        self.name_label.setText("Your name:")
        self.name_label.move(40, 60)

        self.name_input = QLineEdit(self)
        self.name_input.move(110, 60)
        self.name = self.name_input.text()    

        self.btn = QPushButton('Enter', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(100, 90)
        self.btn.clicked.connect(self.hello)

           

    def hello(self):        
        self.name = self.name_input.text()
        my_file = open("Last.txt", "w+")
        my_file.write(self.name)
        my_file.close()        
        base = sqlite3.connect("base.db")
        cur = base.cursor()  
        base.execute('CREATE TABLE IF NOT EXISTS {}(Name TEXT, LVL INT, Score1 INT, Score2 INT, Score3 INT, Score4 INT)'.format('core'))
        cur.execute('INSERT INTO core VALUES(?, ?, ?, ?, ?, ?)', (self.name, 0, 0, 0, 0, 0))
        base.commit()
        cur.close()
        base.close()         
        
        self.ex = Diff()
        self.ex.show()
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
