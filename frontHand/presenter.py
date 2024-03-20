from stock import Stock 
from view import View

class Presenter:
    # initializing the view and the list of stocks
    def __init__(self):
        self.view = View()
        self.stocks = []

    # adding a stock to the list of stocks   
    def add_stock(self, symbol, company_name, current_price):
        stock = Stock(symbol, company_name, current_price)
        self.stocks.append(stock)

    # listing all the stocks
    def list_stocks(self):
        self.view.list_stocks(self.stocks)

    # showing a specific stock
    def show_stock(self, symbol):
        for stock in self.stocks:
            if stock.symbol == symbol:
                self.view.show_stock(stock)
                break

    # deleting a stock from the list of stocks
    def delete_stock(self, symbol):
        for stock in self.stocks:
            if stock.symbol == symbol:
                self.stocks.remove(stock)
                break
            else:
                print(f"Stock with symbol {symbol} not found")
                
    # updating the price of a stock
    def update_stock(self, symbol, new_price):
        for stock in self.stocks:
            if stock.symbol == symbol:
                stock.current_price = new_price
                break
            else:
                print(f"Stock with symbol {symbol} not found")

