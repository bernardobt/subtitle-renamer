from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys, os, re


class Renamer_ui(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('main_ui.ui', self)


        self.installed_folder_path = os.getcwd()
        self.lineEdit_folder.setText(self.installed_folder_path)

        self.ui.pushButton_detect.clicked.connect(self.get_file_list)
        self.show()


    def get_file_list(self):
        self.plainTextEdit_video_list.clear()
        self.plainTextEdit_subs_list.clear()
        self.label_info.setText(f'Reading files...')
        vid_arr = []
        subs_arr = []
        arr = os.listdir(self.lineEdit_folder.text())
        for i, name in enumerate(arr):
            if name.endswith('.' + self.lineEdit_video_format.text()):
                vid_arr.append(name)
                self.plainTextEdit_video_list.appendPlainText(name)
            elif name.endswith('.' + self.lineEdit_subs_format.text()):
                subs_arr.append(name)
                self.plainTextEdit_subs_list.appendPlainText(name)
        self.label_info.setText(f'Finished reading files')
        self.lists = vid_arr, subs_arr
        self.pushButton_rename.setEnabled(True)
        self.pushButton_rename.clicked.connect(
            lambda ch: self.rename_files(self.lists))

    def rename_files(self, lists):
        if len(lists[0]) == len(lists[1]):
            self.label_info.setText(f'Renaming files')
            for counter, item in enumerate(lists[0]):
                new = re.sub(f"{self.lineEdit_video_format.text()}", f"{self.lineEdit_subs_format.text()}", item)
                os.rename((self.lineEdit_folder.text() + '\\' + lists[1][counter]), (self.lineEdit_folder.text() + '\\' + new))
            self.get_file_list()
            self.pushButton_rename.setEnabled(False)
            self.label_info.setText(f'Renamed {len(lists[0])} files')
        else:
            self.label_info.setText(f"Error: Number of files don't match")



app = QtWidgets.QApplication(sys.argv)

ui_window = Renamer_ui()
app.exec_()
