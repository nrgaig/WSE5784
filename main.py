import sys

from PySide6.QtWidgets import QApplication  # Ensure this is imported
from PyQt5.QtWidgets import QApplication
from frontHand import presenter
from PySide6.QtUiTools import QUiLoader

def main():
    app = QApplication(sys.argv)  # Create QApplication instance first
    presenter = presenter.Presenter()
    
    sys.exit(app.exec_())  # Start the application's event loop

if __name__ == "__main__":
    main()
