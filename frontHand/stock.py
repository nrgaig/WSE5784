#model
class Stock: 
    __tablename__ = 'stocks'
    def __init__ (self, symbol, company_name, current_price):
        self.symbol = symbol
        self.company_name = company_name
        self.current_price = current_price
#TODO conect to the database

    def delete_stock(symbol):
        pass
    def add_stock(symbol, company_name, price):
        pass
    def get_all_stocks():
        pass
    def get_stock(symbol):
        pass
    def get_stock_by_company_name(company_name):
        pass
        