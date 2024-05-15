# model
import json

from model.StockModel import StockModel, tiingoPriceDtos
from typing import Optional
# The model is the part of the application that is responsible for managing the data. It receives input from the presenter and processes it.ֹ
import requests

DAYS = 30  # number of days to get the stock data


class Stock:
    def __init__(self, base_url="http://localhost:5210/api/Stock"):
        self.base_url = base_url
        self.Stock_list = []

    #############functions of stock list ############################
    def load_stock_to_list(self, ticker):
        self.Stock_list.append(ticker)
        if self.Stock_list[-1]:
            return True
        return False

    def delete_stock_by_symbol_from_list(self, symbol):
        for stock in self.Stock_list:
            if stock == symbol:
                self.Stock_list.remove(stock)
                return True
        return False

    def get_list(self):
        return self.Stock_list

    ###################### url requests by swagger - by order ######################
    def get_all_stocks_db(self) -> Optional[list[StockModel]]:
        """Fetch all stocks."""
        try:
            response = requests.get(f"{self.base_url}")
            response.raise_for_status()
            json_str = response.text
            json_obj = json.loads(json_str)
            return [StockModel(**obj) for obj in json_obj]
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occurred get_all_stocks: {e}")
        except requests.exceptions.RequestException as e:
            print(f"Error getting stocks get_all_stocks: {e}")
        return None

    def get_stock_and_history_by_id_db(self, stock_id) -> Optional[StockModel]:
        """Fetch a single stock by its database ID."""
        try:
            response = requests.get(f"{self.base_url}/stocks/{stock_id}")
            response.raise_for_status()
            json_str = response.text
            json_obj = json.loads(json_str)
            return StockModel(**json_obj)
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occurred get_stock_by_query_val: {e}")
        except requests.exceptions.RequestException as e:
            print(f"Error getting stocks get_stock_by_query_val: {e}")
        return None

    def get_stock_and_history_by_ticker_db(self, ticker) -> Optional[StockModel]:
        """Fetch a single stock by its database ID."""
        try:
            response = requests.get(f"{self.base_url}/stocks/{ticker}")
            response.raise_for_status()
            json_str = response.text
            json_obj = json.loads(json_str)
            return StockModel(**json_obj)
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occurred get_stock_by_id: {e}")
        except requests.exceptions.RequestException as e:
            print(f"Error getting stock get_stock_by_id: {e}")
            print(f"Error getting stock: {e}")

    def get_stock_by_ticker_tiingo(self, ticker) -> Optional[StockModel]:
        """Fetch a single stock by its exect ticker name."""
        try:
            response = requests.get(f"{self.base_url}/tiingo/{ticker}")
            response.raise_for_status()
            json_str = response.text
            json_obj = json.loads(json_str)
            return StockModel(**json_obj)
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occurred: {e}")
        except requests.exceptions.RequestException as e:
            print(f"Error getting stocks: {e}")

    def get_stock_graph_by_symbol_tiingo(self, ticker) -> Optional[StockModel]:
        """Fetch a single stock by its exect ticker name."""
        try:
            response = requests.get(f"{self.base_url}/tiingo/{ticker}")
            response.raise_for_status()
            json_str = response.text
            json_obj = json.loads(json_str)
            return [StockModel(**obj) for obj in json_obj]
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occurred: {e}")
        except requests.exceptions.RequestException as e:
            print(f"Error getting stocks: {e}")

    def get_stock_by_query_db(self, query):
        """Retrieve stock graph data based on a query."""
        try:
            response = requests.get(f"{self.base_url}/q/{query}")
            if response.status_code == 200:
                json_str = response.text
                json_obj = json.loads(json_str)
                return [StockModel(**obj) for obj in json_obj]
            elif response.status_code == 404:
                return self.post_stock_ticker_data(query, 30)
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occurred: {e}")
        except requests.exceptions.RequestException as e:
            print(f"Error retrieving stock graph data: {e}")
        return None

    def get_stock_by_ticker_val_db(self, query):
        """  get one day stock data """
        try:
            response = requests.get(f"{self.base_url}/s+dayprice/{query}")
            response.raise_for_status()
            json_str = response.text
            json_obj = json.loads(json_str)
            return StockModel(**json_obj)
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occurred: {e}")
        except requests.exceptions.RequestException as e:
            print(f"Error getting stocks: {e}")
        return None

    def get_TiingoPriceDtoList_by_ticker_from_tiingo(self, symbol, days=30) -> Optional[StockModel]:
        """get TiingoPriceDtoList of stock for some days."""
        try:
            response = requests.get(f"{self.base_url}/TiingoPriceDtoList/{symbol}/db/{days}")
            response.raise_for_status()
            json_str = response.text
            json_obj = json.loads(json_str)
            print(json_obj)
            # return 1
            return [tiingoPriceDtos(**obj) for obj in json_obj]
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occurred in priceList: {e}")
        except requests.exceptions.RequestException as e:
            print(f"Error getting stock by symbol in priceList: {e}")
        return None

    def get_description_by_symbol(self, symbol) -> Optional[str]:
        """Fetch a single stock description by its symbol."""
        try:
            return requests.get(f"{self.base_url}/StockDescription/{symbol}")
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occurred in fetching description: {e}")
        except requests.exceptions.RequestException as e:
            print(f"Error getting stock in fetching description: {e}")
        return None

    def update_stock_by_id(self, stock_id, data) -> Optional[StockModel]:
        """Update a stock entry by ID."""
        try:
            response = requests.put(f"{self.base_url}/{stock_id}", json=data)
            response.raise_for_status()
            json_str = response.text
            json_obj = json.loads(json_str)
            return StockModel(**json_obj)
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occurred in updating stock: {e}")
        except requests.exceptions.RequestException as e:
            print(f"Error updating stock: {e}")
        return None

    def delete_stock_by_id(self, stock_id) -> Optional[bool]:
        """Delete a stock entry by ID."""
        try:
            response = requests.delete(f"{self.base_url}/{stock_id}")
            return response.status_code == 204
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occurred in deleting stock: {e}")
        except requests.exceptions.RequestException as e:
            print(f"Error deleting stock: {e}")
        return None

    def get_stock_details_from_db_by_query(self, query):
        """Retrieve stock graph data based on a query."""
        try:
            response = requests.get(f"{self.base_url}/q/{query}")
            if response.status_code == 200:
                json_str = response.text
                json_obj = json.loads(json_str)
                return [StockModel(**obj) for obj in json_obj]
            elif response.status_code == 404:
                pass  # return self.post_stock_ticker_data(query, 30)
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occurred retrieving stock graph: {e}")
        except requests.exceptions.RequestException as e:
            print(f"Error retrieving stock graph data: {e}")
        return None

    def get_stock_graph_by_symbol_from(self, symbol, date_from, source='tiingo'):
        """Retrieve stock graph data from a specified source starting from a specific date."""
        try:
            url = f"{self.base_url}/{source}/{symbol}/graph/{date_from}"
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occurred stock_graph_by_symbol: {e}")
        except requests.exceptions.RequestException as e:
            print(f"Error retrieving stock_graph_by_symbol: {e}")
        return None

    def post_stock_ticker_data(self, ticker, days):
        """Post data to the database regarding a stock's ticker for a specified number of days."""
        try:
            url = f"{self.base_url}/tiingoPost/{ticker}/db/{days}"
            response = requests.post(url)
            response.raise_for_status()
            if (response.status_code == 200):
                print(f"post success")
                return True
            elif (response.status_code == 404):
                print(f"stock not found")
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occurred post_stock_ticker_data: {e}")
        except requests.exceptions.RequestException as e:
            print(f"Error posting stock ticker data: {e}")
        return None
    
    def get_stock_details_by_ticker_db(self,ticker):
        """:return a single stock details by its ticker."""
        try:
            response = requests.get(f"{self.base_url}/stockDto/{ticker}")
            response.raise_for_status()
            json_str = response.text
            json_obj = json.loads(json_str)
            return StockModel(**json_obj)

        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occurred get_stock_by_query_val: {e}")
        except requests.exceptions.RequestException as e:
            print(f"Error getting stocks get_stock_by_query_val: {e}")
        return None

    def delete_all_stocks (self):
        try:
            self.Stock_list.clear()
        except Exception as e:
            print(f"Error deleting all stocks: {str(e)}")
