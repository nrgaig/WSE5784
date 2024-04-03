# from stock import Stock 
# from view import View

from frontHand.stock import Stock
from frontHand.view import StockViewer

class Presenter:
    # initializing the view and the list of stocks
    def __init__(self):
        self.view = StockViewer()
        self.stocks = []

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
        for stock in self.stocks:
            if stock.symbol == symbol:
                self.stocks.remove(stock)
                return
        print(f"Stock with symbol {symbol} not found")

    # deleting a stock according to the company name
    def delete_stock_by_company_name(self, company_name):
        for stock in self.stocks:
            if stock.company_name == company_name:
                self.stocks.remove(stock)
                return
        print(f"Stock with company name {company_name} not found")


    def update_stock_price(self, symbol=None, company_name=None, new_price=None):
        for stock in self.stocks:
            if symbol and stock.symbol == symbol:
                stock.current_price = new_price
                return
            elif company_name and stock.company_name == company_name:
                stock.current_price = new_price
                return
        print("Stock not found")

    #TODO check this method necessary
    def buy_stock(self, symbol, quantity):
        for stock in self.stocks:
            if stock.symbol == symbol:
                stock.buy(quantity)
                print(f"Bought {quantity} shares of {stock.symbol}")
                return
        print(f"Stock with symbol {symbol} not found")

        