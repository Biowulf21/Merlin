import PyQt5
from PyQt5.QtWidgets import QDialog

import ui_files.Ui_SubjectEmail_UI as Ui_SubjectEmail_UI
from ui_files.Ui_SubjectEmail_UI import Ui_Dialog


import ui_files.Ui_EmailBody_UI as Ui_EmailBody_UI
from ui_files.Ui_EmailBody_UI import Ui_EmailBodyWindow


def ChangeEmailSubjectTemplate(textEditString):
    dg = QDialog()
    dg.setWindowTitle("Edit Email Subject")

    win = Ui_Dialog()
    win.setupUi(dg)

    print("abot dri")

    with open("EmailSubject.txt", "r") as file:
        body = file.read()
        win.subjectPlainTextEdit.setPlainText(body)
        file.close()
        dg.exec()

        updatedSubject = win.subjectPlainTextEdit.toPlainText()
        UpdateSubjectTemplate(updatedSubject)


# FIXME: woking but buggy
def UpdateSubjectTemplate(x):
    with open('EmailSubject.txt', 'w') as file:
        file.write(x)


def ChangeEmailBodyTemplate(textEditString):

    dlg = QDialog()
    dlg.setWindowTitle("Edit Email Body")
    window = Ui_EmailBodyWindow()
    window.setupUi(dlg)
    # The text box for the email template reads the appropriate text file so that any changes made can be written into the txt file for use later on
    with open("EmailBody.txt", "r") as file:
        body = file.read()
        window.EmailTemplateTextEdit.setPlainText(body)
        file.close()
        dlg.exec()

        # getting the value of the textedit only works after the save button is pressed and the dialog is closed
        updatedText = window.EmailTemplateTextEdit.toPlainText()
        UpdateEmailBodyTemplate(updatedText)


def UpdateEmailBodyTemplate(x):
    with open('EmailBody.txt', 'w') as file:
        file.write(x)
