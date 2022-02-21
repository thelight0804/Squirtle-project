#타이머 기능
from PyQt5.QtWidgets import *
from GUI import TimerGUI
import sys
import time
import threading #threading 모듈

global CreateTimer
CreateTimer = False #타이머 객체 생성 여부
print(id(CreateTimer))

class Timer:
    def __init__(self, NowRunning, NowPause, Hour, Min, Sec, Percent):
        self._NowRunning = NowRunning # _ = protected # 타이머 진행 상태를 확인
        self._NowPause = NowPause # 일시정지 상태를 확인
        self._Hour = Hour #시간
        self._Min = Min #분
        self._Sec = Sec
        self.__Percent = Percent #__ = private #타이머 진행률
    
    @property #getter
    def NowRunning(self):
        return self._NowRunning

    @property
    def NowPause(self):
        return self._NowPause

    @property
    def Hour(self):
        return self._Hour

    @property
    def Min(self):
        return self._Min

    @property
    def Sec(self):
        return self._Sec

    @property
    def Percent(self):
        return self.__Percent
    
    @NowRunning.setter #setter
    def NowRunning(self, NowRunning):
        if type(NowRunning) is not bool: #bool 형식이 아닐 시
            raise ValueError("Invalid NowRunning")
        self._NowRunning = NowRunning

    @Hour.setter
    def Hour(self, Hour):
        if type(Hour) is not int:
            raise ValueError("Invalid Hour")
        self._Hour = Hour

    @Min.setter
    def Min(self, Min):
        if type(Min) is not int:
            raise ValueError("Invalid Min")
        self._Min = Min

    @Sec.setter
    def Sec(self, Sec):
        if type(Sec) is not int:
            raise ValueError("Invalid Sec")
        self._Sec = Sec

    def CountDown(self): #카운트 다운
        self._Min += -1
        if self._Hour == 0:
            pass
        else:
            self._Hour += -1
        while self._Hour != 0 or self._Min != 0 or self._Sec != 0:
            time.sleep(0.01)
            if self._Sec != 0:
                self._Sec += -1
                if self._Sec % 60 == 0 and self._Min > 0:
                    self._Min += -1
            if self._Min == 0 and self._Hour >0:
                self._Hour += -1
            print(self._Hour, ":", self._Min, ":", self._Sec)
        if self._Hour == 0 or self._Min == 0 or self._Sec == 0:
            self._NowRunning = False

def StartTimer(hour, min): #TODO: timer를 하나만 생성하게 제한하기
    CreateTimer = True
    print(id(Timer.CreateTimer))
    timer = Timer(True, False, hour, min, min*60, 0.0)
    thr1 = threading.Thread(target=timer.CountDown).start()

#TimerGUI 연결
app = QApplication(sys.argv)
gui = TimerGUI.TimerGUI()
app.exec()