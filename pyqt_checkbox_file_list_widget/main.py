import os

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QCheckBox, QHBoxLayout, \
    QVBoxLayout, QWidget, QApplication, QPushButton

from pyqt_checkbox_file_list_widget import CheckBoxFileListWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        allChkBox = QCheckBox('Check all')
        showFilesNameOnlyChkBox = QCheckBox('Show files name only')

        self.__listWidget = CheckBoxFileListWidget()
        self.__listWidget.setDatas([os.path.join(os.getcwd(), filename) for filename in os.listdir(os.getcwd())])
        allChkBox.stateChanged.connect(self.__listWidget.toggleState)
        showFilesNameOnlyChkBox.stateChanged.connect(self.__listWidget.setOnlyFileName)

        lay = QHBoxLayout()
        lay.setAlignment(Qt.AlignLeft)
        lay.addWidget(allChkBox)
        lay.addWidget(showFilesNameOnlyChkBox)
        lay.setContentsMargins(0, 0, 0, 0)

        topLeftWidget = QWidget()
        topLeftWidget.setLayout(lay)

        self.__deleteBtn = QPushButton('Delete')
        self.__deleteBtn.clicked.connect(self.__delete)

        lay = QHBoxLayout()
        lay.setAlignment(Qt.AlignRight)
        lay.addWidget(self.__deleteBtn)
        lay.setContentsMargins(0, 0, 0, 0)

        topRightWidget = QWidget()
        topRightWidget.setLayout(lay)

        lay = QHBoxLayout()
        lay.addWidget(topLeftWidget)
        lay.addWidget(topRightWidget)
        lay.setContentsMargins(0, 0, 0, 0)

        topWidget = QWidget()
        topWidget.setLayout(lay)

        lay = QVBoxLayout()
        lay.addWidget(topWidget)
        lay.addWidget(self.__listWidget)

        mainWidget = QWidget()
        mainWidget.setLayout(lay)

        self.setCentralWidget(mainWidget)

    def __delete(self):
        self.__listWidget.removeCheckedRows()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    htmlViewer = MainWindow()
    htmlViewer.show()
    app.exec_()
