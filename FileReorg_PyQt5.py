import sys, os, glob, shutil
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QInputDialog, QApplication,QAction, QFileDialog, QToolTip,QMessageBox)
#from PyQt4.QtGui import (QWidget, QPushButton, QLineEdit, QInputDialog, QApplication,QAction, QFileDialog, QToolTip,QMessageBox)
"""
class messageBox(QWidget):
    def __init__(self):
        supe().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(100,100,150,50)
        self.setWindowTitle('Message Box')
        self.show()
"""
class mainUI(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.btn = QPushButton('Browse',self)
        self.btn.move(20,20)
        self.btn.clicked.connect(self.showFolderDialog)
        
        self.btn1 = QPushButton('Run',self)
        self.btn1.setToolTip('By pressing this button, the files in the selected folder will be re-organized. Files for forming and switching will be grouped into separate folders')
        self.btn1.move(105,60)
        self.btn1.clicked.connect(self.orgnizeFiles)
        
        self.le = QLineEdit(self)
        self.le.move(130,22)
        
        self.setGeometry(300,300,290,100)
        self.setWindowTitle('Select Folder')
        self.show()

    def showFolderDialog(self):
        foldername = str(QFileDialog.getExistingDirectory(self, 'Select Directory')) #select directory and save it
        self.le.setText(str(foldername)) #display the directory in the text box
        os.chdir(foldername) #change the current working directory

    def orgnizeFiles(self):
        QMessageBox.information(self,'Message','Press Okay and wait until you receive the message "done"')
        try:
            os.stat('form')
        except:
            os.mkdir('form')
        try:
            os.stat('switching')
        except:
            os.mkdir('switching')
        for filename in os.listdir(os.getcwd()):
            if "_form" in filename:
                shutil.copy2(filename,'form')
            elif "_switching" in filename:
                shutil.copy2(filename,'switching')
        #for filename in glob.iglob('*_form*'):
        #    shutil.copy2(filename,'form')
        #for filename in glob.iglob('*_switching*'):
        #    shutil.copy2(filename,'switching')
        QMessageBox.information(self,'Message','done')
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mainUI()
    sys.exit(app.exec_())
        
        
