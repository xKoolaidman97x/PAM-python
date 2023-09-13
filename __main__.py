import os
import time
import pam_commands as pc
import pam_menus as pm
SYSBIN=os.path.dirname(os.path.realpath(__file__))
BIN=f'{SYSBIN}/bin'
DB='PAM'
#print(SYSBIN)
#print(BIN)

###### MENU #########
def mainMenu():
    import pam_commands as pc
    try:
        entrada = pm.logon()
        LOGIN = entrada[0]
        PASS = entrada[1]
    except KeyboardInterrupt:
        exit()
    #print(LOGIN,PASS)
    try:
        tableSetting = pc.DB_SET_TABLE(BIN,LOGIN,PASS,DB)
        TABLE = tableSetting[0]
        COL = tableSetting[1]
        pc.clearScreen()
        print(f"\nTable set to: {TABLE}")
        print(f"Columns set to: {COL}")
        time.sleep(1)
        pc.clearScreen()
    except KeyboardInterrupt:
        exit()
    while True:
        try:
            print("""
                  MAIN MENU

            [01] Select Password
            [02] Update Password
            [03] Delete Password
            [04] New Password
            [05] Set Table
            [69] DB Management
            [99] Exit
            """)
            query = pc.queryNumb("Selection: ")
            #print(query)
            if int(query) == 1:
                pc.selectPass(BIN,LOGIN,PASS,DB,COL,TABLE)
            elif int(query) == 2:
                pc.updatePass(BIN,LOGIN,PASS,DB,COL,TABLE)
            elif int(query) == 3:
                pc.deletePass(BIN,LOGIN,PASS,DB,COL,TABLE)
            elif int(query) == 4:
                pc.newPass(BIN,LOGIN,PASS,DB,COL,TABLE)
            elif int(query) == 5:
                tableSetting = pc.DB_SET_TABLE(BIN,LOGIN,PASS,DB)
                TABLE = tableSetting[0]
                COL = tableSetting[1]
                pc.clearScreen()
                print(f"\nTable set to: {TABLE}")
                print(f"Columns set to: {COL}")
                time.sleep(1)
            elif int(query) == 69:
                pm.dbMenu(BIN,LOGIN,PASS,DB,COL,TABLE)
            elif int(query) == 99:
                pc.clearScreen()
                print('\n\nGoodbye..')
                time.sleep(1)
                exit()
            else:
                print("INCORRECT OPTION")
        except KeyboardInterrupt:
            pc.clearScreen()
            print('\n\nGoodbye..')
            time.sleep(1)
            break


############# Main Code #############
mainMenu()