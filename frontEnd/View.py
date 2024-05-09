import sys

from PySide6 import QtGui
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QListWidget, QLineEdit, \
    QMessageBox, QMenuBar, QMenu
import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import presenter

class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        super().__init__(self.fig)
        self.setParent(parent)

    def plot_data(self, data,color='r'):
        self.axes.clear()
        self.axes.plot(data, color)
        self.axes.set_title('Prices')
        self.axes.set_xlabel('Days')
        self.axes.set_ylabel('Price')
        self.draw()
class View(QMainWindow):

    def __init__(self):
        super().__init__()
        self.presenter = None

        self.Stock_list_view = QListWidget()
        self.StockExtendedDisplay = QListWidget()
        self.list_view_3 = QListWidget()
        self.menuBar = QMenuBar()
        self.menuBar.setObjectName(u"menuBar")
        self.menu = QMenu(self.menuBar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menuBar)
        self.menu_2.setObjectName(u"menu_2")

        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())

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
        self.search_bar.textChanged.connect(self.on_search)
        self.left_layout.addWidget(self.search_bar)
        self.left_layout.addWidget(self.Stock_list_view)

        # Right layout for two lists
        self.right_layout = QVBoxLayout()
        self.plot_canvas = PlotCanvas(self, width=5, height=4, dpi=100)
        self.menuBar = QMenuBar()
        self.right_layout.addWidget(self.StockExtendedDisplay)
        self.right_layout.addWidget(self.plot_canvas)
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
    def on_search(self, query):
        # Method to handle search functionality
        filtered_stocks = self.presenter.load_stock_by_query(query)
        self.load_all_stocks(filtered_stocks)
    def load_all_stocks(self, stocks):
            self.Stock_list_view.clear()
            for stock in stocks:
                self.Stock_list_view.addItem(f"{stock.Ticker}\n"
                                             f"{stock.Name}\n")
            self.Stock_list_view.itemClicked.connect(self.on_item_clicked)

        # load specific stock


    def show_message(self, message):
        QMessageBox.information(self, "Message", message)
    def on_item_clicked(self, item):
        self.StockExtendedDisplay.clear()
        self.StockExtendedDisplay
        tickerItem = item.text().split('\n')[0]
        ItemDescription = self.presenter.load_description_by_symbol(tickerItem)
        self.StockExtendedDisplay.addItem(f"Description: {ItemDescription}\n")
        self.StockExtendedDisplay.setWordWrap(True)
        tingoDtoList = self.presenter.load_stock_by_symbol(tickerItem)
        if tingoDtoList:
            for ting in tingoDtoList:
                  self.StockExtendedDisplay.addItem(f"Date: {ting.Date}   " + f"Close: {ting.Close}   " + f"High: {ting.High}\n" + f"Low: {ting.Low}   " + f"Open: {ting.Open}   " + f"Volume: {ting.Volume}\n")
        if tingoDtoList[0].Close<tingoDtoList[-1].Close:
            self.plot_canvas.plot_data([d.Close for d in tingoDtoList],'g')
        else:
            self.plot_canvas.plot_data([d.Close for d in tingoDtoList])

