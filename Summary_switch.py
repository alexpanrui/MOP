__author__ = 'panrui'
import sys, os
from math import atan,degrees,radians, floor, log10
cwd = sys.argv[1]
# print(cwd)
os.chdir(cwd)
i=0
if os.path.exists('summary_S_R.txt'):
    os.remove('summary_S_R.txt')
fo=open('summary_S_R.txt','w')
fo.write('Wafer\tSite\tDevice\tPad\tRon,p\tRon,n\tRoff,p\tRoff,n\tIcompp\tIcompn\tSwithced?\tVon\tVoff\n')
for filename in os.listdir(os.getcwd()):
    data1=[]
    if ".txt" in filename:
        if "switching" in filename:
            with open(filename) as f:
                data = f.read()

            fname = filename.split('__')
            fname1 = fname[0].split('_')
            fname2 = fname[1].split('_')
            fname3 = fname[2].split('_')
            mode = fname3[0]
            month = fname3[2]
            date = fname3[3]
            second = fname3[4]
            hour = fname3[5]
            temp_min = fname3[6]
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
            data_V = [float(item) for item in list_V]
            data_I = [float(item) for item in list_I]
            data_R = [float(item) for item in list_R]
            #########################find Ron and Roff#################################
            R_v_p = 0.5
            R_v_n = -0.5
            try:
                first = data_V.index(R_v_p)
            except:
                print("file ignored")
                print(filename)
                continue
            R1_p = data_R[first]
            R2_p = data_R[data_V[(first+1):].index(R_v_p)+first+1]
            Ron_p = min(R1_p,R2_p)
            Roff_p = max(R1_p,R2_p)

            first = data_V.index(R_v_n)
            R1_n = data_R[first]
            R2_n = data_R[data_V[(first+1):].index(R_v_n)+first+1]
            Ron_n = min(R1_n,R2_n)
            Roff_n = max(R1_n,R2_n)
            ##########################################################################
            #######################find Icomp for both quadrant#######################
            maxV_index_n = data_V.index(min(data_V))
            Icomp_n = data_I[maxV_index_n]
            maxV_index_p = data_V.index(max(data_V))
            Icomp_p = data_I[maxV_index_p]
            # print(filename)
            # print (min(data_V))
            # # print(maxV_index)
            # print(Icomp)
            Icomp_n = -round(abs(Icomp_n),-int(floor(log10(abs(Icomp_n)))))
            Icomp_p = round(abs(Icomp_p),-int(floor(log10(abs(Icomp_p)))))
            # print(filename)
            # print("Icomp_n:"+ str(Icomp_n))
            # print("Icomp_p:"+ str(Icomp_p))
            ##########################################################################
            ##########################determine switched##############################
            # print(Roff_n)
            # print(Ron_n)
            # print(Roff_p)
            # print(Ron_p)
            if (Roff_n-Ron_n)/10 > 10 and (Roff_p-Ron_p)/10 > 10:
                switched = "yes"
            else:
                switched = "no"
            ##########################################################################
            #########################determine Vswitch################################
            if switched == "yes":
                ######################Von###################################
                x1 = max(data_V)
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
                        # print (x2)
                        if slope < 0.0005:
                            Von = x2
                            break
                ##############################################################
                ###################Voff#######################################
                x1 = min(data_V)
                maxV_index = data_V.index(x1)
                y1 = data_I[maxV_index]
                mfactor = -int(floor(log10(abs(y1))))
                # print(mfactor)
                for index in reversed(range(len(data_V))):
                    y2 = data_I[index]
                    x2 = data_V[index]
                    if x2!=x1:
                        slope = (y2*pow(10,mfactor) - y1*pow(10,mfactor))/(x2 - x1)
                        # print (slope)
                        # print (x2)
                        if slope < 0.0005:
                            Voff = x2
                            break
                #############################################################
            else:
                Von = 0
                Voff = 0
            ##########################################################################
            print(filename)
            # print("Von:"+str(Von))
            # print("Voff:"+str(Voff))
            # print(switched)
            #break
            # fo.write('Wafer\tSite\tDevice\tPad\tRon,p\tRon,n\tRoff,p\tRoff,n\n')
            fo.write(wafer+'\t'+site+'\t'+dType+'\t'+pad+'\t'+str(Ron_p)+'\t'+str(Ron_n)+'\t'+str(Roff_p)+'\t'+str(Roff_n)+'\t'+str(Icomp_p)+'\t'+str(Icomp_n)+'\t'+switched+'\t'+str(Von)+'\t'+str(Voff)+'\n')
            # print('Ron_p:'+str(Ron_p))
            # print('Roff_p:'+str(Roff_p))
            # print('Ron_n:'+str(Ron_n))
            # print('Roff_n:'+str(Roff_n))