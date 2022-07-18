#알람 기능
import Main
from win10toast import ToastNotifier #Windows 10 알림(Toast)
#pip install win10toast 로 설치해야 사용 가능


class alarm:
    def __init__(self, AgainHour, AgainMin):
        self.__AgainHour = AgainHour
        self.__AgainMin = AgainMin

    #Windows 10 알람
    def call(self): 
        toast = ToastNotifier() #win10toast의 ToastNotifier 객체 생성
        toast.show_toast(title=Main.data.Name, msg=Main.data.Content, icon_path="Resource\Squirtle.ico")

    @property
    def AgainHour(self):
        return self.__AgainHour

    @AgainHour.setter
    def AgainHour(self, AgainHour):
        if type(AgainHour) is not int:
            raise ValueError("Invalid AgainHour")
        self.__AgainHour = AgainHour
    
    @property
    def AgainMin(self):
        return self.__AgainMin

    @AgainMin.setter
    def AgainMin(self, AgainMin):
        if type(AgainMin) is not int:
            raise ValueError("Invalid AgainMin")
        self.__AgainMin = AgainMin
