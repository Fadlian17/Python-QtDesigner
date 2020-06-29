from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit, QStackedLayout, QStackedWidget, QVBoxLayout
from PyQt5 import uic
import survey
import sys
import qtmodern.styles
import qtmodern.windows


class App(QWidget):
    def __init__(self):
        super(App, self).__init__()
        uic.loadUi("loginSurvey.ui", self)
        self.pushButton.clicked.connect(self.changeButton)


def changeButton(self):
    # username = self.usernameEdit.text()
    username2 = self.findChild(QLineEdit, "usernameEdit")
    print(username2.text())


class App2(QWidget):
    def __init__(self):
        super(App2, self).__init__()
        uic.loadUi("formSurvey.ui", self)


class MainApp(QMainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        self.first = App()
        self.second = App2()
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.addWidget(self.first)
        self.verticalLayout.addWidget(self.first)

        self.widget = QWidget()
        self.widget.setLayout(self.verticalLayout)

        self.setCentralWidget(self.widget)


if __name__ == "__main__":
    app = QApplication([])
    win = App()
    # win.show()

    qtmodern.styles.dark(app)
    win_new = qtmodern.windows.ModernWindow(win)
    win_new.show()
    app.exec_()
