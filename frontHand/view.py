class View:
    
    # printing the list of stocks to the user
    def list_stocks(self, stocks):
        for stock in stocks:
            print(f"{stock.symbol}: {stock.company_name} at ${stock.current_price}")
    
    # printing a specific stock to the user
    def show_stock(self, stock):
        print(f"Current price of {stock.symbol} ({stock.company_name}) is ${stock.current_price}")
