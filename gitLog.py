import subprocess

def gitLog():
        logInfo = str(subprocess.check_output("git log"))
        logInfo = logInfo.split("\\n")
        
        
        # 寫入txt紀錄
        with open("log.txt", "w") as file:
            #file.write(logInfo)
            for line in logInfo:
                file.write(line)
                file.write("\n")
                
        # 抓出關鍵字
        with open("log.txt", "r") as read:
            
            for line in logInfo:
                if 'Author' in line:
                    name = line.split(" ")  # 切成List
                    fullname = str(name[1])
                    if "<" not in name[2]:
                        fullname = name[1] + name[2]
                    return fullname
                
       
                    
            
    
def main():
    name = gitLog() # return name of the latest commit branch
    print("Author: " + str(name))
    

if __name__ == "__main__":
    main()