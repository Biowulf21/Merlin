# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Merlin.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1420, 691)
        MainWindow.setMinimumSize(QtCore.QSize(1420, 691))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(300, 0))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.fNameLabel = QtWidgets.QLabel(self.frame_2)
        self.fNameLabel.setObjectName("fNameLabel")
        self.formLayout_2.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.fNameLabel)
        self.fName = QtWidgets.QLabel(self.frame_2)
        self.fName.setAutoFillBackground(True)
        self.fName.setText("")
        self.fName.setObjectName("fName")
        self.formLayout_2.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.fName)
        self.lNameLabel = QtWidgets.QLabel(self.frame_2)
        self.lNameLabel.setObjectName("lNameLabel")
        self.formLayout_2.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.lNameLabel)
        self.lName = QtWidgets.QLabel(self.frame_2)
        self.lName.setText("")
        self.lName.setObjectName("lName")
        self.formLayout_2.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.lName)
        self.pNumLabel = QtWidgets.QLabel(self.frame_2)
        self.pNumLabel.setObjectName("pNumLabel")
        self.formLayout_2.setWidget(
            2, QtWidgets.QFormLayout.LabelRole, self.pNumLabel)
        self.pNumber = QtWidgets.QLabel(self.frame_2)
        self.pNumber.setText("")
        self.pNumber.setObjectName("pNumber")
        self.formLayout_2.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.pNumber)
        self.mailLabel = QtWidgets.QLabel(self.frame_2)
        self.mailLabel.setObjectName("mailLabel")
        self.formLayout_2.setWidget(
            3, QtWidgets.QFormLayout.LabelRole, self.mailLabel)
        self.xuMail = QtWidgets.QLabel(self.frame_2)
        self.xuMail.setText("")
        self.xuMail.setObjectName("xuMail")
        self.formLayout_2.setWidget(
            3, QtWidgets.QFormLayout.FieldRole, self.xuMail)
        self.claimDateLabel = QtWidgets.QLabel(self.frame_2)
        self.claimDateLabel.setObjectName("claimDateLabel")
        self.formLayout_2.setWidget(
            4, QtWidgets.QFormLayout.LabelRole, self.claimDateLabel)
        self.claimDate = QtWidgets.QLabel(self.frame_2)
        self.claimDate.setText("")
        self.claimDate.setObjectName("claimDate")
        self.formLayout_2.setWidget(
            4, QtWidgets.QFormLayout.FieldRole, self.claimDate)
        self.claimTimeLabel = QtWidgets.QLabel(self.frame_2)
        self.claimTimeLabel.setObjectName("claimTimeLabel")
        self.formLayout_2.setWidget(
            5, QtWidgets.QFormLayout.LabelRole, self.claimTimeLabel)
        self.claimTime = QtWidgets.QLabel(self.frame_2)
        self.claimTime.setText("")
        self.claimTime.setObjectName("claimTime")
        self.formLayout_2.setWidget(
            5, QtWidgets.QFormLayout.FieldRole, self.claimTime)
        self.statusLabel = QtWidgets.QLabel(self.frame_2)
        self.statusLabel.setObjectName("statusLabel")
        self.formLayout_2.setWidget(
            6, QtWidgets.QFormLayout.LabelRole, self.statusLabel)
        self.status = QtWidgets.QLabel(self.frame_2)
        self.status.setText("")
        self.status.setObjectName("status")
        self.formLayout_2.setWidget(
            6, QtWidgets.QFormLayout.FieldRole, self.status)
        self.verticalLayout_2.addLayout(self.formLayout_2)
        self.selectSubButton = QtWidgets.QPushButton(self.frame_2)
        self.selectSubButton.setObjectName("selectSubButton")
        self.verticalLayout_2.addWidget(self.selectSubButton)
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.xuMailLineEdit = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.xuMailLineEdit.sizePolicy().hasHeightForWidth())
        self.xuMailLineEdit.setSizePolicy(sizePolicy)
        self.xuMailLineEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.xuMailLineEdit.setObjectName("xuMailLineEdit")
        self.gridLayout.addWidget(self.xuMailLineEdit, 0, 0, 1, 1)
        self.xuMailButton = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.xuMailButton.sizePolicy().hasHeightForWidth())
        self.xuMailButton.setSizePolicy(sizePolicy)
        self.xuMailButton.setObjectName("xuMailButton")
        self.gridLayout.addWidget(self.xuMailButton, 0, 1, 1, 1)
        self.lNameLineEdit = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lNameLineEdit.sizePolicy().hasHeightForWidth())
        self.lNameLineEdit.setSizePolicy(sizePolicy)
        self.lNameLineEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.lNameLineEdit.setObjectName("lNameLineEdit")
        self.gridLayout.addWidget(self.lNameLineEdit, 1, 0, 1, 1)
        self.lNameButton = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lNameButton.sizePolicy().hasHeightForWidth())
        self.lNameButton.setSizePolicy(sizePolicy)
        self.lNameButton.setObjectName("lNameButton")
        self.gridLayout.addWidget(self.lNameButton, 1, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 2, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.verticalLayout_2.addWidget(self.frame)
        self.gridLayout_3.addWidget(self.frame_2, 0, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_3)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.receipientLabel = QtWidgets.QLabel(self.frame_3)
        self.receipientLabel.setObjectName("receipientLabel")
        self.verticalLayout.addWidget(self.receipientLabel)
        self.receipentLineEdit = QtWidgets.QLineEdit(self.frame_3)
        self.receipentLineEdit.setObjectName("receipentLineEdit")
        self.verticalLayout.addWidget(self.receipentLineEdit)
        self.subjectLabel = QtWidgets.QLabel(self.frame_3)
        self.subjectLabel.setObjectName("subjectLabel")
        self.verticalLayout.addWidget(self.subjectLabel)
        self.subjectLineEdit = QtWidgets.QLineEdit(self.frame_3)
        self.subjectLineEdit.setObjectName("subjectLineEdit")
        self.verticalLayout.addWidget(self.subjectLineEdit)
        self.bodyLabel = QtWidgets.QLabel(self.frame_3)
        self.bodyLabel.setObjectName("bodyLabel")
        self.verticalLayout.addWidget(self.bodyLabel)
        self.emailBodyText = QtWidgets.QTextEdit(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.emailBodyText.sizePolicy().hasHeightForWidth())
        self.emailBodyText.setSizePolicy(sizePolicy)
        self.emailBodyText.setMinimumSize(QtCore.QSize(400, 0))
        self.emailBodyText.setObjectName("emailBodyText")
        self.verticalLayout.addWidget(self.emailBodyText)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.emailSendButton = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.emailSendButton.sizePolicy().hasHeightForWidth())
        self.emailSendButton.setSizePolicy(sizePolicy)
        self.emailSendButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.emailSendButton.setObjectName("emailSendButton")
        self.gridLayout_2.addWidget(self.emailSendButton, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.frame_5)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.bulkEmailsTextEdit = QtWidgets.QTextEdit(self.frame_5)
        self.bulkEmailsTextEdit.setObjectName("bulkEmailsTextEdit")
        self.verticalLayout_4.addWidget(self.bulkEmailsTextEdit)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.bulkEmailSender = QtWidgets.QPushButton(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.bulkEmailSender.sizePolicy().hasHeightForWidth())
        self.bulkEmailSender.setSizePolicy(sizePolicy)
        self.bulkEmailSender.setObjectName("bulkEmailSender")
        self.horizontalLayout_4.addWidget(self.bulkEmailSender)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.bulkEmailProgressBar = QtWidgets.QProgressBar(self.frame_5)
        self.bulkEmailProgressBar.setProperty("value", 0)
        self.bulkEmailProgressBar.setObjectName("bulkEmailProgressBar")
        self.verticalLayout_4.addWidget(self.bulkEmailProgressBar)
        self.horizontalLayout_3.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.sentTableLabel = QtWidgets.QLabel(self.frame_6)
        self.sentTableLabel.setObjectName("sentTableLabel")
        self.verticalLayout_5.addWidget(self.sentTableLabel)
        self.sentListWidget = QtWidgets.QListWidget(self.frame_6)
        self.sentListWidget.setObjectName("sentListWidget")
        self.verticalLayout_5.addWidget(self.sentListWidget)
        self.failedTableLabel = QtWidgets.QLabel(self.frame_6)
        self.failedTableLabel.setObjectName("failedTableLabel")
        self.verticalLayout_5.addWidget(self.failedTableLabel)
        self.failedListWidget = QtWidgets.QListWidget(self.frame_6)
        self.failedListWidget.setObjectName("failedListWidget")
        self.verticalLayout_5.addWidget(self.failedListWidget)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_5.addWidget(self.pushButton_2)
        self.horizontalLayout_3.addWidget(self.frame_6)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        self.listWidget = QtWidgets.QListWidget(self.frame_4)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_6.addWidget(self.listWidget)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.horizontalLayout_2.addWidget(self.frame_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1420, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuUse_different_File = QtWidgets.QMenu(self.menuFile)
        self.menuUse_different_File.setObjectName("menuUse_different_File")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuForm = QtWidgets.QMenu(self.menubar)
        self.menuForm.setObjectName("menuForm")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuChange_Template = QtWidgets.QMenu(self.menuSettings)
        self.menuChange_Template.setObjectName("menuChange_Template")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionEmail = QtWidgets.QAction(MainWindow)
        self.actionEmail.setObjectName("actionEmail")
        self.actionSubject = QtWidgets.QAction(MainWindow)
        self.actionSubject.setObjectName("actionSubject")
        self.actionApplication_Key = QtWidgets.QAction(MainWindow)
        self.actionApplication_Key.setObjectName("actionApplication_Key")
        self.actionGoogle_Sheets = QtWidgets.QAction(MainWindow)
        self.actionGoogle_Sheets.setObjectName("actionGoogle_Sheets")
        self.actionExcel_File = QtWidgets.QAction(MainWindow)
        self.actionExcel_File.setObjectName("actionExcel_File")
        self.actionCurrent_Google_Form = QtWidgets.QAction(MainWindow)
        self.actionCurrent_Google_Form.setObjectName(
            "actionCurrent_Google_Form")
        self.actionQR_Text = QtWidgets.QAction(MainWindow)
        self.actionQR_Text.setObjectName("actionQR_Text")
        self.menuUse_different_File.addAction(self.actionGoogle_Sheets)
        self.menuUse_different_File.addAction(self.actionExcel_File)
        self.menuFile.addAction(self.menuUse_different_File.menuAction())
        self.menuEdit.addAction(self.actionApplication_Key)
        self.menuView.addAction(self.actionCurrent_Google_Form)
        self.menuChange_Template.addAction(self.actionEmail)
        self.menuChange_Template.addAction(self.actionSubject)
        self.menuChange_Template.addAction(self.actionQR_Text)
        self.menuSettings.addAction(self.menuChange_Template.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuForm.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.fNameLabel.setText(_translate("MainWindow", "First Name: "))
        self.lNameLabel.setText(_translate("MainWindow", "Last Name: "))
        self.pNumLabel.setText(_translate("MainWindow", "Phone Number:"))
        self.mailLabel.setText(_translate("MainWindow", "XU Mail: "))
        self.claimDateLabel.setText(_translate("MainWindow", "Claim Date: "))
        self.claimTimeLabel.setText(_translate("MainWindow", "Claim Time: "))
        self.statusLabel.setText(_translate("MainWindow", "Status:"))
        self.selectSubButton.setText(
            _translate("MainWindow", "Select Subscriber"))
        self.xuMailLineEdit.setPlaceholderText(
            _translate("MainWindow", "Enter XU Mail"))
        self.xuMailButton.setText(_translate("MainWindow", "Search"))
        self.lNameLineEdit.setPlaceholderText(
            _translate("MainWindow", "Enter Last Name"))
        self.lNameButton.setText(_translate("MainWindow", "Search"))
        self.lineEdit_2.setPlaceholderText(_translate(
            "MainWindow", "Enter Different Email Address"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.receipientLabel.setText(_translate("MainWindow", "Receipient"))
        self.receipentLineEdit.setPlaceholderText(
            _translate("MainWindow", "Receipient"))
        self.subjectLabel.setText(_translate("MainWindow", "Email Subject"))
        self.subjectLineEdit.setPlaceholderText(
            _translate("MainWindow", "Enter Email Subject"))
        self.bodyLabel.setText(_translate("MainWindow", "Email Body"))
        self.emailBodyText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt;\">Greetings &lt;Name&gt;,</span></p>\n"
                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans Serif\'; font-size:9pt;\"><br /></p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt;\">Your Photo Package is ready to claim on &lt;Date&gt; at &lt;Time&gt;.</span></p>\n"
                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans Serif\'; font-size:9pt;\"><br /></p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt;\">Make sure to bring...</span></p>\n"
                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans Serif\'; font-size:9pt;\"><br /></p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt;\">In Service, </span></p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt;\">The Crusader Yearbook 2022</span></p></body></html>"))
        self.emailSendButton.setText(_translate("MainWindow", "Send"))
        self.label.setText(_translate("MainWindow", "Bulk Email Sender"))
        self.bulkEmailSender.setText(
            _translate("MainWindow", "Send Bulk Emails"))
        self.sentTableLabel.setText(_translate("MainWindow", "Sent (Emails)"))
        self.failedTableLabel.setText(
            _translate("MainWindow", "Failed ( Emails)"))
        self.pushButton_2.setText(_translate("MainWindow", "Copy Failed"))
        self.label_2.setText(_translate(
            "MainWindow", "Confirm With (Phone Numbers)"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuUse_different_File.setTitle(
            _translate("MainWindow", "Use different File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuForm.setTitle(_translate("MainWindow", "Form"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuChange_Template.setTitle(
            _translate("MainWindow", "Change Template"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionEmail.setText(_translate("MainWindow", "Email"))
        self.actionSubject.setText(_translate("MainWindow", "Subject"))
        self.actionApplication_Key.setText(
            _translate("MainWindow", "Application Key"))
        self.actionGoogle_Sheets.setText(
            _translate("MainWindow", "Google Sheets"))
        self.actionExcel_File.setText(_translate("MainWindow", "Excel File"))
        self.actionCurrent_Google_Form.setText(
            _translate("MainWindow", "Inspect Google Form"))
        self.actionQR_Text.setText(_translate("MainWindow", "QR Text"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
