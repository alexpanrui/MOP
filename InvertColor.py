__author__ = 'panrui'

import sys, os
from PyQt4.QtGui import QWidget, QPushButton, QApplication, QFileDialog,QMessageBox
from PIL import Image, ImageOps


class mainUI(QWidget):
    def __init__(self):
        super(mainUI, self).__init__()

        self.initUI()

    def initUI(self):
        self.btn = QPushButton('Browse',self)
        self.btn.move(60,20)
        self.btn.clicked.connect(self.showFolderDialog)

        self.setGeometry(300,300,200,50)
        self.setWindowTitle('Invert Color')
        self.show()

    def showFolderDialog(self):
        try:
            filelist = QFileDialog.getOpenFileNames(self, 'Select Directory') #select directory and save it
            # for filename in filelist:
            #     # filename = sys.argv[-1]
            #     image = Image.open(filename)
            #     filename_saved = filename + "_inverted" + ".png"
            #     if image.mode == 'RGBA':
            #         r,g,b,a = image.split()
            #         rgb_image = Image.merge('RGB', (r,g,b))
            #
            #         inverted_image = PIL.ImageOps.invert(rgb_image)
            #
            #         r2,g2,b2 = inverted_image.split()
            #
            #         final_transparent_image = Image.merge('RGBA', (r2,g2,b2,a))
            #
            #         final_transparent_image.save(filename_saved)
            #
            #     else:
            #         inverted_image = PIL.ImageOps.invert(image)
            #         inverted_image.save(filename_saved)

            QMessageBox.information(self,'Message','done')
        except:
            print(sys.exc_info()[0])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mainUI()
    sys.exit(app.exec_())