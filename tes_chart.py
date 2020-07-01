from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtChart import QChart, QChartView, QBarSet, QBarSeries, QBarCategoryAxis, QValueAxis
from PyQt5.Qt import Qt
import sys

# Grafik penjualan beras cianjur selama 6 bulan terakhira


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(600, 400)

        barSet0 = QBarSet("Beras Cianjur")
        barSet0.append(50)
        barSet0.append(43)
        barSet0.append(34)
        barSet0.append(54)
        barSet0.append(48)
        barSet0.append(31)
        print(list(barSet0))
        barSet1 = QBarSet("Gula Merah")
        barSet1.append(20)
        barSet1.append(21)
        barSet1.append(22)
        barSet1.append(23)
        barSet1.append(30)
        barSet1.append(35)
        print(list(barSet0))
        series = QBarSeries()
        series.append(barSet0)
        series.append(barSet1)
        chart = QChart()
        chart.addSeries(series)
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Penjualan Beras dan Gula Merah")
        months = ["januari", "februari", "maret", "april", "mei", "juni"]
        axisX = QBarCategoryAxis()
        axisX.append(months)
        axisY = QValueAxis()
        axisY.setRange(0, 54)
        chart.addAxis(axisX, Qt.AlignBottom)
        chart.addAxis(axisY, Qt.AlignLeft)
        chartView = QChartView(chart)
        self.setCentralWidget(chartView)


app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
