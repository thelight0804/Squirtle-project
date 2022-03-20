#프로그램에 필요한 Data를 가지고 있는 클래스

class Data:
    #def __init__(self, Sec, Term, Name, Content, Language, OSBoot):
    def __init__(self):
        self.__Sec = 30 #시간 초
        self.__Term = 60  #다음 타이머가 시작되는 텀
        self.__Name = "Squirtle" #알람 이름
        self.__Content = "스트레칭을 해주세요"#알람 설명
        self.__Language = 0 #현재 언어 0=한국어, 1=영어, 2=일본어
        self.__OSBoot = False #OS 시작 시 프로그램 실행 여부

    def DataInfo(self): #현재 Data 값 출력
        print("Sec = ", self.Sec)
        print("Term = ", self.Term)
        print("Name = ", self.Name)
        print("Content = ", self.Content)
        print("Language = ", self.Language)
        print("OSBoot = ", self.OSBoot)

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
    def Language(self):
        return self.__Language

    @property
    def OSBoot(self):
        return self.__OSBoot

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

    @Language.setter
    def Language(self, Language):
        if type(Language) is not int:
            raise ValueError("Invalid Language")
        self.__Language = Language

    @OSBoot.setter
    def OSBoot(self, OSBoot):
        if type(OSBoot) is not bool:
            raise ValueError("Invalid OSBoot")
        self.__OSBoot = OSBoot

