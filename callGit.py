import subprocess 

def callGit():
    subprocess.call("git --version")
    subprocess.call("git status")
    subprocess.call("git add .")
    subprocess.call("git commit -am \"You commit this branch.\"")
    subprocess.call("git push")

    print("\n\n\n")
    # Print SHA
    print("Your remote SHA: ")
    remoteSHA = subprocess.call("git rev-parse origin")  # To get the latest commit on the remote
    print("Your local SHA: ")
    localSHA = subprocess.call("git rev-parse HEAD")           # To get the latest commit on the local

    # Check branch of 2 side
    if((remoteSHA) == (localSHA)):
        print("Remote and Loacal are same branch.")
    else:
        print("Remote and Loacal are different branch.")


def main():
    callGit()

if __name__ == "__main__":
    main()