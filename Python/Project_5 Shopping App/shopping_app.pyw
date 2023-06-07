import requests
from bs4 import BeautifulSoup
from PyQt5 import QtWidgets, QtGui, QtCore
import sys
import webbrowser

textFont = QtGui.QFont('Century Gothic', 14)

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 800, 600)
        self.setWindowTitle("Shopping App")
        self.center()

        self.data = None

        # Searchbar and its' layout
        self.searchBar = QtWidgets.QLineEdit()
        self.searchBar.setPlaceholderText("What do you want to buy?")
        self.searchBar.returnPressed.connect(self.search)
        self.searchBar.setFixedWidth(280)
        self.searchBar.setFont(textFont)

        self.searchbarLayout = QtWidgets.QHBoxLayout()
        self.searchbarLayout.addStretch()
        self.searchbarLayout.addWidget(self.searchBar)
        self.searchbarLayout.addStretch()

        # Search Button and its' layout
        self.searchButton = QtWidgets.QPushButton("Search")
        self.searchButton.setFont(textFont)
        self.searchButton.setFixedWidth(150)
        self.searchButton.clicked.connect(self.search)

        self.searchButtonLayout = QtWidgets.QHBoxLayout()
        self.searchButtonLayout.addStretch()
        self.searchButtonLayout.addWidget(self.searchButton)
        self.searchButtonLayout.addStretch()

        # Table widget and its' layout
        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.setMinimumSize(600, 350)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.itemDoubleClicked.connect(self.OpenLink)

        self.tableWidgetLayout = QtWidgets.QHBoxLayout()
        self.tableWidgetLayout.addStretch()
        self.tableWidgetLayout.addWidget(self.tableWidget)
        self.tableWidgetLayout.addStretch()

        # Main layout
        self.mainVLayout = QtWidgets.QVBoxLayout()

        self.mainVLayout.addStretch()
        self.mainVLayout.addLayout(self.searchbarLayout)
        self.mainVLayout.addLayout(self.searchButtonLayout)
        self.mainVLayout.addStretch()
        self.mainVLayout.addLayout(self.tableWidgetLayout)
        self.mainVLayout.addStretch()

        self.setLayout(self.mainVLayout)
        self.show()

    def search(self):
        if len(self.searchBar.text().replace(' ', '')) == 0:
            QtWidgets.QMessageBox.critical(self, 'Error!', 'Please type something in search bar', QtWidgets.QMessageBox.Ok)
            return
        self.data = self.getData()
        self.createTable()

    def getData(self):
        my_item = self.searchBar.text()
        my_item = my_item.replace(' ', '+')

        search_url = 'https://www.google.com/search?client=firefox-b-d&q={}&tbm=shop'.format(my_item)

        r = requests.get(search_url)
        soup = BeautifulSoup(r.content, 'html.parser')

        names = list()
        prices = list()
        links = list()

        items = soup.find_all('div', attrs={'class': 'P8xhZc'})
        for item in items:
            name = item.find_all('a')
            names.append(name[0].text)
            if name[0]['href'].startswith('/'):
                temp = name[0]['href']
                links.append(temp[temp.index('=') + 1:])
            else:
                links.append(name[0]['href'])
            price = item.find_all('span', {'class': 'HRLxBb'})
            prices.append(price[0].text)

        return [names, prices, links]

    def OpenLink(self, item: QtWidgets.QTableWidgetItem):
        try:
            if item.column() == 2:
                print(item.text())
        except Exception as e:
            print(e)

    def createTable(self):
        data = self.data
        names = data[0]
        prices = data[1]
        links = data[2]
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(len(data[0]))
        self.tableWidget.setHorizontalHeaderLabels(['Name', 'Price', 'Link'])
        self.tableWidget.setColumnWidth(0, 250)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 200)
        for index in range(len(names)):
            name_item = QtWidgets.QTableWidgetItem(names[index])
            price_item = QtWidgets.QTableWidgetItem(prices[index])
            link_item = QtWidgets.QTableWidgetItem(links[index])
            self.tableWidget.setItem(index, 0, name_item)
            self.tableWidget.setItem(index, 1, price_item)
            self.tableWidget.setItem(index, 2, link_item)

    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()