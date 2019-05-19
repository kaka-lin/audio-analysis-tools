from PyQt5 import QtCore, QtGui, QtWidgets
from gui.fftbox import FFTBox

class AnalysisTab(QtWidgets.QVBoxLayout):
    def __init__(self, parent=None):
        super(AnalysisTab, self).__init__(parent)

        self.fft_box = FFTBox()

        self.addWidget(self.fft_box)
      
        self._setup_ui()
    
    def _setup_ui(self):
        self.retranslateUi()
    
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
