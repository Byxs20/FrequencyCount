import os
from PyQt5 import QtCore, QtGui, QtWidgets

class MyQPlanTextEdit(QtWidgets.QPlainTextEdit):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setAcceptDrops(True)
    
    def dragEnterEvent(self, e: QtGui.QDragEnterEvent) -> None:
        self.strPathFile = e.mimeData().text().replace('file:///', '')
        if self.strPathFile.endswith('.txt'):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e: QtGui.QDropEvent) -> None:
        if os.path.exists(self.strPathFile):
            with open(self.strPathFile, 'r') as f:
                self.setPlainText(f.read())
        else:
            QtWidgets.QMessageBox.critical(self, "温馨提示", "文件不存在!", QtWidgets.QMessageBox.Yes)
