# coding=UTF-8
# Python version: 3.8.1
import os
import sys

str="@startmindmap\n* begin\n"
strend="@endmindmap"
symbol="*"

def get_file_path(root_path,symbol_level):
    global str
    #获取该目录下所有文件名称和目录名称
    dir_or_files = os.listdir(root_path)
    symbol=symbol_level+"*"
    for dir_file in dir_or_files:
        #获取目录或者文件的路径
        dir_file_path=os.path.join(root_path,dir_file)
        str+=symbol+" "+os.path.join(dir_file)+"\n"
        if os.path.isdir(dir_file_path):
            #递归获取所有文件和目录的路径
            get_file_path(dir_file_path,symbol)
        

if __name__ == "__main__":
    flag = True
    while(flag):
        rootpath =input("Please input the directory(finish: end):")
        if os.path.exists(rootpath):
            print("Input Correctly,the directory is reading,please wait")
            get_file_path(rootpath,"*")
            fileW=open("AutoRead.puml","w")  
            fileW.write(str + strend)
            print("Task is finished.")
            fileW.close()
        else:
            if rootpath=="end":
                flag =False
            else:
                print("Input Error,Reinput")
        

    



