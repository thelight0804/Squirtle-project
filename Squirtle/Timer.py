#타이머 기능
from PyQt5.QtWidgets import *
from GUI import TimerGUI
import sys
import time
import threading #threading 모듈
import math

RunTimer = False #타이머 객체 실행 여부
CreateTimer = False #타이머 객체 생성 여부

class Timer:
    _Sec = 0
    _Hour = 0
    _Min = 0

    def __init__(self, Hour, Min, Sec, Percent):
        Timer._Hour = Hour #시간
        Timer._Min = Min #분
        Timer._Sec = Sec
        self.__Percent = Percent #__ = private #타이머 진행률
    
    def __del__(self): #소멸자
        pass
    
    @property
    def _Hour(self):
        return Timer._Hour

    @property
    def _Min(self):
        return Timer._Min

    @property
    def _Sec(self):
        return Timer._Sec

    @property
    def Percent(self):
        return self.__Percent

    @_Hour.setter
    def _Hour(self, Hour):
        if type(Hour) is not int:
            raise ValueError("Invalid Hour")
        Timer._Hour = Hour

    @_Min.setter
    def _Min(self, Min):
        if type(Min) is not int:
            raise ValueError("Invalid Min")
        Timer._Min = Min

    @_Sec.setter
    def _Sec(self, Sec):
        if type(Sec) is not int:
            raise ValueError("Invalid Sec")
        Timer._Sec = Sec

    def CountDown(self): #카운트 다운
        global RunTimer
        global CreateTimer
        RunTimer = True

        if CreateTimer == False:
            Timer._Sec = (Timer._Hour*3600)+(Timer._Min*60) #모두 초로 더한 다음에 초에서 시, 분으로 분배
            CreateTimer = True

        while Timer._Sec > 0:
            if RunTimer == False:
                PauseTimer(self) #일시정지
                break #while문을 빠저 나가면 소멸자가 실행된다
            time.sleep(0.01)
            Timer._Sec += -1
            TimeUpdate()


def StartTimer(hour, min):
    global RunTimer #global : 전역변수인 RunTimer을 사용한다고 선언
    global CreateTimer
    if CreateTimer == True:
        timer = Timer(Timer._Hour, Timer._Min, Timer._Sec, 0.0)
        thr1 = threading.Thread(target=timer.CountDown).start()
    else:
        timer = Timer(hour, min, min*60, 0.0)
        thr1 = threading.Thread(target=timer.CountDown).start()


def PauseTimer(self): #일시정지
    TimeUpdate()

def TimeUpdate(): #타이머 데이터를 GUI에 반영
    Timer._Hour = int(Timer._Sec/3600)
    Timer._Min = int(Timer._Sec/60)
    gui.HLabel.setText(str(Timer._Hour))
    gui.MLabel.setText(str(Timer._Min%60))
    gui.SLabel.setText(str(Timer._Sec%60))
    gui.HLabel.update()
    gui.MLabel.update()
    gui.SLabel.update()


#TimerGUI 연결
app = QApplication(sys.argv)
gui = TimerGUI.TimerGUI()
app.exec()

#TODO: 타이머 종료 시 윈도우 알람까지 가즈아ㅏㅏ!!