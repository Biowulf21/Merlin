
import smtplib
from email.message import EmailMessage

sender = "crusaderyearbook@xu.edu.ph"
password = "uisjoyfegjgudwpp"


def advisory(name, date, time, receipient):
    subject = "[Crusader Yearbook] Claiming Yearbook"
    messagebody = 'Greetings {}, \n\nYour yearbook is ready to claim on {} at {}\n\nIn Service\nThe Crusader Yearbook'.format(name, date, time)

    sendMessage(subject, messagebody, receipient, name)


def sendMessage(subject, body, receipient, name):
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
    print("Message sent to " + receipient + " - " + name)
    if len(failedTo) != 0:
        print("Failed to send to: ")
        print(*failedTo, sep = ", ")

