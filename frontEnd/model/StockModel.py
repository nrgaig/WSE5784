class tiingoPriceDtos:
    def __init__(self, id: int, date: str, close: float, high: float, low: float, open: float, volume: int ,divCash: float, splitFactor: float,stockId: int,stock ):
        self.Id = id
        self.Date = date
        self.Close = close
        self.High = high
        self.Low = low
        self.Open = open
        self.Volume = volume
        self.DivCash = divCash
        self.SplitFactor = splitFactor
        self.StockId = stockId


class StockModel:
    def __init__(self, id: int, name: str, ticker: str, description: str, value: float, tiingoPriceDtos=None):
        self.Id = id
        self.Name = name
        self.Ticker = ticker
        self.Description = description
        self.TiingoPriceDtos = tiingoPriceDtos or []
        self.Value = value

    def __repr__(self) -> str:
        return (f"Name: {self.Name}\n"
                f"Ticker: {self.Ticker}\n"
                f"ID: {self.Id}\n"
                f"Description: {self.Description}\n"
                f"Prices: {self.TiingoPriceDtos}\n"
                f"Value: {self.Value}")
