from stock import Stock 
from view import View

class Presenter:
    def __init__(self):
        self.view = View()
        self.stocks = []
    
    def add_stock(self, symbol, company_name, current_price):
        stock = Stock(symbol, company_name, current_price)
        self.stocks.append(stock)
    
    def list_stocks(self):
        self.view.list_stocks(self.stocks)
    
    def show_stock(self, symbol):
        for stock in self.stocks:
            if stock.symbol == symbol:
                self.view.show_stock(stock)
                break
