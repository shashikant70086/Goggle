import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebKit import *
from PyQt5.QtWebKitWidgets import *
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

  


app = QApplication(sys.argv)

web = QWebView()
web.setWindowIcon(QIcon("new-google-favicon-512.ico")) 
web.setWindowTitle("Google")
web.load(QUrl("https://google.com"))
def load_error(webview, event, url, error):
  webview.load_uri('http://google.com') # not working

browser.connect('load-error', load_error)
web.show()


sys.exit(app.exec_())
