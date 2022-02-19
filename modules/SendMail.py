from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import PyQt5
from PyQt5.QtWidgets import QMessageBox
import sys
import smtplib
from smtplib import SMTP
from email.message import EmailMessage

import markdown
from modules.settings import (HOST, PORT, SENDER, DISPLAY_NAME,
                              PASSWORD, RECIPIENT, MESSAGE_FILE)

import modules.Sheets as sheets

# TODO: Have markdown text formatted into html and send it as email body for formmated texr


def sendEmail(subject, body, email, firstName, lastName):
    msgBox = QMessageBox()
    msgBox.setWindowTitle("Message Successfully Sent")

    sender = "crusaderyearbook@xu.edu.ph"
    password = "uisjoyfegjgudwpp"
    #print(str(all) + " recipients found.\n")
    sent = 0
    failedTo = []
    sendTo = email
    message = EmailMessage()
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = sendTo
    message.set_content(body)
    try:
        with smtplib.SMTP_SSL(HOST, PORT) as smtp:
            #smtp.login(sender, password)
            # print('sending...')
            # smtp.send_message(message)
            sheets.WriteStatus(email)
            #print('internet is slow')
            msgBox.setText("Message sent to " + email + " - " +
                           firstName + " " + lastName + " - " + email)
            msgBox.exec()
            sent = sent+1
            return "Notified"
    except Exception as e:
        failedTo.append(sendTo)

        # summary report

        if len(failedTo) != 0:
            print("Failed to send to: ")
            print(*failedTo, sep=", ")
        return "Not Notified"


def BulkEmailSender(subject, body, email, name, server):
    print('in send mail')
    sender = SENDER
    password = PASSWORD
    #print(str(all) + " recipients found.\n")
    sent = 0

    sentList = []
    unsentList = []
    failedTo = []

    try:

        server.login(user=SENDER, password=PASSWORD)
        print('after login')
        multipart_msg = MIMEMultipart("alternative")

        multipart_msg["Subject"] = subject
        multipart_msg["From"] = DISPLAY_NAME
        multipart_msg["To"] = email
        print('after email deets')

        text = body
        html = markdown.markdown(text)
        # print(f'text is {text}')
        # print(f'html is {html}')
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")
        multipart_msg.attach(part1)
        multipart_msg.attach(part2)

        server.sendmail(SENDER, email, multipart_msg.as_string())
        print('after sending')
        sheets.WriteStatus(email)
        #msgBox.setText("Message sent to " + email + " - " + firstName + " " + lastName + " - " + email)
        # msgBox.exec()
        sent = sent+1
        # FIXME: Should create a list of all receipients that have been sent an email and all receipients whose emails failed
        # FIXME: Status setting should be fixed as right now, there is no way on confirmting that a subscriber is alaready notified
        # append to successfuly sent emails and will return a list with an email that was successfuly sent as well as the notified status
        sentList.append(email)
        sentList.append("Notified")
        print(f"sent to {name}")
        return sentList
    except Exception as e:
        exception_type, exception_object, exception_traceback = sys.exc_info()
        filename = exception_traceback.tb_frame.f_code.co_filename
        line_number = exception_traceback.tb_lineno

        print("Exception type: ", exception_type)
        print("File name: ", filename)
        print("Line number: ", line_number)
        print(e)
        failedTo.append(email)
        # append to unsuccesfully sent emails and will return a list with an  email that was unsuccessfully sent as well as the "Email Failed status"
        unsentList.append(email)
        unsentList.append('Email Failed')

        # summary report
        if len(failedTo) != 0:
            print("Failed to send to: ")
            print(*failedTo, sep=", ")
        return "Not Notified"
