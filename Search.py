import PyQt5
from PyQt5.QtWidgets import QMessageBox



import Sheets
import Subscriber
import Merlin



def SearchUserID(ID):
    try:
        subscriberData = Sheets.SearchID(ID)
        #Segments the subscriber data list into individual pieces of information that can be used to change the UI as well as the email body message
        email = subscriberData[1]
        fname = subscriberData[2]
        lname = subscriberData[3]
        date = subscriberData[4]
        time = subscriberData[5]
        phoneNumber = subscriberData[6]
        status = subscriberData[7]
        subscriber = Subscriber.Subscriber(fname, lname, email, date, time, phoneNumber, status)
        print('abot dinhi')
        return subscriber
    except:
        box = QMessageBox()
        box.setIcon(QMessageBox.Icon.Information)
        box.setWindowTitle("Search Error")
        box.setDetailedText("The search term is either not available in the Google sheets or is blank. Please enter a value that is in the database and try again.")
        box.setInformativeText('You have entered an invalid or unavailable search term.')
        box.setText('Change Search Value')
        box.show()
        print("change value")

def SearchLastName(surname):
    try:
        #chops up the data inside string to specific variables
        subscriberData = Sheets.SearchLastName(surname)
        email = subscriberData[1]
        fname = subscriberData[2]
        lname = subscriberData[3]
        date = subscriberData[4]
        time = subscriberData[5]
        phoneNumber = subscriberData[6]
        status = subscriberData[7]
        #instantiates a subscriber object from the subscriber class
        subscriber = Subscriber.Subscriber(fname, lname, email, date, time, phoneNumber, status)
        return subscriber
    except:
        box = QMessageBox()
        box.setIcon(QMessageBox.Icon.Information)
        box.setWindowTitle("Search Error")
        box.setDetailedText("The search term is either not available in the Google sheets or is blank. Please enter a value that is in the database and try again.")
        box.setInformativeText('You have entered an invalid or unavailable search term.')
        box.setText('Change Search Value')
        box.show()
        print("change value")