from stock import Stock 
from view import View

class Presenter:
    # initializing the view and the list of stocks
    def __init__(self):
        self.view = View().StockViewer()
        self.stocks = Stock() 

    # adding a stock to the list of stocks   
    def add_stock_to_list(self, company_name):
        stock = Stock(company_name)
        self.stocks.append(stock)

    # listing all the stocks
    def list_stocks(self):
        self.view.list_stocks(self.stocks)

    # showing a specific stock according to the symbol
    def show_stock(self, symbol):
        for stock in self.stocks:
            if stock.symbol == symbol:
                self.view.show_stock(stock)
                break
    # showing a specific stock according to the company name
    #TODO integrate this method with search by symbol
    def show_stock(self, company_name):
        for stock in self.stocks:
            if stock.company_name == company_name:
                self.view.show_stock(stock)
                break

    # deleting a stock from the list of stocks according to the symbol
    def delete_stock(self, symbol):
        for stock in self.stocks:
            if stock.symbol == symbol:
                self.stocks.remove(stock)
                break
            else:
                print(f"Stock with symbol {symbol} not found")
    # deleting a stock from the list of stocks according to the company name
    #TODO delete from where?
    def delete_stock(self, company_name):
        for stock in self.stocks:
            if stock.company_name == company_name:
                self.stocks.remove(stock)
                break
            else:
                print(f"Stock with company name {company_name} not found")

    # updating the price of a stock according to the symbol
    def update_stock(self, symbol, new_price):
        for stock in self.stocks:
            if stock.symbol == symbol:
                stock.current_price = new_price
                break
            else:
                print(f"Stock with symbol {symbol} not found")

    # updating the price of a stock according to the company name
    def update_stock(self, company_name, new_price):
        for stock in self.stocks:
            if stock.company_name == company_name:
                stock.current_price = new_price
                break
            else:
                print(f"Stock with company name {company_name} not found")
    #TODO check this method necessary
    def buy_stock(self, symbol, quantity):
        for stock in self.stocks:
            if stock.symbol == symbol:
                stock.buy(quantity)
                break
            else:
                print(f"Stock with symbol {symbol} not found")