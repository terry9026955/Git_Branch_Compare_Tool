import subprocess 

def callGit():
    subprocess.call("git --version")
    subprocess.call("git status")
    subprocess.call("git add .")
    subprocess.call("git commit -am \"You commit this branch.\"")
    subprocess.call("git push")


    print("\nYour remote SHA: ")
    subprocess.call("git rev-parse origin")  # To get the latest commit on the remote
    print("\nYour local SHA: ")
    subprocess.call("git rev-parse HEAD") # To get the latest commit on the local

    

    # 目前要想辦法讀取出subprocess.call()秀出來的內容，不然他現在只會返回0/1
    # print("\nChecking branch...\n")
    # Check branch of 2 side
    # if((remoteSHA) == (localSHA)):
    #     print("Remote and Loacal are same branch.")
    # else:
    #     print("Remote and Loacal are different branch.")

    

def main():
    callGit()

if __name__ == "__main__":
    main()