from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QListWidget, QLineEdit, \
    QMessageBox, QMenuBar, QMenu, QPushButton, QListWidgetItem
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
        self.delete_button = QPushButton("Delete")

        self.delete_button.setEnabled(False)
        self.buy_button = QPushButton("Buy")
        action_s1=QAction("תיק מניות אישי",self)
        action_s2=QAction("סקירה כללית",self)
        action_s1.triggered.connect(self.set_protifolio_window)
        action_s2.triggered.connect(self.set_main_window)
        self.menu = QMenu("פעולות",self)
        self.menuBar.addMenu(self.menu)
        self.menu.addAction(action_s1)
        self.menu.addAction(action_s2)



        self.setMenuBar(self.menuBar)


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

        self.buy_button = QPushButton("Buy")
        self.buy_button.clicked.connect(self.buy_stock)
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

        self.right_layout.addWidget(self.StockExtendedDisplay)
        self.right_layout.addWidget(self.plot_canvas)
        self.right_layout.addWidget(self.buy_button)
        self.right_layout.addWidget(self.delete_button)
        self.delete_button.setStyleSheet("background-color: red")
        self.buy_button.setStyleSheet("background-color: green")
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

        # self.tabs=QTabWidget()
        #
        # self.tabs.setTabPosition(QTabWidget.TabPosition.North)
        # self.tabs.setMovable(True)
        #
        # self.tab1 = QWidget()
        # self.tab2 = QWidget()
        # # lay = QVBoxLayout(self.central_widget)
        # # lay.addWidget(self.tabs)
        # self.setCentralWidget(self.tabs)
        # self.tabs.addTab(self.tab1,"סקירה כללית")
        # self.tabs.addTab(self.tab2,"תיק מניות אישי")
        #
        # # Add both layouts to the main layout
        # self.main_layout.addWidget(self.tabs)

        # Add widgets to tabs


        # layout = QHBoxLayout()
        # layout.addLayout(self.left_layout)
        # layout.addLayout(self.right_layout)
        # self.tabs.addTab(layout,"סקירה כללית")
        # self.tabs.addTab(self.list_view_3,"תיק מניות אישי")

        # Set window properties
        self.setWindowTitle("List View Application")
        self.resize(1024, 768)
       # font = QtGui.QFont("Arial", 10, QtGui.QFont.Bold)
       # self.Stock_list_view.setFont(font)
     #   self.Stock_list_view.setStyleSheet("background-color: #F0F0F0; color: #333;")
    def on_search(self, query):
        # Method to handle search functionality
        if query == "":
            filtered_stocks = self.presenter.get_all_stocks()
        else:
            filtered_stocks = self.presenter.load_stock_by_query(query)
        if filtered_stocks:
            self.load_all_stocks(filtered_stocks)
        else:
            self.Stock_list_view.clear()
            self.Stock_list_view.addItem("No results found")
    def load_all_stocks(self, stocks):
            self.Stock_list_view.clear()
            for stock in stocks:
                item = QListWidgetItem(f"{stock.Ticker}\n"
                                             f"{stock.Name}\n" f"{stock.Value}\n")
                self.Stock_list_view.addItem(item)
            self.Stock_list_view.itemClicked.connect(self.on_item_clicked)


    #

    def show_message(self, message):
        QMessageBox.information(self, "Message", message)
    def on_item_clicked(self, item):
        self.StockExtendedDisplay.clear()

        tickerItem = item.text().split('\n')[0]
        self.presenter.current_stock = tickerItem
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



    def set_protifolio_window(self):
        self.Stock_list_view.clear()
        self.StockExtendedDisplay.clear()
        self.list_view_3.clear()
        # self.plot_canvas.plot_data(data, 'w')
        list = self.presenter.get_list()
        for stock in list:
            s =  self.presenter.load_stock_by_query_val(stock)
            item = QListWidgetItem(f"{s.Ticker}\n"
                                   f"{s.Name}\n" f"{s.Value}\n")
            self.Stock_list_view.addItem(item)

        self.buy_button.setEnabled(False)
        self.delete_button.setEnabled(True)
        self.delete_button.clicked.connect(self.delete_stock)
        self.Stock_list_view.itemClicked.connect(self.on_item_clicked)

    def delete_stock(self):
        self.presenter.delete_stock_by_symbol(self.presenter.current_stock)
        self.set_protifolio_window()
    def set_main_window(self):
        self.Stock_list_view.clear()
        self.StockExtendedDisplay.clear()

        self.buy_button.setEnabled(True)
        self.delete_button.setEnabled(False)
        self.load_all_stocks(self.presenter.get_all_stocks())
        self.Stock_list_view.itemClicked.connect(self.on_item_clicked)
    def buy_stock(self, stock):
        # Here you can implement what happens when the buy button is clicked
        self.presenter.add_stock_to_list(self.presenter.current_stock)


