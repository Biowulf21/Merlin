#GUI Imports
from os import replace
from re import sub
from typing import OrderedDict
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox
import sys
from time import sleep
from threading import *

from UI import Ui_MainWindow
from Ui_EmailBody_UI import Ui_EmailBodyWindow

#module imports
import Template
import Search
import SendMail
import Sheets


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

        #self.ui.bulkEmailProgressBar.set
        

        #Declaring the Buttons
        self.ui.xuMailButton.clicked.connect(self.SearchUserID)
        self.ui.lNameButton.clicked.connect(self.SearchLastName)

        self.ui.selectSubButton.clicked.connect(self.SelectSubscriber)
        self.ui.emailSendButton.clicked.connect(self.sendMessage)

        self.ui.actionEmail.triggered.connect(self.ChangeEmailTemplate)
        self.ui.actionSubject.triggered.connect(self.ChangeSubjectTemplate)

        self.ui.bulkEmailSender.clicked.connect(self.StartThreadOne)

    def StartThreadOne(self):
        self.ui.statusbar.showMessage('Sending Emails')
        print('sulod sa threadings')
        self.threadOne = Thread(target=self.GetEmails())

    def GetEmails(self):
        print('sulod sa get emails')
        listofReceipients = []
        bulkEmails = self.ui.bulkEmailsTextEdit.toPlainText()
        #gets each email from the text edit string and makes them individual elements inside List
        listofReceipients = bulkEmails.split()
        #print(f"text inside text Edit is {bulkEmails}")
        #print(f"list is {listofReceipients}"
       
        self.sendBulkEmails(listofReceipients)


        #sends emails to a group of emails
    def sendBulkEmails(self, listofReceipients):
        self.ui.sentListWidget.clear()
        self.ui.failedListWidget.clear()
        #list of emails that were sent successfuly
        sentList = []

        #list of emails that were unsucessfuly sent
        unsentList = []



        #sets the maximum value of the progress bar to be equal to the length of the list of receipients
        self.ui.bulkEmailProgressBar.setMaximum(len(listofReceipients)+1)


        maxValue = len(listofReceipients)+1
        #print(f"maxvalue is {maxValue}")
        #sets the minimum or initial value or the progress bar
        progressValue = 1
      
        #reads the email subject text file and sets as the email subject line
        with open('EmailSubject.txt', 'r') as file:
            subject = file.read()

        for receipient in listofReceipients:
            #gets the information of every receipient
            receipientInfo = Sheets.SearchID(receipient)
            print(f"receipient info is {receipientInfo}")
            #chops up information into individual variables
            
            if receipientInfo[7] != "None":
                try:
                    print('naa sa try')
                    email = receipientInfo[1]
                    fname = receipientInfo[2]
                    lname = receipientInfo[3]
                    date = receipientInfo[4]
                    time = receipientInfo[5]
                    phoneNumber = receipientInfo[6]
                    status = receipientInfo[7]

                    #calls replacetemplate to replace NAME TIME AND DATE texts inside template
                    body = self.ReplaceTemplate(fname, date, time)
                    progressValue += 1
                    print(f"progress value is {progressValue}")
                    

                    #print(f"receipient info is: {fname} {lname} - {email}")

                    newStatus = SendMail.BulkEmailSender(subject, body, email, fname, lname)
                    print(f"new status = {newStatus[1]}")
                    if newStatus[1] == "Notified":
                        sentList.append(newStatus[0])
                    elif newStatus[1] == "Email Failed": 
                        unsentList.append(newStatus[0])
                    else:
                        pass

                    #self.UpdateStatus(newStatus)
                    sleep(0.5)
                
                except:
                    print('naa sa except')
                    pass
            else:
                print('naa sa else')
                unsentList.append(receipientInfo[1])
                progressValue += 1
            self.ui.bulkEmailProgressBar.setValue(progressValue)


            print(f"sentList is {sentList}\n\n")
            print(f"unsentList is {unsentList}")



            

        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Icon.Information)
        msgBox.setText('Emails Sent')
        self.ui.statusbar.showMessage('Emails sent')
        msgBox.exec()
        if (progressValue == maxValue):
            sleep(1)
            self.ui.bulkEmailProgressBar.setValue(0)
        self.ui.sentListWidget.addItems(sentList)
        self.ui.failedListWidget.addItems(unsentList)

        
    def ReplaceTemplate(self, firstName, date, time):
        #reads the email body text file and sets as email body
        with open ('EmailBody.txt', 'r') as file:
            body = file.read()
            #Changes all the instances of NAME, DATE and TIME that is in the template in the Emailbody.txt file
            for word in (("NAME", firstName), ("DATE", date), ("TIME", time)):
                body = body.replace(*word)
            return body



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

    #updates the subscriber information UI
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
        successSent = []
        subject = self.ui.subjectLineEdit.text()
        body = self.ui.emailBodyText.toPlainText()
        #print(f"body of the textEdit is {body}")
        receipient = self.ui.xuMail.text()
        sendName = self.ui.fName.text()
        sendLName = self.ui.lName.text()
        returnStatus = SendMail.sendEmail(subject, body, receipient, sendName, sendLName)
        newStatus = returnStatus[1]
        #successSent.append(returnStatus[0])
        #print(f"list of successfully sent: {successSent}")
        self.UpdateStatus(newStatus)




    def UpdateStatus(self, status):
        print('updating status')
        #self.ui.status.setText(status)
        print('after updating status')


    


if __name__ == "__main__":
    app = QApplication([])
    win = UI()
    win.setWindowTitle('Merlin - Crusader Email Wizard')
    app.setWindowIcon(QIcon('Merlin-Icon.ico'))
    win.show()
    sys.exit(app.exec())


