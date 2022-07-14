import os
import subprocess


def main():
    gotoPath()
    showFile()

def showFile():
    # subprocess.call('dir', shell=True, cwd = 'D:/Tinghao.Chen/Desktop/SMIGIT') 
    subprocess.call('dir', shell=True) 
    print("--------------------------")


def gotoPath():
    os.chdir('D:/Tinghao.Chen/Desktop/SMIGIT')
    cwd = os.getcwd() 
    print("Current working directory is:", cwd)

if __name__ == "__main__":
    main()