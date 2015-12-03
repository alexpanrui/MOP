import os,sys
from glob import glob
root = sys.argv[1]
cwd = os.path.join(root,"plot")
os.chdir(cwd)
print(os.getcwd())
for filename in os.listdir(os.getcwd()):
#for filename in os.listdir(cwd):
	 if ".png" in filename:
		os.remove(filename)