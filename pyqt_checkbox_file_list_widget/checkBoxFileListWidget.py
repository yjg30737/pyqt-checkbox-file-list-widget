from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QCheckBox

from pyqt_file_list_widget import FileListWidget
from pyqt_checkbox_list_widget import CheckBoxListWidget


class CheckBoxFileListWidget(FileListWidget, CheckBoxListWidget):
    checkedSignal = pyqtSignal(int, Qt.CheckState)

    def __init__(self):
        super().__init__()

    def getCheckedFilenames(self) -> list:
        filenames_to_remove_from_list = []
        if self.isFilenameOnly():
            filenames_to_remove_from_list = [self.getAbsFilename(self.item(i).text())
                                             for i in self.getCheckedRows()]
        else:
            filenames_to_remove_from_list = [self.item(i).text()
                                             for i in self.getCheckedRows()]
        return filenames_to_remove_from_list