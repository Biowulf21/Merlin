# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/storage/James Codes/Python/CYB/Test/EmailBody_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EmailBodyWindow(object):
    def setupUi(self, EmailBodyWindow):
        EmailBodyWindow.setObjectName("EmailBodyWindow")
        EmailBodyWindow.resize(689, 448)
        self.verticalLayout = QtWidgets.QVBoxLayout(EmailBodyWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(EmailBodyWindow)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.EmailTemplateTextEdit = QtWidgets.QTextEdit(self.frame)
        self.EmailTemplateTextEdit.setObjectName("EmailTemplateTextEdit")
        self.verticalLayout_2.addWidget(self.EmailTemplateTextEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.emailTemplateCancelBtn = QtWidgets.QPushButton(self.frame)
        self.emailTemplateCancelBtn.setObjectName("emailTemplateCancelBtn")
        self.horizontalLayout.addWidget(self.emailTemplateCancelBtn)
        self.emailTemplateSaveBtn = QtWidgets.QPushButton(self.frame)
        self.emailTemplateSaveBtn.setObjectName("emailTemplateSaveBtn")
        self.horizontalLayout.addWidget(self.emailTemplateSaveBtn)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(EmailBodyWindow)
        QtCore.QMetaObject.connectSlotsByName(EmailBodyWindow)

    def retranslateUi(self, EmailBodyWindow):
        _translate = QtCore.QCoreApplication.translate
        EmailBodyWindow.setWindowTitle(_translate("EmailBodyWindow", "Email Template - Merlin"))
        self.emailTemplateCancelBtn.setText(_translate("EmailBodyWindow", "Cancel"))
        self.emailTemplateSaveBtn.setText(_translate("EmailBodyWindow", "Save"))
