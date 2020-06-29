from PyQt5.QtWidgets import QStackedWidget, QApplication, QMainWindow, QWidget, QLineEdit, QStackedLayout, QStackedWidget, QVBoxLayout
from PyQt5 import uic
# import survey
import sys
import json
import qtmodern.styles
import qtmodern.windows


class loginSurvey(QWidget):
    def __init__(self):
        super(loginSurvey, self).__init__()
        self.mainUI()
        self.setFixedSize(500, 200)

    def mainUI(self):
        uic.loadUi("loginSurvey.ui", self)


class formSurvey(QWidget):
    def __init__(self):
        super(formSurvey, self).__init__()
        self.mainUI()
        self.setFixedSize(500, 200)

    def mainUI(self):
        uic.loadUi("form.ui", self)


# def changeButton(self):
#     # username = self.usernameEdit.text()
#     username2 = self.findChild(QLineEdit, "usernameEdit")
#     print(username2.text())


# class App2(QWidget):
#     def __init__(self):
#         super(App2, self).__init__()
#         uic.loadUi("formSurvey.ui", self)


class MainApp(QMainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        self.mainUI()

    def mainUI(self):
        self.lSurvey = loginSurvey()
        self.fSurvey = formSurvey()

        # stacked widget
        self.stackLayout = QStackedLayout()
        self.stackLayout.addWidget(self.lSurvey)
        self.stackLayout.addWidget(self.fSurvey)

    def mainLayout(self):
        self.layoutWidget = QVBoxLayout()
        self.layoutWidget.addWidget(self.stackLayout)
        self.setLayout(self.layoutWidget)

    def validation(self):
        valid_data = self.getValue()[0]['user']
        username = self.lSurvey.username.text()
        password = self.lSurvey.password.text()

        if username == "" or password == "":
            print("Username or Password not empty")
        else:
            if username == valid_data['username'] and password == valid_data['password']:
                self.stackLayout.setCurrentIndex(1)
            else:
                print("username or Password not valid!")

    def action_valid(self):
        self.lSurvey.pushButton.clicked.connect(self.validation)

    def getValue(self):
        value = open("datas.json")
        value = json.loads(value)
        return value


if __name__ == "__main__":
    app = QApplication([])
    win = MainApp()
    win.show()
    qtmodern.styles.dark(app)
    win_new = qtmodern.windows.ModernWindow(win)
    win_new.show()
    app.exec_()
