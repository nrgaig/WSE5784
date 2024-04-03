import sys
from PySide6.QtWidgets import QApplication  # Ensure this is imported
from frontHand.presenter import Presenter

def main():
    app = QApplication(sys.argv)  # Create QApplication instance first
    presenter = Presenter()
    presenter.add_stock_to_list("Tech Corp", "TC", 100.0)
    presenter.list_stocks()
    presenter.update_stock_price(symbol="TC", new_price=105.0)
    presenter.buy_stock(symbol="TC", quantity=5)
    sys.exit(app.exec_())  # Start the application's event loop

if __name__ == "__main__":
    main()
