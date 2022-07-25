# get disk ID
# 注意檔名不要取的跟指令名字一樣

from multiprocessing.connection import Client
import subprocess
from subprocess import run
from subprocess import Popen, PIPE
import os
import time

def main(): 
    p = Popen(["diskpart"], stdin=PIPE)
    print("sending data to STDIN")
    
    res1 = p.stdin.write(bytes("list disk\n", 'utf-8'))
    time.sleep(.5)

if __name__ == "__main__":
    main()
    
    
    
    
    #os.system('cmd /k "diskpart"')  
    # try:
    #     os.system('cmd /k "diskpart"')
    #     os.system('cmd /k "list disk"')


    # except:
    #     print('could not execute command')
    
    # command = "diskpart"
    # run(command, shell=True)