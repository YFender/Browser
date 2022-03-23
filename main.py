from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
# from PyQt5 import QtWebEngineWidgets
from mainwindow import *
from sys import argv, exit
from re import match, findall


class Browser(QtWidgets.QMainWindow):
    def __init__(self):
        super(Browser, self).__init__()
        self.ui = Ui_Browser()
        self.ui.setupUi(self)

        self.ui.toolButton_back.clicked.connect(self.back)
        self.ui.toolButton_home.clicked.connect(self.home)
        self.ui.toolButton_search.clicked.connect(self.search)
        self.ui.toolButton_refresh.clicked.connect(self.refresh)

        self.webview = QtWebEngineWidgets.QWebEngineView()
        self.ui.gridLayout.addWidget(self.webview, 1, 0, 1, 7)

        self.home()

    def back(self):
        self.webview.back()

    def refresh(self):
        self.webview.reload()

    def home(self):
        home_page = QtCore.QUrl("https://yandex.ru/")
        self.webview.load(home_page)

    def search(self):
        search_text = self.ui.lineEdit.text()
        if search_text != "":
            if not match('^((ftp|http|https):\/\/)?(www\.)?([A-Za-zА-Яа-я0-9]{1}[A-Za-zА-Яа-я0-9\-]*\.?)*\.{1}[A-Za-zА-Яа-я0-9-]{2,8}(\/([\w#!:.?+=&%@!\-\/])*)?', search_text):
                search_text = QtCore.QUrl(
                    "http://yandex.ru/search/?text=" + search_text)
                self.webview.load(search_text)
            else:
                if not search_text.startswith("http"):
                    try:
                        search_text = QtCore.QUrl("http://" + search_text)
                        self.webview.load(search_text)
                        self.ui.lineEdit.setText(
                            "http://" + self.ui.lineEdit.text())
                    except:
                        search_text = QtCore.QUrl("https://" + search_text)
                        self.webview.load(search_text)
                        self.ui.lineEdit.setText(
                            "https://" + self.ui.lineEdit.text())


if __name__ == "__main__":
    app = QtWidgets.QApplication(argv)
    myapp = Browser()
    myapp.show()
    exit(app.exec_())
