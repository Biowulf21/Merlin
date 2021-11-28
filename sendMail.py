
import smtplib
from email.message import EmailMessage

from PyQt5.QtWidgets import QMainWindow
import UI


class SendMessage(object):
        
    



    def sendMessage(self):
        self.UI = UI.Ui_MainWindow()
        sender = "crusaderyearbook@xu.edu.ph"
        password = "uisjoyfegjgudwpp"

        

        subject = self.UI.subjectLineEdit.text()
        body = self.UI.emailBodyText.toPlainText()
        receipient = self.UI.xuMail.text()
        sendName = self.UI.fName.text()

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
        print("Message sent to " + receipient + " - " + receipient)
        if len(failedTo) != 0:
            print("Failed to send to: ")
            print(*failedTo, sep = ", ")

