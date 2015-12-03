__author__ = 'panrui'
import sys, os, glob, shutil
#from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QInputDialog, QApplication,QAction, QFileDialog, QToolTip,QMessageBox)
from PyQt4.QtGui import (QWidget, QPushButton, QLineEdit, QInputDialog, QApplication,QAction, QFileDialog, QToolTip,QMessageBox,QLabel)
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
global_filelist = []
plot_index = 0
time_stamp = "0"
mode = "undefined"
class mainUI(QWidget):

    def __init__(self):
        super(mainUI, self).__init__()

        self.initUI()

    def initUI(self):
        self.btn = QPushButton('Browse',self)
        self.btn.move(20,20)
        self.btn.clicked.connect(self.showFolderDialog)

        self.btn1 = QPushButton('Load',self)
        #self.btn1.setToolTip('By pressing this button, the files in the selected folder will be re-organized. Files for forming and switching will be grouped into separate folders')
        self.btn1.move(260,20)
        self.btn1.clicked.connect(self.start)

        self.btn_prev = QPushButton('Previous',self)
        self.btn_prev.move(20,120)
        self.btn_prev.clicked.connect(self.prevPlot)

        self.btn_next = QPushButton('Next',self)
        self.btn_next.move(100,120)
        self.btn_next.clicked.connect(self.nextPlot)

        self.btn_mark = QPushButton('Mark',self)
        self.btn_mark.move(180,120)
        self.btn_mark.clicked.connect(self.mark)

        self.btn_unmark = QPushButton('Unmark',self)
        self.btn_unmark.move(260,120)
        self.btn_unmark.clicked.connect(self.unmark)

        self.le = QLineEdit(self)
        self.le.move(100,22)
        self.le.resize(150,20)

        self.label_wafer = QLabel('Wafer',self)
        self.label_wafer.move(20,60)

        self.l_wafer = QLineEdit(self)
        self.l_wafer.move(55,60)
        self.l_wafer.resize(40,20)

        self.label_pad = QLabel('Pad',self)
        self.label_pad.move(20,90)

        self.l_pad = QLineEdit(self)
        self.l_pad.move(55,90)
        self.l_pad.resize(40,20)

        self.label_site = QLabel('Site',self)
        self.label_site.move(120,60)

        self.l_site = QLineEdit(self)
        self.l_site.move(150,60)
        self.l_site.resize(70,20)

        self.label_mode = QLabel('mode',self)
        self.label_mode.move(120,90)

        self.l_mode = QLineEdit(self)
        self.l_mode.move(150,90)
        self.l_mode.resize(70,20)

        self.label_dtype = QLabel('Device Type',self)
        self.label_dtype.move(240,60)

        self.l_dtype = QLineEdit(self)
        self.l_dtype.move(305,60)
        self.l_dtype.resize(40,20)

        self.label_marked = QLabel('Marked',self)
        self.label_marked.move(240,90)

        self.l_marked = QLineEdit(self)
        self.l_marked.move(305,90)
        self.l_marked.resize(40,20)

        self.l_curr = QLineEdit(self)
        self.l_curr.move(20,160)
        self.l_curr.resize(30,20)

        self.label_of = QLabel('of',self)
        self.label_of.move(55,160)

        self.l_total = QLineEdit(self)
        self.l_total.move(70,160)
        self.l_total.resize(30,20)

        self.setGeometry(300,300,350,190)
        self.setWindowTitle('Txt filter')
        self.show()

    def showFolderDialog(self):
        global global_filelist
        global plot_index
        try:
            foldername = str(QFileDialog.getExistingDirectory(self, 'Select Directory')) #select directory and save it
            self.le.setText(str(foldername)) #display the directory in the text box
            os.chdir(foldername) #change the current working directory
            global_filelist=[]
            plot_index = 0
        except:
            print(sys.exc_info()[0])

    def start(self):
        global global_filelist
        global_filelist = []
        for filename in os.listdir(os.getcwd()):
            if ".png" in filename:
                global_filelist.append(filename)

        if global_filelist == []:
            QMessageBox.information(self,'Message','No plots found!')
            return
        self.l_total.setText(str(len(global_filelist)))
        self.l_curr.setText("1")
        plt.ion()
        img = mpimg.imread(global_filelist[0])
        plt.imshow(img)
        plt.show()
        self.extract_info(global_filelist[plot_index])

    def nextPlot(self):
        global global_filelist
        global plot_index
        if global_filelist == []:
            QMessageBox.information(self,'Message','No plots found!')
            return
        plt.close()
        plot_index = plot_index + 1
        if plot_index >= len(global_filelist):
            QMessageBox.information(self,'Message','You have reached the last plots')
            plot_index = len(global_filelist)-1
            img = mpimg.imread(global_filelist[plot_index])
            plt.imshow(img)
            plt.show()
        else:
            img = mpimg.imread(global_filelist[plot_index])
            plt.imshow(img)
            plt.show()
        self.l_curr.setText(str(plot_index+1))
        self.extract_info(global_filelist[plot_index])

    def prevPlot(self):
        global global_filelist
        global plot_index
        if global_filelist == []:
            QMessageBox.information(self,'Message','No plots found!')
            return
        plt.close()
        plot_index = plot_index - 1
        if plot_index < 0:
            QMessageBox.information(self,'Message','You have reached the first plots')
            plot_index = 0
            img = mpimg.imread(global_filelist[plot_index])
            plt.imshow(img)
            plt.show()
        else:
            img = mpimg.imread(global_filelist[plot_index])
            plt.imshow(img)
            plt.show()
        self.l_curr.setText(str(plot_index+1))
        self.extract_info(global_filelist[plot_index])

    def extract_info(self,fname):
        # print(fname)
        global time_stamp
        global mode
        if os.path.exists('..\\filtered\\' + global_filelist[plot_index]):
            self.l_marked.setText('Yes')
        else:
            self.l_marked.setText('No')
        temp = fname.split('__')
        temp1 = temp[0].split('_')
        temp2 = temp[1].split('_')
        temp3 = temp[2].split('_')
        if "switching" in fname:
            mode = "switching"
        elif "form" in fname:
            mode = "form"
        else:
            mode = "undefined"

        month = temp3[1]
        date = temp3[2]
        temp_second = temp3[5]
        hour = temp3[3]
        min = temp3[4]
        wafer = temp1[3]
        site = temp2[0]
        dType = temp2[1]
        temp_pad = temp2[2]
        pad = temp_pad.replace("Pad","")
        #pad = temp_pad[1]
        temp_second = temp_second.split('.')
        second = temp_second[0]
        time_stamp = month + "_" + date + "_" + second + "_" + hour + "_" + min
        # print(time_stamp)
        self.l_wafer.setText(wafer)
        self.l_site.setText(site)
        self.l_dtype.setText(dType)
        self.l_pad.setText(pad)
        self.l_mode.setText(mode)

    def mark(self):
        global time_stamp
        global mode
        os.chdir('..')
        # print(os.getcwd())
        try:
            os.stat('filtered')
        except:
            os.mkdir('filtered')
        os.chdir('plot')
        if global_filelist == []:
            QMessageBox.information(self,'Message','No plots found!')
            return
        #QMessageBox.information(self,'Message','Press Okay and wait until you receive the message "done"')
        if self.l_marked.text() == 'Yes':
            QMessageBox.information(self,'Message','Marked')
            return
        else:
            temp = global_filelist[plot_index].split('.')
            shutil.copy2(global_filelist[plot_index],'..\\filtered')

            if "_R." in global_filelist[plot_index]:
                shutil.copy2(global_filelist[plot_index].replace("_R.","."),'..\\filtered')
            else:
                shutil.copy2(temp[0] + '_R' + '.png','..\\filtered')
            self.l_marked.setText('Yes')

        os.chdir('..')
        os.chdir(mode)
        # print(os.getcwd())
        for filename in os.listdir(os.getcwd()):
            if time_stamp in filename:
                shutil.copy2(filename,'..\\filtered')
                break

        os.chdir('..')

        os.chdir('plot')
        print(os.getcwd())
        print("this is marked")

    def unmark(self):
        global time_stamp
        global mode
        os.chdir('..\\filtered')
        if global_filelist == []:
            QMessageBox.information(self,'Message','No plots found!')
            return
        #QMessageBox.information(self,'Message','Press Okay and wait until you receive the message "done"')
        if self.l_marked.text() == 'No':
            QMessageBox.information(self,'Message','Unmarked')
            # return
        else:
            # os.chdir('..\\filtered')
            print(os.getcwd())
            temp = global_filelist[plot_index].split('.')
            if os.path.exists(global_filelist[plot_index]):
                os.remove(global_filelist[plot_index])

            if "_R." in global_filelist[plot_index]:
                if os.path.exists(global_filelist[plot_index].replace("_R.",".")):
                    os.remove(global_filelist[plot_index].replace("_R.","."))
            else:
                if os.path.exists(temp[0] + '_R' + '.png'):
                    os.remove(temp[0] + '_R' + '.png')
            self.l_marked.setText('No')

        for filename in os.listdir(os.getcwd()):
            if time_stamp in filename:
                os.remove(filename)
                break
        os.chdir('..\\plot')

        print(os.getcwd())
        print("this is unmarked")

    def closeEvent(self, QCloseEvent):
        plt.ioff()
        plt.close()
        QApplication.quit()
        sys.exit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mainUI()
    # sys.exit(app.exec_())
    app.exec_()