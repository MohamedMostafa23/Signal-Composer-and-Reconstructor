from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import pyqtgraph as pg
import matplotlib.pylab as plt
import pandas as pd
import scipy
from scipy import signal
import csv
from PyQt5.QtCore import Qt


class Ui_MainWindow(object):
    signal_counter = 0
    freq = 0
    phase = 0
    mag = 0
    f_sample = 1
    sum_signals = float
    t = np.arange(0.0, 1.0, 0.001)
    signal_list = []
    freq_list = []

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1023, 802)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.SIGNALVEWIR = QtWidgets.QTabWidget(self.centralwidget)
        self.SIGNALVEWIR.setObjectName("SIGNALVEWIR")
        self.SignalViewer = QtWidgets.QWidget()
        self.SignalViewer.setObjectName("SignalViewer")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.SignalViewer)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.graphicsView_3 = pg.PlotWidget(self.SignalViewer)
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.gridLayout_3.addWidget(self.graphicsView_3, 0, 0, 1, 1)
        self.graphicsView_4 = pg.PlotWidget(self.SignalViewer)
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_3.addWidget(self.graphicsView_4, 5, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.SignalViewer)
        self.label_4.setObjectName("label_4")

        self.horizontalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.SignalViewer)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)

        self.gridLayout_3.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.hideButton = QtWidgets.QPushButton(self.SignalViewer)
        self.hideButton.setObjectName("hideButton")
        self.gridLayout_3.addWidget(self.hideButton, 11, 0, 1, 1)
        self.slider = QtWidgets.QSlider(self.SignalViewer)

        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setTickPosition(self.slider.TicksBothSides)
        self.slider.setObjectName("horizontalslider")
        self.slider.setTickInterval(5)
        self.slider.setSingleStep(1)
        self.slider.setMinimum(1)
        self.slider.setMaximum(225)

        self.gridLayout_3.addWidget(self.slider, 4, 0, 1, 1)
        self.SIGNALVEWIR.addTab(self.SignalViewer, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout.setObjectName("gridLayout")
        self.graphicsView_1 = pg.PlotWidget(self.tab_2)
        self.graphicsView_1.setObjectName("graphicsView_1")
        self.gridLayout.addWidget(self.graphicsView_1, 2, 0, 1, 5)
        self.LoadButton = QtWidgets.QPushButton(self.tab_2)
        self.LoadButton.setObjectName("LoadButton")
        self.AddButton = QtWidgets.QPushButton(self.tab_2)
        self.AddButton.setObjectName("AddButton")
        self.label_5.setStyleSheet("color: #330b5b;")
        self.label_5.setFont(QtGui.QFont('Times', 10))
        self.gridLayout.addWidget(self.LoadButton, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.AddButton, 3, 1, 1, 1)
        self.ConfirmButton = QtWidgets.QPushButton(self.tab_2)
        self.ConfirmButton.setObjectName("ConfirmButton")
        self.gridLayout.addWidget(self.ConfirmButton, 5, 1, 1, 1)
        self.Phase_box = QtWidgets.QLineEdit(self.tab_2)
        self.Phase_box.setObjectName("Phase_box")
        self.gridLayout.addWidget(self.Phase_box, 1, 2, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 2)
        self.Freq_box = QtWidgets.QLineEdit(self.tab_2)
        self.Freq_box.setPlaceholderText("")
        self.Freq_box.setObjectName("Freq_box")
        self.gridLayout.addWidget(self.Freq_box, 1, 0, 1, 2)
        self.Mag_box = QtWidgets.QLineEdit(self.tab_2)
        self.Mag_box.setText("")
        self.Mag_box.setObjectName("Mag_box")
        self.gridLayout.addWidget(self.Mag_box, 1, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 4, 1, 1)
        self.label_1 = QtWidgets.QLabel(self.tab_2)
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 0, 0, 1, 2)
        self.graphicsView_2 = pg.PlotWidget(self.tab_2)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.gridLayout.addWidget(self.graphicsView_2, 4, 0, 1, 5)
        self.listWidget = QtWidgets.QListWidget(self.tab_2)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 5, 3, 1, 2)
        self.DeleteButton = QtWidgets.QPushButton(self.tab_2)
        self.DeleteButton.setObjectName("DeleteButton")
        self.gridLayout.addWidget(self.DeleteButton, 5, 2, 1, 1)
        self.SaveButton = QtWidgets.QPushButton(self.tab_2)
        self.SaveButton.setObjectName("SaveButton")
        self.gridLayout.addWidget(self.SaveButton, 5, 0, 1, 1)

        self.SIGNALVEWIR.addTab(self.tab_2, "")
        self.gridLayout_2.addWidget(self.SIGNALVEWIR, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1023, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.SIGNALVEWIR.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.AddButton.clicked.connect(self.composer_add)
        self.DeleteButton.clicked.connect(self.composer_delete)
        self.SaveButton.clicked.connect(self.save_signal)
        self.LoadButton.clicked.connect(self.open_signal)
        self.hideButton.clicked.connect(self.hide_show)
        self.ConfirmButton.clicked.connect(self.confirm_signal)
        self.slider.valueChanged.connect(self.update)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Signal reconstructor"))
        self.label_4.setText(_translate("MainWindow", "Sampling Frequency in HZ:"))
        self.label_5.setText(_translate("MainWindow", "0"))
        self.SIGNALVEWIR.setTabText(self.SIGNALVEWIR.indexOf(self.SignalViewer),
                                    _translate("MainWindow", "SignalViewer"))
        self.AddButton.setText(_translate("MainWindow", "Add Signal"))
        self.ConfirmButton.setText(_translate("MainWindow", "Confirm"))
        self.SaveButton.setText(_translate("MainWindow", "Save"))
        self.LoadButton.setText(_translate("MainWindow", "Load"))
        self.hideButton.setText(_translate("MainWindow", "Hide"))

        self.label_2.setText(
            _translate("MainWindow", "Phase Shift                                                             "))
        self.label_3.setText(_translate("MainWindow", "Magnitude"))
        self.label_1.setText(
            _translate("MainWindow", "Frequancy                                                                   "))
        self.DeleteButton.setText(_translate("MainWindow", "Delete"))
        self.SIGNALVEWIR.setTabText(self.SIGNALVEWIR.indexOf(self.tab_2), _translate("MainWindow", "Composer"))

    def composer_add(self):
        self.graphicsView_1.clear()
        self.graphicsView_2.clear()
        self.mag = float(self.Mag_box.text())
        self.freq = int(self.Freq_box.text())
        self.phase = float(self.Phase_box.text())
        self.listWidget.addItem("{} sin({}t + {})".format(self.mag, self.freq, self.phase))
        self.freq_list.append(self.freq)
        self.get_max_freq()
        self.signal = self.mag * np.sin(2 * np.pi * self.freq * self.t + self.phase)
        self.signal_list.append(self.signal)
        self.graphicsView_1.plot(self.t, self.signal)
        self.sum_signals = sum(self.signal_list)
        self.graphicsView_2.plot(self.t, self.sum_signals)
        self.signal_counter += 1

    def get_max_freq(self):
        self.slider.setMaximum(max(self.freq_list) * 3)
        self.max_freq = max(self.freq_list)

    def composer_delete(self):
        signal_index = self.listWidget.currentRow()
        self.listWidget.takeItem(signal_index)
        del self.signal_list[signal_index]
        del self.freq_list[signal_index]
        self.get_max_freq()
        self.sum_signals = sum(self.signal_list)
        self.graphicsView_2.clear()
        self.graphicsView_2.plot(self.t, self.sum_signals)

    def update(self):
        self.f_sample = self.slider.value()
        self.label_5.setText(str(self.f_sample))
        print(self.f_sample)
        self.confirm_signal()

    def confirm_signal(self):
        self.graphicsView_3.clear()
        self.graphicsView_3.plot(self.t, self.sum_signals)

        self.step_sample = int((len(self.sum_signals)) / self.f_sample)

        self.graphicsView_3.plot(self.t[0::self.step_sample], self.sum_signals[0::self.step_sample], symbol='o', pen=None)

        signal_tuble = scipy.signal.resample(self.sum_signals, 2 * self.f_sample, self.t)
        y = self.sinc_interp(signal_tuble[0], signal_tuble[1], self.t)
        self.graphicsView_4.clear()
        self.graphicsView_4.plot(self.t, y)

    def sinc_interp(self, x_axis_sampled, y_axis_sampled, time_sampled):
        if len(x_axis_sampled) != len(y_axis_sampled):
            raise ValueError('x and s must be the same length')

        # Find the period
        time_period = y_axis_sampled[1] - y_axis_sampled[0]

        sincM = np.tile(time_sampled, (len(y_axis_sampled), 1)) - np.tile(y_axis_sampled[:, np.newaxis], (1, len(time_sampled)))
        sample_signal = np.dot(x_axis_sampled, np.sinc(sincM / time_period))
        return sample_signal

    def save_signal(self):
        with open('dict{}.csv'.format(self.max_freq), 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['values'])
            for i in range(len(self.sum_signals)):
                writer.writerow([self.sum_signals[i]])
        print("signal saved")

    def open_signal(self):
        self.csv_signal, self.format1 = QtWidgets.QFileDialog.getOpenFileName(None, "Load Signal File", "", "*.csv;;")
        index_of_dict = self.csv_signal.find("dict") + 4
        max_freq = self.csv_signal[index_of_dict:-4]
        self.sum_signals = []
        self.signal_dataframe = pd.read_csv(self.csv_signal)
        self.sum_signals = [i for i in self.signal_dataframe.iloc[:, 0]]
        print("max_freq {}".format(max_freq))
        self.slider.setMaximum(int(max_freq) * 3)
        self.update()

    def hide_show(self):
        if self.hideButton.text() == 'Hide':
            self.graphicsView_4.hide()
            self.hideButton.setText("Show")
        else:
            self.graphicsView_4.show()
            self.hideButton.setText("Hide")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
