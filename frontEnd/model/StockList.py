
class StockList:
    def __init__(self):
        self.stocks = []

    def get_all_stocks(self):
        return self.stocks

    def get_stock_by_id(self, stock_id):
        for stock in self.stocks:
            if stock.Id == stock_id:
                return stock
        return None

    def get_stock_from_list_by_symbol(self, symbol):
        for stock in self.stocks:
            if stock.Ticker == symbol:
                return stock
        return None
    def AddStock(self, ticker):
        self.stocks.append(ticker)
        if ticker:
            return True
        return False

    def delete_Stock_by_symbol(self, symbol):
        for stock in self.stocks:
            if stock.Ticker == symbol:
                self.stocks.remove(stock)
                return True
        return False