
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from gui.ui_fftbox import Ui_FFTBox

import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile as wav

class FFTBox(QtWidgets.QGroupBox):
    """  FFT box """
    def __init__(self, parent=None):
        super(FFTBox, self).__init__(parent)

        self.ui = Ui_FFTBox()
        self.ui.setupUi(self)
        self._setup_ui()

    def _setup_ui(self):
        """ """
    
    def openFile(self):
        file, _ = QFileDialog.getOpenFileName(
            self, 
            "Open File",
            "All Files (*);;wav Files (*.wav)")
        self.ui.fileName_lineEdit.setText(file)

        self.readData(file)

    def readData(self, file=None):
        if file:
            fs, data = wav.read(file)
            Ts = 1.0 / fs
            N = len(data)
            t = N / fs
            x = np.arange(0, t, Ts)

            if data.shape[1] == 2:
                left_data = data[:, 0]
                right_data = data[:, 1]

                xw = np.linspace(0.0, 1.0 / (2.0 * Ts), N // 2)
                fft_left = np.fft.fft(left_data)
                yw_left = np.abs(fft_left[: N // 2]) / N
                fft_right = np.fft.fft(right_data)
                yw_right = np.abs(fft_right[: N // 2]) / N

                #self.ui.figure.subplots
                ax1 = self.ui.figure.add_subplot(221)
                ax1.plot(x, left_data, 'k')

                ax2 = self.ui.figure.add_subplot(222)
                ax2.plot(x, right_data, 'k')

                ax3 = self.ui.figure.add_subplot(223)
                ax3.plot(xw, yw_left, 'r')

                ax4 = self.ui.figure.add_subplot(224)
                ax4.plot(xw, yw_right, 'r')

            elif data.shape[1] == 1:
                xw = np.linspace(0.0, 1.0 / (2.0 * Ts), N // 2)
                fft_data = np.fft.fft(data)
                yw = np.abs(fft_data[: N // 2]) / N

                #self.ui.figure.subplots
                ax1 = self.ui.figure.add_subplot(211)
                ax1.plot(x, left_data, 'k')

                ax2 = self.ui.figure.add_subplot(212)
                ax2.plot(xw, yw, 'r')
            
            self.ui.figure.tight_layout()
            self.ui.canvas.draw()
        else:
            print("No data")
