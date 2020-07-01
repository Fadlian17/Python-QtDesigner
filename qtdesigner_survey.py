import json
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter, QAbstractPrintDialog
from PyQt5.QtChart import QtCharts


class loginSurvey(QWidget):
    def __init__(self):
        super(loginSurvey, self).__init__()
        self.mainUI()
        self.setFixedSize(900, 500)

    def mainUI(self):
        uic.loadUi("loginSurvey.ui", self)


class formSurvey(QWidget):
    def __init__(self):
        super(formSurvey, self).__init__()
        self.mainUI()
        self.setFixedSize(1200, 800)
        listdata = ["Indomie Goreng", "Teh Botol Sosro",
                    "Granita", "Okky Jelly Drink", "mangga california", "jeruk sitrun"]
        for i in listdata:
            self.comboBox1.addItem(i)

    def mainUI(self):
        uic.loadUi("formSurvey.ui", self)


class Result(QWidget):
    def __init__(self):
        super(Result, self).__init__()
        self.mainUI()
        self.setFixedSize(1200, 800)

    def mainUI(self):
        uic.loadUi("report.ui", self)


class App(QWidget):
    def __init__(self):
        super(App, self).__init__()
        self.mainUI()
        self.mainLayout()
        self.action()

    def mainUI(self):
        self.login = loginSurvey()
        self.form = formSurvey()
        self.result = Result()
        self.stackedLayout = QStackedLayout()
        self.stackedLayout.addWidget(self.login)
        self.stackedLayout.addWidget(self.form)
        self.stackedLayout.addWidget(self.result)
        self.favoriteItem = ""

        self.form.comboBox1.activated.connect(self.valueCombo1)

    def mainLayout(self):
        self.layout = QVBoxLayout()
        self.layout.addLayout(self.stackedLayout)
        self.setLayout(self.layout)

    def valueCombo1(self, index):
        self.favoriteItem = self.form.comboBox1.itemText(index)

    def values(self):
        favoriteItem = self.favoriteItem
        kelengkapanStok = self.form.spinBox1.value()
        toilet = self.form.spinBox_2.value()
        rakMakanan = self.form.spinBox_3.value()
        rakBuah = self.form.spinBox_4.value()
        rakSusun = self.form.spinBox_5.value()
        refrigator = self.form.spinBox_6.value()
        lantaiToko = self.form.spinBox_7.value()
        lokasiStrategis = self.form.horizontalSlider1.value()
        saranMasukan = self.form.lineEdit.text()
        lahanParkir = ""
        if self.form.checkBox.isChecked():
            lahanParkir = self.form.checkBox.text()
        elif self.form.checkBox_2.isChecked():
            lahanParkir = self.form.checkBox_2.text()
        elif self.form.checkBox_3.isChecked():
            lahanParkir = self.form.checkBox_3.text()

        self.data = {
            "favorite_item": favoriteItem,
            "kelengkapan_stok": kelengkapanStok,
            "toilet": toilet,
            "rak_makanan": rakMakanan,
            "rak_buah": rakBuah,
            "rak_pecah_belah": rakSusun,
            "refrigator": refrigator,
            "lantai_toko": lantaiToko,
            "lokasi_strategis": lokasiStrategis,
            "lahan_parkir": lahanParkir,
            "saran_masukan": saranMasukan
        }

        return self.data

    def resultsResponse(self):
        data = self.values()
        Item = self.result.findChild(QLabel, "label_21")
        Item.setText(data["favorite_item"])
        Stok = self.result.findChild(QLabel, "label_22")
        Stok.setText(str(data["kelengkapan_stok"]))
        Toilet = self.result.findChild(QLabel, "label_2")
        Toilet.setText(str(data["toilet"]))
        RakMakanan = self.result.findChild(QLabel, "label_11")
        RakMakanan.setText(str(data["rak_makanan"]))
        RakBuah = self.result.findChild(QLabel, "label_16")
        RakBuah.setText(str(data["rak_buah"]))
        RakSusun = self.result.findChild(QLabel, "label_12")
        RakSusun.setText(str(data["rak_pecah_belah"]))
        Refrigator = self.result.findChild(QLabel, "label_13")
        Refrigator.setText(str(data["refrigator"]))
        LantaiToko = self.result.findChild(QLabel, "label_14")
        LantaiToko.setText(str(data["lantai_toko"]))
        LokasiStrategis = self.result.findChild(QLabel, "label_18")
        LokasiStrategis.setText(str(data["lokasi_strategis"]))
        lokasi = self.result.findChild(QLabel, "label_19")
        lokasi.setText(data["lahan_parkir"])
        saranMasukan = self.result.findChild(QLabel, "label_32")
        saranMasukan.setText(data["saran_masukan"])

    def act_form(self):
        self.resultsResponse()
        self.stackedLayout.setCurrentIndex(2)

    def act_login(self):

        self.stackedLayout.setCurrentIndex(1)

    def action(self):
        self.login.pushButton.clicked.connect(self.act_login)
        self.form.pushButton.clicked.connect(self.act_form)
        self.result.pushButton.clicked.connect(self.addToJson)
        self.result.pushButton_2.clicked.connect(self.printPdf)

    def addToJson(self):
        data = self.values()
        toJson = json.dumps(data, indent=4)
        fwrite = open('survey.json', 'w')
        fwrite.write(toJson)
        QMessageBox.information(self, "About", "Export to Json Success")

    def printToPdf(self):
        self.printPdf = QPrinter()
        self.dialog = QPrintDialog(self.printPdf)
        if self.dialog.exec_() == QPrintDialog.accepted:
            self.result.document().print_(self.printPdf)

    def getData(self):
        data = open("datas.json")
        data = json.load(data)
        return data


if __name__ == "__main__":
    app = QApplication([])
    window = App()
    window.show()
    window.setFixedSize(800, 650)
    app.exec_()
