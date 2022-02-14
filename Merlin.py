#!/usr/bin/env python3
from threading import *
from time import sleep
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox
from PyQt5.QtGui import QIcon
from re import sub
from os import link, replace
# from modules import Search
# from modules import SendMail
# from modules import Sheets
# from modules import Subscriber
# from modules import Template
import modules.Search as search
import modules.SendMail as sendmail
import modules.Sheets as sheets
import modules.Subscriber as subs
import modules.Template as temp
from ui_files.UI import Ui_MainWindow
from ui_files.Ui_EmailBody_UI import Ui_EmailBodyWindow
from ui_files.Ui_SubjectEmail_UI import Ui_Dialog

import sys


class UI(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Updates the UI of the Subscriber portion of the GUI
        # Starts of with empty string
        UI.UpdateEmailTextBox(self, "", "", "")

        # self.ui.bulkEmailProgressBar.set

        # Declaring the Buttons
        self.ui.xuMailButton.clicked.connect(self.SearchUserID)
        self.ui.lNameButton.clicked.connect(self.SearchLastName)

        self.ui.selectSubButton.clicked.connect(self.SelectSubscriber)
        self.ui.emailSendButton.clicked.connect(self.sendMessage)

        self.ui.actionEmail.triggered.connect(self.ChangeEmailTemplate)
        self.ui.actionSubject.triggered.connect(self.ChangeSubjectTemplate)

        self.ui.bulkEmailSender.clicked.connect(self.GetEmails)

    def GetEmails(self):
        #print('sulod sa get emails')
        listofReceipients = []
        bulkEmails = self.ui.bulkEmailsTextEdit.toPlainText()
        if bulkEmails == "":
            msg = QMessageBox()
            msg.setText("Please enter emails")
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.exec()
        else:

            # gets each email from the text edit string and makes them individual elements inside List
            listofReceipients = bulkEmails.split()
            #print(f"text inside text Edit is {bulkEmails}")
            # print(f"list is {listofReceipients}"

            self.sendBulkEmails(listofReceipients)

        # sends emails to a group of emails

    def sendBulkEmails(self, listofReceipients):
        self.ui.sentListWidget.clear()
        self.ui.failedListWidget.clear()
        # list of emails that were sent successfuly
        sentList = []

        # list of emails that were unsucessfuly sent
        unsentList = []

        # sets the maximum value of the progress bar to be equal to the length of the list of receipients
        maxValue = len(listofReceipients)
        self.ui.bulkEmailProgressBar.setMaximum(maxValue)

        print(f"maxvalue is {maxValue}")
        # sets the minimum or initial value or the progress bar
        progressValue = 1

        # reads the email subject text file and sets as the email subject line
        with open('EmailSubject.txt', 'r') as file:
            subject = file.read()

        for receipient in listofReceipients:
            # gets the information of every receipient
            receipientInfo = sheets.SearchID(receipient)

            # chops up information into individual variables

            if receipientInfo[15] != "None":
                try:
                    print('naa sa try')
                    email = receipientInfo[1]
                    name = receipientInfo[4]
                    link = receipientInfo[3]
                    date = receipientInfo[16]
                    time = receipientInfo[14]
                    phoneNumber = receipientInfo[6]
                    status = receipientInfo[15]

                    # calls replacetemplate to replace NAME TIME AND DATE texts inside template
                    body = self.ReplaceTemplate(name, date, time, link)
                    progressValue += 1

                    print(f"progress value is {progressValue}")

                    #print(f"receipient info is: {fname} {lname} - {email}")

                    newStatus = sendmail.BulkEmailSender(
                        subject, body, email, name)
                    print(f"new status = {newStatus[1]}")
                    if newStatus[1] == "Notified":
                        sentList.append(newStatus[0])
                    elif newStatus[1] == "Email Failed":
                        unsentList.append(newStatus[0])
                    else:
                        pass

                    # self.UpdateStatus(newStatus)
                    sleep(1)

                except Exception as e:
                    exception_type, exception_object, exception_traceback = sys.exc_info()
                    filename = exception_traceback.tb_frame.f_code.co_filename
                    line_number = exception_traceback.tb_lineno

                    print("Exception type: ", exception_type)
                    print("File name: ", filename)
                    print("Line number: ", line_number)
                    print(e)
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

    def ReplaceTemplate(self, firstName, date, time, link):
        # reads the email body text file and sets as email body
        with open('compose.md', 'r') as file:
            body = file.read()
            # Changes all the instances of NAME, DATE and TIME that is in the template in the Emailbody.txt file
            for word in (("NAME", firstName), ("DATE", date), ("TIME", time), ("LINK", link)):
                body = body.replace(*word)
            return body


# FIXME: Program reads Template but when editing, not pressing the save button (just exiting by pressing escape) still updates the template
# Same case for both updating the email body template and for the subject template

    def ChangeSubjectTemplate(self):
        self.dg = QDialog()
        self.win = Ui_Dialog()
        self.win.setupUi(self.dg)
        subjectTextEdit = self.win.subjectPlainTextEdit.toPlainText()
        # calls changemailbodytemplate from Template module and inputs the text
        temp.ChangeEmailSubjectTemplate(subjectTextEdit)

    def ChangeEmailTemplate(self):

        self.dlg = QDialog()
        self.dlg.setWindowTitle("Edit Email Body")

        self.window = Ui_EmailBodyWindow()
        self.window.setupUi(self.dlg)

        emailBodyText = self.window.EmailTemplateTextEdit.toPlainText()
        temp.ChangeEmailBodyTemplate(emailBodyText)

    def UpdateEmailTemplate(self, x):
        with open('compose.md', 'w') as file:
            file.write(self.updatedText)

    def SearchUserID(self):
        xuMail = self.ui.xuMailLineEdit.text()
        self.ui.lNameLineEdit.clear()
        subscriberSearch = search.SearchUserID(xuMail)
        self.updateUser(subscriberSearch)

    def SearchLastName(self):
        # TODO: Search Function for last name should not be case sensitive
        lastName = self.ui.lNameLineEdit.text()
        self.ui.xuMailLineEdit.clear()
        subscriberSearch = search.SearchLastName(lastName)
        self.updateUser(subscriberSearch)

    # updates the email body textEdit

    def UpdateEmailTextBox(self, lname, claimDate, claimTime):

        name = lname
        date = str(claimDate)
        time = str(claimTime)

        with open("compose.md", 'r') as file:
            body = file.read()
            for word in (("NAME", name), ("DATE", date), ("TIME", time)):
                body = body.replace(*word)
                # print(body)

        with open("EmailSubject.txt", 'r') as file:
            subject = file.read()

        self.ui.subjectLineEdit.setText(subject)
        self.ui.emailBodyText.setText(body)

    # updates the subscriber information UI
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
        returnStatus = sendmail.sendEmail(
            subject, body, receipient, sendName, sendLName)
        newStatus = returnStatus[1]
        # successSent.append(returnStatus[0])
        #print(f"list of successfully sent: {successSent}")
        self.UpdateStatus(newStatus)

    def UpdateStatus(self, status):
        print('updating status')
        # self.ui.status.setText(status)
        print('after updating status')


if __name__ == "__main__":
    app = QApplication([])
    win = UI()
    win.setWindowTitle('Merlin - Crusader Email Wizard')
    app.setWindowIcon(QIcon('Merlin-Icon.ico'))
    win.showMaximized()
    sys.exit(app.exec())
