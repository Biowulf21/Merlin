import PyQt5
from PyQt5.QtWidgets import QDialog
import sys

from Ui_EmailBody_UI import Ui_EmailBodyWindow


class Template(QDialog):
    def __init__(self):
        super().__init__()
        


    
    def initUI(self):
        self.dg = QDialog()
        self.template = Ui_EmailBodyWindow
        self.template.setupUi(self.dg)
        
        self.dg.show()
        self.dg.exec()
        print('here')



