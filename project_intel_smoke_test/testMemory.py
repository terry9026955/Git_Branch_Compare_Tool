

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