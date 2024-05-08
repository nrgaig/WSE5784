class StockModel:
    def __init__(self, id: int, name: str, ticker: str, description: str,tiingoPriceDtos: list,value) :
        self.Id = id
        self.Name = name
        self.Ticker = ticker
        self.Description = description
        self.TiingoPriceDtos = tiingoPriceDtos
        self.Value = value
    def __repr__(self) -> str:
        return (f"Name: {self.Name}\n"
                f"Ticker: {self.Ticker}\n"
                f"ID: {self.Id}\n"
                f"Description: {self.Description}\n"
                f"Prices: {self.TiingoPriceDtos}\n"
                f"Value: {self.Value}")