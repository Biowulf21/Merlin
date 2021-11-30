#GUI Imports
from os import replace
from re import sub
from typing import OrderedDict
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox
import sys

from UI import Ui_MainWindow
from Ui_EmailBody_UI import Ui_EmailBodyWindow

#module imports
import Template
import Search
import SendMail


#email imports
import smtplib
from email.message import EmailMessage

from Ui_SubjectEmail_UI import Ui_Dialog




class UI(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)



        #Updates the UI of the Subscriber portion of the GUI
        #Starts of with empty string
        UI.UpdateEmailTextBox(self, "", "", "")
        

        #Declaring the Buttons
        self.ui.xuMailButton.clicked.connect(self.SearchUserID)
        self.ui.lNameButton.clicked.connect(self.SearchLastName)

        self.ui.selectSubButton.clicked.connect(self.SelectSubscriber)
        self.ui.emailSendButton.clicked.connect(self.sendMessage)

        self.ui.actionEmail.triggered.connect(self.ChangeEmailTemplate)
        self.ui.actionSubject.triggered.connect(self.ChangeSubjectTemplate)


#FIXME: Program reads Template but when editing, not pressing the save button (just exiting by pressing escape) still updates the template
#Same case for both updating the email body template and for the subject template

    def ChangeSubjectTemplate(self):
        self.dg = QDialog()
        self.win = Ui_Dialog()
        self.win.setupUi(self.dg)
        subjectTextEdit = self.win.subjectPlainTextEdit.toPlainText()
        #calls changemailbodytemplate from Template module and inputs the text
        Template.ChangeEmailSubjectTemplate(subjectTextEdit)


        


    def ChangeEmailTemplate(self):

        self.dlg = QDialog()
        self.dlg.setWindowTitle("Edit Email Body")
 
        self.window = Ui_EmailBodyWindow()
        self.window.setupUi(self.dlg)

        emailBodyText = self.window.EmailTemplateTextEdit.toPlainText()
        Template.ChangeEmailBodyTemplate(emailBodyText)




    def UpdateEmailTemplate(self, x):
        with open ('EmailBody.txt', 'w') as file:
            file.write(self.updatedText)



 
    def SearchUserID(self):
        xuMail = self.ui.xuMailLineEdit.text()
        self.ui.lNameLineEdit.clear()
        subscriberSearch = Search.SearchUserID(xuMail)
        self.updateUser(subscriberSearch)
        

    def SearchLastName(self):
        #TODO: Search Function for last name should not be case sensitive
        lastName = self.ui.lNameLineEdit.text()
        self.ui.xuMailLineEdit.clear()
        subscriberSearch = Search.SearchLastName(lastName)
        self.updateUser(subscriberSearch)
        
        


    def UpdateEmailTextBox(self, lname, claimDate, claimTime):

        name = lname
        date = str(claimDate)
        time = str(claimTime)
        
        with open ("EmailBody.txt", 'r') as file:
            body = file.read()
            for word in (("NAME", name), ("DATE", date), ("TIME", time)):
                body = body.replace(*word)
                #print(body)
        
        with open ("EmailSubject.txt", 'r') as file:
            subject = file.read()
        
        self.ui.subjectLineEdit.setText(subject)
        self.ui.emailBodyText.setText(body)


    def updateUser(self, subscriber):
        self.ui.lName.setText(subscriber.getLastName)
        self.ui.fName.setText(subscriber.getFirstName)
        self.ui.xuMail.setText(subscriber.getEmail)
        self.ui.pNumber.setText(subscriber.getPhoneNumber)
        self.ui.claimDate.setText(subscriber.getDate)
        self.ui.claimTime.setText(subscriber.getTime)
        self.status = subscriber.getStatus
        #print(f"status is {subscriber.getStatus}")
        self.ui.status.setText(subscriber.getStatus)

    def SelectSubscriber(self):
        fname = self.ui.fName.text()
        lname = self.ui.lName.text()
        date = self.ui.claimDate.text()
        time = self.ui.claimTime.text()

        self.UpdateEmailTextBox(fname, date, time)
        self.ui.receipentLineEdit.setText(fname + " " + lname)


    def sendMessage(self):
        subject = self.ui.subjectLineEdit.text()
        body = self.ui.emailBodyText.toPlainText()
        #print(f"body of the textEdit is {body}")
        receipient = self.ui.xuMail.text()
        sendName = self.ui.fName.text()
        sendLName = self.ui.lName.text()
        newStatus = SendMail.sendEmail(subject, body, receipient, sendName, sendLName)
        self.UpdateStatus(newStatus)




    def UpdateStatus(self, status):
        print('updating status')
        self.ui.status.setText(status)
        print('after updating status')


    


if __name__ == "__main__":
    app = QApplication([])
    win = UI()
    win.setWindowTitle('Merlin - Crusader Email Wizard')
    app.setWindowIcon(QIcon('Merlin-Icon.ico'))
    win.show()
    sys.exit(app.exec())


