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

def main(): 
    # 先開diskpart (加了stdout就不會自動整個印出來在terminal上面)
    p = Popen(["diskpart"], stdin=PIPE, stdout=PIPE)
    # 再下list disk去看disk ID
    p.stdin.write(bytes("list disk\n", 'utf-8'))
    
    
    stdout = str(p.communicate())
    #print(stdout)
    
    # Check Chi or Eng

    
    with open("temp.txt", "w") as wfile:
        stdout.split("\\n")
        wfile.write(stdout)
        
    with open("temp.txt", "r") as rfile:
        for i in rfile:
            str1 = re.findall(r"\\xba\\xcf\\xba\\xd0 (.*?) ", i)
            
            #str1 = i.split("\\r\\n")
            #str1 = re.split("\\r\\n", i)
            
            
            # if str1 is not None:
            #     lines = str1.group(1).split("\n")
            #     for l in lines:
            #         print(l)
            # else:
            #     print("no output")
            
            print("Disk: ", str1[1])
            


    # with open("temp.txt", "wt") as file:
    #     file.write("command\ncommand\ncommand")
    # p = Popen(["diskpart", "/?", bytes("list disk".encode("GBK")), "temp.txt"], stdin=PIPE, )
    #os.remove("temp.txt")
    

    

if __name__ == "__main__":
    main()
    
    
    
    # 測試一:
    #os.system('cmd /k "diskpart"')  
    # try:
    #     os.system('cmd /k "diskpart"')
    #     os.system('cmd /k "list disk"')


    # except:
    #     print('could not execute command')
    
    # 測試二:
    # command = "diskpart"
    # run(command, shell=True)