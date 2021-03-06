# pyqt-checkbox-file-list-widget
PyQt QListWidget for files and supporting the checkbox.

The main class `CheckBoxFileListWidget` inherits from both `FileListWidget`(<a href="https://github.com/yjg30737/pyqt-file-list-widget.git">pyqt-file-list-widget</a>) and `CheckBoxListWidget`(<a href="https://github.com/yjg30737/pyqt-checkbox-list-widget.git">pyqt-checkbox-list-widget</a>).

## Requirements
PyQt5 >= 5.8

## Included Packages
* <a href="https://github.com/yjg30737/pyqt-file-list-widget.git">pyqt-file-list-widget</a> - Parent class
* <a href="https://github.com/yjg30737/pyqt-checkbox-list-widget.git">pyqt-checkbox-list-widget</a> - Parent class

## Feature
* `getCheckedFilenames() -> list`

## Setup
`python -m pip install pyqt-checkbox-file-list-widget`

## Code Example
```python
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
        self.__listWidget.setFilenames([os.path.join(os.getcwd(), filename) for filename in os.listdir(os.getcwd())])
        allChkBox.stateChanged.connect(self.__listWidget.toggleState)
        showFilesNameOnlyChkBox.stateChanged.connect(self.__listWidget.setFilenameOnly)

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
```

Result

https://user-images.githubusercontent.com/55078043/145915698-c0e2550c-cdc9-4aaf-8e96-a729a8d8050f.mp4



