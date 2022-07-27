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
        #stdout = str(stdout.split("\\n"))
        wfile.write(stdout)
        
    # Get all disk ID     
    with open("temp.txt", "r") as rfile:
        for i in rfile:
            str1 = re.findall(r"\\xba\\xcf\\xba\\xd0\s+(.*?) ", i)
            print("Disk: ", str1[1], "\n")
            
    # Get all disk size
    with open("temp.txt", "r") as rfile2:
        for j in rfile2:
            str2 = re.findall(r"\\xb3s\\xbdu\s+(.*?) GB", j)
            print("Size: ", str2[0], " GB\n")
            


if __name__ == "__main__":
    main()
    