import PyQt5
from PyQt5.QtWidgets import QMessageBox

import smtplib
from email.message import EmailMessage

import Sheets


def sendEmail(subject, body, email, firstName, lastName):
    msgBox = QMessageBox()
    msgBox.setWindowTitle("Message Successfully Sent")
    
    sender = "crusaderyearbook@xu.edu.ph"
    password = "uisjoyfegjgudwpp"
    #print(str(all) + " recipients found.\n")
    sent = 0
    failedTo = []; 
    sendTo = email
    message = EmailMessage()
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = sendTo
    message.set_content(body)
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            #smtp.login(sender, password)
            #print('sending...')
            #smtp.send_message(message)
            Sheets.WriteStatus(email)
            #print('internet is slow')
            msgBox.setText("Message sent to " + email + " - " + firstName + " " + lastName + " - " + email)
            msgBox.exec()
            sent = sent+1
            return "Notified"
    except Exception as e:
        failedTo.append(sendTo)
        
        #summary report 

        if len(failedTo) != 0:
            print("Failed to send to: ")
            print(*failedTo, sep = ", ")
        return "Not Notified"

def BulkEmailSender(subject, body, email, firstName, lastName):
    returnList = []    
    sender = "crusaderyearbook@xu.edu.ph"
    password = "uisjoyfegjgudwpp"
    #print(str(all) + " recipients found.\n")
    sent = 0
    
    sentList = []
    unsentList =[]
    failedTo = []


    sendTo = email
    message = EmailMessage()
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = sendTo
    message.set_content(body)
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            #smtp.login(sender, password)
            #smtp.send_message(message)
            #Sheets.WriteStatus(email)
            ##msgBox.setText("Message sent to " + email + " - " + firstName + " " + lastName + " - " + email)
            ##msgBox.exec()
            sent = sent+1
            #FIXME: Should create a list of all receipients that have been sent an email and all receipients whose emails failed
            #FIXME: Status setting should be fixed as right now, there is no way on confirmting that a subscriber is alaready notified
            
            #append to successfuly sent emails and will return a list with an email that was successfuly sent as well as the notified status
            sentList.append(sendTo)
            sentList.append("Notified")
            #print(f"sentlist is: {sentList}")
            return sentList
    except Exception as e:
        failedTo.append(sendTo)
        #append to unsuccesfully sent emails and will return a list with an  email that was unsuccessfully sent as well as the "Email Failed status"
        unsentList.append(sendTo)
        unsentList.append('Email Failed')
        
        #summary report
        if len(failedTo) != 0:
            print("Failed to send to: ")
            print(*failedTo, sep = ", ")
        #return "Not Notified"
