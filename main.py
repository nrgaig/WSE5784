import sys
from frontHand import presenter

def main():
    presenter = presenter()
    presenter.add_new_stock()

if __name__ == "__main__":
    main()