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
            #Sheets.WriteStatus(email)
            ##msgBox.setText("Message sent to " + email + " - " + firstName + " " + lastName + " - " + email)
            ##msgBox.exec()
            sent = sent+1
            #FIXME: Should create a list of all receipients that have been sent an email and all receipients whose emails failed
            #FIXME: Status setting should be fixed as right now, there is no way on confirmting that a subscriber is alaready notified
            sentList.append(sendTo)
            #print(body)
           # return "Notified"
    except Exception as e:
        failedTo.append(sendTo)
        
        #summary report 

        if len(failedTo) != 0:
            print("Failed to send to: ")
            print(*failedTo, sep = ", ")
        #return "Not Notified"

    returnList.append(sentList)
    returnList.append(failedTo)
    returnList.append("Notified")
    print(returnList)
    return returnList