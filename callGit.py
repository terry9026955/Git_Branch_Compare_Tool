import subprocess 

def callGit():
    subprocess.call("git --version")
    subprocess.call("git status")
    subprocess.call("git add .")
    subprocess.call("git commit -am \"You commit this branch.\"")
    subprocess.call("git push")


def main():
    callGit()

if __name__ == "__main__":
    main()