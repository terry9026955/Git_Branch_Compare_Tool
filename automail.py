import subprocess
from subprocess import Popen
import time

import SMI_email as mail

real_time = time.strftime("%Y%m%d_%H%M%S", time.localtime())

# 先叫 batch file執行
# 有跑完就叫 runover() 寄信
def call_batch():
    failFlag = None
    batch_file = ['hello.bat', 'ping_ip.bat', '123.bat']
    for i in range(len(batch_file)):
        try:
            batchfile = batch_file[i]
            subprocess.call(batchfile, timeout = 2)  
            
        except subprocess.TimeoutExpired as e:
            failFlag = True
            print("Error!!!!!!\nBatch file run failed!")
            print("Error happend in {} {}".format(batch_file[i],""))
            FailScript = batch_file[i]
            
            break
    if failFlag:
        mail.runover("Fail", FailScript)
    else:
        mail.runover("PASS", None)
    
        
    
    
    


if __name__ == "__main__":
    call_batch()



# 執行完就寄信