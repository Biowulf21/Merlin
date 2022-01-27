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
        fname = subscriberData[4]
        lname = subscriberData[3]
        date = subscriberData[16]
        time = subscriberData[14]
        phoneNumber = subscriberData[6]
        status = subscriberData[15]
        subscriber = Subscriber.Subscriber(fname, lname, email, date, time, phoneNumber, status)
        print('abot dinhi')
        return subscriber
    except:
        print("change value")

def SearchLastName(surname):
    print("in 2nd search lname")
    try:
        print('in try')
        #chops up the data inside string to specific variables
        subscriberData = Sheets.SearchLastName(surname)
        print(f'subscriber data is {subscriberData}')
        email = subscriberData[1]
        fname = subscriberData[4]
        lname = subscriberData[3]
        date = subscriberData[16]
        time = subscriberData[14]
        phoneNumber = subscriberData[6]
        status = subscriberData[15]
        #instantiates a subscriber object from the subscriber class
        subscriber = Subscriber.Subscriber(fname, lname, email, date, time, phoneNumber, status)
        return subscriber
    except:
        print("change value")