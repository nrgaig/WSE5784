import sys

from PySide6 import QtGui
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QListWidget, QLineEdit, \
    QMessageBox, QMenuBar


class View(QMainWindow):

    def __init__(self):
        super().__init__()
        self.presenter = None

        self.Stock_list_view = QListWidget()
        self.StockExtendedDisplay = QListWidget()
        self.list_view_3 = QListWidget()
        self.menuBar = QMenuBar()
        self.menuBar.setObjectName(u"menuBar")


    def set_presenter(self, presenter):
        self.presenter = presenter
        self.setup_ui()


    def user_action(self):
        # Example user action that needs data handling
        if self.presenter:
            self.presenter.handle_user_action()

    def setup_ui(self):
        # Setup user interface components here

        self.load_all_stocks(self.presenter.get_all_stocks())
     #   self.load_stock_exetend(self.presenter.get_stock())
        # Initialize the central widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QHBoxLayout(self.central_widget)
        
        # Left layout for one list and the search bar
        self.left_layout = QVBoxLayout()
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("חפש כאן")
        self.left_layout.addWidget(self.search_bar)
        self.left_layout.addWidget(self.Stock_list_view)

        # Right layout for two lists
        self.right_layout = QVBoxLayout()

        self.right_layout.addWidget(self.StockExtendedDisplay)
        self.right_layout.addWidget(self.list_view_3)
        self.right_layout.setSpacing(10)  # Add spacing between the two lists
        
        # Add both layouts to the main layout
        self.main_layout.addLayout(self.left_layout, 1)  # Half width
        self.main_layout.addLayout(self.right_layout, 1)  # Half width
        self.Stock_list_view.setWordWrap(True)

        # Styling to increase readability and manage item height dynamically
        self.Stock_list_view.setStyleSheet("""
               QListWidget {
                   background-color: #F0F0F0;
                   color: #333;
               }
               QListWidget::item {
                   margin: 4px;
               }
           """)
        # Set window properties
        self.setWindowTitle("List View Application")
        self.resize(1024, 768)
       # font = QtGui.QFont("Arial", 10, QtGui.QFont.Bold)
       # self.Stock_list_view.setFont(font)
     #   self.Stock_list_view.setStyleSheet("background-color: #F0F0F0; color: #333;")

    def load_all_stocks(self, stocks):
            self.Stock_list_view.clear()
            for stock in stocks:
                self.Stock_list_view.addItem(f"{stock}")

        # load specific stock
    def load_stock_exetend(self, id):
            self.StockExtendedDisplay.Clear()
            stock = self.presenter.get_stock(id)
            self.StockExtendedDisplay.addItem(f"Symbol: {stock['symbol']}")
            self.StockExtendedDisplay.addItem(f"Name: {stock['name']}")
            self.StockExtendedDisplay.addItem(f"Price: {stock['price']}")
            self.StockExtendedDisplay.addItem(f"Change: {stock['change']}")
            self.StockExtendedDisplay.addItem(f"Change Percent: {stock['change_percent']}")
            self.StockExtendedDisplay.addItem(f"Day High: {stock['day_high']}")
            self.StockExtendedDisplay.addItem(f"Day Low: {stock['day_low']}")
            self.StockExtendedDisplay.addItem(f"Year High: {stock['year_high']}")
            self.StockExtendedDisplay.addItem(f"Year Low: {stock['year_low']}")
            self.StockExtendedDisplay.addItem(f"Market Cap: {stock['market_cap']}")
            self.StockExtendedDisplay.addItem(f"Volume: {stock['volume']}")
            self.StockExtendedDisplay.addItem(f"Stock Exchange: {stock['stock_exchange']}")

    def show_message(self, message):
        QMessageBox.information(self, "Message", message)
