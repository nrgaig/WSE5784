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
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(917, 768)
        self.actionAdd = QAction(MainWindow)
        self.actionAdd.setObjectName(u"actionAdd")
        icon = QIcon()
        icon.addFile(u"../icons/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAdd.setIcon(icon)
        self.actionDelete = QAction(MainWindow)
        self.actionDelete.setObjectName(u"actionDelete")
        icon1 = QIcon()
        icon1.addFile(u"../icons/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionDelete.setIcon(icon1)
        self.actionRefresh = QAction(MainWindow)
        self.actionRefresh.setObjectName(u"actionRefresh")
        icon2 = QIcon()
        icon2.addFile(u"../icons/refresh.png", QSize(), QIcon.Normal, QIcon.Off)
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
        self.portfolioList = QListView(self.infoFrame)
        self.portfolioList.setObjectName(u"portfolioList")
        self.portfolioList.setGeometry(QRect(10, 40, 431, 301))
        self.listFrame = QFrame(self.infoFrame)
        self.listFrame.setObjectName(u"listFrame")
        self.listFrame.setGeometry(QRect(450, 0, 435, 707))
        self.vivoList = QListView(self.listFrame)
        self.vivoList.setObjectName(u"vivoList")
        self.vivoList.setGeometry(QRect(0, 30, 421, 671))

        self.lineEdit = QLineEdit(self.listFrame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QRect(0, 0, 411, 21))
        self.lineEdit.textChanged.connect(self.lineEdit.textChanged)

        self.portfolioList_2 = QListView(self.infoFrame)
        self.portfolioList_2.setObjectName(u"portfolioList_2")
        self.portfolioList_2.setGeometry(QRect(10, 380, 431, 301))

        self.mainLayout.addWidget(self.infoFrame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 917, 22))
        self.menu = QMenu(self.menuBar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.menuBar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setProperty("main_window", QCoreApplication.translate("MainWindow", u"Share Portfolio Manager", None))
        self.actionAdd.setText(QCoreApplication.translate("MainWindow", u"Add Stock", None))
        self.actionDelete.setText(QCoreApplication.translate("MainWindow", u"Delete Stock", None))
        self.actionRefresh.setText(QCoreApplication.translate("MainWindow", u"Refresh List", None))
#if QT_CONFIG(tooltip)
        self.portfolioList.setToolTip(QCoreApplication.translate("MainWindow", u"Portfolio", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.vivoList.setToolTip(QCoreApplication.translate("MainWindow", u"Vivo Stock List", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.portfolioList_2.setToolTip(QCoreApplication.translate("MainWindow", u"Portfolio", None))
#endif // QT_CONFIG(tooltip)
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u05ea\u05d9\u05e7 \u05d4\u05de\u05e0\u05d9\u05d5\u05ea \u05e9\u05dc\u05d9", None))
    # retranslateUi

