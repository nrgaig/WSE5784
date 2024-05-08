from PySide6.QtWidgets import QApplication
from View import View
from Stock import Stock
from presenter import presenter
import sys
def setup_mvp():
    model = Stock()
    view_instance = View()
    presenter_instance = presenter(view_instance, model)
    return view_instance

def main():
    app = QApplication(sys.argv)
    view_instance = setup_mvp()
    view_instance.show()
    app.exec()

if __name__ == '__main__':
    main()
