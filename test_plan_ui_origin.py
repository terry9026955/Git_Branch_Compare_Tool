from ast import Str
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import mainui as ui
import subprocess
import use_inbox_delete_smi_driver_tp
import configparser
import os
import logging
import time
from functools import partial





class Main(QMainWindow, ui.Ui_MainWindow):
    SHA = None
    stopmissionFlag = False
    version_number = "20220718A_BETA"
    # determine if application is a script file or frozen exe
    if getattr(sys, 'frozen', False):   #確認是打包好的exe檔案還是本地的script檔案
        wrapper_path = os.path.dirname(sys.executable) #抓路徑位址
    elif __file__:
        wrapper_path = os.path.dirname(__file__)
    print("Wrapper Path is: ", wrapper_path)

        
    def __init__(self): #建構子
        super().__init__()  #繼承QtWidgets.QMainWindow跟Ui_MainWindow建構子的內容
        self.setupUi(self)  #將UI做建立的動作
        #self.setAcceptDrops(True)
        self.initiAct()     
        self.setAcceptDrops(True)   #使能夠支持拖動操作
        
        
        # 這邊可能要改成 thread 去做
        self.list_add_text() #應該是關於拖動功能
        self.pushButton_2.clicked.connect(self.removeSel) #按鈕功能
        self.pushButton_3.clicked.connect(self.getfile)
        self.pushButton_4.clicked.connect(self.tiggerStopcommand)
        self.pushButton.clicked.connect(self.getInfo)

        self.comboBox.currentIndexChanged.connect(self.enableCheckbox)  #用於事件改動時的處理方式(改A框，B框內容自動改變)
    

    def tiggerStopcommand(self):
        Main.stopmissionFlag = True
        return
    
    
    def getInfo(self):
        #Initializaion of stopmissionFlag
        Main.stopmissionFlag = False
        
        ini = self.loadini()
        folderPath = ini.value("Folder/path")
        gitPath = ini.value("Git_path/path")
        
        # get number of list 
        listNumber = self.listWidget.count()
        # get name of batch file
        scriptList = []
        for i in range(listNumber):
            #res = yield self.listWidget.item(i)
            scriptname = str(self.listWidget.item(i).text())
            scriptList.append(scriptname)
            
        ini_branch = ini.value("Branch/branch")   
        self.threadRunSHA(folderPath, listNumber, scriptList, ini_branch, gitPath)
        
    
    def threadRunSHA(self, folderpath, listWidget_count, scriptList, branch, gitPath):
        
        self.thread = QThread(parent=self)
        
        self.worker = getSHA()
        # Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Connect signals and slots
        
        self.thread.started.connect(partial(self.worker.main, gitPath))

        # 當收到finished, 線程結束
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        
        
        self.thread.finished.connect(self.thread.deleteLater)
        
        # commit
        self.worker.SHAwrite.connect(self.SHAwrite)
        self.worker.endTigger.connect(partial(self.threadRunbatch, folderpath, listWidget_count, scriptList, branch, Main.SHA))
        # Start the thread
        self.thread.start()
        
    
    def threadRunbatch(self, folderpath, listWidget_count, scriptList, branch, SHA, endTigger):
        
        #print(endTigger, folderpath, listWidget_count, scriptList, branch, SHA)
        self.thread = QThread(parent=self)
        
        self.worker = runBatchcommand()
        # Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Connect signals and slots
        
        self.thread.started.connect(partial(self.worker.mainWork, endTigger, folderpath, listWidget_count, scriptList, branch, SHA))

        self.worker.loopTigger.connect(partial(self.threadRunSHA, folderpath, listWidget_count, scriptList, branch))
        
        # 當收到finished, 線程結束
        
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        
        
        self.thread.finished.connect(self.thread.deleteLater)

        
        # Start the thread
        self.thread.start()


    def enableCheckbox(self):
        val = str(self.comboBox.currentText()) #目前選項中的值

        if val == "DVT":
            self.checkBox.setEnabled(True)  #設定元件是否可用
            self.checkBox.setChecked(False) 
        elif val == "3rd party":
            self.checkBox.setEnabled(False)
            self.checkBox.setChecked(True)
        else:
            self.checkBox.setEnabled(True)



    #抓ini路徑
    def loadini(self):
        # 原本寫的樣子:
        settings = QSettings(Main.wrapper_path+'/config.ini', QSettings.IniFormat)
        
        # 先設絕對路徑看能不能寫:
        # settings = QSettings('D:\Tinghao.Chen\Desktop\Git_Command_Test', QSettings.IniFormat)
        print("Loadini setting is: ", settings)
        return settings


    def initiAct(self):
        try:
            config = configparser.ConfigParser()    #python讀取ini設定檔案
            config.read(Main.wrapper_path+'/config.ini')

            ini = self.loadini()

            ini_selection = ini.value("test_plan/selection")    #QSettings.value(): read

            ini_branch = ini.value("Branch/branch")

            ini_SHA = ini.value("SHA/sha")
            try:
                

                ini_file = config['%General']

                filelist = ini_file.parser._sections["%General"]
                
                for k,v in filelist.items():
                    
                    self.listWidget.addItem(filelist[k])

                self.comboBox.addItems(ini_selection)
            except:
                tigger = False
                with open(Main.wrapper_path+"/config.ini", 'r') as f:
                    for row in f:
                        if "[%General]" in row:
                            tigger = True
                            pass
                        if tigger == True:
                            #print(row)
                            if "filepath_" in row:
                                name = row.split("=")[1]
                                #print(name)
                                
                                self.listWidget.addItem(name)

            self.lineEdit.setText(ini_branch)
            self.lineEdit_2.setText(ini_SHA)
            self.run_memory()
        except Exception:
            Log_Format = "%(levelname)s %(asctime)s - %(message)s"
            real_time = time.strftime("%Y%m%d_%H%M%S", time.localtime())
            log_name = Main.wrapper_path+"/log/"+real_time+"_logfile.log"
            logging.basicConfig(filename = log_name,
                                filemode = "w",
                                format = Log_Format, 
                                level = logging.DEBUG)

            logger = logging.getLogger()

            #Testing our Logger

            logger.error("Error Message from initiAct", exc_info=True)
        

    def dragEnterEvent(self, event):

        
        event.accept()
        event.acceptProposedAction()
        



    def dropEvent(self,event):

        
        file_name = event.mimeData().text()

        if 'file:///' in file_name:
            file_name = file_name.replace('file:///', '')
            #print(file_name)
        
            self.listWidget.addItem(file_name) 
            


    def list_add_text(self):

        self.listWidget.setDragEnabled(True) #支援拖動操作
        self.listWidget.setAcceptDrops(True)

        return


    def removeSel(self):

        listItems = self.listWidget.selectedItems()

        config = configparser.ConfigParser()
        config.read(Main.wrapper_path+'/config.ini')
        if not listItems: return

        for item in listItems:
            
            a = self.listWidget.item(self.listWidget.row(item)).text()
            print(a)
            self.listWidget.takeItem(self.listWidget.row(item))

            
            for i in config.options("%General"):
                if config.get("%General", i) == a:

                    print(i, '=', config.get("%General", i))
                
                    if config.has_section("%General") == True:

                        config.remove_option("%General", i)
                        config.write(open(Main.wrapper_path+'/config.ini', 'w'))
            

    # def get_list_item(self):

    #     for i in range(self.listWidget.count()):
    #         #res = yield self.listWidget.item(i)
        
    #         print(self.listWidget.item(i).text())

    def create_batch_run(self, wrapper_path):
        file_name = 'RunOnce.bat'
        f = open(file_name, 'w+')
        script = "cd /d "+ wrapper_path + "\ncall " + wrapper_path+"\\test_plan_ui_"+Main.version_number+".exe"
        f.write(script)
        f.close()
        return



    def reboot_reg(self, wrapper_path):
        cmd_reg = ["reg", "add", "HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunOnce", "/v", "RunScript", "/t", "REG_SZ", "/d", wrapper_path+"\\RunOnce.bat"]
        r = subprocess.run(cmd_reg, stdout=subprocess.PIPE)
        if r.returncode == 0:
            pass
        else:
            print(r.returncode)
        


    def getfile(self):

        # 選取資料夾對話視窗
        dig = QFileDialog.getExistingDirectory()
        # # setting gui can open any files

        config = configparser.ConfigParser()
        config.read(Main.wrapper_path+'/config.ini')
        config.set('Folder',"path", str(dig))
        newini = open("config.ini", 'w')
        config.write(newini)
        newini.close
        try:
            config.add_section('%General')
        except:
            pass

        if dig != "":
            filelist = os.listdir(dig)
            print(filelist)

            if len(filelist) != 0:
                
                filenumber = 0

                for i in range(len(filelist)):
                    
                    if ".bat" in filelist[i]:
                        
                        filenumber = filenumber + 1

                        self.listWidget.addItem(filelist[i])

                        config.set('%General',"filepath_"+str(filenumber), filelist[i])

                        newini = open("config.ini", 'w')
                        config.write(newini)
                        newini.close

                        #ini.setValue("General/filepath_"+str(i+1), filelist[i])

                    if ".exe" in filelist[i]:
                        
                        filenumber = filenumber + 1

                        self.listWidget.addItem(filelist[i])


                        config.set('%General',"filepath_"+str(filenumber), filelist[i])

                        newini = open(Main.wrapper_path+'/config.ini', 'w')
                        config.write(newini)
                        newini.close
            else:
                None


        return


    def renew_ini(self):
        
        new_scriptlist = []
        config = configparser.ConfigParser()
        config.read(Main.wrapper_path+'/config.ini')

        for i in range(self.listWidget.count()):
            #res = yield self.listWidget.item(i)
            scriptname = str(self.listWidget.item(i).text())
            new_scriptlist.append(scriptname)

        ini_file = config['%General']

        filelist = ini_file.parser._sections["%General"]
        
        istep = 0
        restigger = False
        for op,s in filelist.items():
            istep = istep + 1

            if restigger == True:
                config.set("Runonce_trigger", "started", op)
                restigger = False

            config.set("%General", op, new_scriptlist[istep-1])
            if "Restart" in new_scriptlist[istep-1]:
                restigger = True
                
            with open('config.ini', 'w') as configfile:
                config.write(configfile)
        
        



    def run_memory(self):
        
        try:
            config = configparser.ConfigParser()
            config.read(Main.wrapper_path+'/config.ini')

            tigger = config['Runonce_trigger']['tigger']
            path = config['Folder']['path']
            path = path.replace("/", "\\")
            started_tigger = False
            
            if tigger == "1":
                started = config['Runonce_trigger']['started']
                filelist = config['%General']
                for key in filelist:
                    
                    if key == started:
                        started_tigger = True
                        # print(key)
                        # print(config['%General'][key])
                    if started_tigger == True:
                        
                        next_file = config['%General'][key]
                        next_file = next_file.split(".")[0]
                        print("Run on next file or script : " + next_file)
                        #print(path+"\\"+next_file+".bat")
                        #r = subprocess.run(["cd", "/d", path], stdout=subprocess.PIPE)
                        r = subprocess.run([path+"/"+next_file+".bat"], stdout=subprocess.PIPE, shell=True)

                        if r.returncode != 0:
                            print("Got return code not success.")
                            print(r.stdout)

                config.set('Runonce_trigger',"tigger", "0")

                newini = open(Main.wrapper_path+'/config.ini', 'w')
                config.write(newini)
                newini.close
                
        except Exception:

            Log_Format = "%(levelname)s %(asctime)s - %(message)s"
            real_time = time.strftime("%Y%m%d_%H%M%S", time.localtime())
            log_name = Main.wrapper_path+"/log/"+real_time+"_logfile.log"
            logging.basicConfig(filename = log_name,
                                filemode = "w",
                                format = Log_Format, 
                                level = logging.DEBUG)

            logger = logging.getLogger()

            #Testing our Logger

            logger.error("Error Message from run_memory", exc_info=True)

        return
    
    # 這邊做讀寫新舊SHA，然後做紀錄
    def SHAwrite(self, remoteSHA):
        ini = self.loadini()
        
        currentSHA = ini.value("SHA/sha")
        lastSHA = ini.value("Last_SHA/last_sha")
        
        if (currentSHA == "" and lastSHA == ""):
            ini.setValue("SHA/sha", remoteSHA)
            ini.setValue("Last_SHA/last_sha",remoteSHA)
        elif(currentSHA != "" and currentSHA != remoteSHA):
            ini.setValue("Last_SHA/last_sha", currentSHA)
            ini.setValue("SHA/sha", remoteSHA)
            
            
        



    # def get_list_item(self, endTigger):
        
    #     try:
    #         if endTigger == True:
    #             self.renew_ini()
    #             branch_input = self.lineEdit.text()
    #             SHA_input = self.lineEdit_2.text()

    #             setting = self.loadini()
    #             setting.setValue("Branch/branch", branch_input)
    #             setting.setValue("SHA/SHA", SHA_input)

    #             folderpath = setting.value("Folder/path")
                
    #             for i in range(self.listWidget.count()):
    #                 #res = yield self.listWidget.item(i)
    #                 scriptname = str(self.listWidget.item(i).text())

    #                 file_path = folderpath + "/" + scriptname
                    

    #                 if scriptname != "":
                        
    #                     if "0-1_NVMe_Preparation_2269" in file_path:

    #                         if branch_input == "":

    #                             branch_input = ""

    #                         if SHA_input == "":

    #                             SHA_input = ""

    #                         procress = subprocess.run([file_path, branch_input, SHA_input])

    #                         if self.checkBox.isChecked():
    #                             command = use_inbox_delete_smi_driver_tp.main()
    #                             print(123)

    #                     elif "Restart" in file_path:

    #                         setting.setValue("Runonce_trigger/tigger", "1")
    #                         self.create_batch_run(Main.wrapper_path)
    #                         self.reboot_reg(Main.wrapper_path)
    #                         procress = subprocess.run([file_path])

    #                         break

    #                     else:

    #                         procress = subprocess.run([file_path])

    #                     if procress.returncode == 0:
    #                         pass
    #                     else:
    #                         print("Got return code not success.")
    #                         print(procress.stdout)
    #         else:
                
    #             print("endTigger recived None")


    #     except Exception:

    #         Log_Format = "%(levelname)s %(asctime)s - %(message)s"
    #         real_time = time.strftime("%Y%m%d_%H%M%S", time.localtime())
    #         log_name = Main.wrapper_path+"/log/"+real_time+"_logfile.log"
    #         logging.basicConfig(filename = log_name,
    #                             filemode = "w",
    #                             format = Log_Format, 
    #                             level = logging.DEBUG)

    #         logger = logging.getLogger()

    #         #Testing our Logger

    #         logger.error("Error Message from get_list_item", exc_info=True)
         
         

class getSHA(QThread):
    
    finished = pyqtSignal()

    endTigger = pyqtSignal(bool)
    
    SHAreturn = pyqtSignal(str)
    
    # Write SHA to main thread
    SHAwrite = pyqtSignal(str)
    
    def __init__(self, parent=None):
        QThread.__init__(self, parent=parent)
        
        

    def checkBranch(self, real_time):
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
            print("【Remote】 and 【Loacal】 are \'same\' branch.")
            self.SHAwrite.emit(str(remoteSHA))
            return False
        else:
            print("【Remote】 and 【Loacal】 are \'different\' branch.")
            self.gitPull()

        # return SHA
        self.writeSHA(real_time, remoteSHA, localSHA)
        Main.SHA = str(remoteSHA)
        print("Main.SHA: ", Main.SHA)
        
        # using signal write to main thread 
        self.SHAwrite.emit(str(remoteSHA))
        return True
        
    # Write SHA info into SHA.log
    def writeSHA(self, real_time, remoteSHA, localSHA):
        with open(Main.wrapper_path+"/auto_log/"+ real_time +"_SHA_log.log", "w") as file:
            file.write(real_time + ": \n")
            file.write("remote SHA: " + remoteSHA + "\n")
            file.write("local SHA:  " + localSHA + "\n\n")


    def gitPull(self):
        subprocess.call("git fetch -p")
        subprocess.call("git pull") 


    def gitPush(self):
        subprocess.call("git add .")
        subprocess.call("git commit -am \"File modified.\"")
        subprocess.call("git push")


    def gitCheck(self):
        subprocess.call("git --version")
        subprocess.call("git status")


    def showFile(self):
        subprocess.call('dir', shell=True, cwd = 'D:/Tinghao.Chen/Desktop/SMIGIT') 
        subprocess.call('dir', shell=True) 


    def gotoPath(self, gitPath):
        os.chdir(gitPath)
        # os.chdir('D:/SourceCode_SM2269')
        cwd = os.getcwd() 
        print("Current working directory is:", cwd)
        

    def gitLog(self):
        logInfo = str(subprocess.check_output("git log"))
        logInfo = logInfo.split(" ")
        #print(logInfo)
        
        with open("log.txt", "w") as file:
            #file.write(logInfo)
            for line in logInfo:
                file.write(line)
                file.write("\n")
        with open("log.txt", "r") as read:
            readfile = read.readlines()[19]
            
        print("Author: " + readfile)
        
        return True
        
        
    def main(self, gitPath):
        try:
            real_time = time.strftime("%Y%m%d_%H%M%S", time.localtime())
            # Go to directory (git repository)
            self.gotoPath(gitPath)
            # showFile()
            # gitCheck()

            # Get SHA
            compareTigger = self.checkBranch(real_time)
            
            if compareTigger == True:
                tiggerList = self.gitLog()
                
                self.endTigger.emit(tiggerList)
                
                self.finished.emit()
            else:
                
                for i in range(3):
                    if Main.stopmissionFlag == True:
                        break
                    else:
                        time.sleep(1)
                        
                if Main.stopmissionFlag == True:
                    self.finished.emit()
                else:   
                    self.main(gitPath)
            
        except Exception:

            Log_Format = "%(levelname)s %(asctime)s - %(message)s"
            real_time = time.strftime("%Y%m%d_%H%M%S", time.localtime())
            log_name = Main.wrapper_path+"/log/"+real_time+"_logfile.log"
            logging.basicConfig(filename = log_name,
                                filemode = "w",
                                format = Log_Format, 
                                level = logging.DEBUG)

            logger = logging.getLogger()
            logger.error("Error Message from Class of getSHA", exc_info=True)
            self.finished.emit()
            
        

class runBatchcommand(QThread):
    
    finished = pyqtSignal()
   
    loopTigger = pyqtSignal(str)
    
    
    def __init__(self, parent=None):
        QThread.__init__(self, parent=parent)
    
    
    def mainWork(self, endTigger, folderpath, listWidget_count, scriptList, branch_input, SHA_input):
        print(SHA_input)
        
        try:
            if endTigger == True:
                


                #folderpath = setting.value("Folder/path")
                
                for i in range(listWidget_count):
                    #res = yield self.listWidget.item(i)
                    stopFlag = Main.stopmissionFlag
                    
                    time.sleep(3)
                    if stopFlag == False:
                        scriptname = str(scriptList[i])

                        file_path = folderpath + "/" + scriptname
                        

                        if scriptname != "":
                            
                            if "0-1_NVMe_Preparation" in file_path:

                                if branch_input == None:

                                    branch_input = ""

                                if SHA_input == None:

                                    SHA_input = ""
                                    
                                if branch_input != "" and SHA_input != "":
                                    branch_input = ""

                                procress = subprocess.run([file_path, branch_input, SHA_input])

                                # if self.checkBox.isChecked():
                                #     command = use_inbox_delete_smi_driver_tp.main()
                                    

                            elif "Restart" in file_path or "restart" in file_path:
                                
                                procress = subprocess.run([file_path])

                                break

                            else:

                                procress = subprocess.run([file_path])

                            if procress.returncode == 0:
                                pass
                            else:
                                print("Got return code not success.")
                                print(procress.stdout)
                    else:
                        
                        
                        break
                
            else:
                
                print("endTigger recived False")
                

            
            
        except Exception:

            Log_Format = "%(levelname)s %(asctime)s - %(message)s"
            real_time = time.strftime("%Y%m%d_%H%M%S", time.localtime())
            log_name = Main.wrapper_path+"/log/"+real_time+"_logfile.log"
            logging.basicConfig(filename = log_name,
                                filemode = "w",
                                format = Log_Format, 
                                level = logging.DEBUG)

            logger = logging.getLogger()

            #Testing our Logger

            logger.error("Error Message from get_list_item", exc_info=True)
        
        if stopFlag == False:
            self.loopTigger.emit(SHA_input)
        else:
            self.finished.emit()
 

        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())