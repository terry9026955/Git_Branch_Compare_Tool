import os
import subprocess
import time

real_time = time.strftime("%Y%m%d_%H%M%S", time.localtime())


def main():
    # Go to directory (git repository)
    gotoPath()
    showFile()

    # Get SHA
    checkBranch()


def checkBranch():
    print("\nChecking branch...\n")

    # Get the latest SHA of github
    remoteSHA = str(subprocess.check_output("git rev-parse origin"))
    remoteSHA = remoteSHA.replace("b'", "")
    remoteSHA = remoteSHA[:8]   # Get former 8 SHA codes
    
    localSHA = str(subprocess.check_output("git rev-parse HEAD"))
    localSHA = localSHA.replace("b'", "")
    localSHA = localSHA[:8]

    print("remote SHA: ", remoteSHA)
    print("local SHA: ", localSHA)

    if((remoteSHA) == (localSHA)):  # Check SHA of 2 side
        print("【Remote】 and 【Loacal】 are \'same\' branch.")
    else:
        print("【Remote】 and 【Loacal】 are \'different\' branch.")
        gitPull()
    
    writeSHA(remoteSHA, localSHA)


# Write SHA info into SHA.log
def writeSHA(remoteSHA, localSHA):
    with open("./SHA_log/"+ real_time +"_SHA._log.log", "w") as file:
        file.write(real_time + ": \n")
        file.write("remote SHA: " + remoteSHA + "\n")
        file.write("local SHA:  " + localSHA + "\n\n")


def gitPull():
    subprocess.call("git fetch -p")
    subprocess.call("git pull") 


def gitPush():
    subprocess.call("git add .")
    subprocess.call("git commit -am \"File modified.\"")
    subprocess.call("git push")


def gitCheck():
    subprocess.call("git --version")
    subprocess.call("git status")


def showFile():
    subprocess.call('dir', shell=True, cwd = 'D:/Tinghao.Chen/Desktop/SMIGIT') 
    subprocess.call('dir', shell=True) 


def gotoPath():
    os.chdir('D:/Tinghao.Chen/Desktop/Git_Command_Test')
    # os.chdir('D:/Tinghao.Chen/Desktop/SMIGIT')
    cwd = os.getcwd() 
    print("Current working directory is:", cwd)



if __name__ == "__main__":
    main()