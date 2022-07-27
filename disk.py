# get disk ID
# 注意檔名不要取的跟指令名字一樣
# VSCode要記得用管理員權限打開並在poweeshell下去執行，不然會出一堆問題!

from multiprocessing.connection import Client
import subprocess
from subprocess import *
import os
import time
import sys
import re
from turtle import st

def get_disk_info(): 
    # 先開diskpart (加了stdout就不會自動整個印出來在terminal上面)
    p = Popen(["diskpart"], stdin=PIPE, stdout=PIPE)
    # 再下list disk去看disk ID
    p.stdin.write(bytes("list disk\n", 'utf-8'))
    
    stdout = str(p.communicate())
    
    # Write list disk information to txt for recording
    with open("temp.txt", "w") as wfile:
        wfile.write(stdout)
        
    # Get all disk ID     
    with open("temp2.txt", "r") as rfile:
        for i in rfile:
            str1 = re.findall(r"\\xba\\xcf\\xba\\xd0\s+(.*?) ", i)
            print("Disk: ", str1)

    disksize = []    
            
    # Get all disk size
    with open("temp2.txt", "r") as rfile2:
        for j in rfile2:
            str2 = re.findall(r"\\xb3s\\xbdu\s+(.*?) GB", j)
            disksize = str2
            print("Size: ", str2, " GB")
            # str2.sort()
            # print(str2)
            

    # Check which ID is power ID / device ID...
    ind = []
    for i in disksize:
        if int(i) > 500:
            #print("disk size: ", i)
            ind.append(i)
            #print(ind)
    print('-------------------------------')
    print("disk ID: ", disksize.index(ind[0]), "\ndisk size: ", ind[0])
    
    
def only_show_disk():
    p = Popen(["diskpart"], stdin=PIPE)
    p.stdin.write(bytes("list disk\n", 'utf-8'))
    
    
def get_full_disk():
    # 先開diskpart (加了stdout就不會自動整個印出來在terminal上面)
    p = Popen(["diskpart"], stdin=PIPE, stdout=PIPE)
    # 再下list disk去看disk ID
    p.stdin.write(bytes("list disk\n", 'utf-8'))
    
    stdout = str(p.communicate())
    
    # Write list disk information to txt for recording
    with open("temp.txt", "w") as wfile:
        wfile.write(stdout)
        
    # # Get all disk ID     
    # with open("temp.txt", "r") as rfile:
    #     for i in rfile:
    #         str1 = re.findall(r"Disk\s+(.*?) ", i)
    #         str1 = str1[1:]
    #         print("Disk: ", str1)

    # disksize = []    
            
    # Get all disk size
    with open("temp.txt", "r") as rfile2:
        content = rfile2.readline().split("\\r\\n")
        #print(content)

        for item in content:
            if "Disk" in item:

                if "Online" in item:
                    item = item.split(" ")
                    newItem = []
                    for element in item:
                        if element != "":
                            newItem.append(element)
                    #print(newItem)
                    if "KB" in newItem[4]:
                        #print("Disk: ", newItem[1], "Compacity: ", newItem[3])
                        if int(newItem[3]) < 2000:
                            print("PW ID", "Disk: ", newItem[1], "Compacity: ", newItem[3])
    
    
if __name__ == "__main__":
    get_disk_info()
    