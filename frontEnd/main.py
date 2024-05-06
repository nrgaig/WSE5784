import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from MainWindow import MainWindow
import Stock
import presenter

def main():
    app = QApplication(sys.argv)
    view = MainWindow()
    model = Stock()
    # Use a different name for the presenter instance
    presenter_instance = presenter.Presenter(view, model)
    view.show()
    app.exec()

if __name__ == '__main__':
    main()