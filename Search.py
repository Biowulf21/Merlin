import Subscriber
import Sheets

class Search():
    #FIXME: QLINEEDITS SHOULD CLEAR AFTER SEARCHING USING ANOTHER QLINEEDIT
    def SearchUserID(self):
        self.ui.lNameLineEdit.clear()
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
        self.Search.updateUser(self, subscriber)

    def SearchLastName(self):
        self.ui.xuMail.clear()
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
        print(subscriber.getLastName)
        #UI.UpdateUserInfo(self)
        self.Search.updateUser(self,subscriber)


    def updateUser(self, subscriber):
        self.ui.lName.setText(subscriber.getLastName)
        self.ui.fName.setText(subscriber.getFirstName)
        self.ui.xuMail.setText(subscriber.getEmail)
        self.ui.pNumber.setText(subscriber.getPhoneNumber)
        self.ui.claimDate.setText(subscriber.getDate)
        self.ui.claimTime.setText(subscriber.getTime)
        self.ui.status.setText(subscriber.getStatus)