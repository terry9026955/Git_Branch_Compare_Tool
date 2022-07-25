from cmath import log
import subprocess
import sys
import os

wrapper_path = os.path.dirname(sys.executable)

def gitLog():
        logInfo = str(subprocess.check_output("git log -p -1"))
        logInfo = logInfo.split("\\n")
        #print(logInfo)
        
        print("wrapper_path: ", wrapper_path)
        cwd = os.getcwd()
        print("cur path: ", cwd)
        
        # 寫入txt紀錄
        #with open("log.txt", "w") as file:
        with open(cwd + "\log.txt", "w") as file:
            #file.write(logInfo)
            for line in logInfo:
                file.write(line)
                file.write("\n")
                
        # 抓出關鍵字
        with open(cwd + "\log.txt", "r") as read:
            for line in logInfo:
                if 'Author' in line:    # 抓最新的那一筆
                    print("Author info: ", line)
                    break
                    

    
def main():

    
    name = gitLog() # return name of the latest commit branch
    print("Author: " + str(name))
    

if __name__ == "__main__":
    main()