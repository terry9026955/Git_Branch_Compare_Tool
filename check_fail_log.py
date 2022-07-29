# get fail log info
import os
from re import T


def get_fail_log():
    # 檔案路徑(可能會變動)
    path = 'D:\Tinghao.Chen\Desktop\WeeklyScriptList_Intel_EH_3.sl_0001'

    checkError = False                                              # 檢查有無 scan 到 fail log 訊息
    
    # for loop 掃全部檔名
    for filename in os.listdir(path):
        with open(os.path.join(path, filename), 'r') as f:
            text = f.read()                                         # 把當前路徑中所有檔案裡面所有的文字內容全存起來
            # print(text)                                           # 每一份檔案的內容全印出來
            
            if '.dsf Fail' in text:
                # print(text)                                       # 會把出錯的那一個 log file 之內容全印出來
                text = text.split('\n')                             # 切成 list
                readFlag = False                                    # 不印內容
                checkError = True                                   # 發現 Error code
                for line in text:
                    if readFlag == True:  
                        print(line)
                    elif '.dsf Fail' in line and readFlag == False:
                        print('Fail log error code: \n', line)      # 印出全部檔案當中出錯的那一行資訊(檔名與時間)
                        readFlag = True
                    elif '                  ' in line:
                        readFlag == False
                        
                        # 剩下存取 error code 內容功能...
     
    # check passed or not           
    if checkError == True:
        print("Script Failed!")
    else:
        print("Script Passed!")
                
           



if __name__ == "__main__":
    get_fail_log()

