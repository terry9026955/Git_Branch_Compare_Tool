from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

settings = QSettings("config.ini", QSettings.IniFormat)

gitPath = settings.value("Git_path/path")
print(gitPath)