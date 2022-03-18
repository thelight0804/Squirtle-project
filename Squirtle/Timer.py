#타이머 기능
from PyQt5.QtWidgets import *
from GUI import TimerGUI
import sys
import time, Data
import threading #threading 모듈
import Alarm

RunTimer = False #타이머 객체 실행 여부
CreateTimer = False #타이머 객체 생성 여부
data = Data.Data()

class Timer:
    __Sec = 0

    def __init__(self, Sec):
        self.__Sec = Sec #초
    
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

    def CountDown(self): #카운트 다운
        global RunTimer
        global CreateTimer
        RunTimer = True

        if CreateTimer == False:
            #Timer._Sec = (Timer._Hour*3600)+(Timer._Min*60) #모두 초로 더한 다음에 초에서 시, 분으로 분배
            CreateTimer = True
        TimeUpdate(self)

        while self.Sec > 0:
            if RunTimer == False:
                PauseTimer(self) #일시정지
                break #while문을 빠져 나가면 소멸자가 실행된다
            time.sleep(0.01) #TODO 시간 조정
            self.Sec += -1
            TimeUpdate(self)
            if self.Sec == 0:
                #Timer._Sec = (Timer._Hour*3600)+(Timer._Min*60) #시간 재설정으로 타이머 재시작
                CallAlram() #윈도우10 Toast 알람

def StartTimer(): #Timer 생성
    global RunTimer #global : 전역변수인 RunTimer을 사용한다고 선언
    global CreateTimer
    if CreateTimer == True:
        timer = Timer(data.Sec)
        thr1 = threading.Thread(target=timer.CountDown).start()
    else:
        timer = Timer(data.Sec)
        thr1 = threading.Thread(target=timer.CountDown).start()

def PauseTimer(self): #일시정지
    TimeUpdate(self)

def ResetTimer(self): #초기화
    global RunTimer
    global CreateTimer
    RunTimer = False
    CreateTimer = False
    Timer.Sec = 0
    TimeUpdate(self)
    gui.ShowTimerCombo()

def TimeUpdate(self): #타이머 데이터를 GUI에 반영
    gui.HLabel.setText(str(int(self.Sec/3600)).zfill(2)) #.zfill : 원하는 개수만큼 '0' 채우기
    gui.MLabel.setText(str(int(self.Sec/60%60)).zfill(2))
    gui.SLabel.setText(str(self.Sec%60).zfill(2))
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