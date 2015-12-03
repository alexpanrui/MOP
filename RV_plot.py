#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from matplotlib import rcParams
import sys, os, glob, shutil
import math
rcParams.update({'figure.autolayout':True})
root = sys.argv[1]
cwd = os.path.join(root,sys.argv[2])
print(cwd)
os.chdir(cwd)
i = 0
isSwitching = 0
for filename in os.listdir(os.getcwd()):
	if ".txt" in filename:
		data1 = []
#fname = "IV_vs_T_14A1__R3C9PTS9_SNM1_Pad 4__switching_read_10_09_31_15_53.txt"

		with open(filename) as f:
			data = f.read()

		fname = filename.split('__')
		fname1 = fname[0].split('_')
		fname2 = fname[1].split('_')
		fname3 = fname[2].split('_')
		if "switching" in filename:
			mode = fname3[0]
			month = fname3[2]
			date = fname3[3]
			second = fname3[4]
			hour = fname3[5]
			temp_min = fname3[6]
			isSwitching = 1
		else:
			fname4 = fname[3].split('_')
			mode = fname3[0]
			month = fname4[1]
			date = fname4[2]
			second = fname4[3]
			hour = fname4[4]
			temp_min = fname4[5]
			isSwitching = 0

		wafer = fname1[3]
		site = fname2[0]
		dType = fname2[1]
		pad = fname2[2]
		temp_min = temp_min.split('.')
		minute = temp_min[0]
		fsname = "IV_vs_T_" + wafer + "__" + site + "_" + dType + "_" + pad + "__" + mode + "_" + month + "_" + date + "_" + hour + "_" + minute + "_" + second + "_R" + ".png"
		#print (fname)
		data = data.split('\n')
		for x in data:
		    if i >19:
		        data1.append(x)
		    i = i + 1
		data1.remove('')
		#data.clear(); #this is not compatible with python 2.7
		del data[:]
		i = 0

		x = [row.split("\t")[0] for row in data1]
		y = [row.split("\t")[2] for row in data1]

		fig = plt.figure()

		ax1 = fig.add_subplot(111)

		ax1.minorticks_on()

		ax1.set_title("Wafer " + wafer + ", Site " + site + ", " + dType + ", " + pad)    
		ax1.set_xlabel('V(V)')
		ax1.set_ylabel('R(ohms)')
		ax1.set_yscale('log')
		ax1.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.2e'))

		ax1.xaxis.set_minor_formatter(mtick.FormatStrFormatter('%.2f'))
		ax1.xaxis.set_minor_locator(mtick.AutoMinorLocator(2))
		#ax1.yaxis.set_minor_formatter(mtick.FormatStrFormatter('%.2e'))
		#ax1.yaxis.set_minor_locator(mtick.AutoMinorLocator(2))

		ax1.grid(b=True, which='major',color='b',linestyle='-')
		ax1.grid(b=True, which='minor',color='r',linestyle='--')

		ax1.plot(x,y, color='black', label='the data')

		step = math.floor(len(x)/10)
		arrow_index = 0
		if len(x) != 0 and step != 0:
                        while arrow_index < len(x):
                                try:
                                        arrow_index = int(arrow_index)
                                        ax1.annotate("", xy=(x[arrow_index],y[arrow_index]), xycoords='data', xytext=(x[arrow_index-1],y[arrow_index-1]), textcoords='data',arrowprops=dict(arrowstyle="->",connectionstyle= "arc3"))
                                        arrow_index = arrow_index + step
                                except:
                                        print(filename)
                                        print(sys.exc_info())

		#leg = ax1.legend()
		savepath = '..\plot'
		fsname = os.path.join(savepath,fsname)
		try:
                        fig.savefig(fsname)
                except:
                        print(filename)
                        print(sys.exc_info())
		plt.close()
		#plt.show()
