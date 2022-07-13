import subprocess 
import time

real_time = time.strftime("%Y%m%d_%H%M%S", time.localtime())


# Call git server and do branch checking
def callGit():
    checkBranch()
    #gitPull()
    print("\nCalling git and Pushing are done.")


# Get remote and local SHA and then comparing 
def checkBranch():
    print("\nChecking branch...\n")

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
    with open("SHA.log","a") as file:
        file.write(real_time + ": \n")
        file.write("remote SHA: " + remoteSHA + "\n")
        file.write("local SHA: " + localSHA + "\n\n")


def gitPull():
    subprocess.call("git fetch -p")
    subprocess.call("git pull") 


def gitPush():
    subprocess.call("git add .")
    subprocess.call("git commit -am \"You commit this.\"")
    subprocess.call("git push")


def gitCheck():
    subprocess.call("git --version")
    subprocess.call("git status")


def main():
    callGit()
    

if __name__ == "__main__":
    main()