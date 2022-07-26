# get disk ID
# 注意檔名不要取的跟指令名字一樣

from multiprocessing.connection import Client
import subprocess
from subprocess import run
from subprocess import *
import os
import time

def main(): 
    # 先開diskpart
    p = Popen(["diskpart"], stdin=PIPE)
    print("sending data to STDIN")
    
    # 再下list disk去看disk ID
    res1 = str(p.stdin.write(bytes("list disk\n", 'utf-8')))
    time.sleep(.5)
    


if __name__ == "__main__":
    main()
    
    
    
    # VSCode要記得用管理員權限打開並在poweeshell下去執行，不然會出一堆問題!
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