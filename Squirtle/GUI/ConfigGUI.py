import Timer, Main
import FileModule

from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui
from PyQt5.QtGui import QIcon


#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
if(Main.data.Language == 0):
    form_class = uic.loadUiType(r"GUI\\ConfigGUI_KR.ui")[0]
elif(Main.data.Language == 1):
    form_class = uic.loadUiType(r"GUI\\ConfigGUI_EN.ui")[0]
else:
    form_class = uic.loadUiType(r"GUI\\ConfigGUI_JP.ui")[0]


#화면을 띄우는데 사용되는 Class 선언
class ConfigGUI(QDialog, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self) #.ui를 연결 시켜준다
        self.setWindowTitle('Config')
        self.setWindowIcon(QIcon('..\Resource\icon\config.png'))
        self.show()

        #버튼 이벤트
        self.InfoBTN.clicked.connect(self.InfoClicked) #정보
        self.OKBTN.clicked.connect(self.OKClicked) #확인
        self.CancelBTN.clicked.connect(self.CancelClicked) #취소

        #comboBox 설정
        self.HcomboBox.setFixedSize(80,50)
        self.McomboBox.setFixedSize(80,50)
        for i in range(0, 13): #Hour 시간 추가
            if i<10: #1의 자리 '0' 추가
                self.HcomboBox.addItem('0'+str(i))
            else:
                self.HcomboBox.addItem(str(i))
        for i in range(0, 12): #Min 시간 추가
            if i<2:
                self.McomboBox.addItem('0'+str(i*5))
            else:
                self.McomboBox.addItem(str(i*5))
        
        ##초기 값으로 설정
        self.HcomboBox.setCurrentIndex(int(Main.data.Sec/3600))
        self.McomboBox.setCurrentIndex(int(Main.data.Sec/60%60/5))

        #lineEdit 설정
        self.OnlyInt = QtGui.QIntValidator()
        self.TermlineEdit.setValidator(self.OnlyInt) #int 값만 받기
        self.TermlineEdit.setFixedSize(80,50)

        ##기존 값 반영
        self.TermlineEdit.setText(str(int(Main.data.Term/60))) #Main.data.Sec() 오류!
        self.NamelineEdit.setText(Main.data.Name)
        self.ContentlineEdit.setText(Main.data.Content)
        self.AutoStartcheckBox.setChecked(Main.data.AutoStart)
        self.LangcomboBox.setCurrentIndex(Main.data.Language)
        self.SaveObject()

    #정보 버튼 클릭 시
    def InfoClicked(self): 
        """
        1. 기본 String 변수를 선언해 준다
        2. 각 언어마다 변수의 값을 다르게 지정한다
        3. 저장된 변수를 출력한다
        """
        Title = '프로그램 정보'
        Description = "개발자 : 박상현(thelight0804) \n프로그램 버전 : 1.0\nSpecial Thanks : ING'S(Nifskor)"

        if(Main.data.Language == 0):
            Title = '프로그램 정보'
            Description = "개발자 : 박상현(thelight0804)\n프로그램 버전 : 1.0\nSpecial Thanks : ING'S(Nifskor)"
        elif(Main.data.Language == 1):
            Title = 'Program Information'
            Description = "Developer : thelight0804\nProgram version : 1.0\nSpecial Thanks : ING'S(Nifskor)"
        else:
            Title = 'プログラム情報'
            Description = "プログラマー : thelight0804\nプログラム version : 1.0\nSpecial Thanks : ING'S(Nifskor)"
        QMessageBox.about(self, Title, Description)

    #확인 버튼 클릭 시
    def OKClicked(self): 
        TimerError = '시간을 설정해 주세요'
        Title = '경고'
        Description = '저장하시겠습니까?\n(언어 변경은 재시작해 주세요)'
        
        #언어 선택 별 언어 변경
        if(self.LangcomboBox.currentIndex() == 0):
            Title = '경고'
            Description = '저장하시겠습니까?\n(언어 변경은 재시작해 주세요)'
        elif(self.LangcomboBox.currentIndex() == 1):
            Title = 'Warning'
            Description = 'Are you sure you want to save?\n(Please restart the language changePlease restart the language change)'
        else:
            Title = '注意'
            Description = 'セーブしますか?\n(言語変更はリスタートしてください)'

        if(Main.data.Language == 0):
            TimerError = '시간을 설정해 주세요'
        elif(Main.data.Language == 1):
            TimerError = 'Please set the time'
        else:
            TimerError = '時間を設定してください'

        if int(self.HcomboBox.currentText()) == 0 and int(self.McomboBox.currentText()) == 0: # 0:0에서 타이머 시작 방지
            QMessageBox.about(self, 'Error', TimerError)
        else:
            result = QMessageBox.question(self, Title, Description)
            if result == QMessageBox.Yes: #Yes를 누를 시
                self.SaveObject()
                Timer.ResetTimer()
                self.close() #현재 Dialog 닫기
            else: pass
            
    #취소 버튼 클릭 시
    def CancelClicked(self): 
        self.close()

    #입력 값 저장
    def SaveObject(self): 
        Main.data.Sec = (int(self.HcomboBox.currentText())*3600)+(int(self.McomboBox.currentText())*60)
        Main.data.Term = int(self.TermlineEdit.text())*60 #lineEdit의 text 반환
        Main.data.Name = self.NamelineEdit.text()
        Main.data.Content = self.ContentlineEdit.text()
        if self.AutoStartcheckBox.isChecked() : Main.data.AutoStart = True
        else : Main.data.AutoStart = False
        Main.data.Language = self.LangcomboBox.currentIndex()

        #파일에 저장
        SaveFile = FileModule.SerializationData(Main.data.Sec, Main.data.Term, Main.data.Name, Main.data.Content, Main.data.AutoStart, Main.data.Language)
        FileModule.SaveData(SaveFile)
