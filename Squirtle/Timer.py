#타이머 기능

from PyQt5.QtWidgets import *
from GUI import TimerGUI
import sys
import time
import Data, Alarm
import threading #threading 모듈

data = Data.Data() #Data 객체 생성
RunTimer = False #타이머 객체 실행 여부
CreateTimer = False #타이머 객체 생성 여부
Break = False #휴식 타이머 여부
TimerSec = data.Sec #일시정지 했을 시 사용할 Sec

class Timer:
    def __init__(self, Sec):
        self.__Sec = Sec #초
    
    def __del__(self): #소멸자
        print("소멸자 실행")

    @property
    def Sec(self):
        return self.__Sec

    @Sec.setter
    def Sec(self, Sec):
        if type(Sec) is not int:
            raise ValueError("Invalid Sec")
        self.__Sec = Sec

    @property
    def thr(self):
        return self.__thr

    @thr.setter
    def thr(self, thr):
        self.__thr = thr

    def CountDown(self): #카운트 다운
        global RunTimer
        global CreateTimer
        global TimerSec
        global Break

        # if CreateTimer == False:
        #     CreateTimer = True
        # else:
        #     self.Sec = TimerSec
        self.TimeUpdate()
        while self.Sec > 0:
            if RunTimer == False: #일시정지
                self.TimeUpdate()
                #StartTimer()
                break #while문을 빠져 나가면 소멸자가 실행된다
            time.sleep(0.1) #TODO 시간 조정
            self.Sec += -1
            #TimerSec += -1
            self.TimeUpdate()
            if self.Sec == 0 and Break == False: #타이머가 끝난 경우
                CallAlram() #윈도우10 Toast 알람
                Break = True
            elif self.Sec == 0 and Break == True: #휴식 타이머가 끝난 경우
                Break = False
        StartTimer()

    def TimeUpdate(self): #타이머 데이터를 GUI에 반영
        gui.HLabel.setText(str(int(self.Sec/3600)).zfill(2)) #.zfill : 원하는 개수만큼 '0' 채우기
        gui.MLabel.setText(str(int(self.Sec/60%60)).zfill(2))
        gui.SLabel.setText(str(self.Sec%60).zfill(2))
        gui.HLabel.update()
        gui.MLabel.update()
        gui.SLabel.update()
    
def PauseTimer(Timer):
    BreakTimer = Timer(Timer.Sec)
    del Timer

def StartTimer(): #Timer 생성
    global RunTimer #global : 전역변수인 RunTimer을 사용한다고 선언
    global CreateTimer
    global Break
    if Break == False:
        timer = Timer(data.Sec)
    else:
        timer = Timer(data.Term)
    threading.Thread(target=timer.CountDown).start()

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

#TimerGUI 연결
app = QApplication(sys.argv)
gui = TimerGUI.TimerGUI()
app.exec() #app이 끝날 때 까지 loop로 돌린다