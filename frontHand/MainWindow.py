# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(986, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.mainLayout.setObjectName("mainLayout")
        self.listFrame = QtWidgets.QFrame(self.centralwidget)
        self.listFrame.setObjectName("listFrame")
        self.listLayout = QtWidgets.QVBoxLayout(self.listFrame)
        self.listLayout.setObjectName("listLayout")
        self.vivoList = QtWidgets.QListView(self.listFrame)
        self.vivoList.setObjectName("vivoList")
        self.listLayout.addWidget(self.vivoList)
        self.mainLayout.addWidget(self.listFrame)
        self.infoFrame = QtWidgets.QFrame(self.centralwidget)
        self.infoFrame.setObjectName("infoFrame")
        self.infoLayout = QtWidgets.QVBoxLayout(self.infoFrame)
        self.infoLayout.setObjectName("infoLayout")
        self.toolBar = QtWidgets.QToolBar(self.infoFrame)
        self.toolBar.setObjectName("toolBar")
        self.infoLayout.addWidget(self.toolBar)
        self.portfolioList = QtWidgets.QListView(self.infoFrame)
        self.portfolioList.setObjectName("portfolioList")
        self.infoLayout.addWidget(self.portfolioList)
        self.clockDisplay = QtWidgets.QLCDNumber(self.infoFrame)
        self.clockDisplay.setSegmentStyle(QtCore.Qt.Flat)
        self.clockDisplay.setObjectName("clockDisplay")
        self.infoLayout.addWidget(self.clockDisplay)
        self.mainLayout.addWidget(self.infoFrame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionAdd = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdd.setIcon(icon)
        self.actionAdd.setObjectName("actionAdd")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../icons/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDelete.setIcon(icon1)
        self.actionDelete.setObjectName("actionDelete")
        self.actionRefresh = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../icons/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRefresh.setIcon(icon2)
        self.actionRefresh.setObjectName("actionRefresh")
        self.toolBar.addAction(self.actionAdd)
        self.toolBar.addAction(self.actionDelete)
        self.toolBar.addAction(self.actionRefresh)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Share Portfolio Manager"))
        self.vivoList.setToolTip(_translate("MainWindow", "Vivo Stock List"))
        self.portfolioList.setToolTip(_translate("MainWindow", "Portfolio"))
        self.actionAdd.setText(_translate("MainWindow", "Add Stock"))
        self.actionDelete.setText(_translate("MainWindow", "Delete Stock"))
        self.actionRefresh.setText(_translate("MainWindow", "Refresh List"))
import icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
