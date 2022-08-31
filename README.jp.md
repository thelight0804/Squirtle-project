# **Squirtle** <a href="https://thelight0804.notion.site/Python-Project-8b62c4996c7949fdb76744557e083546" target="Notion"><img src="https://img.shields.io/badge/Notion-d4d4d4?style=flat-square&logo=Notion&logoColor=black"/></a>
<p align="center">

パソコンの作業中に腰の健康のために、ユーザーが設定した時間がたてばWindows 10の通知を送って、ユーザーに休みの時間を伝えるプログラムです。
<p align="center">
<img src="https://user-images.githubusercontent.com/69424845/182019075-887b46b8-4c6c-4045-958b-b2d1ce8c38ef.gif" height="50%" width="50%"/> </p>

<br>

# インストール方法

1. GitHub repository releasesで実行の圧縮ファイルをダウンロードします。
2. Squirtle.exe ファイルを実行します。


### ソースコード寄与

プログラムのコードをコンパイルするためには二つのライブラリをインストールしなければなりません。ただプログラムを実行するだけでしたらこの過程を飛ばしてもいいです。

1. **PyQt5 インストール**
    
    ```powershell
    $ pip install PyQt5
    ```
    
2. **win10toast インストール**
    
    ```powershell
    $ pip install win10toast
    ```
    
<br>

# 機能説明

### 1. タイマー
<p align="center">
<img src="https://user-images.githubusercontent.com/69424845/182019094-bc5f9d70-d2ce-4a61-9b27-fd1a3c26cc1a.png"  height="50%" width="50%"/> </p>



1. **設定**
    - タイマーの時間、通知の内容などを変更することができます。
2. **タイマー画面**
    - 設定された時間によってタイマーが進みます。
3. **タイマーリセット**
    - タイマー時間が設定された時間に戻ります。
4. **スタート / ストップ**
    - タイマーをスタートや止めます。

### 2. 設定
<p align="center">
<img src="https://user-images.githubusercontent.com/69424845/187685494-f17440ab-fc53-4a0c-bfd0-97fae148766d.png"  height="50%" width="50%"/> </p>


1. タイマーの時間を設定します。
2. タイマーが終わった後に体操や休みの時間を設定します。
3. タイマーが終わった後に通知の名と内容を設定します。
4. Squirtleプログラムを実行するとき、自動でタイマーがスタートできるように設定します。
5. UIの言語を変更します。（韓国語、英語、日本語）

### 3. 通知の例

タイマーが終わったら、通知をWindows 通知(Toast content)を利用してユーザーに通知を送ります。
<p align="center">
<img src="https://user-images.githubusercontent.com/69424845/182019107-a88a3990-b7f3-49c0-bacf-8a23f5d9b630.png"  height="50%" width="50%"/>
<img src="https://user-images.githubusercontent.com/69424845/182019109-7390258e-2c3a-497f-b8d4-68c98e43805b.png"  height="50%" width="50%"/> </p>



<br>

# 使用技術および開発環境

### 開発環境

> Visual Studio Code, Qt Designer
> 

### プログラミング言語

> Python
> 

### ライブラリ

> PyQt5, win10toast
> 

<br>

# ****参加者****

- **パク サンヒョン 박상현 [thelight0804]** (thelight0804@gmail.com) <a href="https://github.com/thelight0804" target="GitHub"><img src="https://img.shields.io/badge/GitHub-000000?style=flat-square&logo=GitHub&logoColor=white"/></a>
<a href="https://thelight0804.notion.site/thelight0804/Home-5db858012eb44e4ab1150eeaadec236d" target="Notion"><img src="https://img.shields.io/badge/Notion-d4d4d4?style=flat-square&logo=Notion&logoColor=black"/></a>

    
- **チェ インス 최인수 [Nifskor]** <a href="https://github.com/Nifskor" target="GitHub"><img src="https://img.shields.io/badge/GitHub-000000?style=flat-square&logo=GitHub&logoColor=white"/></a>
    
<br>

# プロジェクト期間

- 2022/02/01 ~ 2022/05/09
