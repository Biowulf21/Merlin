#GUI Imports
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from UI import Ui_MainWindow

import Sheets


class UI(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        self.ui.xuMailButton.clicked.connect(self.SearchUserID)
        self.ui.lNameButton.clicked.connect(self.SearchLastName)

    def SearchUserID(self):
        xuMail = self.ui.xuMailLineEdit.text()
        Sheets.SearchID(xuMail)

    def SearchLastName(self):
        lastName = self.ui.lNameLineEdit.text()

        Sheets.SearchLastName(lastName)






    

    


if __name__ == "__main__":
    app = QApplication([])
    win = UI()
    win.show()
    sys.exit(app.exec())


