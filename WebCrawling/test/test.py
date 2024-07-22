import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

class insert_page(QtWidgets.QMainWindow): 
    def __init__(self):
        super(insert_page, self).__init__()
        insert_file_path = os.path.join(os.path.dirname(__file__), 'test.ui')
        loadUi(insert_file_path, self)
        
        self.plot([1,2,3,4,5,6,7,8,9,10],[30,32,34,32,35,31,15,32,34,36])

    def plot(self, x, y):
        self.graphWidget.plot(x,y)


def window():
    # 현재 파일의 경로로 작업 디렉토리를 변경
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    app = QApplication(sys.argv)
    login_window = insert_page()
    login_window.show()

    sys.exit(app.exec_())
window()