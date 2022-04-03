from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
# from PyQt5 import QtWebEngineWidgets
from mainwindow import Ui_Browser, icons_rc
from sys import argv, exit
from re import match, findall


class Browser(QtWidgets.QMainWindow):
    def __init__(self):
        super(Browser, self).__init__()
        self.ui = Ui_Browser()
        self.ui.setupUi(self)

        self.webview = QWebEngineView()
        self.ui.gridLayout.addWidget(self.webview, 1, 0, 1, 7)

        self.ui.toolButton_back.clicked.connect(self.webview.back)
        self.ui.toolButton_home.clicked.connect(self.home)
        self.ui.toolButton_search.clicked.connect(self.search)
        self.ui.toolButton_refresh.clicked.connect(self.webview.reload)
        self.ui.toolButton_forward.clicked.connect(self.webview.forward)

        self.ui.toolButton_back.setToolTip("Назад")
        self.ui.toolButton_refresh.setToolTip("Обновить страницу")
        self.ui.toolButton_search.setToolTip("Поиск")
        self.ui.toolButton_home.setToolTip("Домой")

        self.ui.toolButton_forward.hide()
        self.ui.toolButton_back.hide()


        self.webview.urlChanged.connect(self.check)


        self.home()

    def check(self):
        self.ui.lineEdit.setText(f"{self.webview.url().toString()}")

        if self.webview.page().action(QWebEnginePage.Back).isEnabled():
            self.ui.toolButton_back.show()
        else:
            self.ui.toolButton_back.hide()

        if self.webview.page().action(QWebEnginePage.Forward).isEnabled():
            self.ui.toolButton_forward.show()
        else:
            self.ui.toolButton_forward.hide()

    def home(self):
        home_page = QtCore.QUrl("https://google.com")
        self.webview.load(home_page)

    def search(self):
        search_text = self.ui.lineEdit.text()
        print(match(
            '^((ftp|http|https):\/\/)?(www\.)?([A-Za-zА-Яа-я0-9]{1}[A-Za-zА-Яа-я0-9\-]*\.?)*\.{1}[A-Za-zА-Яа-я0-9-]{2,8}(\/([\w#!:.?+=&%@!\-\/])*)?', search_text))
        if search_text != "":
            if not match('^((ftp|http|https):\/\/)?(www\.)?([A-Za-zА-Яа-я0-9]{1}[A-Za-zА-Яа-я0-9\-]*\.?)*\.{1}[A-Za-zА-Яа-я0-9-]{2,8}(\/([\w#!:.?+=&%@!\-\/])*)?', search_text):
                search_text = QtCore.QUrl(
                    "https://google.com/search?q=" + search_text)
                try:
                    self.webview.load(search_text)
                except:
                    print("huy")
            else:
                if not search_text.startswith("http"):
                    search_text = QtCore.QUrl("http://" + search_text)
                    self.webview.load(search_text)
                else:
                    search_text = QtCore.QUrl(search_text)
                    self.webview.load(search_text)


if __name__ == "__main__":
    app = QtWidgets.QApplication(argv)
    myapp = Browser()
    myapp.show()
    exit(app.exec_())
    exit(app.exec_())
