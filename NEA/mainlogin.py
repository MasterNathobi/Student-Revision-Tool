import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QBrush,QColor,QPixmap
from PyQt5.QtWidgets import QDialog, QApplication, QListWidgetItem
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
from datetime import datetime
import sqlite3
brush1 = QBrush(QColor(30,30,200,255))
brush1.setStyle(Qt.SolidPattern)

def quitfunc():
    print("quit")
    app.closeAllWindows()

def hasher(password):
    hashed = password
    return hashed

def checkLogin(user,passw):
    ID = None
    passw = hasher(passw)
    correct = False
    sqliteConnection = sqlite3.connect('StudyCS.db')
    cursor = sqliteConnection.cursor()
    accounts = cursor.execute("SELECT username, password,ID FROM accounts").fetchall()
    for account in accounts:
        if account[0]== user and account[1] == passw:
            ID = account[2]
            correct = True
    sqliteConnection.commit()
    cursor.close()
    return(correct,ID)

def updatedatabase(user = None):
    sqliteConnection = sqlite3.connect('StudyCS.db')
    cursor = sqliteConnection.cursor()
    if user != None:
        for topic in user.topics:
            for question in topic.questions:
                attemsuccess = cursor.execute("SELECT attempted,success FROM questionsuccess WHERE questionID =  "+str(question.questionID)+" AND ID = '"+str(user.ID)+"'").fetchall()
                attem,success = attemsuccess[0][0],attemsuccess[0][1]
                attem +=question.attempted
                success +=question.successes
                if question.inclasttest == 'True':
                    inclasttest = 'True'
                else:
                    inclasttest = 'False'
                print("UPDATE questionsuccess SET attempted = "+str(attem)+",success = "+str(success)+",inclasttest = "+"'"+inclasttest+"'"+" WHERE questionID =  "+str(question.questionID)+" AND ID = '"+str(user.ID)+"'")
                cursor.execute("UPDATE questionsuccess SET attempted = "+str(attem)+",success = "+str(success)+",inclasttest = "+"'"+inclasttest+"'"+" WHERE questionID =  "+str(question.questionID)+" AND ID = '"+str(user.ID)+"'")
                sqliteConnection.commit()
    numquestions = cursor.execute("SELECT COUNT(*) FROM questions").fetchone()
    success=[0]*int(numquestions[0])
    attempts=[0]*int(numquestions[0])
    for i in range(1,int(numquestions[0])+1):
        questionsuccessrate = cursor.execute("SELECT attempted,success FROM questionsuccess WHERE questionID = "+str(i)).fetchall()
        for j in questionsuccessrate:
            if j[0]>0:
                success[i-1] += (int(j[1]))
                attempts[i-1] += (int(j[0]))
                
    for i in range(1,int(numquestions[0])+1):
        cursor.execute("UPDATE questions SET success = "+str(success[i-1])+", attempts = "+str(attempts[i-1])+" WHERE questionID = "+str(i)).fetchall()
        difficultycalc = cursor.execute("SELECT success, attempts FROM questions WHERE questionID = "+str(i)).fetchall()
        print(str(i))
        print(difficultycalc)
        difficultycalc = difficultycalc[0]
        print(difficultycalc)
        difficultycalc = str(difficultycalc[0]/difficultycalc[1])
        sqliteConnection.commit()
        cursor.execute("UPDATE questions SET difficulty = "+difficultycalc+" WHERE questionID = "+str(i))
    sqliteConnection.commit()
    cursor.close()
        

def tologin():
    login = Login()
    widget.addWidget(login)
    widget.setCurrentIndex(widget.currentIndex()+1)

def tomainmenu(user):
    print('main')
    mainmenu = MainMenu(user)
    widget.addWidget(mainmenu)
    widget.setCurrentIndex(widget.currentIndex()+1)

def totopicslist(user):
    topicslist = TopicsList(user)
    widget.addWidget(topicslist)
    widget.setCurrentIndex(widget.currentIndex()+1)

def totopicload(topic,user):
    topicmenu = TopicMenu(topic,user)
    widget.addWidget(topicmenu)
    widget.setCurrentIndex(widget.currentIndex()+1)

def setuptest(typeoftest,user,num,questiontype):
    testwin = TestWin(typeoftest,user,num,questiontype)
    widget.addWidget(testwin)
    widget.setCurrentIndex(widget.currentIndex()+1)
    
class userobj():
    def __init__(self,ID):
        self.ID = ID
    
    def addtopics(self,topics):
        self.topics = topics
        
class topicObj():
    def __init__(self,topicID,topic):
        self.topicID = topicID
        self.topic = topic
        self.questions = []

class questionObj():
    def __init__(self,questionID,topicID,question,ans1,ans2,ans3,ans4,correct,difficulty):
        self.topicID = str(topicID)
        self.questionID = str(questionID)
        self.question = str(question)
        self.ans1 = str(ans1)
        self.ans2 = str(ans2)
        self.ans3 = str(ans3)
        self.ans4 = str(ans4)
        self.correct = correct
        self.difficulty = difficulty
       
    
    def addsuccesses(self,attempted=0,success=0,inclasttest='False'):
        self.attempted = attempted
        self.successes = success
        self.inclasttest = inclasttest
    
    def __str__(self):
        attributes = self.topicID+' '+self.questionID+' '+self.question+' '+self.ans1+' '+self.ans2+' '+self.ans3+' '+self.ans4+' '+str(self.correct)+' '+str(self.attempted)+' '+str(self.successes)+' '+str(self.difficulty)   
        attributes = str(attributes)
        return(attributes)
        
class TestWin(QDialog):
    # implemented as class as this is how pyqt5 handles windows
    def __init__(self,typeoftest,user,num,questiontype):
        super(TestWin,self).__init__()
        #check type of question, make program ignore num
        if questiontype == 'All Questions':
            num = -1
        #make user an attribute so its accessible anywhere in class
        self.user = user
        #load the window
        loadUi("Testwin.ui",self)
        # hide end of test message
        self.endtest.hide()
        #connect buttons to subroutines in program/methods of the class
        self.b2main_2.clicked.connect(lambda: tomainmenu(self.user))
        self.quit_2.clicked.connect(quitfunc)
        self.b2topiclist.clicked.connect(self.backtotopicsFunc)
        self.b2main.clicked.connect(lambda: tomainmenu(self.user))
        self.quit.clicked.connect(quitfunc)
        questionset = []
        # create question packs
        # slight difference in code when doing quick test or not 
        if typeoftest == 'quick':
            self.title.setText('Quick Test')
            self.b2topic.hide()
            for topic in user.topics:
                for question in topic.questions:
                    if questiontype == 'Incorrect last testing':
                        print(question.inclasttest)
                        if question.inclasttest == 'True':
                            print('add')
                            questionset.append(question)
                    elif questiontype == 'All Questions':
                        questionset.append(question)
                    if len(questionset) == num:
                        break
                        
        else:
            # find correct topic to link back to
            for topicset in self.user.topics:
                if topicset.topic == typeoftest:
                    break
            self.b2topic.clicked.connect(lambda: totopicload(topicset,self.user))
            self.title.setText(typeoftest)
            for topic in user.topics:
                if topic.topic == typeoftest:
                    for question in topic.questions:
                        if questiontype == 'Incorrect last testing':
                            if question.inclasttest:
                                questionset.append(question)
                        elif questiontype == 'All Questions':
                            questionset.append(question)
                        if len(questionset) == num:
                            break
        # run test
        print(len(questionset))
        print(questionset)
        if len(questionset)>0:
            print('run2')
            self.finish = False
            self.correct = -1
            self.correctquestions=0
            self.questionset = questionset
            self.quesindex = 0
            self.ans = ''
            self.updatedisplay()
            self.ans1b.clicked.connect(lambda: self.checkans('1'))
            self.ans2b.clicked.connect(lambda: self.checkans('2'))
            self.ans3b.clicked.connect(lambda: self.checkans('3'))
            self.ans4b.clicked.connect(lambda: self.checkans('4'))
            self.ans = ''
        else:
            self.question.setText("No questions fit those options. Go back to main menu")
            
    
    def updatedisplay(self):
        #changes text boxes to questions and answers for next question
        self.question.setText((self.questionset[self.quesindex].question))
        self.ans1.setText((self.questionset[self.quesindex].ans1))
        self.ans2.setText(self.questionset[self.quesindex].ans2)
        self.ans3.setText(self.questionset[self.quesindex].ans3)
        self.ans4.setText(self.questionset[self.quesindex].ans4)
        
    def checkans(self,answer=0):
        # check if its the correct answer and go to next question
        self.correct = self.questionset[self.quesindex].correct
        if int(answer) == int(self.correct):
            self.updateobj(True)
        else:
            self.updateobj(False)
        self.checkend()
        if not self.finish:
            self.quesindex+=1
        self.updatedisplay()
        
    def updateobj(self,correct):
        #update user object with new question successes
        for topic in self.user.topics:
            for question in topic.questions:
                if question.questionID == self.questionset[self.quesindex].questionID:
                    question.attempted+=1
                    if correct:
                        question.successes+=1
                        self.correctquestions+=1
                        question.inclasttest = 'False'
                    else:
                        question.inclasttest = 'True'

    def checkend(self):
        # check if its the end of the test and update database if it is
        if self.quesindex+1 == len(self.questionset):
            self.finish = True
            self.endtest.show()
            self.title_2.setText("Test Complete")
            text="You got "+str(self.correctquestions)+" correct and "+str((len(self.questionset)-self.correctquestions))+" wrong"
            self.message.setText(text)
            updatedatabase(self.user)
        pass    
            
        
    def backtotopicsFunc(self):
        totopicslist(self.user)      
            
                            
            
                    
class TopicMenu(QDialog):
    def __init__(self,topicset,user):
        super(TopicMenu,self).__init__()
        self.user = user
        self.topicset = topicset
        loadUi("topicmenu.ui",self)
        self.error.hide()
        self.questview.hide()
        self.mainmenu.clicked.connect(lambda: tomainmenu(self.user))
        self.backtopics.clicked.connect(self.backtotopicsFunc)
        self.questselect.clicked.connect(self.selectFunc)
        self.quit.clicked.connect(quitfunc)
        self.cancel.clicked.connect(self.cancelfunc)
        self.title.setText(self.topicset.topic)
        self.addQuestions()
    
    def addQuestions(self):
        for questionset in self.topicset.questions:
            item = QListWidgetItem(questionset.question)
            item.setForeground(brush1)
            self.listWidget.addItem(item)
                
    def backtotopicsFunc(self):
        totopicslist(self.user)
    
    def selectFunc(self):
        item = self.listWidget.currentItem()
        if item == None:
            self.error.show()
        else:
            sqliteConnection = sqlite3.connect('StudyCS.db')
            cursor = sqliteConnection.cursor()
            for topic in self.user.topics:
                for questionobject in topic.questions:
                    if questionobject.question == item.text():
                        if questionobject.correct == 1:
                            self.correctanswer = questionobject.ans1
                        if questionobject.correct == 2:
                            self.correctanswer = questionobject.ans2
                        if questionobject.correct == 3:
                            self.correctanswer = questionobject.ans3
                        if questionobject.correct == 4:
                            self.correctanswer = questionobject.ans4
                         
                        self.questinfo.addItem(QListWidgetItem(str(questionobject.question)))
                        self.questinfo.addItem(QListWidgetItem(str(self.correctanswer)))
                        self.questinfo.addItem(QListWidgetItem("Correct: "+str(questionobject.successes)))
                        self.questinfo.addItem(QListWidgetItem("Attempts: "+str(questionobject.attempted)))
                         
                        self.questview.show()
                        break
    def cancelfunc(self):
        self.questinfo.clear()
        self.questview.hide()    
    
class TopicsList(QDialog):
    def __init__(self,user):
        super(TopicsList,self).__init__()
        self.user = user
        loadUi("topicslist.ui",self)
        self.error.hide()
        self.Topictest.hide()
        self.selecttopic.clicked.connect(self.checkclicked)
        self.quit.clicked.connect(quitfunc)
        self.mainmenu.clicked.connect(lambda: tomainmenu(self.user))
        self.topictest.clicked.connect(self.loadtopictest)
        self.loaditems()
        
    def loaditems(self):
        for topicset in self.user.topics:
            item = QListWidgetItem(topicset.topic)
            item.setForeground(brush1)
            self.listWidget.addItem(item)
            
    def checkclicked(self):
        item = self.listWidget.currentItem()
        if item == None:
            self.error.show()
        else:
            for topicset in self.user.topics:
                if topicset.topic == item.text():
                    totopicload(topicset,self.user)
                
    def loadtopictest(self):
        item = self.listWidget.currentItem()
        if item == None:
            self.error.show()
        else:
            def run():
                num = self.spinBox.value()
                questiontype = self.comboBox.currentText()
                for topicset in self.user.topics:
                    if topicset.topic == item.text():
                        setuptest(item.text(),self.user,num,questiontype)
            def cancelfunc():
                self.Topictest.hide()
            self.Topictest.show()
            self.title1.setText("Topic Test\n"+item.text())
            self.cancel.clicked.connect(cancelfunc)
            self.confirm.clicked.connect(run)

def setUpTopics(user):
    sqliteConnection = sqlite3.connect('StudyCS.db')
    cursor = sqliteConnection.cursor()
    topics = cursor.execute("SELECT topicID,topicname FROM topics").fetchall()
    sqliteConnection.commit()
    TOPICS = []
    for topic in topics:
        newobject = topicObj(topic[0],topic[1])
        TOPICS.append(newobject)
    for topicset in TOPICS:
        questions = cursor.execute("SELECT question,ans1,ans2,ans3,ans4,questionID,correct,difficulty FROM questions WHERE questions.topicID = '"+topicset.topicID+"'").fetchall()
        sqliteConnection.commit()
        for questionset in questions:
            questobj = questionObj(questionset[5],topicset.topicID,questionset[0],questionset[1],questionset[2],questionset[3],questionset[4],questionset[6],questionset[7])
            topicset.questions.append(questobj)
    progress = cursor.execute("SELECT questionID,attempted,success,inclasttest FROM questionsuccess WHERE ID = '"+user.ID+"'").fetchall()
    print(progress)
    sqliteConnection.commit()
    for questionprogress in progress:
        for topic in TOPICS:
            for question in topic.questions:
                if int(question.questionID) == int(questionprogress[0]):
                    question.addsuccesses(questionprogress[1],questionprogress[2],questionprogress[3])
    for topic in TOPICS:
        for question in topic.questions:
            try:
                question.attempted
            except:
                question.addsuccesses()
    user.addtopics(TOPICS)
    return user

class MainMenu(QDialog):
    def __init__(self,user,):
        super(MainMenu,self).__init__()
        loadUi("menu.ui",self) 
        self.quicktestopt.hide()
        self.topics.clicked.connect(self.topicsfunc)
        self.quicktest.clicked.connect(self.quicktestfunc)
        self.logout.clicked.connect(self.logoutfunc)
        self.quit.clicked.connect(quitfunc)
        pixmap1 = QPixmap('84043.jpg')
        self.label.setPixmap(pixmap1)
        self.user = user
    def topicsfunc(self):
        totopicslist(self.user)
    def quicktestfunc(self):
        def run():
            num = self.spinBox.value()
            questiontype = self.comboBox.currentText()
            setuptest('quick',self.user,num,questiontype)
        def cancelfunc():
            self.quicktestopt.hide()
        self.quicktestopt.show()
        self.cancel.clicked.connect(cancelfunc)
        self.confirm.clicked.connect(run)
    def settingsfunc(self):
        pass
    def logoutfunc(self):
        del self.user
        tologin()
        

class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("login.ui",self)
        self.loginbutton.clicked.connect(self.loginfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.createaccbutton.clicked.connect(self.gotocreate)
        self.quit.clicked.connect(quitfunc)
        self.incorrectpass.hide()
        self.incorrectpass2.hide()

    def loginfunction(self):
        username=self.username.text()
        password=self.password.text()
        correct,ID = checkLogin(username,password)
        user = userobj(ID)
        if correct:
            self.user = setUpTopics(user)
            tomainmenu(user)
        else:
            self.incorrectpass.show()
            self.incorrectpass2.show()
        
        
    def gotocreate(self):
        createacc=CreateAcc()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex()+1)

class CreateAcc(QDialog):
    def __init__(self):
        super(CreateAcc,self).__init__()
        loadUi("createacc.ui",self)
        self.listWidget.hide()
        self.signupbutton.clicked.connect(self.createaccfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.BTL.clicked.connect(tologin)
        self.quit.clicked.connect(quitfunc)
        
        
    def createaccfunction(self):
        self.listWidget.clear()
        errors = []
        # blank checks
        if self.username.text() == '':
            errors.append("Username cannot be blank")
        if self.firstname.text() == '':
            errors.append("Firstname cannot be blank")
        if self.surname.text() == '':
            errors.append("Surname cannot be blank")
        if self.password.text() == '':
            errors.append("Password cannot be blank")
        if self.username.text() == '':
            errors.append("Confirm Password cannot be blank")
        
        if any(i.isdigit() for i in self.firstname.text()):
            errors.append("Firstname cannot include any numbers")
        if any(i.isdigit() for i in self.surname.text()):
            errors.append("surname cannot include any numbers")
        # password checks
        if self.password.text()==self.confirmpass.text():
            password=self.password.text()
            if len(password) < 10 :
                errors.append('Password must be at least 10 characters long')
            chars = list(""""(){}[]|`¬¦ "%^&"<>:;#~_-+=,@.""")
            if any(x in password for x in chars):
                errors.append('Password must not include any of the characters:')
                characters = ''
                characters+=chars[0]
                for i in chars[1:len(chars)]:
                    characters+=', '+i
                errors.append(characters)   
        else:
            errors.append("Passwords don't match")
        
        
        if len(errors) == 0:
            password = hasher(password)
            username=self.username.text()
            firstname=self.firstname.text()
            surname=self.surname.text()
            acccreate(firstname,surname,username,password)
            tologin()
        else:
            for error in errors:
                self.listWidget.show()
                self.listWidget.addItem(QListWidgetItem(error))

def acccreate(first,sur,user,passw):
    try:
        first = first.title()
        sur = sur.title()
        sqliteConnection = sqlite3.connect('StudyCS.db')
        cursor = sqliteConnection.cursor()
        now = datetime.now()
        joindate = now.strftime("%Y-%m-%d %H:%M:%S")
        ID = (first[0:3]).title()+(sur[0:3]).title()+now.strftime('%d%m%S')
        query = """INSERT INTO accounts VALUES ('"""+ID+"','"+user+"','"+passw+"','"+first+"','"+sur+"','"+str(joindate)+"')"
        cursor.execute(query)
        sqliteConnection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print(502)
    for i in range(4):
        try:
            sqliteConnection = sqlite3.connect('StudyCS.db')
            cursor = sqliteConnection.cursor()
            query = """INSERT INTO questionsuccess VALUES ('"""+ID+"','"+str(i+1)+"',"+'0'+","+'0'+","+'False'+")"
            cursor.execute(query)
            sqliteConnection.commit()
            cursor.close()

        except sqlite3.Error as error:
            print(513)
        
        
            
app=QApplication(sys.argv)
updatedatabase()
mainwindow=Login()
widget=QtWidgets.QStackedWidget()
widget.setWindowTitle("StudyCS.exe")
widget.addWidget(mainwindow)
widget.setFixedWidth(800)
widget.setFixedHeight(600)
widget.show()
app.exec_()

