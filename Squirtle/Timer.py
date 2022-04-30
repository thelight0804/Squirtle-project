#타이머 기능

from PyQt5.QtWidgets import *
from GUI import TimerGUI
import sys
import time, threading #threading 모듈
import Data, Alarm, FileModule
#로컬 Data 파일 열기
try:
    f = open('SaveData.json', 'r')
except FileNotFoundError: #파일이 없을 시
    data = Data.Data(3600, 60, "Squirtle", "스트레칭을 해주세요", False, 0) #Data 객체 생성
    SaveFile = FileModule.SerializationData(data.Sec, data.Term, data.Name, data.Content, data.AutoStart, data.Language)
    FileModule.SaveData(SaveFile)
else: #파일이 있을 시
    LoadFile = FileModule.LoadData()
    data = Data.Data(LoadFile[0], LoadFile[1], LoadFile[2], LoadFile[3], LoadFile[4], LoadFile[5])


PauseTimer = False #타이머 객체 실행 여부
Break = False #휴식 타이머
TimerSec = data.Sec #일시정지 했을 시 사용할 Sec

class Timer:
    def __init__(self, Sec):
        self.__Sec = Sec #초
    
    def __del__(self): #소멸자
        #print("소멸자 실행")
        pass

    @property
    def Sec(self):
        return self.__Sec

    @Sec.setter
    def Sec(self, Sec):
        if type(Sec) is not int:
            raise ValueError("Invalid Sec")
        self.__Sec = Sec

    def CountDown(self): #카운트 다운
        global TimerSec
        global Break
        ChangeColor(Break)
        self.TimeUpdate()
        while self.Sec > 0:
            time.sleep(1) #TODO 시간 조정
            if PauseTimer == False: #일시정지
                TimerSec = self.Sec
                self.TimeUpdate()
                break #while문을 빠져 나가면 소멸자가 실행된다
            self.Sec += -1
            self.TimeUpdate()
            if self.Sec == 0 and Break == False: #타이머가 끝난 경우
                CallAlram() #윈도우10 Toast 알람
                Break = True
                ChangeColor(Break)
                self.Sec = data.Term
            elif self.Sec == 0 and Break == True: #휴식 타이머가 끝난 경우
                Break = False
                ChangeColor(Break)
                self.Sec = data.Sec

    def TimeUpdate(self): #타이머 데이터를 GUI에 반영
        gui.HLabel.setText(str(int(self.Sec/3600)).zfill(2)) #.zfill : 원하는 개수만큼 '0' 채우기
        gui.MLabel.setText(str(int(self.Sec/60%60)).zfill(2))
        gui.SLabel.setText(str(self.Sec%60).zfill(2))
        gui.HLabel.update()
        gui.MLabel.update()
        gui.SLabel.update()

def ChangeColor(Break):
    if Break == True:
        gui.HLabel.setStyleSheet("QLabel {color: #3d9454;}")
        gui.MLabel.setStyleSheet("QLabel {color: #3d9454;}")
        gui.SLabel.setStyleSheet("QLabel {color: #3d9454;}")
        gui.LMarkLabel.setStyleSheet("QLabel {color: #3d9454;}")
        gui.RMarkLabel.setStyleSheet("QLabel {color: #3d9454;}")
    else:
        gui.HLabel.setStyleSheet("QLabel {color: #f9c684;}")
        gui.MLabel.setStyleSheet("QLabel {color: #f9c684;}")
        gui.SLabel.setStyleSheet("QLabel {color: #f9c684;}")
        gui.LMarkLabel.setStyleSheet("QLabel {color: #f9c684;}")
        gui.RMarkLabel.setStyleSheet("QLabel {color: #f9c684;}")


def StartTimer(): #Timer 생성
    global PauseTimer #global : 전역변수인 RunTimer을 사용한다고 선언
    if PauseTimer == True:
        timer = Timer(TimerSec)
    else:
        timer = Timer(data.Sec)
    threading.Thread(target=timer.CountDown).start()

def ResetTimer(): #초기화
    global TimerSec
    global Break
    global PauseTimer

    PauseTimer = False
    Break = False
    TimerSec = data.Sec

    ChangeColor(Break)

    #기본 값으로 돌아가기
    gui.HLabel.setText(str(int(data.Sec/3600)).zfill(2))
    gui.MLabel.setText(str(int(data.Sec/60%60)).zfill(2))
    gui.SLabel.setText(str(data.Sec%60).zfill(2))
    gui.HLabel.update()
    gui.MLabel.update()
    gui.SLabel.update()

def CallAlram():#알람 객체 생성
    alarm = Alarm.alarm(0, 0)
    alarm.call()

#TimerGUI 연결
app = QApplication(sys.argv)
gui = TimerGUI.TimerGUI()

if data.AutoStart == True: #자동 실행 체크 시
    gui.StartBtnCliked()
app.exec() #app이 끝날 때 까지 loop로 돌린다