from typing import Optional
import StockModel


class presenter:
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.view.set_presenter(self)

    def get_all_stocks(self):
        try:
            stocks = self.model.get_all_stocks()
            if stocks:
                return stocks
            else:
                if hasattr(self.view, 'show_message'):
                    self.view.show_message("No stocks available")
        except Exception as e:
            self.view.show_message(f"Error loading stocks: {str(e)}")

    def load_stock_by_id(self, stock_id):
        try:
            stock = self.model.get_stock_by_id(stock_id)
            if stock:
                return stock
            else:
                self.view.show_message("Stock not found")
        except Exception as e:
            self.view.show_message(f"Error fetching stock: {str(e)}")


    def load_stock_by_symbol(self, symbol):
        try:
            stock = self.model.get_stock_by_symbol(symbol)
            if stock:
                return stock
            else:
                self.view.show_message("Stock not found")
        except Exception as e:
            self.view.show_message(f"Error fetching stock by symbol: {str(e)}")

    def load_description_by_symbol(self, symbol):
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
                    self.load_stock_by_id(stock_id)  # Refresh the displayed stock
                else:
                    self.view.show_message("Failed to update stock")
            except Exception as e:
                self.view.show_message(f"Error updating stock: {str(e)}")

    def delete_stock(self, stock_id):
        try:
            result = self.model.delete_stock_by_id(stock_id)
            if result:
                self.view.show_message("Stock deleted successfully")
                self.get_all_stocks()  # Refresh the stock list
            else:
                self.view.show_message("Failed to delete stock")
        except Exception as e:
            self.view.show_message(f"Error deleting stock: {str(e)}")

    def load_stock_graph(self, symbol, date_from, source='tiingo'):
        try:
            graph_data = self.model.get_stock_graph_by_symbol_from(symbol, date_from, source)
            if graph_data:
                self.view.display_stock_graph(graph_data)
            else:
                self.view.show_message("Stock graph data not available")
        except Exception as e:
            self.view.show_message(f"Error loading stock graph: {str(e)}")

    def post_ticker_data(self, ticker, days):
        try:
            result = self.model.post_stock_ticker_data(ticker, days)
            if result:
                self.view.show_message("Ticker data posted successfully")
            else:
                self.view.show_message("Failed to post ticker data")
        except Exception as e:
            self.view.show_message(f"Error posting ticker data: {str(e)}")
