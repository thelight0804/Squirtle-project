#타이머 기능

from PyQt5.QtWidgets import *
from GUI import TimerGUI
import sys
import time
import Data, Alarm
import threading #threading 모듈

RunTimer = False #타이머 객체 실행 여부
CreateTimer = False #타이머 객체 생성 여부
data = Data.Data()
class Timer:
    def __init__(self, Sec, Break):
        self.__Sec = Sec #초
        self.__Break = Break #타이머가 끝났는지 확인
    
    def __del__(self): #소멸자
        pass

    @property
    def Sec(self):
        return self.__Sec

    @Sec.setter
    def Sec(self, Sec):
        if type(Sec) is not int:
            raise ValueError("Invalid Sec")
        self.__Sec = Sec

    @property
    def Break(self):
        return self.__Break

    @Break.setter
    def Break(self, Break):
        if type(Break) is not bool:
            raise ValueError("Invalid Break")
        self.__Break = Break

    def CountDown(self): #카운트 다운
        global RunTimer
        global CreateTimer
        RunTimer = True

        if CreateTimer == False:
            CreateTimer = True
        self.TimeUpdate()

        while self.Sec > 0:
            if RunTimer == False:
                self.PauseTimer() #일시정지
                break #while문을 빠져 나가면 소멸자가 실행된다
            time.sleep(0.01) #TODO 시간 조정
            self.Sec += -1
            self.TimeUpdate()
            if self.Sec == 0 and self.Break == False: #타이머가 끝난 경우
                CallAlram() #윈도우10 Toast 알람
                CallBreakTimer()
            elif self.Sec == 0 and self.Break == True: #휴식 타이머가 끝난 경우
                self.Break = False
                self.Sec = data.Sec

    def PauseTimer(self): #일시정지
        self.TimeUpdate()

    def TimeUpdate(self): #타이머 데이터를 GUI에 반영
        gui.HLabel.setText(str(int(self.Sec/3600)).zfill(2)) #.zfill : 원하는 개수만큼 '0' 채우기
        gui.MLabel.setText(str(int(self.Sec/60%60)).zfill(2))
        gui.SLabel.setText(str(self.Sec%60).zfill(2))
        gui.HLabel.update()
        gui.MLabel.update()
        gui.SLabel.update()

def StartTimer(): #Timer 생성
    global RunTimer #global : 전역변수인 RunTimer을 사용한다고 선언
    global CreateTimer
    if CreateTimer == True:
        timer = Timer(data.Sec, False)
        thr = threading.Thread(target=timer.CountDown).start()
    else:
        timer = Timer(data.Sec, False)
        thr = threading.Thread(target=timer.CountDown).start()

def ResetTimer(): #초기화
    global RunTimer
    global CreateTimer
    RunTimer = False
    CreateTimer = False
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

def CallBreakTimer(): #휴식 타이머 객체 생성
    breakTimer = Timer(data.Term, True)
    breakTimer.CountDown()

#TimerGUI 연결
app = QApplication(sys.argv)
gui = TimerGUI.TimerGUI()
app.exec() #app이 끝날 때 까지 loop로 돌린다