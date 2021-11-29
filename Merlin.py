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
import Sheets
import Subscriber


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


    def Change(self, x):
        print('Dick')
        #print(x)
        with open ("EmailBody.txt", "w") as file:
            file.write(x)
#FIXME: TEXTEDIT FOR EDITING EMAIL TEMPLATE CAN'T BE SEEN BY OTHER METHODS AND THUS CAN'T WRITE TO FILE
#WILL PROBABLY NEED TO REFACTOR SHITTY CODE YAWA
    def ChangeEmailTemplate(self):

        self.dlg = QDialog()
        self.dlg.setWindowTitle("Edit Email")
 
        self.window = Ui_EmailBodyWindow()
        self.window.setupUi(self.dlg)
 
        
        with open ("EmailBody.txt", "r") as file:
            body = file.read()
            self.window.EmailTemplateTextEdit.setPlainText(body)
            file.close()

        print(self.emailText)
        #self.window.emailTemplateSaveBtn.clicked.connect(lambda: self.Change(self.emailText))
            

        self.dlg.exec()
        
       # self.tmplt = ChangeTemplate.Template
       # self.window = QtWidgets.QDialog()
       # #Calls change email template method from Changetemplate file and uses self.window as argument
       # self.tmplt.ChangeEmailTemplate(self, self.window)



    def ChangeSubjectTemplate(self):
        pass

 
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
            self.box = QMessageBox()
            self.box.setIcon(QMessageBox.Icon.Information)
            self.box.setWindowTitle("Search Error")
            self.box.setDetailedText("The search term is either not available in the Google sheets or is blank. Please enter a value that is in the database and try again.")
            self.box.setInformativeText('You have entered an invalid or unavailable search term.')
            self.box.setText('Change Search Value')
            self.box.show()
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
            self.box = QMessageBox()
            self.box.setIcon(QMessageBox.Icon.Information)
            self.box.setWindowTitle("Search Error")
            self.box.setDetailedText("The search term is either not available in the Google sheets or is blank. Please enter a value that is in the database and try again.")
            self.box.setInformativeText('You have entered an invalid or unavailable search term.')
            self.box.setText('Change Search Value')
            self.box.show()
            print("change value")
        
        


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
        self.ui.status.setText(subscriber.getStatus)

    def SelectSubscriber(self):
        fname = self.ui.fName.text()
        lname = self.ui.lName.text()
        date = self.ui.claimDate.text()
        time = self.ui.claimTime.text()

        self.UpdateEmailTextBox(fname, date, time)
        self.ui.receipentLineEdit.setText(fname + " " + lname)


    def sendMessage(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Message Successfully Sent")
        
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
        msgBox.setText("Message sent to " + receipient + " - " + sendName + " " + sendLName + " - " + receipient)
        msgBox.show()
        if len(failedTo) != 0:
            print("Failed to send to: ")
            print(*failedTo, sep = ", ")



    










if __name__ == "__main__":
    app = QApplication([])
    win = UI()
    win.setWindowTitle('Merlin - Crusader Email Wizard')
    app.setWindowIcon(QIcon('Merlin-Icon.ico'))
    win.show()
    sys.exit(app.exec())


