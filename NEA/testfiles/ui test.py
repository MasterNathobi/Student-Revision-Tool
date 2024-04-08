import sys
from PyQt5 import QtCore,QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWin", "MainWin"))
        loadUi("queswinui.ui",self)
        self.question.setText("hioii") 
        self.ans1.setText("question2 ptato")
        self.ans2.setText("question3 ptato")
        self.ans3.setText("question4 ptato")
        self.ans4.setText("question5 ptato")
        
    def loginfunction(self):
        email=self.email.text()
        password=self.password.text()
        print("Successfully logged in with email: ", email, "and password:", password)

    def gotocreate(self):
        createacc=CreateAcc()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex()+1)

class CreateAcc(QDialog):
    def __init__(self):
        super(CreateAcc,self).__init__()
        loadUi("createacc.ui",self)
        self.signupbutton.clicked.connect(self.createaccfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpass.setEchoMode(QtWidgets.QLineEdit.Password)

    def createaccfunction(self):
        email = self.email.text()
        if self.password.text()==self.confirmpass.text():
            password=self.password.text()
            print("Successfully created acc with email: ", email, "and password: ", password)
            login=Login()
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex()+1)



app=QApplication(sys.argv)
mainwindow=Login()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(800)
widget.setFixedHeight(600)
widget.show()
app.exec_()
