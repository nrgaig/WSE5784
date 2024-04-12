# from stock import Stock 
# from view import View
import frontHand.stock as stock
from view import StockViewer

# from frontHand.stock import Stock
# from frontHand.view import StockViewer

class Presenter:
#
# The Presenter class is responsible for handling the logic of the application.
#

    # initializing the view and the list of stocks
    def __init__(self):
        self.view = StockViewer()
      #  self.view.stock_list.itemClicked.connect(self.stock_clicked)
        self.load_stocks()

    def load_stocks(self):
        stocks = stock.get_all_stocks()
        if stocks:
            self.view.list_stocks(stocks)
        else:
            self.view.show_message("No stocks available")

    # adding a stock to the list of stocks   
    def add_stock_to_list(self,symbol, company_name, price):
        try:
            stock.add_stock(symbol, company_name, price)
            self.load_stocks()
            self.view.show_message("Stock added successfully")
        except Exception as e:
            self.view.show_message(f"Error adding stock: {e}")


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
            stock.delete_stock(symbol)
            self.load_stocks()
            self.view.show_message("Stock deleted successfully")
        except Exception as e:
            self.view.show_message(f"Error deleting stock: {e}")

    # deleting a stock according to the company name
    def delete_stock_by_company_name(self, company_name):
        try:
            stock.delete_stock(company_name)
            self.load_stocks()
            self.view.show_message("Stock deleted successfully")
        except Exception as e:
            self.view.show_message(f"Error deleting stock: {e}")
        
    def update_stock_price(self, symbol=None, company_name=None, new_price=None):
        try:
            stock.update_stock(symbol, company_name, new_price)
            self.load_stocks()
            self.view.show_message("Stock updated successfully")
        except Exception as e:
            self.view.show_message(f"Error updating stock price: {e}")
        

    #TODO check this method necessary
    def buy_stock(self, symbol, quantity):
        try:
            #stock = 
            self._buy_stock(symbol, quantity)
        except Exception as e:
            print(f"Error buying stock: {e}")

        # for stock in self.stocks:
        #     if stock.symbol == symbol:
        #         stock.buy(quantity)
        #         print(f"Bought {quantity} shares of {stock.symbol}")
        #         return
        # print(f"Stock with symbol {symbol} not found")

        