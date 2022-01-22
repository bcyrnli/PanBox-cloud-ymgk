#Greekli kütüphanelerin eklenmesi
from PyQt5 import QtCore, QtGui, QtWidgets
import os,sys,shutil
from PyQt5.QtWidgets import QScrollArea,qApp,QPushButton,QHBoxLayout,QVBoxLayout,QWidget,QApplication,QMainWindow
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon, QPixmap

from wakeonlan import send_magic_packet
import time
from tkinter import *
import os
import pyotp
import qrcode
from PIL import ImageTk, Image

#Giriş ekranı sınıfı
class Ui_Form(QMainWindow):
    def setupUi(self,Form):
        super().__init__()
        Form.setObjectName("PanBox")
        Form.resize(366, 396)
        Form.setStyleSheet("background-color: rgb(50, 50, 50);")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 220, 321, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.usernameText = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.usernameText.setStyleSheet("height:24px;\n"
"border-bottom:2px solid black;\n"
"border-radius:10px;\n"
"font:bold 16px;\n"
"color:white;\n"
"")
        self.usernameText.setAlignment(QtCore.Qt.AlignCenter)
        self.usernameText.setObjectName("usernameText")
        self.verticalLayout.addWidget(self.usernameText)
        self.userpassText = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.userpassText.setStyleSheet("height:24px;\n"
"border-bottom:2px solid black;\n"
"border-radius:10px;\n"
"font:bold 16px;\n"
"color:white;")
        self.userpassText.setEchoMode(QtWidgets.QLineEdit.Password)
        self.userpassText.setAlignment(QtCore.Qt.AlignCenter)
        self.userpassText.setObjectName("userpassText")
        self.verticalLayout.addWidget(self.userpassText)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setStyleSheet("height:34px;\n"
"border:2px solid white;\n"
"background-color:black;\n"
"border-radius:10px;\n"
"font:bold 20px;\n"
"color:white;")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        #self.pushButton.QShortcut(QKeySequence("Return"),self)
        self.pushButton.clicked.connect(self.fonk1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 10, 221, 201))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("panBox.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
    
            
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "PanBox"))
        self.usernameText.setPlaceholderText(_translate("Form", "Username(admin)"))
        self.userpassText.setPlaceholderText(_translate("Form", "Password(admin)"))
        self.pushButton.setText(_translate("Form", "Giriş"))
    def fonk1(self):
        if(self.usernameText.text()=="admin" and self.userpassText.text()=="admin"):
            self.usernameText.clear()
            self.userpassText.clear()
            self.Form = QtWidgets.QWidget()
            self.ui = Ui_Form2()
            self.ui.setupUi2(self.Form)
            self.Form.show()
#QRCODE doğrulama ekranı sınıfı
class Ui_Form2(object):
    def setupUi2(self, Form):
        print("furkan")
        Form.setObjectName("Form")
        Form.resize(366, 396)
        Form.setStyleSheet("background-color: rgb(50, 50, 50);")
        self.qrPass = QtWidgets.QLineEdit(Form)
        self.qrPass.setAlignment(QtCore.Qt.AlignCenter)
        self.qrPass.setPlaceholderText("Şifre")
        self.qrPass.setGeometry(QtCore.QRect(50, 280, 251, 31))
        self.qrPass.setStyleSheet("height:24px;\n"
"border-bottom:2px solid black;\n"
"border-radius:10px;\n"
"font:bold 16px;\n"
"color:white;")
        self.qrPass.setObjectName("qrPass")
        self.serverOpen = QtWidgets.QPushButton(Form)
        self.serverOpen.setGeometry(QtCore.QRect(50, 320, 251, 41))
        self.serverOpen.setStyleSheet("height:34px;\n"
"border:2px solid white;\n"
"background-color:black;\n"
"border-radius:10px;\n"
"font:bold 20px;\n"
"color:white;")
        self.serverOpen.setObjectName("serverOpen")
        self.serverOpen.clicked.connect(self.login)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 60, 231, 201))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("qrcode.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(100, 10, 141, 20))
        self.label_2.setStyleSheet("color:white;\n"
"font:bold 14px;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(50, 30, 261, 16))
        self.label_3.setStyleSheet("color:white;\n"
"font:bold 14px;")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        #QRCODE oluşuran fonksiyon
        QtCore.QMetaObject.connectSlotsByName(Form)
        base32secret = pyotp.random_base32()
        print('Secret:', base32secret)
        mes=""
        code=qrcode.QRCode(
            version=1,
            error_correction= qrcode.constants.ERROR_CORRECT_L,
            box_size=5,
            border= 4
            )
        code.add_data("otpauth://totp/panbox?secret={}".format(base32secret))
        code.make(fit=True)
        image=code.make_image(fill_color=(0,0,0),back_color="white")
        image.save("qrcode.png")
        
        self.totp = pyotp.TOTP(base32secret)
        print(self.totp.now())
        print(type(self.totp.now()))
        your_code = self.totp.now()
        
        print(self.totp.verify(your_code))
    #QRCODE ile giriş fonksiyonu
    def login(self):
        print(self.totp.now())
        if(self.qrPass.text()==self.totp.now()):
            self.mainn=MainWin()
            self.mainn.show()
            #Sunucuyu açmak için kullanılan kodlar
            send_magic_packet('80:FA:5B:2D:75:B2', ip_address='192.168.1.255')
            print ("PC Worked....")
            mes="PC Worked..."
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "QRCODE"))
        self.serverOpen.setText(_translate("Form", "Sunucumu Aç"))
        self.label_2.setText(_translate("Form", "Giriş Başarılı"))
        self.label_3.setText(_translate("Form", "Lütfen QR okutunuz ve Şifreyi Giriniz"))
#Sunucu ve dosya konumları(Tesler için konum ana bilgisayara göre ayarlandı) 
mainPc="C:/Users/furka/Desktop/Main Files"
raspEPc="C:/Users/furka/Desktop/G"
#raspEPc="//DESKTOP-J340J4S/Users/bcyar/Desktop/ymgk"
raspFPc="C:/Users/furka/Desktop/F"
raspGPc="C:/Users/furka/Desktop/G"
raspHPc="C:/Users/furka/Desktop/H"
copyTest="C:/Users/furka/Desktop/CopyTest"
#Uygulama arayüz sınıfı
class MainWin(QScrollArea): 
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: rgb(50, 50, 50);")
        self.setWindowTitle("Main İnterface")
        self.setGeometry(800,200,800,800)
        self.init_ui()
    def init_ui(self):
        self.mainPcBut=QPushButton("Ana bilgisayar Dosyaları")
        self.mainPcBut.setStyleSheet("height:34px;\n"
"border:2px solid white;\n"
"background-color:black;\n"
"border-radius:10px;\n"
"font:bold 12px;\n"
"color:white;\n"
"padding-left:2px;")
        self.mainPcBut.setShortcut("Return")
        self.raspEfiles=QPushButton("E Dosyaları")
        self.raspEfiles.setStyleSheet("height:34px;\n"
"border:2px solid white;\n"
"background-color:black;\n"
"border-radius:10px;\n"
"font:bold 12px;\n"
"color:white;\n"
"padding-left:2px;")
        self.raspFfiles=QPushButton("F dosyaları")
        self.raspFfiles.setStyleSheet("height:34px;\n"
"border:2px solid white;\n"
"background-color:black;\n"
"border-radius:10px;\n"
"font:bold 12px;\n"
"color:white;\n"
"padding-left:2px;")
        self.raspGFiles=QPushButton("G dosyaları")
        self.raspGFiles.setStyleSheet("height:34px;\n"
"border:2px solid white;\n"
"background-color:black;\n"
"border-radius:10px;\n"
"font:bold 12px;\n"
"color:white;\n"
"padding-left:2px;")
        self.raspHfiles=QPushButton("H Dosyaları")
        self.raspHfiles.setStyleSheet("height:34px;\n"
"border:2px solid white;\n"
"background-color:black;\n"
"border-radius:10px;\n"
"font:bold 12px;\n"
"color:white;\n"
"padding-left:2px;")
        self.refresh=QPushButton("Yenile")
        self.refresh.setStyleSheet("height:34px;\n"
"border:2px solid white;\n"
"background-color:black;\n"
"border-radius:10px;\n"
"font:bold 12px;\n"
"color:white;\n"
"padding-left:2px;")
        self.req=QPushButton("Sunucu Kapat")
        self.req.setStyleSheet("height:34px;\n"
"border:2px solid white;\n"
"background-color:black;\n"
"border-radius:10px;\n"
"font:bold 12px;\n"
"color:white;\n")
        self.caseBut=QPushButton("")
        self.shutdown=QPushButton("")
        self.shutdown.setShortcut("Ctrl+Q")
        self.shutdown.setStyleSheet("border:none;")
        self.caseBut.setStyleSheet("border:none;")
        self.copyPix=QPixmap("copy.png")
        
        self.delPix=QPixmap("delete.png")
        self.closePix=QPixmap("close.png")
        self.mainfile=0
        self.raspE=0
        self.raspF=0
        self.raspG=0
        self.raspH=0
        self.mainHbox=QHBoxLayout()
        self.mainVbox=QVBoxLayout()
        self.filesBox=QVBoxLayout()
        self.mainVbox.addWidget(self.caseBut)
        self.mainVbox.addWidget(self.mainPcBut)
        self.mainVbox.addWidget(self.req)
        self.mainVbox.addWidget(self.raspEfiles)
        self.mainVbox.addWidget(self.raspFfiles)
        self.mainVbox.addWidget(self.raspGFiles)
        self.mainVbox.addWidget(self.raspHfiles)
        self.mainVbox.addWidget(self.refresh)
        self.mainVbox.addStretch()
        self.mainVbox.addWidget(self.shutdown)
        self.mainHbox.addLayout(self.mainVbox)
        self.mainHbox.addLayout(self.filesBox)
        widget=QWidget()
        layout=QVBoxLayout(widget)
        layout.setAlignment(Qt.AlignTop)
        layout.addLayout(self.mainHbox)
        self.setWidget(widget)
        self.setWidgetResizable(True)
        self.setLayout(self.mainHbox)
        self.mainPcBut.clicked.connect(self.mainFilesBut)
        self.raspEfiles.clicked.connect(self.raspEBut)
        self.raspFfiles.clicked.connect(self.raspFBut)
        self.raspGFiles.clicked.connect(self.raspGBut)
        self.raspHfiles.clicked.connect(self.raspHBut)
        self.req.clicked.connect(self.requestBut)
        self.shutdown.clicked.connect(self.shutDown)
        self.refresh.clicked.connect(self.mainRef)
        self.mainFilesBut()
        self.raspEBut()
        self.raspFBut()
        self.raspGBut()
        self.raspHBut()
        
    def requestBut(self):
        print("Pc Closed...")
    #AnaBilgisayar konumundaki bütün dosyalara erişilen kodlar
    def mainFilesBut(self):
        os.chdir(mainPc)
        mainfiles=os.listdir()
        if len(mainfiles)==0:
            self.caseBut.setText("Klasör Boş")
            self.caseBut.setStyleSheet("background-color:green;font-size:16px;")
        else:
            self.mainHeaderBut=QPushButton("Ana Bilgisayar Dosyaları")
            self.mainHeaderBut.setStyleSheet("height:34px;\n"
"border:2px solid white;\n"
"background-color:black;\n"
"border-radius:10px;\n"
"font:bold 20px;\n"
"color:white;\n")
            self.mainAllCopy = QPushButton("  ")
            self.mainAllCopy.setIcon(QIcon(self.copyPix))
            self.mainAllCopy.setFixedWidth(50)
            self.mainAllCopy.setFixedHeight(25)
            self.mainAllCopy.setIconSize(QSize(50, 35))
            self.mainAllCopy.setStyleSheet("border:none;")
            self.vboxMain=QVBoxLayout()
            self.hboxMain=QHBoxLayout()
            self.hboxMain.addWidget(self.mainHeaderBut)
            self.hboxMain.addWidget(self.mainAllCopy)
            self.vboxMain.addLayout(self.hboxMain)
            
            for i in mainfiles:
                self.objName=i
                self.i=QPushButton(i)
                self.i.setStyleSheet("height:24px;\n"
"border-bottom:2px solid black;\n"
"border-radius:10px;\n"
"font:bold 16px;\n"
"color:white;"
                                         )
                self.mainCopBut=QPushButton("")
                self.mainCopBut.setIcon(QIcon(self.copyPix))
                self.mainCopBut.setFixedWidth(50)
                self.mainCopBut.setFixedHeight(25)
                self.mainCopBut.setIconSize(QSize(50, 35))
                self.mainCopBut.setStyleSheet("height:24px;\n"
"border-bottom:2px solid black;\n"
"border-radius:10px;\n"
"font:bold 6px;\n"
"color:white;")
                self.mainCopBut.resize(50, 50)
                self.mainCopBut.setObjectName(self.objName)


                self.mainDelBut = QPushButton("")
                self.mainDelBut.setIcon(QIcon(self.delPix))
                self.mainDelBut.setFixedWidth(50)
                self.mainDelBut.setFixedHeight(25)
                self.mainDelBut.setIconSize(QSize(50, 25))
                self.mainDelBut.setStyleSheet("height:24px;\n"
"border-bottom:2px solid black;\n"
"border-radius:10px;\n"
"font:bold 16px;\n"
"color:white;")
                self.mainDelBut.resize(50, 50)
                self.mainDelBut.setObjectName(self.objName)


                self.filesHbox=QHBoxLayout()
                self.filesHbox.addWidget(self.mainCopBut)
                self.filesHbox.addWidget(self.mainDelBut)
                self.filesHbox.addWidget(self.i)
                self.vboxMain.addLayout(self.filesHbox)
                self.filesBox.addLayout(self.vboxMain)
                self.i.clicked.connect(self.mainClck)
                self.mainCopBut.clicked.connect(self.mainCopy)
                self.mainDelBut.clicked.connect(self.mainDel)
                self.mainfile+=1
            self.mainPcBut.setEnabled(False)
    #Dosyaya tıklandığında çalıştıran fonksiyon
    def mainClck(self):
        os.chdir(mainPc)
        os.startfile(self.sender().text())
    #Seçilen dosyanın kopyalanmasını sağlayan fonksiyon
    def mainCopy(self):
        os.chdir(raspEPc)
        mainfiles = os.listdir()
        self.caseFCopy = 0
        for i in mainfiles:
            if i == self.sender().objectName():
                self.caseECopy += 1
                break
        if self.caseECopy >= 1:
            self.caseBut.setText("Bu İsimde Bir\nDosya Zaten Var")
            self.caseBut.setStyleSheet("background-color:#c8f902")
        else:
            os.chdir(mainPc)
            if os.path.isdir(self.sender().objectName()):
                shutil.move(self.sender().objectName(), raspEPc)
                if os.path.isfile(self.sender().objectName()):
                    shutil.copy(self.sender().objectName(), raspEPc)
            elif os.path.isfile(self.sender().objectName()):
                shutil.copy(self.sender().objectName(), raspEPc)
            else:
                shutil.copy(self.sender().objectName(), raspEPc)
            self.mainCopy()
        """os.chdir(raspEPc)
        mainfiles = os.listdir()
        self.caseECopy=0
        for i in mainfiles:
            if i==self.sender().objectName():
                self.caseECopy+=1
                break
        if  self.caseECopy>=1:
            self.caseBut.setText("Bu İsimde Bir\nDosya Zaten Var")
            self.caseBut.setStyleSheet("background-color:#c8f902")
        else:
            os.chdir(mainPc)
            if os.path.isdir(self.sender().objectName()):
                shutil.move(self.sender().objectName(), raspEPc)
                if os.path.isfile(self.sender().objectName()):
                    shutil.copy(self.sender().objectName(), raspEPc)
            elif os.path.isfile(self.sender().objectName()):
                shutil.copy(self.sender().objectName(), raspEPc)
            else:
                shutil.copy(self.sender().objectName(), raspEPc)"""
    #Seçilen dosyanın silinmesini sağlayan fonksiyon
    def mainDel(self):
        os.chdir(mainPc)
        if os.path.isdir(self.sender().objectName()):
            os.rmdir(self.sender().objectName())
        elif os.path.isfile(self.sender().objectName()):
            os.remove(self.sender().objectName())
        else:
            os.remove(self.sender().objectName())
        self.mainRef()
    def mainClear(self):
        def clearLayout(layout):
            while layout.count() > 0:
                item = layout.takeAt(0)
                if not item:
                    continue
                w = item.widget()
                if w:
                    w.deleteLater()

        a = self.mainfile
        for k in range(a):
            clearLayout(self.vboxMain.itemAt(k + 1))
        clearLayout(self.hboxMain)
        clearLayout(self.vboxMain)

        self.mainfile = 0
    #Sunuuda yaratılan kalsördeki dosyalara erişilen fonksiyon
    def raspEBut(self):
        os.chdir(raspEPc)
        filesE=os.listdir()
        if len(filesE)==0:
            self.caseBut.setText("Klasör Boş")
            self.caseBut.setStyleSheet("background-color:green;font-size:16px;")
        else:
            self.headerEBut=QPushButton("PanBox Main Files")
            self.headerEBut.setStyleSheet("height:34px;\n"
"border:2px solid white;\n"
"background-color:black;\n"
"border-radius:10px;\n"
"font:bold 20px;\n"
"color:white;\n")
            self.butEClear = QPushButton("")
            self.butEClear.setShortcut("Alt+E")
            self.butEClear.setIcon(QIcon(self.closePix))
            self.butEClear.setFixedWidth(50)
            self.butEClear.setFixedHeight(25)
            self.butEClear.setIconSize(QSize(50, 30))
            self.butEClear.setStyleSheet("border:none;")

            self.allECopy = QPushButton("  ")
            self.allECopy.setIcon(QIcon(self.copyPix))
            self.allECopy.setFixedWidth(50)
            self.allECopy.setFixedHeight(25)
            self.allECopy.setIconSize(QSize(50, 35))
            self.allECopy.setStyleSheet("border:none;")

            self.butEClear.clicked.connect(self.clearEBut)
            self.allECopy.clicked.connect(self.allCopyEBut)
            self.vboxE=QVBoxLayout()
            self.hboxE=QHBoxLayout()
            self.hboxE.addWidget(self.headerEBut)
            self.hboxE.addWidget(self.allECopy)
            self.hboxE.addWidget(self.butEClear)
            self.vboxE.addLayout(self.hboxE)
            for i in filesE:
                self.objEName=i
                self.i=QPushButton(i)
                self.i.setStyleSheet("height:24px;\n"
"border-bottom:2px solid black;\n"
"border-radius:10px;\n"
"font:bold 16px;\n"
"color:white;")
                self.copyEBut=QPushButton("")
                self.copyEBut.setIcon(QIcon(self.copyPix))
                self.copyEBut.setFixedWidth(50)
                self.copyEBut.setFixedHeight(25)
                self.copyEBut.setIconSize(QSize(50, 35))
                self.copyEBut.setStyleSheet("height:24px;\n"
"border-bottom:2px solid black;\n"
"border-radius:10px;\n"
"font:bold 16px;\n"
"color:white;")

                self.copyEBut.setObjectName(self.objEName)
                self.delEBut=QPushButton("")
                self.delEBut.setIcon(QIcon(self.delPix))
                self.delEBut.setFixedWidth(50)
                self.delEBut.setFixedHeight(25)
                self.delEBut.setIconSize(QSize(50, 25))
                self.delEBut.setStyleSheet("height:24px;\n"
"border-bottom:2px solid black;\n"
"border-radius:10px;\n"
"font:bold 16px;\n"
"color:white;")
                self.delEBut.setObjectName(self.objEName)
                self.filesHBox=QHBoxLayout()
                self.filesHBox.addWidget(self.copyEBut)
                self.filesHBox.addWidget(self.delEBut)
                self.filesHBox.addWidget(self.i)
                self.vboxE.addLayout(self.filesHBox)
                self.filesBox.addLayout(self.vboxE)

                self.i.clicked.connect(self.fileEBut)
                self.copyEBut.clicked.connect(self.copyEClck)
                self.delEBut.clicked.connect(self.delEClck)
                self.raspE+=1
            self.raspEfiles.setEnabled(False)
    #Sunucudaki dosyaları açmak için kullanılan fonksiyon
    def fileEBut(self):
        os.chdir(raspEPc)
        os.startfile(self.sender().text())
    #Sunucudan bilgisayara dosya kopyalamayı sağlayan fonksiyon
    def copyEClck(self):
        os.chdir(mainPc)
        mainfiles = os.listdir()
        self.caseECopy=0
        for i in mainfiles:
            if i==self.sender().objectName():
                self.caseECopy+=1
                break
        if  self.caseECopy>=1:
            self.caseBut.setText("Bu İsimde Bir\nDosya Zaten Var")
            self.caseBut.setStyleSheet("background-color:#c8f902")
        else:
            os.chdir(raspEPc)
            if os.path.isdir(self.sender().objectName()):
                shutil.move(self.sender().objectName(), mainPc)
                if os.path.isfile(self.sender().objectName()):
                    shutil.copy(self.sender().objectName(), mainPc)
            elif os.path.isfile(self.sender().objectName()):
                shutil.copy(self.sender().objectName(), mainPc)
            else:
                shutil.copy(self.sender().objectName(), mainPc)
            self.mainCopy()
    #Sunucudaki dosyaları silmek için kullanılan fonksiyon
    def delEClck(self):
        os.chdir(raspEPc)
        if os.path.isdir(self.sender().objectName()):
            os.rmdir(self.sender().objectName())
        elif os.path.isfile(self.sender().objectName()):
            os.remove(self.sender().objectName())
        else:
            os.remove(self.sender().objectName())
        self.mainRef()
    #Sunucudaki dosyayı kapatmak için kullanılan fonksiyon
    def clearEBut(self):
        def clearLayout(layout):
            while layout.count() > 0:
                item = layout.takeAt(0)
                if not item:
                    continue
                w = item.widget()
                if w:
                    w.deleteLater()

        a = self.raspE
        for k in range(a):
            clearLayout(self.vboxE.itemAt(k + 1))
        clearLayout(self.hboxE)
        clearLayout(self.vboxE)
        self.raspEfiles.setEnabled(True)
        self.raspE=0
    #Sunucudaki bütün dosyaları kopyalamak için kullanılan fonksiyon
    def allCopyEBut(self):
        os.chdir(raspEPc)
        filesE=os.listdir()
        for i in filesE:
            if os.path.isdir(i):
                shutil.move(i, copyTest)
                if os.path.isfile(i):
                    shutil.copy(i, copyTest)
            elif os.path.isfile(i):
                shutil.copy(i, copyTest)
            else:
                shutil.copy(i, copyTest)
        self.caseBut.setText("Bütün Dosyalar\nKopyalandı")
        self.caseBut.setStyleSheet("background-color:green;border:none;font-size:16px")


    def raspFBut(self):
        os.chdir(raspFPc)
        filesF=os.listdir()
        self.headerFBut = QPushButton("F Dosyaları")
        self.headerFBut.setStyleSheet("height:34px;\n"
"border:2px solid white;\n"
"background-color:black;\n"
"border-radius:10px;\n"
"font:bold 20px;\n"
"color:white;\n")

        self.butFClear = QPushButton("")
        self.butFClear.setShortcut("Alt+F")
        self.butFClear.setIcon(QIcon(self.closePix))
        self.butFClear.setFixedWidth(50)
        self.butFClear.setFixedHeight(25)
        self.butFClear.setIconSize(QSize(50, 30))
        self.butFClear.setStyleSheet("border:none;")

        self.allFCopy = QPushButton("  ")
        self.allFCopy.setIcon(QIcon(self.copyPix))
        self.allFCopy.setFixedWidth(50)
        self.allFCopy.setFixedHeight(25)
        self.allFCopy.setIconSize(QSize(50, 35))
        self.allFCopy.setStyleSheet("border:none;")

        self.butFClear.clicked.connect(self.clearFBut)
        self.allFCopy.clicked.connect(self.allCopyFBut)
        self.vboxF = QVBoxLayout()
        self.hboxF = QHBoxLayout()
        self.hboxF.addWidget(self.headerFBut)
        self.hboxF.addWidget(self.allFCopy)
        self.hboxF.addWidget(self.butFClear)
        self.vboxF.addLayout(self.hboxF)
        self.filesBox.addLayout(self.vboxF)
        self.raspFfiles.setEnabled(False)
        if len(filesF)==0:
            self.caseBut.setText("F Klasörü Boş")
            self.caseBut.setStyleSheet("background-color:yellow;font-size:16px;")
        else:

            for i in filesF:
                self.objFName=i
                self.i=QPushButton(i)
                self.i.setStyleSheet("height:24px;\n"
"border-bottom:2px solid black;\n"
"border-radius:10px;\n"
"font:bold 16px;\n"
"color:white;")
                self.copyFBut=QPushButton("")
                self.copyFBut.setIcon(QIcon(self.copyPix))
                self.copyFBut.setFixedWidth(50)
                self.copyFBut.setFixedHeight(25)
                self.copyFBut.setIconSize(QSize(50, 35))
                self.copyFBut.setStyleSheet("height:24px;\n"
"border-bottom:2px solid black;\n"
"border-radius:10px;\n"
"font:bold 16px;\n"
"color:white;")

                self.copyFBut.setObjectName(self.objFName)
                self.delFBut=QPushButton("")
                self.delFBut.setIcon(QIcon(self.delPix))
                self.delFBut.setFixedWidth(50)
                self.delFBut.setFixedHeight(25)
                self.delFBut.setIconSize(QSize(50, 25))
                self.delFBut.setStyleSheet("height:24px;\n"
"border-bottom:2px solid black;\n"
"border-radius:10px;\n"
"font:bold 16px;\n"
"color:white;")
                self.delFBut.setObjectName(self.objFName)

                self.filesHBox=QHBoxLayout()
                self.filesHBox.addWidget(self.copyFBut)
                self.filesHBox.addWidget(self.delFBut)
                self.filesHBox.addWidget(self.i)
                self.vboxF.addLayout(self.filesHBox)
                self.filesBox.addLayout(self.vboxF)

                self.i.clicked.connect(self.fileFBut)
                self.copyFBut.clicked.connect(self.copyFClck)
                self.delFBut.clicked.connect(self.delFClck)
                self.raspF+=1
            self.raspFfiles.setEnabled(False)
    def fileFBut(self):
        os.chdir(raspFPc)
        os.startfile(self.sender().text())
    def copyFClck(self):
        os.chdir(mainPc)
        mainfiles = os.listdir()
        self.caseFCopy = 0
        for i in mainfiles:
            if i == self.sender().objectName():
                self.caseFCopy += 1
                break
        if self.caseFCopy >= 1:
            self.caseBut.setText("Bu İsimde Bir\nDosya Zaten Var")
            self.caseBut.setStyleSheet("background-color:#c8f902")
        else:
            os.chdir(raspFPc)
            if os.path.isdir(self.sender().objectName()):
                shutil.move(self.sender().objectName(), mainPc)
                if os.path.isfile(self.sender().objectName()):
                    shutil.copy(self.sender().objectName(), mainPc)
            elif os.path.isfile(self.sender().objectName()):
                shutil.copy(self.sender().objectName(), mainPc)
            else:
                shutil.copy(self.sender().objectName(), mainPc)
            self.mainCopy()
    def delFClck(self):
        os.chdir(raspFPc)
        if os.path.isdir(self.sender().objectName()):
            os.rmdir(self.sender().objectName())
        elif os.path.isfile(self.sender().objectName()):
            os.remove(self.sender().objectName())
        else:
            os.remove(self.sender().objectName())
        self.mainRef()
    def clearFBut(self):
        def clearLayout(layout):
            while layout.count() > 0:
                item = layout.takeAt(0)
                if not item:
                    continue
                w = item.widget()
                if w:
                    w.deleteLater()

        a = self.raspF
        for k in range(a):
            clearLayout(self.vboxF.itemAt(k + 1))
        clearLayout(self.hboxF)
        clearLayout(self.vboxF)
        self.raspFfiles.setEnabled(True)
        self.raspF=0
    
    def allCopyFBut(self):
        os.chdir(raspFPc)
        filesF=os.listdir()
        for i in filesF:
            if os.path.isdir(i):
                shutil.move(i, copyTest)
                if os.path.isfile(i):
                    shutil.copy(i, copyTest)
            elif os.path.isfile(i):
                shutil.copy(i, copyTest)
            else:
                shutil.copy(i, copyTest)
        self.caseBut.setText("Bütün Dosyalar\nKopyalandı")
        self.caseBut.setStyleSheet("background-color:green;border:none;font-size:16px")

    def raspGBut(self):
        os.chdir(raspGPc)
        filesG=os.listdir()
        self.headerGBut = QPushButton("G Dosyaları")
        self.headerGBut.setStyleSheet("height:34px;\n"
"border:2px solid white;\n"
"background-color:black;\n"
"border-radius:10px;\n"
"font:bold 20px;\n"
"color:white;\n")
        self.butGClear = QPushButton("")
        self.butGClear.setShortcut("Alt+G")
        self.butGClear.setIcon(QIcon(self.closePix))
        self.butGClear.setFixedWidth(50)
        self.butGClear.setFixedHeight(25)
        self.butGClear.setIconSize(QSize(50, 30))
        self.butGClear.setStyleSheet("border:none;")

        self.allGCopy = QPushButton("  ")
        self.allGCopy.setIcon(QIcon(self.copyPix))
        self.allGCopy.setFixedWidth(50)
        self.allGCopy.setFixedHeight(25)
        self.allGCopy.setIconSize(QSize(50, 35))
        self.allGCopy.setStyleSheet("border:none;")

        self.butGClear.clicked.connect(self.clearGBut)
        self.allGCopy.clicked.connect(self.allCopyGBut)
        self.vboxG = QVBoxLayout()
        self.hboxG = QHBoxLayout()
        self.hboxG.addWidget(self.headerGBut)
        self.hboxG.addWidget(self.allGCopy)
        self.hboxG.addWidget(self.butGClear)
        self.vboxG.addLayout(self.hboxG)
        self.filesBox.addLayout(self.vboxG)
        if len(filesG)==0:
            self.caseBut.setText("Klasör Boş")
            self.caseBut.setStyleSheet("background-color:green;font-size:16px;")
        else:

            for i in filesG:
                self.objGName=i
                self.i=QPushButton(i)
                self.i.setStyleSheet("height:24px;\n"
"border-bottom:2px solid black;\n"
"border-radius:10px;\n"
"font:bold 16px;\n"
"color:white;")
                self.copyGBut=QPushButton("")
                self.copyGBut.setIcon(QIcon(self.copyPix))
                self.copyGBut.setFixedWidth(50)
                self.copyGBut.setFixedHeight(25)
                self.copyGBut.setIconSize(QSize(50, 35))
                self.copyGBut.setStyleSheet("height:24px;\n"
"border-bottom:2px solid black;\n"
"border-radius:10px;\n"
"font:bold 16px;\n"
"color:white;")
                self.copyGBut.setObjectName(self.objGName)

                self.delGBut=QPushButton("")
                self.delGBut.setIcon(QIcon(self.delPix))
                self.delGBut.setFixedWidth(50)
                self.delGBut.setFixedHeight(25)
                self.delGBut.setIconSize(QSize(50, 25))
                self.delGBut.setStyleSheet("height:24px;\n"
"border-bottom:2px solid black;\n"
"border-radius:10px;\n"
"font:bold 16px;\n"
"color:white;")

                self.delGBut.setObjectName(self.objGName)
                self.filesHBox=QHBoxLayout()
                self.filesHBox.addWidget(self.copyGBut)
                self.filesHBox.addWidget(self.delGBut)
                self.filesHBox.addWidget(self.i)
                self.vboxG.addLayout(self.filesHBox)
                self.filesBox.addLayout(self.vboxG)

                self.i.clicked.connect(self.fileGBut)
                self.copyGBut.clicked.connect(self.copyGClck)
                self.delGBut.clicked.connect(self.delGClck)
                self.raspG+=1
            self.raspGFiles.setEnabled(False)
    def fileGBut(self):
        os.chdir(raspFPc)
        os.startfile(self.sender().text())
    def copyGClck(self):
        os.chdir(mainPc)
        mainfiles = os.listdir()
        self.caseGCopy = 0
        for i in mainfiles:
            if i == self.sender().objectName():
                self.caseGCopy += 1
                break
        if self.caseGCopy >= 1:
            self.caseBut.setText("Bu İsimde Bir\nDosya Zaten Var")
            self.caseBut.setStyleSheet("background-color:#c8f902")
        else:
            os.chdir(raspGPc)
            if os.path.isdir(self.sender().objectName()):
                shutil.move(self.sender().objectName(), mainPc)
                if os.path.isfile(self.sender().objectName()):
                    shutil.copy(self.sender().objectName(), mainPc)
            elif os.path.isfile(self.sender().objectName()):
                shutil.copy(self.sender().objectName(), mainPc)
            else:
                shutil.copy(self.sender().objectName(), mainPc)
            self.mainCopy()
    def delGClck(self):
        os.chdir(raspGPc)
        if os.path.isdir(self.sender().objectName()):
            os.rmdir(self.sender().objectName())
        elif os.path.isfile(self.sender().objectName()):
            os.remove(self.sender().objectName())
        else:
            os.remove(self.sender().objectName())
        self.mainRef()
    def clearGBut(self):
        def clearLayout(layout):
            while layout.count() > 0:
                item = layout.takeAt(0)
                if not item:
                    continue
                w = item.widget()
                if w:
                    w.deleteLater()

        a = self.raspG
        for k in range(a):
            clearLayout(self.vboxG.itemAt(k + 1))
        clearLayout(self.hboxG)
        clearLayout(self.vboxG)
        self.raspGFiles.setEnabled(True)
        self.raspG=0
    def allCopyGBut(self):
        os.chdir(raspGPc)
        filesG=os.listdir()
        for i in filesG:
            if os.path.isdir(i):
                shutil.move(i, copyTest)
                if os.path.isfile(i):
                    shutil.copy(i, copyTest)
            elif os.path.isfile(i):
                shutil.copy(i, copyTest)
            else:
                shutil.copy(i, copyTest)
        self.caseBut.setText("Bütün Dosyalar\nKopyalandı")
        self.caseBut.setStyleSheet("background-color:green;border:none;font-size:16px")

    def raspHBut(self):
        os.chdir(raspHPc)
        filesH=os.listdir()
        self.headerHBut = QPushButton("H Dosyaları")
        self.headerHBut.setStyleSheet("height:34px;\n"
"border:2px solid white;\n"
"background-color:black;\n"
"border-radius:10px;\n"
"font:bold 20px;\n"
"color:white;\n")
        self.butHClear = QPushButton("")
        self.butHClear.setShortcut("Alt+H")
        self.butHClear.setIcon(QIcon(self.closePix))
        self.butHClear.setFixedWidth(50)
        self.butHClear.setFixedHeight(25)
        self.butHClear.setIconSize(QSize(50, 30))
        self.butHClear.setStyleSheet("border:none;")

        self.allHCopy = QPushButton("  ")
        self.allHCopy.setIcon(QIcon(self.copyPix))
        self.allHCopy.setFixedWidth(50)
        self.allHCopy.setFixedHeight(25)
        self.allHCopy.setIconSize(QSize(50, 35))
        self.allHCopy.setStyleSheet("border:none;")

        self.butHClear.clicked.connect(self.clearHBut)
        self.allHCopy.clicked.connect(self.allCopyHBut)
        self.vboxH = QVBoxLayout()
        self.hboxH = QHBoxLayout()
        self.hboxH.addWidget(self.headerHBut)
        self.hboxH.addWidget(self.allHCopy)
        self.hboxH.addWidget(self.butHClear)
        self.vboxH.addLayout(self.hboxH)
        self.filesBox.addLayout(self.vboxH)
        if len(filesH)==0:
            self.caseBut.setText("Klasör Boş")
            self.caseBut.setStyleSheet("background-color:green;font-size:16px;")
        else:
            for i in filesH:
                self.objHName=i
                self.i=QPushButton(i)
                self.i.setStyleSheet("height:24px;\n"
"border-bottom:2px solid black;\n"
"border-radius:10px;\n"
"font:bold 16px;\n"
"color:white;")
                self.copyHBut=QPushButton("")
                self.copyHBut.setIcon(QIcon(self.copyPix))
                self.copyHBut.setFixedWidth(50)
                self.copyHBut.setFixedHeight(25)
                self.copyHBut.setIconSize(QSize(50, 35))
                self.copyHBut.setStyleSheet("height:24px;\n"
"border-bottom:2px solid black;\n"
"border-radius:10px;\n"
"font:bold 16px;\n"
"color:white;")
                self.copyHBut.setObjectName(self.objHName)

                self.delHBut=QPushButton("")
                self.delHBut.setIcon(QIcon(self.delPix))
                self.delHBut.setFixedWidth(50)
                self.delHBut.setFixedHeight(25)
                self.delHBut.setIconSize(QSize(50, 25))
                self.delHBut.setStyleSheet("height:24px;\n"
"border-bottom:2px solid black;\n"
"border-radius:10px;\n"
"font:bold 16px;\n"
"color:white;")
                self.delHBut.setObjectName(self.objGName)

                self.filesHBox=QHBoxLayout()
                self.filesHBox.addWidget(self.copyHBut)
                self.filesHBox.addWidget(self.delHBut)
                self.filesHBox.addWidget(self.i)
                self.vboxH.addLayout(self.filesHBox)
                self.filesBox.addLayout(self.vboxH)

                self.i.clicked.connect(self.fileHBut)
                self.copyHBut.clicked.connect(self.copyHClck)
                self.delHBut.clicked.connect(self.delHClck)
                self.raspH+=1
            self.raspHfiles.setEnabled(False)
    def fileHBut(self):
        os.chdir(raspHPc)
        os.startfile(self.sender().text())
    def copyHClck(self):
        os.chdir(mainPc)
        mainfiles = os.listdir()
        self.caseHCopy = 0
        for i in mainfiles:
            if i == self.sender().objectName():
                self.caseHCopy += 1
                break
        if self.caseHCopy >= 1:
            self.caseBut.setText("Bu İsimde Bir\nDosya Zaten Var")
            self.caseBut.setStyleSheet("background-color:#c8f902")
        else:
            os.chdir(raspHPc)
            if os.path.isdir(self.sender().objectName()):
                shutil.move(self.sender().objectName(), mainPc)
                if os.path.isfile(self.sender().objectName()):
                    shutil.copy(self.sender().objectName(), mainPc)
            elif os.path.isfile(self.sender().objectName()):
                shutil.copy(self.sender().objectName(), mainPc)
            else:
                shutil.copy(self.sender().objectName(), mainPc)
            self.mainCopy()
    def delHClck(self):
        os.chdir(raspHPc)
        if os.path.isdir(self.sender().objectName()):
            os.rmdir(self.sender().objectName())
        elif os.path.isfile(self.sender().objectName()):
            os.remove(self.sender().objectName())
        else:
            os.remove(self.sender().objectName())
        self.mainRef()
    def clearHBut(self):
        def clearLayout(layout):
            while layout.count() > 0:
                item = layout.takeAt(0)
                if not item:
                    continue
                w = item.widget()
                if w:
                    w.deleteLater()

        a = self.raspH
        for k in range(a):
            clearLayout(self.vboxH.itemAt(k + 1))
        clearLayout(self.hboxH)
        clearLayout(self.vboxH)
        self.raspHfiles.setEnabled(True)
        self.raspH=0
    def allCopyHBut(self):
        os.chdir(raspHPc)
        filesH=os.listdir()
        for i in filesH:
            if os.path.isdir(i):
                shutil.move(i, copyTest)
                if os.path.isfile(i):
                    shutil.copy(i, copyTest)
            elif os.path.isfile(i):
                shutil.copy(i, copyTest)
            else:
                shutil.copy(i, copyTest)
        self.caseBut.setText("Bütün Dosyalar\nKopyalandı")
        self.caseBut.setStyleSheet("background-color:green;border:none;font-size:16px")

    def shutDown(self):
        qApp.quit()
    def mainRef(self):
        self.mainClear()
        self.clearEBut()
        self.clearFBut()
        self.clearGBut()
        self.clearHBut()
        self.caseBut.setText("Yenileniyor...")
        self.caseBut.setStyleSheet("background-color:#c8f902")
        self.mainFilesBut()
        self.raspEBut()
        self.raspFBut()
        self.raspGBut()
        self.raspHBut()
        self.caseBut.setText("Yenilendi")
        self.caseBut.setStyleSheet("background-color:#c8f902")
    def mainCopy(self):
        self.copiedHbox = QHBoxLayout()
        self.copiedObjName = self.sender().objectName()
        self.copiedFile = QPushButton(self.sender().objectName())
        self.copiedFile.setStyleSheet("height:24px;\n"
"border-bottom:2px solid black;\n"
"border-radius:10px;\n"
"font:bold 16px;\n"
"color:white;")

        self.copiedCopBut = QPushButton("")
        self.copiedCopBut.setIcon(QIcon(self.copyPix))
        self.copiedCopBut.setFixedWidth(50)
        self.copiedCopBut.setFixedHeight(25)
        self.copiedCopBut.setIconSize(QSize(50, 25))
        self.copiedCopBut.setStyleSheet("height:24px;\n"
"border-bottom:2px solid black;\n"
"border-radius:10px;\n"
"font:bold 16px;\n"
"color:white;")
        self.copiedCopBut.resize(50, 50)
        self.copiedCopBut.setObjectName(self.copiedObjName)

        self.copiedDelBut = QPushButton("")
        self.copiedDelBut.setIcon(QIcon(self.delPix))
        self.copiedDelBut.setFixedWidth(50)
        self.copiedDelBut.setFixedHeight(25)
        self.copiedDelBut.setIconSize(QSize(50, 25))
        self.copiedDelBut.setStyleSheet("height:24px;\n"
"border-bottom:2px solid black;\n"
"border-radius:10px;\n"
"font:bold 16px;\n"
"color:white;")
        self.copiedDelBut.resize(50, 50)
        self.copiedDelBut.setObjectName(self.copiedObjName)

        self.copiedHbox.addWidget(self.copiedCopBut)
        self.copiedHbox.addWidget(self.copiedDelBut)
        self.copiedHbox.addWidget(self.copiedFile)
        self.vboxMain.addLayout(self.copiedHbox)
        self.copiedFile.clicked.connect(self.mainClck)
        self.copiedCopBut.clicked.connect(self.mainCopy)
        self.copiedDelBut.clicked.connect(self.mainDel)
#Arayüz sınıflarını aktive eden kısım
if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    Form.setWindowTitle("PanBox")
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
