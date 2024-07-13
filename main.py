import sys
import os
import time
try:
     import pyi_splash as ps
except:
     pass
from PyQt6.QtGui import QGuiApplication, QPalette, QColor
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtQuick import QQuickWindow
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QFileDialog, QLabel, QWidget, QGridLayout, QCheckBox
from PyQt6.QtCore import pyqtSlot, QSize, Qt
from File_uploader import *
from pathlib import Path


#import file
#from file import Ui_MainWindow
# Initialize variables
lf = File_uploader()
filename = ""
file_text = "File to upload"

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setStyleSheet("QLabel#failed{\n"
        "background-color : white;\n"
        "color: red\n"
        "}")
        self.setWindowTitle("RAG File Uploader")
        self.layout = QGridLayout()
        self.widget = QWidget()
        self.widget.setObjectName("Widget")
        self.widget.setLayout(self.layout)
        self.setFixedSize(600, 300)
        self.label = QLabel(file_text)
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.uploadButton = QPushButton(parent=self.widget)
        self.uploadButton.setText("Upload file")
        self.uploadButton.setEnabled(False)

        self.selectButton = QPushButton(self)
        self.selectButton.setText("Select file")

        self.closeButton = QPushButton(self)
        self.closeButton.setText("Close")      
        self.closeButton.setFixedWidth(50)

        self.uploadedBox = QCheckBox()
        self.uploadedBox.setEnabled(False)
        self.uploadedBox.setChecked(False)
        self.uploadedBox.setText("Uploaded")

        self.processedBox = QCheckBox()
        self.processedBox.setEnabled(False)
        self.processedBox.setChecked(False)
        self.processedBox.setText("Processed")

        self.labelFailed = QLabel()
        self.labelFailed.setObjectName("failed")
        self.labelFailed.setWordWrap(True)
        self.labelFailed.setText("Warning: Uploading files takes a significant amount of time. Be patient")        

        self.setCentralWidget(self.widget)
        self.layout.addWidget(self.selectButton,0,0)
        self.layout.addWidget(self.label,0,1)
        self.layout.addWidget(self.uploadButton,1,0)
        self.layout.addWidget(self.closeButton,2,3)
        self.layout.addWidget(self.labelFailed,2,0)
        self.layout.addWidget(self.uploadedBox,1,1)
        self.layout.addWidget(self.processedBox,1,2)
        #selectButton.setFixedWidth(60)
        #selectButton.setFixedHeight(50)

        self.selectButton.clicked.connect(self.getFile)
        self.uploadButton.clicked.connect(self.upload)
        self.closeButton.clicked.connect(self.close)
        #self.uploadButton.setEnabled(self.changed)
        
        
        #self.ui = Ui_MainWindow()
        #self.ui.setupUi(self)
    
    def splash():
         ps.update_text("Loading")



    def changed(self):
         self.uploadButton.changed = self.uploadButton.setText(file_text)

    def getFile(self):
            fname = QFileDialog.getOpenFileName()
            file_text = fname[0]
            self.label.setText(file_text)
            self.uploadButton.setEnabled(True)

    def upload(self):
         text = self.label.text()
         print(text)
         code = lf.load_file(text)
         if code == 200:
              self.uploadedBox.setChecked(True)
              time.sleep(5)
              self.process()
         else:
              self.labelFailed.setText("File Upload Failed. Contact SysAdmin")
              print(code)
              return
          

    def process(self):
         print("Scanning")
         code = lf.scanner()
         if code == 200:
              self.processedBox.setChecked(True) 
              return
         else:
              self.labelFailed.setText("File Processing Failed. Contact SysAdmin")
              print(code)
              return
          
class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        #palette.setColor(QPalette.ColorRole.Window, QColor(color))
        palette.setColor(QPalette.ColorRole.Text, QColor(color))
        self.setPalette(palette)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    try:
         splash()
    except:
         pass
    main_gui = Main()

    try:
         ps.update_text("")
         ps.close
    except:
         pass
    

    main_gui.show()
#    engine = QQmlApplicationEngine()
#   engine.quit.connect(app.quit)
#    engine.load('./main.qml')
    sys.exit(app.exec())

