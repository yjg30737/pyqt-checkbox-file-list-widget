from PyQt5.QtCore import Qt, pyqtSignal

from pyqt_file_list_widget import FileListWidget
from pyqt_checkbox_list_widget import CheckBoxListWidget


class CheckBoxFileListWidget(FileListWidget, CheckBoxListWidget):
    checkedSignal = pyqtSignal(int, Qt.CheckState)

    def __init__(self):
        super().__init__()