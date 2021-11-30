import PyQt5
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox


class UI(QMainWindow):
    def __init(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = QMainWindow()

        msgbox = QMessageBox()
        msgbox.setText('Checking')
        msgbox.setStandardButtons(QMessageBox.y)

if __name__ == "__main__":
    app = QApplication([])
    win = QMainWindow()
    win.setWindowTitle('Merlin - Crusader Email Wizard')
    #app.setWindowIcon(QIcon('Merlin-Icon.ico'))
    win.show()
    sys.exit(app.exec())