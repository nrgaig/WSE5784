# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLineEdit,
    QListView, QMainWindow, QMenu, QMenuBar,
    QScrollBar, QSizePolicy, QStatusBar, QWidget)



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(878, 768)
        self.actionAdd = QAction(MainWindow)
        self.actionAdd.setObjectName(u"actionAdd")
        icon = QIcon()
        icon.addFile(u"../../../Users/ziv52/.designer/icons/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAdd.setIcon(icon)
        self.actionDelete = QAction(MainWindow)
        self.actionDelete.setObjectName(u"actionDelete")
        icon1 = QIcon()
        icon1.addFile(u"../../../Users/ziv52/.designer/icons/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionDelete.setIcon(icon1)
        self.actionRefresh = QAction(MainWindow)
        self.actionRefresh.setObjectName(u"actionRefresh")
        icon2 = QIcon()
        icon2.addFile(u"../../../Users/ziv52/.designer/icons/refresh.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionRefresh.setIcon(icon2)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mainLayout = QHBoxLayout(self.centralwidget)
        self.mainLayout.setObjectName(u"mainLayout")
        self.verticalScrollBar = QScrollBar(self.centralwidget)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setOrientation(Qt.Vertical)

        self.mainLayout.addWidget(self.verticalScrollBar)

        self.infoFrame = QFrame(self.centralwidget)
        self.infoFrame.setObjectName(u"infoFrame")
        self.StockExtendedDisplay = QListView(self.infoFrame)
        self.StockExtendedDisplay.setObjectName(u"StockExtendedDisplay")
        self.StockExtendedDisplay.setGeometry(QRect(10, 40, 431, 301))
        self.listFrame = QFrame(self.infoFrame)
        self.listFrame.setObjectName(u"listFrame")
        self.listFrame.setGeometry(QRect(450, 0, 435, 707))
        self.StockDisplay = QListView(self.listFrame)
        self.StockDisplay.setObjectName(u"StockDisplay")
        self.StockDisplay.setGeometry(QRect(0, 30, 421, 671))
        self.lineEdit = QLineEdit(self.listFrame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QRect(0, 0, 411, 21))
        self.StockGraph = QListView(self.infoFrame)
        self.StockGraph.setObjectName(u"StockGraph")
        self.StockGraph.setGeometry(QRect(10, 380, 431, 301))

        self.mainLayout.addWidget(self.infoFrame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 878, 22))
        self.menu = QMenu(self.menuBar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menuBar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi
    def list_stocks(self, stocks):
        self.listView.clear()
        for stock in stocks:
            self.listView.addItem(f"{stock['symbol']} - {stock['name']}")

    def show_message(self, message):
        #todo Implement a method to show messages, e.g., error messages or confirmations.
        print(message)
    def retranslateUi(self, MainWindow):
        MainWindow.setProperty("main_window", QCoreApplication.translate("MainWindow", u"Share Portfolio Manager", None))
        self.actionAdd.setText(QCoreApplication.translate("MainWindow", u"Add Stock", None))
        self.actionDelete.setText(QCoreApplication.translate("MainWindow", u"Delete Stock", None))
        self.actionRefresh.setText(QCoreApplication.translate("MainWindow", u"Refresh List", None))
#if QT_CONFIG(tooltip)
        self.StockExtendedDisplay.setToolTip(QCoreApplication.translate("MainWindow", u"Portfolio", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.StockDisplay.setToolTip(QCoreApplication.translate("MainWindow", u"Vivo Stock List", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u05d7\u05e4\u05e9 \u05db\u05d0\u05df ", None))
#if QT_CONFIG(tooltip)
        self.StockGraph.setToolTip(QCoreApplication.translate("MainWindow", u"Portfolio", None))
#endif // QT_CONFIG(tooltip)
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u05ea\u05d9\u05e7 \u05d4\u05de\u05e0\u05d9\u05d5\u05ea \u05e9\u05dc\u05d9", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u05db\u05dc \u05d4\u05de\u05e0\u05d9\u05d5\u05ea", None))
    # retranslateUi


