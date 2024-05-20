from datetime import datetime, time, timedelta
import pytz

import pytz
from PySide6 import QtGui, QtWidgets
from PySide6.QtCore import QTimer
from PySide6.QtGui import QAction, Qt
from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QListWidget, QLineEdit, \
    QMessageBox, QMenuBar, QMenu, QPushButton, QListWidgetItem, QLabel
import matplotlib

matplotlib.use("Qt5Agg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        super().__init__(self.fig)
        self.setParent(parent)

    def plot_data(self, data, color='r'):
        self.axes.clear()
        self.axes.plot(data, color)
        self.axes.set_title('Prices')
        self.axes.set_xlabel('Days')
        self.axes.set_ylabel('Price')
        self.draw()

    def clear_plot(self):
        """Clears the plot canvas."""
        self.axes.clear()  # Clear the axes
        self.draw()  # Redraw the canvas to show the cleared state



MARKET_OPEN = time(9, 30)
MARKET_CLOSE = time(16, 0)
NY_TZ = pytz.timezone('America/New_York')


class View(QMainWindow):

    def __init__(self):
        super().__init__()
        self.query = None
        self.presenter = None

    def set_presenter(self, presenter):
        self.presenter = presenter
        self.setup_ui()

    def setup_ui(self):
        # Setup user interface components here

        self.Stock_list_view = QListWidget()
        self.StockExtendedDisplay = QListWidget()
        self.Stock_list_view.itemClicked.connect(self.on_item_clicked)

        # buttons
        self.delete_button = QPushButton("Sell")
        self.delete_button.setEnabled(False)
        self.delete_button.clicked.connect(self.delete_stock)
        self.buy_button = QPushButton("Buy")
        self.buy_button.setEnabled(True)
        self.buy_button.clicked.connect(self.buy_stock)
        self.delete_button.setStyleSheet("background-color: red" "font color: white")
        self.buy_button.setStyleSheet("background-color: green" "font color: white")
        search_button = QPushButton("🔍 tiingo search")
        search_button.clicked.connect(self.on_APIsearch)

        # Menu bar
        self.menuBar = QMenuBar()
        action_s1 = QAction("תיק מניות אישי", self)
        action_s2 = QAction("סקירה כללית", self)
        action_s1.triggered.connect(self.set_protifolio_window)
        action_s2.triggered.connect(self.set_main_window)
        self.menu = QMenu("פעולות", self)
        self.menuBar.addMenu(self.menu)
        self.menu.addAction(action_s1)
        self.menu.addAction(action_s2)
        self.setMenuBar(self.menuBar)

        # Load all stocks
        self.load_all_stocks(self.presenter.get_all_stocks_db())

        # Initialize the central widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QHBoxLayout(self.central_widget)

        # Left layout for one list and the search bar
        self.left_layout = QVBoxLayout()
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("חפש כאן")
        self.search_bar.textChanged.connect(self.on_search)
        search_layout = QHBoxLayout()
        search_layout.addWidget(self.search_bar)
        search_layout.addWidget(search_button)
        self.left_layout.addLayout(search_layout)

        self.left_layout.addWidget(self.Stock_list_view)

        # Right layout for two lists
        self.right_layout = QVBoxLayout()
        self.plot_canvas = PlotCanvas(self, width=5, height=4, dpi=100)

        # Add widgets to the right layout
        self.right_layout.addWidget(self.StockExtendedDisplay)
        self.right_layout.addWidget(self.plot_canvas)
        self.right_layout.addWidget(self.buy_button)
        self.right_layout.addWidget(self.delete_button)
        self.right_layout.setSpacing(10)  # Add spacing between the two lists

        # Add both layouts to the main layout
        self.main_layout.addLayout(self.left_layout, 1)  # Half width
        self.main_layout.addLayout(self.right_layout, 1)  # Half width
        self.Stock_list_view.setWordWrap(True)

        # # Styling to increase readability and manage item height dynamically
        # self.Stock_list_view.setStyleSheet("""
        #        QListWidget {
        #            background-color: #F0F0F0;
        #            color: #333;
        #        }
        #        QListWidget::item {
        #            margin: 4px;
        #        }
        #    """)


        # Set window properties
        self.setWindowTitle("List View Application")
        self.resize(1024, 768)

        font = QtGui.QFont("Arial", 10, QtGui.QFont.Bold)
        self.Stock_list_view.setFont(font)

        self.market_status_label = QLabel("Market Closed", self)
        self.market_status_label.setAlignment(Qt.AlignCenter)
        font = self.market_status_label.font()
        font.setPointSize(12)
        self.market_status_label.setFont(font)
        self.right_layout.insertWidget(1, self.market_status_label)  # Add below the clock

        # Add a button to delete all stocks from the portfolio
        self.delete_all_button = QPushButton("Sell All Stocks")
        self.delete_all_button.setEnabled(False)
        self.delete_all_button.clicked.connect(self.delete_all_stocks)
        self.right_layout.addWidget(self.delete_all_button)

        # Additional code for daily change indicator next to the graph
        self.daily_change_label = QLabel("monthly Change: +0.00 (0.00%)", self)
        self.right_layout.insertWidget(3, self.daily_change_label)

        # Clock setup
        self.clock_label = QLabel("00:00:00", self)
        self.clock_label.setAlignment(Qt.AlignCenter)
        font = self.clock_label.font()
        font.setPointSize(16)  # Increase font size for better visibility
        self.clock_label.setFont(font)

        # Timer to update the clock every second
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_clock)
        self.timer.start(1000)  # Update every 1000 milliseconds (1 second)

        # Adjusting the layout to include the clock
        self.right_layout.insertWidget(0, self.clock_label)  # Add the clock at the top of the right layout

        self.setStyleSheet("""
                QMainWindow {
                    background-color: #343a40;  /* Dark gray background */
                    color: #f8f9fa;            /* Light text color */
                }
                QPushButton {
                    background-color: #007bff; /* Bootstrap blue */
                    color: white;
                    border-radius: 5px;
                    padding: 6px;
                    font-size: 16px;
                }
                QPushButton:hover {
                    background-color: #0056b3; /* Darker blue on hover */
                }
                QLabel {
                    font-size: 14px;
                }
                QListWidget {
                    background-color: #495057; /* Darker gray for lists */
                    color: #f8f9fa;
                    border: none;
                    border-radius: 5px;
                }
                QLineEdit {
                    border-radius: 5px;
                    padding: 6px;
                    background-color: #ced4da; /* Light gray background */
                    color: #343a40;            /* Dark text for contrast */
                }
            """)

        # Enhance font across the application
        font = QtGui.QFont("Helvetica", 10)
        self.setFont(font)

        # Styling and positioning the clock and market status labels
        self.clock_label.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.market_status_label.setStyleSheet("font-size: 18px; padding: 8px;")

        # Adjust layout spacings and padding
        self.main_layout.setSpacing(20)  # Increase spacing between left and right layouts
        self.left_layout.setSpacing(10)
        self.right_layout.setSpacing(10)

        # Adding shadows to widgets for a more layered look
        shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(15)
        shadow.setColor(QtGui.QColor('black'))
        shadow.setOffset(2)
        self.Stock_list_view.setGraphicsEffect(shadow)
        self.StockExtendedDisplay.setGraphicsEffect(shadow)
        self.plot_canvas.setGraphicsEffect(shadow)

        # Adjust margins for cleaner layout borders
        self.left_layout.setContentsMargins(10, 10, 10, 10)
        self.right_layout.setContentsMargins(10, 10, 10, 10)

        # Update layout after styling changes
        self.central_widget.setLayout(self.main_layout)

        self.total_share_value_label = QLabel("Total Share Value: $0.00", self)
        self.total_share_value_label.setAlignment(Qt.AlignCenter)
        font = self.total_share_value_label.font()
        font.setPointSize(14)
        self.total_share_value_label.setFont(font)
        self.left_layout.insertWidget(2, self.total_share_value_label)  # Add below the market status label
        self.total_share_value_label.setStyleSheet("color: green;")  # Set label color to green
        self.total_share_value_label.setVisible(False)

    def calculate_total_share_value(self):
        stock_list = self.presenter.get_list()
        total_value = sum(
            stock[1] * self.presenter.load_stock_details_by_ticker_db(stock[0]).Value for stock in stock_list)
        self.total_share_value_label.setText(f"Total Share Value: ${total_value:.2f}")

    def update_clock(self):
        now = datetime.now(NY_TZ)
        self.clock_label.setText(now.strftime("%H:%M:%S"))
        self.update_market_status(now)

    def delete_all_stocks(self):
        self.presenter.delete_all_stocks()
        self.set_protifolio_window()
        self.calculate_total_share_value()


    def update_market_status(self, now):
        # Determine if the market is open or closed
        if now.date().weekday() < 5 and MARKET_OPEN <= now.time() <= MARKET_CLOSE:
            self.market_status_label.setText("שוק המניות פתוח")
            self.market_status_label.setStyleSheet("color: green;")  # Set label color to green
            self.clock_label.setStyleSheet("color: green;")  # Set clock color to green
        else:
            self.market_status_label.setText("שוק המניות סגור")
            self.market_status_label.setStyleSheet("color: red;")
            self.clock_label.setStyleSheet("color: red;")  # Set clock color to red

    #   self.Stock_list_view.setStyleSheet("background-color: #F0F0F0; color: #333;")
    def on_search(self, query):
        # Method to handle search functionality
        self.query = query
        self.Stock_list_view.clear()
        if query == "":
            filtered_stocks = self.presenter.get_all_stocks_db()
        else:
            filtered_stocks = self.presenter.load_stock_by_query_db(query)  # or []
        if filtered_stocks:
            for stock in filtered_stocks:
                if stock:
                    item = QListWidgetItem(f"{stock.Ticker}\n"
                                           f"{stock.Name}\n" f"{stock.Value}\n")
                    self.Stock_list_view.addItem(item)
        else:
            # self.Stock_list_view.clear()
            self.Stock_list_view.addItem("No results found")

    def load_all_stocks(self, stocks):
        self.Stock_list_view.clear()
        for stock in stocks:
            item = QListWidgetItem(f"{stock.Ticker}\n"
                                   f"{stock.Name}\n" f"{stock.Value}\n")
            self.Stock_list_view.addItem(item)

    #

    def show_message(self, message):
        QMessageBox.information(self, "Message", message)

    def on_item_clicked(self, item):
        # Extract the ticker from the selected item
        tickerItem = item.text().split('\n')[0]
        self.presenter.current_stock = tickerItem

        self.StockExtendedDisplay.clear()

        tickerItem = item.text().split('\n')[0]
        self.presenter.current_stock = tickerItem
        ItemDescription = self.presenter.load_description_by_symbol(tickerItem)
        self.StockExtendedDisplay.addItem(f"Description: {ItemDescription}\n")
        self.StockExtendedDisplay.setWordWrap(True)
        #        tingoDtoList = self.presenter.load_priceList_by_symbol(tickerItem)
        tiingoPricesList = self.presenter.load_stock_by_ticker_from_tiingo(tickerItem)
        if tiingoPricesList:
            for ting in tiingoPricesList:
                self.StockExtendedDisplay.addItem(
                    f"Date: {ting.Date}   " + f"Close: {ting.Close}   " + f"High: {ting.High}\n" + f"Low: {ting.Low}   " + f"Open: {ting.Open}   " + f"Volume: {ting.Volume}\n")
            if tiingoPricesList[0].Close < tiingoPricesList[-1].Close:
                self.plot_canvas.plot_data([d.Close for d in tiingoPricesList], 'g')
            else:
                self.plot_canvas.plot_data([d.Close for d in tiingoPricesList])

        self.presenter.fetch_daily_stock_prices(tickerItem)


    def update_daily_change(self, open_price, close_price):
        change = close_price - open_price
        percent_change = (change / open_price) if open_price != 0 else 0
        arrow = "↑" if change >= 0 else "↓"
        color = "green" if change >= 0 else "red"
        self.daily_change_label.setText(f"Monthly Change: {arrow}{change:.2f} ({percent_change:.2%})")
        self.daily_change_label.setStyleSheet(f"color: {color}")

    def set_protifolio_window(self):
        self.Stock_list_view.clear()
        self.StockExtendedDisplay.clear()
        self.plot_canvas.clear_plot()  # Clear the plot canvas
        self.total_share_value_label.setVisible(True)

        stock_list = self.presenter.get_list()
        for stock in stock_list:
            s = self.presenter.load_stock_details_by_ticker_db(stock[0])
            item = QListWidgetItem(f"{s.Ticker}\n"
                                   f"{s.Name}\n" f"{s.Value *stock[1]}\n")
            self.Stock_list_view.addItem(item)

        self.buy_button.setEnabled(False)
        self.delete_all_button.setEnabled(True)
        self.delete_button.setEnabled(True)

        self.calculate_total_share_value()


    def delete_stock(self):
        self.presenter.delete_stock_by_symbol(self.presenter.current_stock)
        self.set_protifolio_window()
        self.calculate_total_share_value()


    def set_main_window(self):
        self.Stock_list_view.clear()
        self.StockExtendedDisplay.clear()
        self.plot_canvas.clear_plot()  # Clear the plot canvas
        self.total_share_value_label.setVisible(False)


        self.buy_button.setEnabled(True)
        self.delete_button.setEnabled(False)
        self.delete_all_button.setEnabled(False)
        self.load_all_stocks(self.presenter.get_all_stocks_db())

    def buy_stock(self, stock):
        # Here you can implement what happens when the buy button is clicked
        self.presenter.add_stock_to_list(self.presenter.current_stock)

    def on_APIsearch(self):
        print(self.query)
        stock = self.presenter.post_ticker_data(self.query)
        if stock:
            stock = self.presenter.load_stock_by_query_db(self.query)
            self.Stock_list_view.clear()
            self.load_all_stocks(stock)
        else:
            print("error postin search button")
