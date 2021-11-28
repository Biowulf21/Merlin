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


class UI(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        UI.UpdateEmailTextBox(self, "", "", "")
        self.show()

        self.ui.xuMailButton.clicked.connect(self.SearchUserID)
        #print('back in main after email search')
        self.ui.lNameButton.clicked.connect(self.SearchLastName)
        #print('back in main after last name search')
        self.ui.selectSubButton.clicked.connect(self.SelectSubscriber)

    #def UpdateUserInfo(self):

       # self.ui.fName.text() = 
    def SearchUserID(self):
        xuMail = self.ui.xuMailLineEdit.text()
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
        print("In Search ID")

    def SearchLastName(self):
        #TODO: Search Function for last name should not be case sensitive
        lastName = self.ui.lNameLineEdit.text()
        subscriberData = Sheets.SearchLastName(lastName)
        email = subscriberData[1]
        fname = subscriberData[2]
        lname = subscriberData[3]
        date = subscriberData[4]
        time = subscriberData[5]
        phoneNumber = subscriberData[6]
        status = subscriberData[7]

        subscriber = Subscriber.Subscriber(fname, lname, email, date, time, phoneNumber, status)
        #UI.UpdateUserInfo(self)
        self.ui.xuMailLineEdit.clear()
        UI.updateUser(self,subscriber)
        #print("In Search Last Name")
        


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
        name = self.ui.fName.text()
        date = self.ui.claimDate.text()
        time = self.ui.claimTime.text()

        self.UpdateEmailTextBox(name, date, time)
    










if __name__ == "__main__":
    app = QApplication([])
    win = UI()
    win.show()
    sys.exit(app.exec())


