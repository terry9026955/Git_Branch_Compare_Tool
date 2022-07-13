from asyncore import read
import subprocess
import os

# 執行CMD指令的部分我先跳過...
def cmd():
    print("----------------")
    f = os.popen(r"ls", "r")
    l = f.read()
    print(l)
    f.close()

def main():
    cmd()

if __name__ == "__main__":
    main()