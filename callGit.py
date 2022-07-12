import subprocess 

def callGit():
    subprocess.call("git --version")
    subprocess.call("git status")
    subprocess.call("git add .")
    subprocess.call("git commit -am \"You commit this branch.\"")
    subprocess.call("git push")

    # Print SHA
    subprocess.call("git rev-parse origin/master")  # To get the latest commit on the remote
    subprocess.call("git rev-parse HEAD")           # To get the latest commit on the local


def main():
    callGit()

if __name__ == "__main__":
    main()