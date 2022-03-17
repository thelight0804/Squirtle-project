import sys, Timer
from tkinter.messagebox import YES
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtGui

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("GUI\ConfigGUI.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class ConfigGUI(QDialog, form_class) :

    def __init__(self) :

        super().__init__()
        self.setupUi(self) #.ui를 연결 시켜준다
        self.show()
        #버튼 이벤트
        self.InfoBTN.clicked.connect(self.InfoClicked) #정보
        self.OKBTN.clicked.connect(self.OKClicked) #확인
        self.CancelBTN.clicked.connect(self.CancelClicked) #취소

        #입력 값
        ##TermlineEdit을 int 값만 받게 설정
        self.OnlyInt = QtGui.QIntValidator()
        self.TermlineEdit.setValidator(self.OnlyInt)

        ##기존 값 반영
        #self.TermlineEdit.setText(str(Term))
        self.TermlineEdit.setText(str(Timer.data.Term)) #Timer.data.Sec() 오류!
        self.NamelineEdit.setText(Timer.data.Name)
        self.ContentlineEdit.setText(Timer.data.Content)
        self.LangcomboBox.setCurrentIndex(Timer.data.Language)
        self.BootcheckBox.setChecked(Timer.data.OSBoot)
        self.SaveObject()

    def InfoClicked(self): #정보 버튼 클릭 시
        QMessageBox.about(self, '프로그램 정보', '개발자 : 박상현\n프로그램 버전 : 0.1')
        
    def OKClicked(self): #확인 버튼 클릭 시
        result = QMessageBox.question(self, '경고', '저장하시겠습니까?')
        if result == QMessageBox.Yes: #Yes를 누를 시
            self.SaveObject()
            self.close() #현재 Dialog 닫기
        else: pass
        
    def CancelClicked(self): #취소 버튼 클릭 시
        self.close()

    def SaveObject(self): #입력 값 저장
        Timer.data.Term = int(self.TermlineEdit.text()) #lineEdit의 text 반환
        Timer.data.Name = self.NamelineEdit.text()
        Timer.data.Content = self.ContentlineEdit.text()
        Timer.data.Language = self.LangcomboBox.currentIndex() #comboBox의 index 값
        if self.BootcheckBox.isChecked() : Timer.data.OSBoot = True

# if  __name__ == "__main__" :
#     #QApplication : 프로그램을 실행시켜주는 클래스
#     app = QApplication(sys.argv) 

#     #ConfigGUI의 인스턴스 생성
#     myWindow = ConfigGUI() 

#     #프로그램 화면을 보여주는 코드
#     myWindow.show()

#     #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
#     app.exec_()