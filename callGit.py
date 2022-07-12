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
    subprocess.call("git rev-parse origin/master")  # To get the latest commit on the remote
    print("Your local SHA: ")
    subprocess.call("git rev-parse HEAD")           # To get the latest commit on the local


def main():
    callGit()

if __name__ == "__main__":
    main()