# **Squirtle** <a href="https://www.notion.so/thelight0804/Squirtle-7ba0fbbdeb44413281dd8271672a3092?pvs=4" target="Notion"><img src="https://img.shields.io/badge/Notion-d4d4d4?style=flat-square&logo=Notion&logoColor=black"/></a>
<p align="center">

컴퓨터 작업 중 허리 건강을 위해, 사용자가 설정한 시간이 되면 Windows 10 알림을 통해 사용자에게 휴식 시간을 알려주는 프로그램입니다.
<p align="center">
<img src="https://user-images.githubusercontent.com/69424845/182019075-887b46b8-4c6c-4045-958b-b2d1ce8c38ef.gif" height="50%" width="50%"/> </p>

<br>

# 설치 방법

1. GitHub repository releases에서 실행 압축파일을 다운받습니다.
2. Squirtle.exe 파일을 실행합니다.


### 코드 기여

해당 코드를 컴파일하기 위해서는 두 가지의 라이브러리를 설치해야 합니다. 단순히 프로그램을 실행하기 위해서는 해당 과정을 건너뛰어도 됩니다.

1. **PyQt5 설치**
    
    ```powershell
    $ pip install PyQt5
    ```
    
2. **win10toast 설치**
    
    ```powershell
    $ pip install win10toast
    ```
    
<br>

# 기능 설명

### 1. 타이머
<p align="center">
<img src="https://user-images.githubusercontent.com/69424845/182019094-bc5f9d70-d2ce-4a61-9b27-fd1a3c26cc1a.png"  height="50%" width="50%"/> </p>



1. **환경설정**
    - 타이머 시간, 알림 내용 등을 변경할 수 있습니다.
2. **타이머 화면**
    - 설정한 시간에 따라 타이머가 진행됩니다.
3. **초기화**
    - 타이머 시간을 설정한 시간으로 초기화 합니다.
4. **시작 / 일시 정지**
    - 타이머를 시작하거나 일시 정지 합니다.

### 2. 환경설정
<p align="center">
<img src="https://user-images.githubusercontent.com/69424845/182019097-a1178676-e729-433d-972d-8af3ce29fe68.png"  height="50%" width="50%"/> </p>


1. 타이머 시간을 설정합니다.
2. 타이머가 끝난 후 스트레칭 및 휴식 시간을 설정합니다.
3. 타이머가 끝난 후 알림창의 이름과 내용을 설정합니다.
4. Squirtle 프로그램 실행 시 자동으로 타이머가 시작하도록 설정합니다.
5. UI의 언어를 변경합니다. (한국어, 영어, 일본어)

### 3. 알림 예시

타이머가 끝나면 알림을 Windows 알림(Toast content)을 이용하여 사용자에게 알림을 보냅니다.
<p align="center">
<img src="https://user-images.githubusercontent.com/69424845/182019107-a88a3990-b7f3-49c0-bacf-8a23f5d9b630.png"  height="50%" width="50%"/>
<img src="https://user-images.githubusercontent.com/69424845/182019109-7390258e-2c3a-497f-b8d4-68c98e43805b.png"  height="50%" width="50%"/> </p>



<br>

# 사용 기술 및 개발 환경

### 개발 환경

> Visual Studio Code, Qt Designer
> 

### 개발 언어

> Python
> 

### 라이브러리

> PyQt5, win10toast
> 

<br>

# ****참여자****

- **박상현 [thelight0804]** (thelight0804@gmail.com) <a href="https://github.com/thelight0804" target="GitHub"><img src="https://img.shields.io/badge/GitHub-000000?style=flat-square&logo=GitHub&logoColor=white"/></a>
<a href="https://thelight0804.notion.site/thelight0804/Home-5db858012eb44e4ab1150eeaadec236d" target="Notion"><img src="https://img.shields.io/badge/Notion-d4d4d4?style=flat-square&logo=Notion&logoColor=black"/></a>

    
- **최인수 [Nifskor]** <a href="https://github.com/Nifskor" target="GitHub"><img src="https://img.shields.io/badge/GitHub-000000?style=flat-square&logo=GitHub&logoColor=white"/></a>
    
<br>

# 프로젝트 기간

- 2022/02/01 ~ 2022/05/09
