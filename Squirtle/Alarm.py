#알람 기능

from win10toast import ToastNotifier #Windows 10 알림(Toast)
#pip install win10toast 로 설치해야 사용 가능


class alarm:
    def __init__(self, AgainHour, AgainMin):
        self.__AgainHour = AgainHour
        self.__AgainMin = AgainMin
    
    def call(self): #Windows 10 알람
        toaster = ToastNotifier() #win10toast의 ToastNotifier 객체 생성
        toaster.show_toast(title="1시간이 지났습니다", msg="스트레칭을 해주세요", icon_path="..\Assets\icon\Squirtle.ico", duration=10)

    #property & setter
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
