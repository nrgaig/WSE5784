#model

# The model is the part of the application that is responsible for managing the data. It receives input from the presenter and processes it.ֹ
from presenter import Presenter
import requests
class Stock: 
    def __init__(self, base_url="http://localhost:5210/api/Stock"):
        self.base_url = base_url

    def get_all_stocks(self):
        """Fetch all stocks."""
        try:
            response = requests.get(f"{self.base_url}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occurred: {e}")
        except requests.exceptions.RequestException as e:
            print(f"Error getting stocks: {e}")
        return None

    def get_stock_by_id(self, stock_id):
        """Fetch a single stock by its database ID."""
        try:
            response = requests.get(f"{self.base_url}/{stock_id}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occurred: {e}")
        except requests.exceptions.RequestException as e:
            print(f"Error getting stock: {e}")
        return None

    def get_stock_by_symbol(self, symbol):
        """Fetch a single stock by its symbol."""
        try:
            response = requests.get(f"{self.base_url}/tiingo/{symbol}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occurred: {e}")
        except requests.exceptions.RequestException as e:
            print(f"Error getting stock by symbol: {e}")
        return None

    def update_stock_by_id(self, stock_id, data):
        """Update a stock entry by ID."""
        try:
            response = requests.put(f"{self.base_url}/{stock_id}", json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occurred: {e}")
        except requests.exceptions.RequestException as e:
            print(f"Error updating stock: {e}")
        return None

    def delete_stock_by_id(self, stock_id):
        """Delete a stock entry by ID."""
        try:
            response = requests.delete(f"{self.base_url}/{stock_id}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occurred: {e}")
        except requests.exceptions.RequestException as e:
            print(f"Error deleting stock: {e}")
        return None

    def get_stock_graph_by_symbol_from(self, symbol, date_from, source='tiingo'):
        """Retrieve stock graph data from a specified source starting from a specific date."""
        try:
            url = f"{self.base_url}/{source}/{symbol}/graph/{date_from}"
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occurred: {e}")
        except requests.exceptions.RequestException as e:
            print(f"Error retrieving stock graph data: {e}")
        return None

    def post_stock_ticker_data(self, ticker, days):
        """Post data to the database regarding a stock's ticker for a specified number of days."""
        try:
            url = f"{self.base_url}/tiingoPost/{ticker}/db/{days}"
            response = requests.post(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occurred: {e}")
        except requests.exceptions.RequestException as e:
            print(f"Error posting stock ticker data: {e}")
        return None
    
