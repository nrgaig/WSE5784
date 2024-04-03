import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QListWidget,
    QLabel,
    QWidget,
    QPushButton,
)
from datetime import datetime
import pytz

class StockInfoWindow(QMainWindow):
    def __init__ (self, stock_name, parent=None):
        super().__init__(parent)
        self.setWindowTitle(f"Stock Information - {stock_name}")
        self.setGeometry(100, 100, 400, 300)
        self.layout = QVBoxLayout()
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_widget.setLayout(self.layout)

        self.stock_label = QLabel(f"Stock: {stock_name}")
        self.layout.addWidget(self.stock_label)

        self.company_label = QLabel("Company Information:")
        self.layout.addWidget(self.company_label)

        self.close_button = QPushButton("Close")
        self.close_button.clicked.connect(self.close)
        self.layout.addWidget(self.close_button)

class StockViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stock Viewer")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        # self.central_widget.setLayout(self.layout)

        self.layout = QVBoxLayout(self.central_widget)  # Set layout for central widget

        # Clock label
        self.clock_label = QLabel()
        self.layout.addWidget(self.clock_label)

        # Stock label
        self.stock_label = QLabel("Stocks:")
        self.layout.addWidget(self.stock_label)

        self.stock_list = QListWidget()
        # self.stock_list.addItems(["Apple", "Alphabet", "Meta", "Tesla"])
        # self.stock_list.itemClicked.connect(self.show_stock_info)
        self.layout.addWidget(self.stock_list)

        self.update_clock()

    def update_clock(self):
        ny_timezone = pytz.timezone("America/New_York")
        ny_time = datetime.now(ny_timezone).strftime("%Y-%m-%d %H:%M:%S")
        self.clock_label.setText(f"New York Time: {ny_time}")

        ny_open = datetime.now(ny_timezone).time().replace(hour=9, minute=30)
        ny_close = datetime.now(ny_timezone).time().replace(hour=16, minute=0)

        current_time = datetime.now(ny_timezone).time()
        if ny_open <= current_time <= ny_close:
            status = "Open"
        else:
            status = "Closed"

        self.clock_label.setText(f"New York Time: {ny_time} | Status: {status}")
    
    def list_stocks(self, stocks):
     self.stock_list.clear()  # Assuming stock_list is a QListWidget
     for stock in stocks:
        self.stock_list.addItem(f"{stock.symbol}: {stock.company_name} at ${stock.current_price}")

    def show_stock_info(self, item):
        stock_name = item.text()
        stock_info_window = StockInfoWindow(stock_name, parent=self)
        stock_info_window.show()





# class View:
    
#     # printing the list of stocks to the user
#     def list_stocks(self, stocks):
#         for stock in stocks:
#             print(f"{stock.symbol}: {stock.company_name} at ${stock.current_price}")
    
#     # printing a specific stock to the user
#     def show_stock(self, stock):
#         print(f"Current price of {stock.symbol} ({stock.company_name}) is ${stock.current_price}")
