import configparser



scriptFolder = "C:\\Tools\\testplan_ui_20220428_bata\\SMI_Power_Cycle_Test_GSD_mode"
name = scriptFolder.split("\\")
sname = name[len(name)-1]
with open(scriptFolder + "/" + sname + ".bat") as f:
    for line in f.readlines():
        if "PowerCyclingTest.bat" in line:
            line = line.split('"')
            for e in line:
                if "\\" in e:
                    print(e.replace(".bat", ".ini"))
