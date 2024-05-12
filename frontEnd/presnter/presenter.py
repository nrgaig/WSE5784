from typing import Optional
from model import StockModel


# The presenter is the part of the application that is responsible for handling user input
# and responding to it. It receives input from the view and processes it.
class presenter:
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.current_stock: Optional[StockModel] = None
        self.view.set_presenter(self)

    #################functions of stock list ############################
    def get_list(self):
        return self.model.get_list()

    def delete_stock_by_symbol(self, symbol):
        """ delete stock by symbol from the list in db"""
        self.model.delete_stock_by_symbol_from_list(symbol)

    def add_stock_to_list(self, ticker):
        """ add stock by symbol to the list in db"""
        try:
            result = self.model.load_stock_to_list(ticker)
            if result:
                self.view.show_message("Stock added successfully")
            else:
                self.view.show_message("Failed to add stock")
        except Exception as e:
            self.view.show_message(f"Error adding stock: {str(e)}")

    ################# return from the model ############################
    # return all stocks from the model db
    def get_all_stocks_db(self):
        """ return all stocks from the model db"""
        try:
            stocks = self.model.get_all_stocks_db()
            if stocks:
                return stocks
            else:
                if hasattr(self.view, 'show_message'):
                    self.view.show_message("No stocks available")
        except Exception as e:
            self.view.show_message(f"Error loading stocks: {str(e)}")

    # return stock by id from the model db
    def load_stock_and_history_by_id_db(self, stock_id):
        """ return stock by id from the model db """
        try:
            stock = self.model.get_stock_and_history_by_id_db(stock_id)
            if stock:
                return stock
            else:
                self.view.show_message("Stock not found")
        except Exception as e:
            self.view.show_message(f"Error fetching stock: {str(e)}")

    # return single stock by ticker from the model db
    def load_stock_and_history_by_ticker_db(self, ticker):
        """ return single stock by ticker from the model db """
        try:
            stock = self.model.get_stock_and_history_by_ticker_db(ticker)
            if stock:
                return stock
            else:
                self.view.show_message("Stock not found")
        except Exception as e:
            self.view.show_message(f"Error fetching stock: {str(e)}")

    # return stock by symbol from the model db
    # def load_stock_and_history_by_ticker_db(self, ticker):
    #     """ return single stock by ticker from the model db """
    #     try:
    #         stock = self.model.get_stock_and_history_by_ticker_db(ticker)
    #         if stock:
    #             return stock
    #         else:
    #             self.view.show_message("Stock not found")
    #     except Exception as e:
    #         self.view.show_message(f"Error fetching stock: {str(e)}")

    def load_stock_by_ticker_tiingo(self, ticker):
        """ return stock by ticker from the tiingo api """
        try:
            stock = self.model.get_stock_by_ticker_from_tiingo(ticker)
            if stock:
                return stock
            else:
                print("Stock not found")
        except Exception as e:
            print(f"Error fetching stock: {str(e)}")

    # return stock by symbol from the tiingo api
    def load_stock_graph_by_symbol_tiingo(self, ticker):
        """ return stock by ticker from the tiingo api """
        try:
            stock = self.model.get_stock_graph_by_symbol_tiingo(ticker)
            if stock:
                return stock
            else:
                print("Stock not found")
                return None

        except Exception as e:
            print(f"Error fetching stock: {str(e)}")

    # return stock by symbol from the model db
    def load_stock_by_query_db(self, query):
        """ return stock by query from the model db """
        try:

            return self.model.get_stock_details_from_db_by_query(query)

        except Exception as e:
            print(f"Error fetching stock by query: {str(e)}")

    # return one stock by ticker from the model db
    def get_stock_by_ticker_val_db(self, ticker):
        """ return one day stock data """
        try:
            stock = self.model.get_stock_by_ticker_val_db(ticker)
            if stock:
                return stock
            else:
                print("Stock not found")
        except Exception as e:
            print(f"Error fetching stock: {str(e)}")

    # return stock by symbol from the model db
    def load_stock_by_ticker_from_tiingo(self, ticker):
        """ return stock by ticker from the tiingo api """
        try:
            stock = self.model.get_TiingoPriceDtoList_by_ticker_from_tiingo(ticker)
            if stock:
                return stock
            else:
                print("Stock not found")
                return None
        except Exception as e:
            print(f"Error fetching stock by symbol: {str(e)}")

    # return description by symbol from the model db
    def load_description_by_symbol(self, symbol):
        """ return description by symbol from the model db """
        try:
            description = self.model.get_description_by_symbol(symbol)
            if description:
                return description.text
            else:
                self.view.show_message("Stock not found")
        except Exception as e:
            self.view.show_message(f"Error fetching stock description: {str(e)}")

    def update_stock(self, stock_id, data):
        try:
            result = self.model.update_stock_by_id(stock_id, data)
            if result:
                self.view.show_message("Stock updated successfully")
                self.load_stock_and_history_by_id_db(stock_id)  # Refresh the displayed stock
            else:
                self.view.show_message("Failed to update stock")
        except Exception as e:
            self.view.show_message(f"Error updating stock: {str(e)}")

    def delete_stock_by_id(self, stock_id):
        try:
            result = self.model.delete_stock_by_id(stock_id)
            if result:
                self.view.show_message("Stock deleted successfully")
                self.get_all_stocks_db()  # Refresh the stock list
            else:
                self.view.show_message("Failed to delete stock")
        except Exception as e:
            self.view.show_message(f"Error deleting stock: {str(e)}")

    def load_stock_graph(self, symbol, date_from, source='tiingo'):
        """ Load stock graph data by symbol and date range."""
        try:
            graph_data = self.model.get_stock_graph_by_symbol_from(symbol, date_from, source)
            if graph_data:
                self.view.display_stock_graph(graph_data)
            else:
                self.view.show_message("Stock graph data not available")
        except Exception as e:
            self.view.show_message(f"Error loading stock graph: {str(e)}")

    def post_ticker_data(self, ticker, days=30):
        """add stock the db from tiingo api"""
        try:
            res = self.model.get_stock_by_ticker_val_db(ticker)
            if (res == None):
                result = self.model.post_stock_ticker_data(ticker, days)
                if result:
                    self.view.show_message("Ticker data posted successfully")
                    return True
                else:
                    self.view.show_message("Failed to post ticker data")
        except Exception as e:
            self.view.show_message(f"Error posting ticker data: {str(e)}")
        return None