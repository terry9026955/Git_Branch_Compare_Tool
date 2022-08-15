# One Touch Tool of SMI automation project
* Go to the specific directory of your local repo
* To get SHA of the latest commit from remote git repository
* Check remote and local branch are same or not
* If same: 
    * git add, commit, and push (confirm file be modified)
* If different:
    * git pull (get new branch to sync)
* Record SHA detail and time
* Parse specific fail log contents and record into 'error_code.log'
* Send script error message email to RD

 <br/>

## 工作項目:
* 自動化測試軟體開發
* 多執行續(多線程)軟體專案開發
* 透過subprocess呼叫command line指令
* 執行自動開卡程序
* 檢查與比對本地與遠端之Git Server版本，並對不同條件依序執行不同操作
    * 抓server的code下來進行同步
    * 固定時間循環做檢查  
    * 開機後自啟動  
* Fail log keyword parsing 
* 多人的寄信通知功能與測試
