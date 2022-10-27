import sys
import string
from src import GUI
from collections import Counter
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox


class Main(QMainWindow, GUI.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.str_lower = string.ascii_lowercase
        self.str_upper = string.ascii_uppercase
        self.setWindowIcon(QtGui.QIcon("./images/Logo.ico")) # 设置软件图标
        self.setFixedSize(self.width(), self.height()) # 禁止窗口最大化
        self.tableWidget.verticalHeader().setVisible(False) # 表格不显示表头

        # 信号
        self.pushButton.clicked.connect(self.show_info)

    def get_text(self):
        if (text := self.plainTextEdit.toPlainText()) != "":
            return text.replace("\r", "").replace("\n", "").replace("\t", "")
        QMessageBox.information(self, "温馨提示", "您输入的内容为空!", QMessageBox.Yes)

    def get_radioButtonState(self):
        if self.radioButton.isChecked():
            return 1
        elif self.radioButton_2.isChecked():
            return 2
        elif self.radioButton_3.isChecked():
            return 3
        elif self.radioButton_4.isChecked():
            return 4
        elif self.radioButton_5.isChecked():
            return 5

    def get_checkBoxState(self):
        return self.checkBox.isChecked()

    def get_frequency(self):
        text = self.get_text()
        if text is not None:
            # 检查单选按钮情况
            radioButtonState = self.get_radioButtonState()
            if radioButtonState == 2:
                text = filter(lambda chr: chr in self.str_upper, text)
                text = "".join(text)
            elif radioButtonState == 3:
                text = filter(lambda chr: chr in self.str_lower, text)
                text = "".join(text)
            elif radioButtonState == 4:
                text = text.upper()
            elif radioButtonState == 5:
                text = text.lower()

            dic = Counter(text)
            # 从大到小排序
            sort_info = sorted(dic.items(), key=lambda i:i[1], reverse=True) # [('e', 39915), ... ('z', 264)]
            
            # 获取总字母数量
            number = sum(num for _, num in sort_info)

            # 添加频率
            edit_info = ""
            table_info = []
            for index, (character, num) in enumerate(sort_info):
                if num != 0:
                    frequency = round((num / number) * 100, 4)
                    edit_info += character
                    table_info.append((index + 1, character, num, frequency))
            return edit_info, table_info

    def show_info(self):
        if (ret := self.get_frequency()) is not None:
            edit_info, table_info = ret
            self.tableWidget.setRowCount(len(table_info))
            for x in range(self.tableWidget.rowCount()):
                for y in range(self.tableWidget.columnCount()):
                    item = QTableWidgetItem(str(table_info[x][y]))
                    item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                    self.tableWidget.setItem(x, y, item)

            self.plainTextEdit_2.setPlainText(edit_info[::-1]) if self.get_checkBoxState() else self.plainTextEdit_2.setPlainText(edit_info)

if __name__ == "__main__":
    # QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling) # DPI自适应
    app = QApplication(sys.argv)
    ui = Main()
    ui.show()
    sys.exit(app.exec_())