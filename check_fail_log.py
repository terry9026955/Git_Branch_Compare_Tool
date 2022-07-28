# get fail log info

path = 'D:\Tinghao.Chen\Desktop\WeeklyScriptList_Intel_EH_3.sl_0001'

with open(path+'\DataGC_BG_DstBlk_ErsFail_S2T.log', 'r') as read:
    cnt = 0
    for i in read:
        if cnt < 10:
            print(i)
            cnt += 1
    