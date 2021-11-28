#GUI Imports
from re import sub
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
        self.show()

        self.ui.xuMailButton.clicked.connect(self.SearchUserID)
        self.ui.lNameButton.clicked.connect(self.SearchLastName)

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
        print("In Search Last Name")
        


    def updateUser(self, subscriber):
        self.ui.lName.setText(subscriber.getLastName)
        self.ui.fName.setText(subscriber.getFirstName)
        self.ui.xuMail.setText(subscriber.getEmail)
        self.ui.pNumber.setText(subscriber.getPhoneNumber)
        self.ui.claimDate.setText(subscriber.getDate)
        self.ui.claimTime.setText(subscriber.getTime)
        self.ui.status.setText(subscriber.getStatus)
    










if __name__ == "__main__":
    app = QApplication([])
    win = UI()
    win.show()
    sys.exit(app.exec())


