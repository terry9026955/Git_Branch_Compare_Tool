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
                    
                    
                    # name = line.split(" ")  # 切成List
                    # fullname = str(name[1])
                    # if "<" not in name[2]:
                    #     fullname = name[1] + name[2]
                    # return fullname
        
        return True
        
        
        
        
             
# if getattr(sys, 'frozen', False):   #確認是打包好的exe檔案還是本地的script檔案
#     wrapper_path = os.path.dirname(sys.executable) #抓路徑位址
# elif __file__:
#     wrapper_path = os.path.dirname(__file__)
# print("Wrapper Path is: ", wrapper_path)
             
                
# def gitLog(self):
#         logInfo = str(subprocess.check_output("git log -p -1"))
#         logInfo = logInfo.split(" ")
#         print("log info: ",logInfo)
#         #print("log info: ", logInfo)
        
        
#         with open(wrapper_path + "/log.txt", "w") as file:
#             #file.write(logInfo)
#             file.write("GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG")
#             for line in logInfo:
#                 file.write(line)
#                 file.write("\n")
#         #print("Wrapper_path: ", Main.wrapper_path)
#         # 抓出關鍵字
#         with open(wrapper_path + "/log.txt", "r") as read:
#             cnt = 0
#             for line in logInfo:
#                 if "Author" in line:
#                     if cnt <= 1:
#                         print("Author info: ", line)
#                         cnt += 1
                    
            
#             #readfile = read.readlines()[19]
            
#         #print("Author: " + readfile)
        
#         return True
                    
            
    
def main():

    
    name = gitLog() # return name of the latest commit branch
    print("Author: " + str(name))
    

if __name__ == "__main__":
    main()