__author__ = 'panrui'
import sys, os
from math import atan,degrees,radians, floor, log10
# cwd = os.path.join(sys.argv[1],sys.argv[2])
# print(cwd)
cwd = sys.argv[1]
os.chdir(cwd)
i=0
if os.path.exists('summary_f_R.txt'):
    os.remove('summary_f_R.txt')
fo=open('summary_f_R.txt','w')
fo.write('Wafer\tSite\tDevice\tPad\tRvirgin\tRform\tIcompf\tformed?\tVform\n')
formed = "no"
for filename in os.listdir(os.getcwd()):
    data1=[]
    if ".txt" in filename:
        if "_form" in filename:
            print(filename)
            with open(filename) as f:
                data = f.read()

            fname = filename.split('__')
            fname1 = fname[0].split('_')
            fname2 = fname[1].split('_')
            fname3 = fname[2].split('_')
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
            data = data.split('\n')

            for x in data:
                if i >19:
                    data1.append(x)
                i = i + 1
            data1.remove('')
            #data.clear(); #this is not compatible with python 2.7
            del data[:]
            i = 0

            list_V = [row.split("\t")[0] for row in data1]
            list_I = [row.split("\t")[1] for row in data1]
            list_R = [row.split("\t")[2] for row in data1]
            data_V = [float(i) for i in list_V]
            data_I = [float(i) for i in list_I]
            data_R = [float(i) for i in list_R]
            #################find Rvirgin and Rform####################
            R_v = -0.5
            first = data_V.index(R_v)
            Rvirgin = data_R[first]
            Rform = data_R[data_V[(first+1):].index(R_v)+first+1]
            ##########################################################
            ###############find Icomp#################################
            maxV_index = data_V.index(min(data_V))
            Icomp = data_I[maxV_index]
            # print(filename)
            # print (min(data_V))
            # # print(maxV_index)
            # print(Icomp)
            if Icomp < 0:
                Icomp = -round(abs(Icomp),-int(floor(log10(abs(Icomp)))))
            else:
                Icomp = round(abs(Icomp),-int(floor(log10(abs(Icomp)))))
            ###########################################################
            ###################determine formed########################
            R_v = -1
            first = data_V.index(R_v)
            Rhigh = data_R[first]
            Rlow = data_R[data_V[(first+1):].index(R_v)+first+1]
            if Rhigh/Rlow > 10:
                formed = "yes"
            else:
                formed = "no"
            ###########################################################
            ###################determine Vform#########################
            if formed == "yes":
                x1 = min(data_V)
                maxV_index = data_V.index(x1)
                y1 = data_I[maxV_index]
                mfactor = -int(floor(log10(abs(y1))))
                # print(mfactor)
                for index in range(len(data_V)):
                    y2 = data_I[index]
                    x2 = data_V[index]
                    if x2!=x1:
                        slope = (y2*pow(10,mfactor) - y1*pow(10,mfactor))/(x2 - x1)
                        # print (slope)
                        if slope < 0.0005:
                            Vform = x2
                            break
            else:
                Vform = 0
            ###########################################################
            fo.write(wafer+'\t'+site+'\t'+dType+'\t'+pad+'\t'+str(Rvirgin)+'\t'+str(Rform)+'\t'+str(Icomp)+'\t'+ formed +'\t'+ str(Vform) +'\n')
            formed = "no"

            # print(Rvirgin)
            # print(Rform)