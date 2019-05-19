from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QSizePolicy

# matplotlib
from matplotlib.backends.qt_compat import QtCore, QtWidgets, is_pyqt5
if is_pyqt5():
    from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
else:
    from matplotlib.backends.backend_qt4agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure

class Ui_FFTBox(object):
    def setupUi(self, fftBox):
        fftBox.setObjectName("FFTBox")

        self.gridLayout = QtWidgets.QGridLayout(fftBox)
        self.gridLayout.setHorizontalSpacing(12)
        self.gridLayout.setVerticalSpacing(12)

        self.open_button = QtWidgets.QPushButton(fftBox)
        self.open_button.setObjectName("open_button")
        self.plot_button = QtWidgets.QPushButton(fftBox)
        self.plot_button.setObjectName("plot_button")
        self.fileName_lineEdit = QtWidgets.QLineEdit(fftBox)
        self.fileName_lineEdit.setReadOnly(True)
        self.fileName_lineEdit.setObjectName("fileName_lineEdit")

        # Embedding `matplotlib` in Qt
        self.widget = QtWidgets.QWidget()
        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setParent(self.widget)
        self.canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.canvas.updateGeometry()
        self.toolbar = NavigationToolbar(self.canvas, self.widget)

        # StatusBar
        self.statusbar = QtWidgets.QStatusBar(fftBox)
        self.statusbar.setObjectName("statusbar")
        #fftBox.setStatusBar(self.statusbar)
        
        self.gridLayout.addWidget(self.fileName_lineEdit, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.open_button, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.plot_button, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.canvas, 2, 0, 1, 3)
        self.gridLayout.addWidget(self.toolbar, 3, 0, 1, 3)
        self.gridLayout.addWidget(self.statusbar, 4, 0, 1, 3)

        self.retranslateUi(fftBox)

        self.open_button.clicked.connect(fftBox.openFile)
        #self.plot_button.clicked.connect(fftBox.plotData)

    def retranslateUi(self, fftBox):
        _translate = QtCore.QCoreApplication.translate
        fftBox.setTitle(_translate("FFTBox", "Plot FFT of Signal"))
        self.open_button.setText(_translate("FFTBox", "Open"))
        self.plot_button.setText(_translate("FFTBox", "Plot"))
        
