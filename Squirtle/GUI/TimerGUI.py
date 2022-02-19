# cmd에서 pip3 install PyQt5 명령어를 이용하여 PyQt5를 설치해야 한다
#박스 레이아웃 사용 (https://wikidocs.net/21945 참조)

import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtCore import *

class TimerGUI(QWidget): #클래스
    def __init__(self): #생성자
        self.Hour = 00
        self.Min = 00

        super().__init__()
        self.setWindowTitle('Squirtle') #프로그램 이름
        font = QFont('나눔고딕', 15) #폰트 설정
        self.setFont(font)
        self.resize(1080, 720) #창 사이즈
        self.init_UI()

    def init_UI(self):
        ##버튼 구현
        #환경설정 버튼
        ConfigBtn = QPushButton('', self) #ConfigBtn 버튼 구현
        ConfigBtn.setIcon(QtGui.QIcon('..\Assets\icon\config.svg')) #아이콘 구현 (상대경로)
        ConfigBtn.setIconSize(QtCore.QSize(50,50)) #아이콘 크기
        ConfigBtn.setFlat(True) #버튼 테두리 없애기
        ConfigBtn.clicked.connect(self.ConfigBtnClicked) #버튼 클릭 했을 때 ConfigBtn_clicked 함수 호출

        #Reset 버튼
        ResetBtn = QPushButton('', self)
        ResetBtn.setIcon(QtGui.QIcon('..\Assets\icon\\reset.svg')) #\r은 옵션이라 \\r를 사용하였다
        ResetBtn.setIconSize(QtCore.QSize(50,50))
        ResetBtn.setFlat(True)

        #타이머 변경 버튼
        ChangeBtn = QPushButton('사용자\n타이머', self)
        ChangeBtn.setIconSize(QtCore.QSize(50,50))

        #Start 버튼
        StartBtn = QPushButton('', self)
        StartBtn.setIcon(QtGui.QIcon('..\Assets\icon\start.svg'))
        StartBtn.setIconSize(QtCore.QSize(50,50))
        StartBtn.setFlat(True)
        StartBtn.clicked.connect(self.StartBtnCliked)

        ##ComboBox 구현
        self.Hcombo = QComboBox(self) #시
        self.MCombo = QComboBox(self) #분
        for i in range(0, 13): #Hour 시간 추가
            if i<10: #1의 자리 '0' 추가
                self.Hcombo.addItem('0'+str(i))
            else:
                self.Hcombo.addItem(str(i))
        for i in range(0, 12): #Min 시간 추가
            if i<2:
                self.MCombo.addItem('0'+str(i*5))
            else:
                self.MCombo.addItem(str(i*5))

        ##QLable 구현
        label = QLabel(':', self)
        label.setAlignment(Qt.AlignCenter)

        ##상태바 구현
        self.TimerBar = QProgressBar() #TODO: 원형 바 어떻게 해야 할까..ㅠ
        self.timer = QTimer()
        self.step = 0

        ##Box 레이아웃
        #수평
        hboxUp = QHBoxLayout() #수평 box 생성
        hboxUp.addWidget(ConfigBtn) #ConfigBtn 버튼 생성
        hboxUp.addStretch(1) #비율이 1인 빈 공간 생성
        
        hboxMid = QHBoxLayout() #ComboBox 레이아웃
        hboxMid.setContentsMargins(450, 0, 450, 0) #Left, Up, Right, Down
        hboxMid.addWidget(self.Hcombo)
        hboxMid.addWidget(label)
        hboxMid.addWidget(self.MCombo)
        hboxMid.addWidget(self.TimerBar)

        hboxDown = QHBoxLayout() #초기와, 타이머변경, 시작 레이아웃
        hboxDown.addStretch(10)
        hboxDown.addWidget(ResetBtn)
        hboxDown.addStretch(1)
        hboxDown.addWidget(ChangeBtn)
        hboxDown.addStretch(1)
        hboxDown.addWidget(StartBtn)
        hboxDown.addStretch(10)
        
        #수직
        vbox = QVBoxLayout() #수직 box 생성
        vbox.addLayout(hboxUp)
        vbox.addStretch(10)
        vbox.addLayout(hboxMid)
        vbox.addStretch(10)        
        vbox.addLayout(hboxDown)
        vbox.setContentsMargins(0, 0, 0, 50)

        self.setLayout(vbox) #수직 box를 메인 레이아웃으로 설정

        ##창 출력
        self.center() #창을 화면 중앙으로
        self.show() #창 출력

    def ConfigBtnClicked(self): #Config 버튼 클릭
        self.Hour = self.Hcombo.currentText()
        self.Min = self.MCombo.currentText()
        QMessageBox.about(self, 'hour', self.Hour+" : "+self.Min)

    def StartBtnCliked(self): #Start 버튼 클릭
        self.Hour = self.Hcombo.currentText()
        self.Min = self.MCombo.currentText()
        QMessageBox.about(self, 'hour', self.Hour+" : "+self.Min)
        
    def timerEvent(self, e): #타이머 이벤트
        if self.step >= 100:
            self.timer.stop()
            self.TimerBar.setValue(0)
            return

        self.step = self.step + 1
        self.TimerBar.setValue(self.step)
        
    def center(self): #창의 화면을 중앙으로
        qr = self.frameGeometry() #창의 위치와 크기 정보를 가져온다
        cp = QDesktopWidget().availableGeometry().center() #현재 모니터의 위치를 파악한다
        qr.moveCenter(cp) #창을 cp로 이동한다
        self.move(qr.topLeft())