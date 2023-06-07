import requests
from bs4 import BeautifulSoup
from PyQt5 import QtWidgets, QtGui, QtCore
import sys
import webbrowser
from dataclasses import dataclass
from urllib.parse import unquote

textFont = QtGui.QFont('Century Gothic', 14)
@dataclass
class Item:
    name: str
    price: str
    link: str
    link_shortened: str

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 800, 600)
        self.setWindowTitle("Shopping App")
        self.center()

        self.data: list[Item] = None

        # region UI STUFF
        # Searchbar and its layout
        self.searchBar = QtWidgets.QLineEdit()
        self.searchBar.setPlaceholderText("What do you want to buy?")
        self.searchBar.returnPressed.connect(self.search)
        self.searchBar.setFixedWidth(280)
        self.searchBar.setFont(textFont)

        self.searchbarLayout = QtWidgets.QHBoxLayout()
        self.searchbarLayout.addStretch()
        self.searchbarLayout.addWidget(self.searchBar)
        self.searchbarLayout.addStretch()

        # Search Button and its layout
        self.searchButton = QtWidgets.QPushButton("Search")
        self.searchButton.setFont(textFont)
        self.searchButton.setFixedWidth(150)
        self.searchButton.clicked.connect(self.search)

        self.searchButtonLayout = QtWidgets.QHBoxLayout()
        self.searchButtonLayout.addStretch()
        self.searchButtonLayout.addWidget(self.searchButton)
        self.searchButtonLayout.addStretch()

        # Table widget and its layout
        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.setMinimumSize(600, 350)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.itemDoubleClicked.connect(self.open_link)

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
        # endregion

        self.show()

    # Searches given prompt in google shopping page and creates the table accordingly
    def search(self):
        if len(self.searchBar.text().replace(' ', '')) == 0:
            QtWidgets.QMessageBox.critical(self, 'Error!', 'Please type something in the search bar', QtWidgets.QMessageBox.Ok)
            return
        self.data = self.get_item_list()
        self.createTable()

    # Parses item list from HTML using beautifulsoup4
    def get_item_list(self):
        my_item = self.searchBar.text()
        my_item = my_item.replace(' ', '+')

        search_url = 'https://www.google.com/search?q={}&tbm=shop'.format(my_item)

        r = requests.get(search_url)
        soup = BeautifulSoup(r.content, 'html.parser')
        
        item_list = list()

        items = soup.find_all('div', attrs={'class': 'P8xhZc'})
        for item in items:
            name_element = item.find_all('a')[0]
            
            name: str = name_element.text
            price = item.find_all('span', {'class': 'HRLxBb'})[0].text
            link: str = ''
            link_shortened: str = ''
            
            if name_element['href'].startswith('/'):
                link_fullstr = name_element['href']
                link = link_fullstr[link_fullstr.index('=') + 1:]
            else:
                link = name_element['href']
            link = unquote(link)
            
            max_link_len = 25
            if len(link) > max_link_len:
                link_shortened = link[:(max_link_len - 3)] + '...'
            else:
                link_shortened = link
            
            item_list.append(Item(name, price, link, link_shortened))

        return item_list

    def open_link(self, table_item: QtWidgets.QTableWidgetItem):
        try:
            if table_item.column() == 2:
                row_items: list[QtWidgets.QTableWidgetItem] = []
                for col in range(self.tableWidget.columnCount()):
                    current_item = self.tableWidget.item(table_item.row(), col)
                    row_items.append(current_item)
                
                name, price, link_shortened = row_items
                for item in self.data:
                    if item.name == name.text() and item.price == price.text() and item.link_shortened == link_shortened.text():
                        webbrowser.open(item.link)
                        break
                
        except Exception as e:
            print(e)

    def createTable(self):
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(len(self.data))
        self.tableWidget.setHorizontalHeaderLabels(['Name', 'Price', 'Link'])
        self.tableWidget.setColumnWidth(0, 250)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 200)
        
        for index, item in enumerate(self.data):
            name_item = QtWidgets.QTableWidgetItem(item.name)
            price_item = QtWidgets.QTableWidgetItem(item.price)
            link_item = QtWidgets.QTableWidgetItem(item.link_shortened)
            self.tableWidget.setItem(index, 0, name_item)
            self.tableWidget.setItem(index, 1, price_item)
            self.tableWidget.setItem(index, 2, link_item)

    # Centers the application to monitor's center
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