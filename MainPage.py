from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
import os
import sys
import cv2

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 320)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background_im = QtWidgets.QLabel(self.centralwidget)
        self.background_im.setGeometry(QtCore.QRect(0, 0, 480, 320))
        self.background_im.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.background_im.setText("")
        self.background_im.setPixmap(QtGui.QPixmap("BackFont/back.jpg"))
        self.background_im.setScaledContents(True)
        self.background_im.setObjectName("background_im")
        self.ensi_im = QtWidgets.QLabel(self.centralwidget)
        self.ensi_im.setGeometry(QtCore.QRect(10, 10, 80, 100))
        self.ensi_im.setText("")
        self.ensi_im.setPixmap(QtGui.QPixmap("BackFont/ensi.png"))
        self.ensi_im.setScaledContents(True)
        self.ensi_im.setObjectName("ensi_im")
        self.manouba_im = QtWidgets.QLabel(self.centralwidget)
        self.manouba_im.setGeometry(QtCore.QRect(390, 10, 80, 100))
        self.manouba_im.setText("")
        self.manouba_im.setPixmap(QtGui.QPixmap("BackFont/mannouba.png"))
        self.manouba_im.setScaledContents(True)
        self.manouba_im.setObjectName("manouba_im")
        self.welcome_im = QtWidgets.QLabel(self.centralwidget)
        self.welcome_im.setGeometry(QtCore.QRect(100, 20, 291, 120))
        self.welcome_im.setText("")
        self.welcome_im.setPixmap(QtGui.QPixmap("BackFont/welcome.png"))
        self.welcome_im.setScaledContents(True)
        self.welcome_im.setObjectName("welcome_im")
        self.pointButton = QtWidgets.QPushButton(self.centralwidget)
        self.pointButton.setGeometry(QtCore.QRect(290, 230, 152, 61))
        self.pointButton.setStyleSheet("  background: #4162a8;\n"
"  border-top: 1px solid #38538c;\n"
"  border-right: 1px solid #1f2d4d;\n"
"  border-bottom: 1px solid #151e33;\n"
"  border-left: 1px solid #1f2d4d;\n"
"  border-radius: 4px;\n"
"  -webkit-box-shadow: inset 0 1px 10px 1px #5c8bee, 0 1px 0 #1d2c4d, 0 6px 0 #1f3053, 0 8px 4px 1px #111111;\n"
"  box-shadow: inset 0 1px 10px 1px #5c8bee, 0 1px 0 #1d2c4d, 0 6px 0 #1f3053, 0 8px 4px 1px #111111;\n"
"  color: #fff;\n"
"  font-size: 150%;\n"
"  margin-bottom: 10px;\n"
"  padding: 10px 0 12px 0;\n"
"  text-align: center;\n"
"  text-shadow: 0 -1px 1px #1e2d4d;\n"
"  width: 150px;")
        self.pointButton.setObjectName("pointButton")
        self.pointButton.clicked.connect(self.Pointer)
        
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(50, 230, 152, 61))
        self.addButton.setStyleSheet("  background: #4162a8;\n"
"  border-top: 1px solid #38538c;\n"
"  border-right: 1px solid #1f2d4d;\n"
"  border-bottom: 1px solid #151e33;\n"
"  border-left: 1px solid #1f2d4d;\n"
"  border-radius: 4px;\n"
"  -webkit-box-shadow: inset 0 1px 10px 1px #5c8bee, 0 1px 0 #1d2c4d, 0 6px 0 #1f3053, 0 8px 4px 1px #111111;\n"
"  box-shadow: inset 0 1px 10px 1px #5c8bee, 0 1px 0 #1d2c4d, 0 6px 0 #1f3053, 0 8px 4px 1px #111111;\n"
"  color: #fff;\n"
"  font-size: 150%;\n"
"  margin-bottom: 10px;\n"
"  padding: 10px 0 12px 0;\n"
"  text-align: center;\n"
"  text-shadow: 0 -1px 1px #1e2d4d;\n"
"  width: 150px;")
        self.addButton.setObjectName("addButton")
        self.addButton.clicked.connect(self.Authentification)
        self.text_mess = QtWidgets.QLabel(self.centralwidget)
        self.text_mess.setGeometry(QtCore.QRect(20, 160, 441, 48))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.text_mess.setFont(font)
        self.text_mess.setObjectName("text_mess")
        self.footer = QtWidgets.QLabel(self.centralwidget)
        self.footer.setGeometry(QtCore.QRect(200, 290, 91, 20))
        self.footer.setObjectName("footer")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FacePointer"))
        self.pointButton.setText(_translate("MainWindow", "Pointer"))
        self.addButton.setText(_translate("MainWindow", "Ajouter un individu"))
        self.text_mess.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; font-style:italic; color:#5500ff;\">Sujet: Mise en œuvre d’un système de gestion d’accès à</span></p><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; font-style:italic; color:#5500ff;\">base de reconnaissance faciale et détection des émotions</span></p></body></html>"))
        self.footer.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-style:italic; text-decoration: underline;\">PCD 2019 - ENSI</span></p></body></html>"))

    def Authentification(self):
        self.window = QtWidgets.QMainWindow()
        self.auth = Authentifier()
        self.auth.setupUi(self.window)
        self.window.show()
        #self.window.hide()
    
    def Pointer(self):
        if len(os.listdir('dataset')) == 0:
            print ("Pas d'employés inscrits !!")
        else:
            os.system('python 03_face_recognition.py')

class Authentifier(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(360, 200)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background_im = QtWidgets.QLabel(self.centralwidget)
        self.background_im.setGeometry(QtCore.QRect(0, 0, 360, 200))
        self.background_im.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.background_im.setText("")
        self.background_im.setPixmap(QtGui.QPixmap("BackFont/back.jpg"))
        self.background_im.setScaledContents(True)
        self.background_im.setObjectName("background_im")
        self.auth_title = QtWidgets.QLabel(self.centralwidget)
        self.auth_title.setGeometry(QtCore.QRect(110, 10, 154, 23))
        self.auth_title.setObjectName("auth_title")
        self.admin_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.admin_txt.setGeometry(QtCore.QRect(110, 50, 231, 31))
        self.admin_txt.setObjectName("admin_txt")
        self.psw_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.psw_txt.setEchoMode(QtWidgets.QLineEdit.Password)
        self.psw_txt.setGeometry(QtCore.QRect(110, 100, 231, 31))
        self.psw_txt.setObjectName("psw_txt")
        self.admin_mess = QtWidgets.QLabel(self.centralwidget)
        self.admin_mess.setGeometry(QtCore.QRect(20, 60, 51, 18))
        self.admin_mess.setObjectName("admin_mess")
        self.psw_mess = QtWidgets.QLabel(self.centralwidget)
        self.psw_mess.setGeometry(QtCore.QRect(20, 110, 81, 16))
        self.psw_mess.setObjectName("psw_mess")
        self.ok_button = QtWidgets.QPushButton(self.centralwidget)
        self.ok_button.clicked.connect(self.AddIndiv)
        self.ok_button.setGeometry(QtCore.QRect(30, 150, 151, 51))
        self.ok_button.setStyleSheet("  background: #4162a8;\n"
"  border-top: 1px solid #38538c;\n"
"  border-right: 1px solid #1f2d4d;\n"
"  border-bottom: 1px solid #151e33;\n"
"  border-left: 1px solid #1f2d4d;\n"
"  border-radius: 4px;\n"
"  -webkit-box-shadow: inset 0 1px 10px 1px #5c8bee, 0 1px 0 #1d2c4d, 0 6px 0 #1f3053, 0 8px 4px 1px #111111;\n"
"  box-shadow: inset 0 1px 10px 1px #5c8bee, 0 1px 0 #1d2c4d, 0 6px 0 #1f3053, 0 8px 4px 1px #111111;\n"
"  color: #fff;\n"
"  font-size: 150%;\n"
"  margin-bottom: 10px;\n"
"  padding: 10px 0 12px 0;\n"
"  text-align: center;\n"
"  text-shadow: 0 -1px 1px #1e2d4d;\n"
"  width: 150px;")
        self.ok_button.setObjectName("ok_button")
        self.cancel_button = QtWidgets.QPushButton(self.centralwidget)
        #self.cancel_button.clicked.connect(QtWidgets.qApp.quit)
        #self.cancel_button.clicked.connect(Dialog.reject)
        self.cancel_button.setGeometry(QtCore.QRect(190, 150, 151, 51))
        self.cancel_button.setStyleSheet("  background: #4162a8;\n"
"  border-top: 1px solid #38538c;\n"
"  border-right: 1px solid #1f2d4d;\n"
"  border-bottom: 1px solid #151e33;\n"
"  border-left: 1px solid #1f2d4d;\n"
"  border-radius: 4px;\n"
"  -webkit-box-shadow: inset 0 1px 10px 1px #5c8bee, 0 1px 0 #1d2c4d, 0 6px 0 #1f3053, 0 8px 4px 1px #111111;\n"
"  box-shadow: inset 0 1px 10px 1px #5c8bee, 0 1px 0 #1d2c4d, 0 6px 0 #1f3053, 0 8px 4px 1px #111111;\n"
"  color: #fff;\n"
"  font-size: 150%;\n"
"  margin-bottom: 10px;\n"
"  padding: 10px 0 12px 0;\n"
"  text-align: center;\n"
"  text-shadow: 0 -1px 1px #1e2d4d;\n"
"  width: 150px;")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "S'authentifier"))
        self.auth_title.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; text-decoration: underline;\">Authentification</span></p></body></html>"))
        self.admin_mess.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-style:italic;\">Admin:</span></p></body></html>"))
        self.psw_mess.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-style:italic;\">Mot de passe:</span></p></body></html>"))
        self.ok_button.setText(_translate("MainWindow", "OK"))
        self.cancel_button.setText(_translate("MainWindow", "Cancel"))
    
    def AddIndiv(self):
        adminValue = self.admin_txt.text()
        pswValue = self.psw_txt.text()
        if adminValue == "admin" and pswValue == "pass":         
            self.window = QtWidgets.QMainWindow()
            self.auth = Ajouter_individu()
            self.auth.setupUi(self.window)
            self.window.show()
        else:
            msg = QMessageBox()
            msg.setText("ERREUR !!")
            msg.setInformativeText("Erreur de connexion")
            msg.setWindowTitle("ERREUR")
            msg.setDetailedText("Veulliez verifier votre id ou mot de passe")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

class Ajouter_individu(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(360, 200)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background_im = QtWidgets.QLabel(self.centralwidget)
        self.background_im.setGeometry(QtCore.QRect(0, 0, 360, 200))
        self.background_im.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.background_im.setText("")
        self.background_im.setPixmap(QtGui.QPixmap("BackFont/back.jpg"))
        self.background_im.setScaledContents(True)
        self.background_im.setObjectName("background_im")
        self.auth_title = QtWidgets.QLabel(self.centralwidget)
        self.auth_title.setGeometry(QtCore.QRect(90, 10, 184, 23))
        self.auth_title.setObjectName("auth_title")
        self.admin_mess = QtWidgets.QLabel(self.centralwidget)
        self.admin_mess.setGeometry(QtCore.QRect(10, 50, 51, 18))
        self.admin_mess.setObjectName("admin_mess")
        self.admin_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.admin_txt.setGeometry(QtCore.QRect(70, 50, 261, 21))
        self.admin_txt.setObjectName("admin_txt")
        self.admin_mess_2 = QtWidgets.QLabel(self.centralwidget)
        self.admin_mess_2.setGeometry(QtCore.QRect(10, 80, 51, 18))
        self.admin_mess_2.setObjectName("admin_mess_2")
        self.admin_txt_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.admin_txt_2.setGeometry(QtCore.QRect(70, 80, 261, 21))
        self.admin_txt_2.setObjectName("admin_txt_2")
        self.admin_mess_3 = QtWidgets.QLabel(self.centralwidget)
        self.admin_mess_3.setGeometry(QtCore.QRect(10, 110, 51, 18))
        self.admin_mess_3.setObjectName("admin_mess_3")
        self.admin_txt_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.admin_txt_3.setGeometry(QtCore.QRect(70, 110, 261, 21))
        self.admin_txt_3.setObjectName("admin_txt_3")
        self.ok_button = QtWidgets.QPushButton(self.centralwidget)
        self.ok_button.clicked.connect(self.StartTrain)
        self.ok_button.setGeometry(QtCore.QRect(30, 150, 151, 51))
        self.ok_button.setStyleSheet("  background: #4162a8;\n"
"  border-top: 1px solid #38538c;\n"
"  border-right: 1px solid #1f2d4d;\n"
"  border-bottom: 1px solid #151e33;\n"
"  border-left: 1px solid #1f2d4d;\n"
"  border-radius: 4px;\n"
"  -webkit-box-shadow: inset 0 1px 10px 1px #5c8bee, 0 1px 0 #1d2c4d, 0 6px 0 #1f3053, 0 8px 4px 1px #111111;\n"
"  box-shadow: inset 0 1px 10px 1px #5c8bee, 0 1px 0 #1d2c4d, 0 6px 0 #1f3053, 0 8px 4px 1px #111111;\n"
"  color: #fff;\n"
"  font-size: 150%;\n"
"  margin-bottom: 10px;\n"
"  padding: 10px 0 12px 0;\n"
"  text-align: center;\n"
"  text-shadow: 0 -1px 1px #1e2d4d;\n"
"  width: 150px;")
        self.ok_button.setObjectName("ok_button")
        self.cancel_button = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_button.setGeometry(QtCore.QRect(190, 150, 151, 51))
        self.cancel_button.setStyleSheet("  background: #4162a8;\n"
"  border-top: 1px solid #38538c;\n"
"  border-right: 1px solid #1f2d4d;\n"
"  border-bottom: 1px solid #151e33;\n"
"  border-left: 1px solid #1f2d4d;\n"
"  border-radius: 4px;\n"
"  -webkit-box-shadow: inset 0 1px 10px 1px #5c8bee, 0 1px 0 #1d2c4d, 0 6px 0 #1f3053, 0 8px 4px 1px #111111;\n"
"  box-shadow: inset 0 1px 10px 1px #5c8bee, 0 1px 0 #1d2c4d, 0 6px 0 #1f3053, 0 8px 4px 1px #111111;\n"
"  color: #fff;\n"
"  font-size: 150%;\n"
"  margin-bottom: 10px;\n"
"  padding: 10px 0 12px 0;\n"
"  text-align: center;\n"
"  text-shadow: 0 -1px 1px #1e2d4d;\n"
"  width: 150px;")
        self.cancel_button.setObjectName("cancel_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ajouter un individu"))
        self.auth_title.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; text-decoration: underline;\">Ajouter un individu</span></p></body></html>"))
        self.admin_mess.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-style:italic;\">Nom:</span></p></body></html>"))
        self.admin_mess_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-style:italic;\">Prenom:</span></p></body></html>"))
        self.admin_mess_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-style:italic;\">Poste:</span></p></body></html>"))
        self.ok_button.setText(_translate("MainWindow", "OK"))
        self.cancel_button.setText(_translate("MainWindow", "Cancel"))
        
    def StartTrain(self):
        os.system('python 01_face_dataset.py')
        os.system('python 02_face_training.py')


app = QtCore.QCoreApplication.instance()
if app is None:
    app = QApplication(sys.argv)
main = QMainWindow()
window = Ui_MainWindow()
window.setupUi(main)
main.show()
sys.exit(app.exec_())
