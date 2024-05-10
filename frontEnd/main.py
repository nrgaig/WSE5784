from PySide6.QtWidgets import QApplication
from view.View import View
from model.Stock import Stock
from presnter.presenter import presenter
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
