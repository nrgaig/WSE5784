from typing import Optional

from frontEnd.MainWindow import MainWindow
from frontEnd import Stock ,StockModel

#
# The Presenter class is responsible for handling the logic of the application.
# It receives input from the user and sends it to the model for processing.
#

    # initializing the view and the list of stocks
class Presenter:
    # The Presenter class handles the application logic and mediates between the view and the model.
    def __init__(self, view:MainWindow, model:Stock):
        self.view = view
        self.model = model

        self.StockList=Optional[list[StockModel]]

    def show_MainWindow(self):
        self.load_all_stocks()

        self.view.show_main_window()

    def show_view2(self):
        pass

    def load_all_stocks(self):
        stocks:Optional[list[StockModel]] = self.model.get_all_stocks()
        if stocks:
            self.view.list_stocks(stocks)
        else:
            self.view.show_message("No stocks available")

    def load_stock_by_id(self, stock_id):
        stock = self.model.get_stock_by_id(stock_id)
        if stock:
            self.view.display_stock(stock)
        else:
            self.view.show_message("Stock not found")

    def load_stock_by_symbol(self, symbol):
        stock = self.model.get_stock_by_symbol(symbol)
        if stock:
            self.view.display_stock(stock)
        else:
            self.view.show_message("Stock not found")

    def update_stock(self, stock_id, data):
        result = self.model.update_stock_by_id(stock_id, data)
        if result:
            self.view.show_message("Stock updated successfully")
        else:
            self.view.show_message("Failed to update stock")

    def delete_stock(self, stock_id):
        result = self.model.delete_stock_by_id(stock_id)
        if result:
            self.view.show_message("Stock deleted successfully")
        else:
            self.view.show_message("Failed to delete stock")

    def load_stock_graph(self, symbol, date_from, source='tiingo'):
        graph_data = self.model.get_stock_graph_by_symbol_from(symbol, date_from, source)
        if graph_data:
            self.view.display_stock_graph(graph_data)
        else:
            self.view.show_message("Stock graph data not available")

    def post_ticker_data(self, ticker, days):
        result = self.model.post_stock_ticker_data(ticker, days)
        if result:
            self.view.show_message("Ticker data posted successfully")
        else:
            self.view.show_message("Failed to post ticker data")


