import subprocess 

def callGit():
    subprocess.call("git --version")
    subprocess.call("git status")
    subprocess.call("git add .")
    subprocess.call("git commit -am \"You commit this branch.\"")
    subprocess.call("git push")


    # print("\nYour remote SHA: ")
    # subprocess.call("git rev-parse origin")  # To get the latest commit on the remote
    # print("\nYour local SHA: ")
    # subprocess.call("git rev-parse HEAD") # To get the latest commit on the local

    print("\nCalling git and Push are done.")



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
        subprocess.call("git pull") # If diff, then pull from remote
    
    

def main():
    callGit()
    checkBranch()

if __name__ == "__main__":
    main()