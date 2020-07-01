import json
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter, QAbstractPrintDialog
from PyQt5.QtChart import *
from PyQt5.Qt import Qt
from PyQt5.QtGui import QIcon
import requests


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


class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.mainUI()
        self.mainLayout()
        self.action()
        self.toolBarsSurvey()
        self.addToolBar(self.toolBarHome)
        self.addToolBar(self.toolBarForm)

    def mainUI(self):
        self.login = loginSurvey()
        self.form = formSurvey()
        self.result = Result()
        self.stackedLayout = QStackedLayout()
        self.stackedLayout.addWidget(self.login)
        self.stackedLayout.addWidget(self.form)
        self.stackedLayout.addWidget(self.result)
        self.stackedLayout.addWidget(self.chart())
        self.favoriteItem = ""

        self.form.comboBox1.activated.connect(self.valueCombo1)

    def mainLayout(self):
        self.layout = QWidget()
        self.layout.setLayout(self.stackedLayout)
        self.setCentralWidget(self.layout)

    def toolBarsSurvey(self):
        self.toolBarForm = QToolBar()
        buttonToolbar = QAction(QIcon("icon/market.png"), "test", self)
        self.toolBarForm.addAction(buttonToolbar)
        buttonToolbar.triggered.connect(self.tab_chart)

        self.toolBarHome = QToolBar()
        buttonToolbar = QAction(QIcon("icon/person.png"), "test", self)
        self.toolBarHome.addAction(buttonToolbar)
        buttonToolbar.triggered.connect(self.tab_home)

    def tab_chart(self):
        self.stackedLayout.setCurrentIndex(3)

    def tab_home(self):
        self.stackedLayout.setCurrentIndex(0)

    def getDataJson(self):
        with open('survey.json', 'r') as respon:
            data = json.load(respon)
        return data

    def chart(self):
        respon = requests.get(
            "https://res.cloudinary.com/sivadass/raw/upload/v1535817394/json/products.json")
        json = respon.json()

        harga = list(map(lambda a: a['price'], json))
        barset0 = QBarSet("Harga Buah")
        for i in harga:
            barset0.append(i)

        series = QBarSeries()
        series.append(barset0)

        chart = QChart()
        chart.addSeries(series)
        chart.setAnimationOptions(QChart.SeriesAnimations)

        name = list(map(lambda a: a['name'], json))
        axisX = QBarCategoryAxis()
        axisX.append(name)

        axisY = QValueAxis()
        axisY.setRange(0, 950)

        chart.addAxis(axisX, Qt.AlignBottom)
        chart.addAxis(axisY, Qt.AlignLeft)
        chartView = QChartView(chart)
        return chartView

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

    # show to login page

    def act_login(self):
        self.stackedLayout.setCurrentIndex(1)

    # show to form page

    def act_form(self):
        self.resultsResponse()
        self.stackedLayout.setCurrentIndex(2)

    def addToJson(self):
        data = self.values()
        toJson = json.dumps(data, indent=4)
        fwrite = open('survey.json', 'w')
        fwrite.write(toJson)
        QMessageBox.information(self, "About", "Survey Berhasil Di Export")

    # pdf print
    def getToPrint(self):
        data = self.values()
        text = """
                    Hasil Survey Supermarket 

            Item Favorite: {}
            Kelengkapan Stok: {}
            Toilet: {}
            Rak Makanan: {}
            Rak Buah: {}
            Rak Susun: {}
            Refrigator: {}
            Lantai Toko: {}
            Lokasi Strategis: {}
            Lahan Parkir: {}
            Saran Masukan Anda :{}

            Semoga Harimu Menyenangkan 
        """.format(data["favorite_item"], data["kelengkapan_stok"], data["toilet"], data['rak_makanan'], data["rak_buah"], data["rak_pecah_belah"], data["refrigator"], data["lantai_toko"], data["lokasi_strategis"], data["lahan_parkir"], data["saran_masukan"])
        self.textArea = QTextEdit()
        self.textArea.setText(text)
        self.button = QPushButton("Print")
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.textArea)
        self.layout.addWidget(self.button)
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)
        self.button.clicked.connect(self.printTo)

    # print dialog
    def printTo(self):
        self.printer = QPrinter()
        self.dialog = QPrintDialog(self.printer)
        if self.dialog.exec_() == QDialog.Accepted:
            self.textArea.document().print_(self.dialog.printer())

    def action(self):
        self.username = self.login.findChild(QLineEdit, "lineEdit1")
        self.password = self.login.findChild(QLineEdit, "lineEdit_2")
        self.login.pushButton.clicked.connect(self.act_login)
        self.form.pushButton.clicked.connect(self.act_form)
        self.result.pushButton.clicked.connect(self.addToJson)
        btnPrint = self.result.findChild(QPushButton, "pushButton_2")
        btnPrint.clicked.connect(self.getToPrint)


if __name__ == "__main__":
    app = QApplication([])
    window = App()
    window.show()
    window.setWindowTitle("Survey Market")
    window.resize(1200, 800)
    app.exec_()
