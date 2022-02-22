#타이머 기능
from PyQt5.QtWidgets import *
from GUI import TimerGUI
import sys
import time
import threading #threading 모듈
import math

CreateTimer = False #타이머 객체 생성 여부

class Timer:
    def __init__(self, NowRunning, NowPause, Hour, Min, Sec, Percent):
        self._NowRunning = NowRunning # _ = protected # 타이머 진행 상태를 확인
        self._NowPause = NowPause # 일시정지 상태를 확인
        self._Hour = Hour #시간
        self._Min = Min #분
        self._Sec = Sec
        self.__Percent = Percent #__ = private #타이머 진행률
    
    def __del__(self): #소멸자
        print("소멸자 실행!")
    
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
        #모두 초로 더한 다음에 초에서 시, 분으로 분배
        self._Sec = (self._Hour*3600)+(self._Min*60)
        while self._Sec > 0:
            time.sleep(0.01)
            self._Sec += -1
            self._Hour = int(self._Sec/3600)
            self._Min = int(self._Sec/60)
            gui.HLabel.setText(str(self._Hour))
            gui.MLabel.setText(str(self._Min))
            gui.SLabel.setText(str(self._Sec))
            print(self._Hour, ":", self._Min%60, ":", self._Sec%60)
            #TODO: gui에 반영하기

        self._NowRunning = False
        global CreateTimer
        CreateTimer = False
        del self #timer 소멸 #del timer 에러!
        # gui.Hcombo.show()
        # gui.MCombo.show()
        # gui.HLabel.hide()
        # gui.MLabel.hide()


def StartTimer(hour, min):
    global CreateTimer #global : 전역변수인 CreateTimer을 사용한다고 선언
    CreateTimer = True
    timer = Timer(True, False, hour, min, min*60, 0.0)
    thr1 = threading.Thread(target=timer.CountDown).start()

#TimerGUI 연결
app = QApplication(sys.argv)
gui = TimerGUI.TimerGUI()
app.exec()