import os
import sys
import re

pathlist = []

def subtxtstr(retinfopath,str1,str2):
    f=open(retinfopath,'r')                           
    alllines=f.readlines()
    f.close()
    f=open(retinfopath,'w+')
    for eachline in alllines:
        c=re.sub(str1,str2,eachline)
        f.writelines(c)
    f.close()

def searchhash(root, target):
    global pathlist
    items = os.listdir(root)
    for item in items:
        path = os.path.join(root, item)
        if os.path.isdir(path):
            searchhash(path, target)
        elif item.find('_hash') != -1 and item.split('.')[-1] == target:
            pathlist.append(path)        

def main():

    global pathlist
    databasepath = sys.path[0] + "\\APT_Digital_Weapon-master"
    searchhash(databasepath,'md')
  
    for retinfopath in pathlist:
        line =0
        f=open(retinfopath,'r')                           
        alllines=f.readlines()
        f.close()
        f=open(retinfopath,'w+')
        for eachline in alllines:
            line = line + 1
            if(line>=3):
                f.write(eachline[1:])
        f.close()

        subtxtstr(retinfopath,'\|',' ')
        subtxtstr(retinfopath,'\[','')
        subtxtstr(retinfopath,'\]',';')

    writepath = sys.path[0] + "\\hash-APT_Digital_Weapon.txt"

    for retinfopath in pathlist:
        print retinfopath
        createdir = retinfopath.rsplit("\\",1)
        orgname = createdir[1].split('.')
        orgstring = "#" + orgname[0]

        f=open(retinfopath,'r')                           
        data=f.read()
        f.close
        
        with open(writepath,'a+') as file_handle:
            file_handle.write("\n")
            file_handle.write(orgstring)
            file_handle.write("\n")
            file_handle.write(data)
            file_handle.close

if __name__=="__main__":
    main()    
