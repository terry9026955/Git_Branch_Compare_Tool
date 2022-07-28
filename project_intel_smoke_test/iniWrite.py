# 讀寫ini檔案用的測試codd

# 讀取ini的路徑，並CD過去
from configparser import ConfigParser 
import os
import subprocess
from turtle import goto


def gotoPath():
    cwd_cur = os.getcwd() # 目前路徑
    conf = ConfigParser()
    conf.read('config2.ini')
    path = conf['Git_path']['path'] # ini 裡面的路徑
    print("cur path: ", path)

    os.chdir(path)  # CD過去抓branch資訊
    cwd = os.getcwd() 
    #print("Current working directory is:", cwd)
    
    remoteSHA = checkBranch()   # 把remote SHA 傳回來
    #print("get remote SHA")
    os.chdir(cwd_cur)   # 切回原本路徑
    #print("go back to the path: ", cwd_cur)
    return remoteSHA # 回傳到main
        


def checkBranch():
    print("\nChecking branch...\n")

    # Get the latest SHA of github
    remoteSHA = str(subprocess.check_output("git rev-parse origin"))
    remoteSHA = remoteSHA.replace("b'", "")
    remoteSHA = remoteSHA[:8]   # Get former 8 SHA codes
    
    localSHA = str(subprocess.check_output("git rev-parse HEAD"))
    localSHA = localSHA.replace("b'", "")
    localSHA = localSHA[:8]

    print("remote SHA: ", remoteSHA)
    print("local SHA: ", localSHA)

    if((remoteSHA) == (localSHA)):  # Check SHA of 2 side
        # print("\'Remote\' and \'Loacal\' are \'same\' branch.")
        pass
    else:
        # print("\'Remote\' and \'Loacal\' are \'different\' branch.")
        pass
    return str(remoteSHA)



# ini 裡面資料的讀取
def checkSHA():
    conf = ConfigParser()
    conf.read('config2.ini')
    
    item_old = str(conf["Last_SHA"]["last_sha"])
    print("old SHA: ", item_old)
    item_cur = str(conf["SHA"]["sha"])
    print("new SHA: ", item_cur)

    # 都空就先pull
    if (item_old == "") and (item_cur == ""):
        print("Last_SHA and SHA all nothing")
        #->PULL
        
    # 比對新舊SHA結果
    if item_cur != item_old:
        # print('iniSHA different')
        pass
    else:
        # print('iniSHA equal')
        pass
    

# remoteSHA寫入進去ini
def iniWrite(remoteSHA):
    conf = ConfigParser()
    conf.read('config2.ini')
    
    if (str(conf["Last_SHA"]["last_sha"]) == "" and str(conf["SHA"]["sha"]) == ""):   # 一開始如果都沒有寫入的話就更新SHA
        conf.set('SHA', 'sha', remoteSHA)
        conf.set('Last_SHA', 'last_sha', remoteSHA)
        conf.write(open('config2.ini', 'w'))    #做寫入讓ini內容更新
        # print("no enough data so write to sha")
    elif ((str(conf["SHA"]["sha"]) != "") and (str(conf["SHA"]["sha"]) != remoteSHA)):  # 如果SHA有內容且跟之前的不同
        SHA_cur = str(conf["SHA"]["sha"])
        conf.set('Last_SHA', 'last_sha', SHA_cur)   # 原本的SHA放到舊的last_sha裡面
        conf.set('SHA', 'sha', remoteSHA)           # 新的SHA去更新sha裡面的值
        conf.write(open('config2.ini', 'w'))
        # print("update all data")
    #conf.set('Last_SHA', 'last_sha', remoteSHA)    
        
def main():
    conf = ConfigParser()
    conf.read('config2.ini')
    
    remoteSHA = gotoPath()  # 接收來自checkBranch的SHA資訊
    checkSHA()  # 查看ini file裡面的新舊SHA
    remoteSHA2 = "123"
    iniWrite(remoteSHA)
    
            
if __name__ == "__main__":
    main()




