
import MainWindow

from stock import Stock
class Presenter:
#
# The Presenter class is responsible for handling the logic of the application.
# It receives input from the user and sends it to the model for processing.
#

    # initializing the view and the list of stocks
    def __init__(self,view, model):
        self.view = view
        self.model = model


        
    def show_MainWindow(self):
        self.main_window.set_current_view(MainWindow())

    def show_view2(self):
        self.main_window.set_current_view(View2())

    def load_stocks(self):
        stocks = self.model.get_all_stocks()
        if stocks:
            self.view.list_stocks(stocks)
        else:
            self.view.show_message("No stocks available")

    # adding a stock to the list of stocks   
    def add_stock_to_list(self,symbol, company_name, price):
        stock = Stock(company_name=company_name, symbol=symbol, current_price=price)
        self.stocks.append(stock)

    # listing all the stocks
    def list_stocks(self):
        if not self.stocks:
            print("No stocks available.")
        else:
            self.view.list_stocks(self.stocks)
    # showing a stock according to the symbol or the company name
    def show_stock(self, symbol=None, company_name=None):
        for stock in self.stocks:
            if symbol and stock.symbol == symbol:
                self.view.show_stock(stock)
                return
            elif company_name and stock.company_name == company_name:
                self.view.show_stock(stock)
                return
        print("Stock not found") #TODO replace the message?

    # deleting a stock according to the symbol 
    def delete_stock_by_symbol(self, symbol):
        try:
            delete_stock(symbol)
            self.load_stocks()
            self.view.show_message("Stock deleted successfully")
        except Exception as e:
            self.view.show_message(f"Error deleting stock: {e}")

    # deleting a stock according to the company name
    def delete_stock_by_company_name(self, company_name):
        try:
            delete_stock(company_name)
            self.load_stocks()
            self.view.show_message("Stock deleted successfully")
        except Exception as e:
            self.view.show_message(f"Error deleting stock: {e}")

        try:
            stock.delete_stock(company_name)
            self.load_stocks()
            self.view.show_message("Stock deleted successfully")
        except Exception as e:
            self.view.show_message(f"Error deleting stock: {e}")

    def update_stock_price(self, symbol=None, company_name=None, new_price=None):
        try:
            update_stock(symbol, company_name, new_price)
            self.load_stocks()
            self.view.show_message("Stock updated successfully")
        except Exception as e:
            self.view.show_message(f"Error updating stock price: {e}")


