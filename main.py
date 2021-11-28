#GUI Imports
from os import replace
from re import sub
from typing import OrderedDict
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from UI import Ui_MainWindow

import Sheets
import Subscriber
import sendMail

#email imports

import smtplib
from email.message import EmailMessage



class UI(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.msg = sendMail.SendMessage()
        UI.UpdateEmailTextBox(self, "", "", "")
        self.show()

        self.ui.xuMailButton.clicked.connect(self.SearchUserID)
        #print('back in main after email search')
        self.ui.lNameButton.clicked.connect(self.SearchLastName)
        #print('back in main after last name search')
        self.ui.selectSubButton.clicked.connect(self.SelectSubscriber)
        self.ui.emailSendButton.clicked.connect(self.sendMessage)

    #def UpdateUserInfo(self):
    #TODO: Refactor and Modularize code

    
       # self.ui.fName.text() = 
    def SearchUserID(self):
        xuMail = self.ui.xuMailLineEdit.text()
        try:
            subscriberData = Sheets.SearchID(xuMail)
            email = subscriberData[1]
            fname = subscriberData[2]
            lname = subscriberData[3]
            date = subscriberData[4]
            time = subscriberData[5]
            phoneNumber = subscriberData[6]
            status = subscriberData[7]
            subscriber = Subscriber.Subscriber(fname, lname, email, date, time, phoneNumber, status)
            self.ui.lNameLineEdit.clear()
            UI.updateUser(self, subscriber)
        except:
            print("change value")

    def SearchLastName(self):
        #TODO: Search Function for last name should not be case sensitive
        lastName = self.ui.lNameLineEdit.text()
        try:
            subscriberData = Sheets.SearchLastName(lastName)
            email = subscriberData[1]
            fname = subscriberData[2]
            lname = subscriberData[3]
            date = subscriberData[4]
            time = subscriberData[5]
            phoneNumber = subscriberData[6]
            status = subscriberData[7]
            subscriber = Subscriber.Subscriber(fname, lname, email, date, time, phoneNumber, status)
            self.ui.xuMailLineEdit.clear()
            UI.updateUser(self,subscriber)
        except:
            print("Change value")
        
        


    def UpdateEmailTextBox(self, lname, claimDate, claimTime):

        name = lname
        date = str(claimDate)
        time = str(claimTime)
        
        with open ("EmailBody.txt", 'r') as file:
            body = file.read()
            for word in (("NAME", name), ("DATE", date), ("TIME", time)):
                body = body.replace(*word)
                print(body)
        
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
        self.ui.status.setText(subscriber.getStatus)

    def SelectSubscriber(self):
        fname = self.ui.fName.text()
        lname = self.ui.lName.text()
        date = self.ui.claimDate.text()
        time = self.ui.claimTime.text()

        self.UpdateEmailTextBox(fname, date, time)
        self.ui.receipentLineEdit.setText(fname + lname)


    def sendMessage(self):
        sender = "crusaderyearbook@xu.edu.ph"
        password = "uisjoyfegjgudwpp"

        subject = self.ui.subjectLineEdit.text()
        body = self.ui.emailBodyText.toPlainText()
        receipient = self.ui.xuMail.text()
        sendName = self.ui.fName.text()
        sendLName = self.ui.lName.text()

        #print(str(all) + " recipients found.\n")
        sent = 0
        failedTo = []; 

        sendTo = receipient
        message = EmailMessage()
        message['Subject'] = subject
        message['From'] = sender
        message['To'] = sendTo
        message.set_content(body)

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.login(sender, password)
                smtp.send_message(message)

                sent = sent+1
        except Exception as e:
            failedTo.append(sendTo)
        
        #summary report 
        print("Message sent to " + receipient + " - " + sendName + sendLName + " - " + receipient)
        if len(failedTo) != 0:
            print("Failed to send to: ")
            print(*failedTo, sep = ", ")



    










if __name__ == "__main__":
    app = QApplication([])
    win = UI()
    win.show()
    sys.exit(app.exec())


