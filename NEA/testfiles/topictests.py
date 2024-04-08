# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 16:11:12 2022

@author: natha
"""

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi


def quitfunc():
    print("lol")
    app.closeAllWindows()
def mainmenu()
    
class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("topicslist.ui",self)
        self.select.clicked.connect(self.checkclicked)
        self.quit.clicked.connect(quitfunc)
        self.mainmenu.clicked.connect(quitfunc)

    
    def checkclicked(self):
        item = self.listWidget.currentItem()
        print(item.text())
        
    
app=QApplication(sys.argv)
mainwindow=Login()
widget=QtWidgets.QStackedWidget()
widget.setWindowTitle("StudyCS.exe")
widget.addWidget(mainwindow)
widget.setFixedWidth(800)
widget.setFixedHeight(600)
widget.show()
app.exec_()