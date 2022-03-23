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

        self.ui.toolButton_back.setToolTip("Назад")
        self.ui.toolButton_refresh.setToolTip("Обновить страницу")
        self.ui.toolButton_search.setToolTip("Поиск")
        self.ui.toolButton_home.setToolTip("Домой")

        self.webview.urlChanged.connect(
            lambda: self.ui.lineEdit.setText(f"{self.webview.url().toString()}"))

        self.home()

    def back(self):
        self.webview.back()

    def refresh(self):
        self.webview.reload()

    def home(self):
        home_page = QtCore.QUrl("https://google.com")
        self.webview.load(home_page)

    def search(self):
        # print(self.webview.page().url())
        search_text = self.ui.lineEdit.text()
        if search_text != "":
            print(match(
                '^((ftp|http|https):\/\/)?(www\.)?([A-Za-zА-Яа-я0-9]{1}[A-Za-zА-Яа-я0-9\-]*\.?)*\.{1}[A-Za-zА-Яа-я0-9-]{2,8}(\/([\w#!:.?+=&%@!\-\/])*)?', search_text))
            if not match('^((ftp|http|https):\/\/)?(www\.)?([A-Za-zА-Яа-я0-9]{1}[A-Za-zА-Яа-я0-9\-]*\.?)*\.{1}[A-Za-zА-Яа-я0-9-]{2,8}(\/([\w#!:.?+=&%@!\-\/])*)?', search_text):
                search_text = QtCore.QUrl(
                    "https://google.com/search?q=" + search_text)
                self.webview.load(search_text)
                # print(self.webview.page().url())
            else:
                if not search_text.startswith("http"):
                    search_text = QtCore.QUrl("http://" + search_text)
                    self.webview.load(search_text)
                    # self.ui.lineEdit.setText(
                    #     "http://" + self.ui.lineEdit.text())
                    # print(self.webview.page().url())


if __name__ == "__main__":
    app = QtWidgets.QApplication(argv)
    myapp = Browser()
    myapp.show()
    exit(app.exec_())
