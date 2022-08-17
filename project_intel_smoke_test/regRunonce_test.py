import subprocess
import os
import sys
import time

if getattr(sys, 'frozen', False):   #確認是打包好的exe檔案還是本地的script檔案
    wrapper_path = os.path.dirname(sys.executable) #抓路徑位址
elif __file__:
    wrapper_path = os.path.dirname(__file__)
#print("Wrapper Path is: ", wrapper_path)


def regRunonce(wrapper_path):
    cmd_reg = ["reg", "add", "HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunOnce", "/v", "RunScript", "/t", "REG_SZ", "/d", wrapper_path+"\\SMI_OneTouch_20220816A.exe"]
    r = subprocess.run(cmd_reg, stdout=subprocess.PIPE)
    if r.returncode == 0:
        print(123)
        return True
    else:
        print(r.returncode)
        return False

if __name__ == "__main__":
    print(wrapper_path)
    time.sleep(3)
    regRunonce(wrapper_path)
