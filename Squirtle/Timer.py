#타이머 기능
from PyQt5.QtWidgets import *
from GUI import TimerGUI
import sys

class Timer:
    def __init__(self, NowRunning, NowPause, Hour, Min, Percent):
        self._NowRunning = NowRunning # _ = protected # 타이머 진행 상태를 확인
        self._NowPause = NowPause # 일시정지 상태를 확인
        self._Hour = Hour #시간
        self._Min = Min #분
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
    def Percent(self):
        return self.__Percent
    
    @NowRunning.setter #setter
    def NowRunning(self, NowRunning):
        if type(NowRunning) is not bool: #bool 형식이 아닐 시
            raise ValueError("Invalid NowRunning")
        self._NowRunning = NowRunning

    @Hour.setter #setter
    def Hour(self, Hour):
        if type(Hour) is not int:
            raise ValueError("Invalid Hour")
        self._Hour = Hour

timer = Timer(False, False, 0, 0, 0.0)

#TimerGUI 연결
app = QApplication(sys.argv)
gui = TimerGUI.TimerGUI()
app.exec()

#gui.Hour의 값 가져오기
#하 됐다ㅠㅠㅠㅠ
timer.Hour = int(gui.Hour)
print(timer.Hour)