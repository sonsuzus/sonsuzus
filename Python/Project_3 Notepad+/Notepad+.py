import sys
from PyQt5 import QtWidgets, QtGui, QtCore

new_file_suffix = 1

class Tab(QtWidgets.QWidget):

    def __init__(self, title: str, to: QtWidgets.QTabWidget, text = '', saved = False):
        super().__init__()
        # Tab settings
        self.title = title
        self.saved = saved
        self.file_saved = self.saved
        self.to = to
        self.to.addTab(self, self.title)
        global new_file_suffix
        new_file_suffix += 1
        self.real_filepath = ''

        # UI
        self.text_edit = QtWidgets.QTextEdit()
        self.text_edit.setText(text)
        self.text_edit.textChanged.connect(self.text_changed)
        self.text_edit.setTabStopDistance(16)

        # Letter counter
        self.letter_counter = QtWidgets.QLabel("Letter Counter: 0")
        self.letter_counter.setMinimumHeight(30)

        # Word counter
        self.word_counter = QtWidgets.QLabel("Word Counter: 0")
        self.word_counter.setMinimumHeight(30)

        # Clear button
        self.clear_button = QtWidgets.QPushButton("Clear")
        self.clear_button.clicked.connect(self.text_edit.clear)

        # Undo button
        self.undo_button = QtWidgets.QPushButton("Undo")
        self.undo_button.clicked.connect(self.text_edit.undo)

        # Redo button
        self.redo_button = QtWidgets.QPushButton("Redo")
        self.redo_button.clicked.connect(self.text_edit.redo)

        #Layouts
        self.bottomLayout = QtWidgets.QHBoxLayout()
        self.bottomLayout.addWidget(self.letter_counter)
        self.bottomLayout.addStretch()
        self.bottomLayout.addWidget(self.undo_button)
        self.bottomLayout.addWidget(self.clear_button)
        self.bottomLayout.addWidget(self.redo_button)
        self.bottomLayout.addStretch()
        self.bottomLayout.addWidget(self.word_counter)

        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.addWidget(self.text_edit)
        self.mainLayout.addLayout(self.bottomLayout)

        self.setLayout(self.mainLayout)

    def text_changed(self):
        self.letter_counter.setText("Letter Counter: {}".format(len(self.text_edit.toPlainText())))
        self.word_counter.setText("Word Counter: {}".format(len(self.text_edit.toPlainText().split())))
        self.file_saved = False

        if self.title[-1] != '*':
            self.title = self.title + '*'
            self.to.setTabText(self.to.indexOf(self.to.currentWidget()), self.title)

    def getTitle(self):
        if not self.file_saved:
            return self.title[:-1]
        return self.title

class Window(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 600, 600)
        self.center()
        self.setWindowTitle("Notepad+")
        self.main_widget = QtWidgets.QWidget()

        # Tabs
        self.tabs = QtWidgets.QTabWidget()
        self.tabs.setMovable(True)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        Tab("new {}".format(new_file_suffix), self.tabs)

        # Layout
        self.mainHLayout = QtWidgets.QHBoxLayout()
        self.mainHLayout.addWidget(self.tabs)

        self.mainVLayout = QtWidgets.QVBoxLayout()
        self.mainVLayout.addLayout(self.mainHLayout)

        self.main_widget.setLayout(self.mainVLayout)
        self.setCentralWidget(self.main_widget)

        # Menus
        self.menu = self.menuBar()

        self.file = self.menu.addMenu("File")
        self.file.addAction("New...", self.create_new, "CTRL+N")
        self.file.addAction("Open...", self.open_file, "CTRL+O")
        self.file.addAction("Save...", self.save_file, "CTRL+S")
        self.file.addAction("Close...", self.close_tab, "CTRL+W")

        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def open_file(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, "Open...")
        filename = filename[0]
        if filename == '':
            return
        text = ""
        with open(filename, 'r') as file:
            text = file.read()
        real_path = filename
        tab_title = filename.split('/')
        tab_title = tab_title[-1]
        new_tab = Tab(tab_title, self.tabs, text, True)
        self.tabs.setCurrentIndex(self.tabs.indexOf(new_tab))
        new_tab.real_filepath = real_path


    def create_new(self):
        global new_file_suffix
        index = new_file_suffix - 1
        Tab("new {}".format(new_file_suffix), self.tabs)
        self.tabs.setCurrentIndex(index)

    def close_tab(self):
        current_tab = self.tabs.currentWidget()
        current = self.tabs.indexOf(current_tab)

        if current_tab.text_edit.toPlainText() == '':
            self.tabs.removeTab(current)
        elif current_tab.file_saved and current_tab.saved:
            self.tabs.removeTab(current)
        else:
            yes_no_box = QtWidgets.QMessageBox.question(self, " ", "Do you want to save '{}'?".format(current_tab.getTitle()), QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel, QtWidgets.QMessageBox.Yes)
            if yes_no_box == QtWidgets.QMessageBox.Yes:
                self.save_file()
                self.tabs.removeTab(current)
            elif yes_no_box == QtWidgets.QMessageBox.No:
                self.tabs.removeTab(current)

        if self.tabs.currentIndex() == -1:
            self.close()

    def save_file(self):
        current = self.tabs.currentIndex()
        current_tab = self.tabs.currentWidget()
        if current_tab.saved:
            with open(current_tab.real_filepath, 'w', encoding='utf-8') as file:
                file.write(current_tab.text_edit.toPlainText())
            current_tab.file_saved = True
            if current_tab.title[-1] == '*':
                current_tab.title = current_tab.title[:-1]
            self.tabs.setTabText(self.tabs.indexOf(current_tab), current_tab.title)

            return
        filename = QtWidgets.QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt)\nAll Files(*.*)")[0]
        if filename == '':
            return

        with open(filename, 'w', encoding='utf-8') as file:
            file.write(current_tab.text_edit.toPlainText())

        current_tab.real_filepath = filename
        filename = filename.split('/')[-1]
        self.tabs.setTabText(current, filename)
        current_tab.title = filename
        current_tab.saved = True
        current_tab.file_saved = True


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    app.exec_()

if __name__ == "__main__":
    main()
