# get fail log info
import os
from re import T

path = 'D:\Tinghao.Chen\Desktop\WeeklyScriptList_Intel_EH_3.sl_0001'

for filename in os.listdir(path):
    with open(os.path.join(path, filename), 'r') as f:
        text = f.read() # 把當前路徑中所有檔案裡面所有的文字內容全存起來
        # print(text)   # 全部檔案內容印出來
        
        if '.dsf Fail' in text:
            #print('Fail log info: ', text) # 會把出錯的那整個file內容印出來
            text = text.split('\n')         # 切成list
            for line in text:
                if '.dsf Fail' in line:
                    print('Fail log info: ', line)  # 印出全部檔案當中出錯的那一行資訊(檔名與時間)





# # 路徑下的所有檔名
# filename = os.listdir(path)
# print(filename[0])

# with open(path+'\WL_FG_FwDL_Commit_ForEH.log', 'r') as read:
#     readFlag = False
#     for i in read:
#         # 印出整段結尾錯誤訊息
#         # if readFlag == True:  
#         #     print(i)
#         if '.dsf Fail' in i and readFlag == False:
#             print('Fail log info: ', i)
#             readFlag = True
    
        
        



# 抓最新時間
# 抓文件.dsf Fail
# for loop 開檔案