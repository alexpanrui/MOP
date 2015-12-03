
"""
Created on Wed Nov  4 14:00:26 2015

@author: sudhakmo
"""
import csv
import os
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams.update({'figure.autolayout':True})
"""
Please provide the path for the file below.
"""

#os.chdir(path='C:/Users/sudhakmo.AUTH/Documents/KRONOS/REF_FILE')

"""
Enter the name of the file replacing 'test.csv'
"""

with open('test.csv', 'r') as f:
    reader = csv.reader(f)
    c = csv.writer(open("bin.csv", "w", newline=''))
    c.writerow(['Time','D11','D10','D09','D08','D07','D06','D05','D04','D03','D02','D01','D00'])
    for row in reader:
        hex_data=row[1]
        time_data=row[0]
        binary_data = bin(int(hex_data, 16))[2:].zfill(12)
        bin_chunks = [binary_data[i:(i+1)] for i in range(len(binary_data)//1)]
        bin_chunks.insert(0,time_data)
        c.writerow(bin_chunks)
with open('bin.csv', 'r') as bin_data:
    reader_file = csv.reader(bin_data)
    time =[]
    d=[[],[],[],[],[],[],[],[],[],[],[],[]]
    next(reader_file)
    for row in reader_file:
        time.append(row[0])
        for x in range(0,12):
            d[x].append(row[12-x])
    fig = plt.figure(figsize= (20,20))
    ax11 = fig.add_subplot(12,1,12)
    ax11.set_xlabel('TIME')
    ax11.set_ylabel('D11')
    ax11.set_ylim([-0.1,1.1])
    ax11.plot(time,d[11], c='r')
    ax10 = fig.add_subplot(12,1,11, sharex=ax11)
    ax10.set_ylabel('D10')
    ax10.set_ylim([-0.1,1.1])
    ax10.plot(time,d[10], c='r')
    plt.setp(ax10.get_xticklabels(), visible=False)
    #a09
    ax09 = fig.add_subplot(12,1,10, sharex=ax11)
    ax09.set_ylabel('D9')
    ax09.set_ylim([-0.1,1.1])
    ax09.plot(time,d[9], c='r')
    plt.setp(ax09.get_xticklabels(), visible=False)
    #a08
    ax08 = fig.add_subplot(12,1,9, sharex=ax11)
    ax08.set_ylabel('D8')
    ax08.set_ylim([-0.1,1.1])
    ax08.plot(time,d[8], c='r')
    plt.setp(ax08.get_xticklabels(), visible=False)
    #a07
    ax07 = fig.add_subplot(12,1,8, sharex=ax11)
    ax07.set_ylabel('D7')
    ax07.set_ylim([-0.1,1.1])
    ax07.plot(time,d[7], c='r')
    plt.setp(ax07.get_xticklabels(), visible=False)
    #a06
    ax06 = fig.add_subplot(12,1,7, sharex=ax11)
    ax06.set_ylabel('D6')
    ax06.set_ylim([-0.1,1.1])
    ax06.plot(time,d[6], c='r')
    plt.setp(ax06.get_xticklabels(), visible=False)
    #a05
    ax05 = fig.add_subplot(12,1,6, sharex=ax11)
    ax05.set_ylabel('D5')
    ax05.set_ylim([-0.1,1.1])
    ax05.plot(time,d[5], c='r')
    plt.setp(ax05.get_xticklabels(), visible=False)
    #a04
    ax04 = fig.add_subplot(12,1,5, sharex=ax11)
    ax04.set_ylabel('D4')
    ax04.set_ylim([-0.1,1.1])
    ax04.plot(time,d[4], c='r')
    plt.setp(ax04.get_xticklabels(), visible=False)
    #a03
    ax03 = fig.add_subplot(12,1,4, sharex=ax11)
    ax03.set_ylabel('D3')
    ax03.set_ylim([-0.1,1.1])
    ax03.plot(time,d[3], c='r')
    plt.setp(ax03.get_xticklabels(), visible=False)
    #a02
    ax02 = fig.add_subplot(12,1,3, sharex=ax11)
    ax02.set_ylabel('D2')
    ax02.set_ylim([-0.1,1.1])
    ax02.plot(time,d[2], c='r')
    plt.setp(ax02.get_xticklabels(), visible=False)
    #a01
    ax01 = fig.add_subplot(12,1,2, sharex=ax11)
    ax01.set_ylabel('D1')
    ax01.set_ylim([-0.1,1.1])
    ax01.plot(time,d[1], c='r')
    plt.setp(ax01.get_xticklabels(), visible=False)
    #a00
    ax00 = fig.add_subplot(12,1,1, sharex=ax11)
    ax00.set_ylabel('D0')
    ax00.set_ylim([-0.1,1.1])
    ax00.plot(time,d[0], c='r')
    plt.setp(ax00.get_xticklabels(), visible=False)
    mng = plt.get_current_fig_manager()
    mng.window.showMaximized()
    plt.show()


