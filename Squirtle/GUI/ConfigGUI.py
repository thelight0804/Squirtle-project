import sys
from PyQt5.QtWidgets import *

class ConfigGUI(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Config')
        self.setGeometry(100, 100, 200, 100)
        self.show()
#TODO Dialog가 자동으로 꺼지는 거 수정
if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())