from stat import S_ISREG, ST_CTIME, ST_MODE
import os, sys, time
dir_path = input('Enter File Name :')
if os.path.exists(dir_path)==True:
    data = (os.path.join(dir_path, fn) for fn in os.listdir(dir_path))
    data = ((os.stat(path), path) for path in data)
    data = ((stat[ST_CTIME], path)
               for stat, path in data if S_ISREG(stat[ST_MODE]))

    for cdate, path in sorted(data):
        print(os.path.basename(path) ,':',time.ctime(cdate))


    i=1
    path=dir_path
    name=input('Enter newfile name :')
    for filename in os.listdir(path):
        os.rename(os.path.join(path,filename),os.path.join(path,name+str(i)+'.jpg'))
        i=i+1
    print(os.listdir(dir_path))
else:
    print('File Not Found.Please Enter the correct path')
        