from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

tigger = config['Runonce_trigger']['tigger']
path = config['Folder']['path']
path = path.replace("/", "\\")
started_tigger = False
fList = []
print("RunOnce Trigger == 1")
started = config['Runonce_trigger']['started']
filelist = config['%General']
for key in filelist:
    f = config['%General'][key]
    fList.append(f)
print(fList)