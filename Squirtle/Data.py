#프로그램에 필요한 Data를 가지고 있는 클래스

class Data:
    #def __init__(self, Sec, Term, Name, Content, Language, OSBoot):
    def __init__(self, Sec, Term, Name, Content, AutoStart, Language):
        self.__Sec = Sec #시간 초
        self.__Term = Term  #다음 타이머가 시작되는 텀
        self.__Name = Name #알람 이름
        self.__Content = Content#알람 설명
        self.__AutoStart = AutoStart #프로그램 실행 시 타이머 자동 시작
        self.__Language = Language #언어 (0 : 한국어, 1 : 영어, 2 : 일본어)

    def DataInfo(self): #현재 Data 값 출력
        print("Sec = ", self.Sec)
        print("Term = ", self.Term)
        print("Name = ", self.Name)
        print("Content = ", self.Content)
        print("AutoStart = ", self.AutoStart)

    @property
    def Sec(self):
        return self.__Sec

    @property
    def Term(self):
        return self.__Term
    
    @property
    def Name(self):
        return self.__Name

    @property
    def Content(self):
        return self.__Content

    @property
    def AutoStart(self):
        return self.__AutoStart

    @property
    def Language(self):
        return self.__Language

    @Sec.setter
    def Sec(self, Sec):
        if type(Sec) is not int:
            raise ValueError("Invalid Sec")
        self.__Sec = Sec

    @Term.setter
    def Term(self, Term):
        if type(Term) is not int:
            raise ValueError("Invalid Term")
        self.__Term = Term

    @Name.setter
    def Name(self, Name):
        if type(Name) is not str:
            raise ValueError("Invalid Name")
        self.__Name = Name

    @Content.setter
    def Content(self, Content):
        if type(Content) is not str:
            raise ValueError("Invalid Content")
        self.__Content = Content

    @AutoStart.setter
    def AutoStart(self, AutoStart):
        if type(AutoStart) is not bool:
            raise ValueError("Invalid AutoStart")
        self.__AutoStart = AutoStart

    @Language.setter
    def Language(self, Language):
        if type(Language) is not int:
            raise ValueError("Invalid Language")
        self.__Language = Language

