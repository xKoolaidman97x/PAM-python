import pam_commands as pc
import time
def logon():
    import pam_commands as pc
    pc.clearScreen()
    import os
    print("""
                    WELCOME TO PAM
          
    P.A.M. stands for Password Asstive Module, and
    is used to manage and protect your passwords.

    """)
    LOGIN = pc.queryStr('Username: ')
    PASS = pc.queryStr_secure('Password: ')
    try:
        os.system(f'mysql -u {LOGIN} --password={PASS}')
    except:
        logon()
    os.system('pwd')
    return LOGIN,PASS
def dbMenu(BIN,LOGIN,PASS,DB,COL,TABLE):
    import pam_commands as pc
    pc.clearScreen()
    while True:
        try:
            print("""
                  DB MENU

            [01] Create Backup
            [02] Load Backup
            [03] Destroy All
            [04] SHOW ALL PASSWORDS
            [21] Advanced Menu
            [50] Main Menu
            [99] Exit
            """)
            query = pc.queryNumb("Selection: ")
            if int(query) == 1:
                pc.DB_CREATE_BACKUP(BIN,LOGIN,PASS,DB,TABLE)
            elif int(query) == 2:
                pc.DB_LOAD_BACKUP(BIN,LOGIN,PASS,DB,TABLE)
            elif int(query) == 3:
                pc.DB_DESTROY_ALL(BIN,LOGIN,PASS,DB,TABLE)
            elif int(query) == 4:
                pc.DB_SHOW_ALL(BIN,LOGIN,PASS,DB,TABLE)
            elif int(query) == 21:
                advancedMenu(BIN,LOGIN,PASS,DB,COL,TABLE)
            elif int(query) == 50:
                pc.clearScreen()
                break
            elif int(query) == 99:
                pc.clearScreen()
                print('\n\nGoodbye..')
                time.sleep(1)
                exit()
            else:
                print("INCORRECT OPTION")
        except KeyboardInterrupt:
            break
def advancedMenu(BIN,LOGIN,PASS,DB,COL,TABLE):
    import pam_commands as pc
    pc.clearScreen()
    while True:
        try:
            print("""
            [01] Create User
            [02] Load Backup
            [03] Destroy All
            [04] EASTER EGG
            [42] Update SHELLS
            [69] BACK
            [99] Exit
            """)
            query = pc.queryNumb("Selection: ")
            if int(query) == 1:
                pc.DB_CREATE_USER()
            elif int(query) == 2:
                pc.DB_LOAD_BACKUP(BIN,LOGIN,PASS,DB,TABLE)
            elif int(query) == 3:
                pc.DB_DESTROY_ALL(BIN,LOGIN,PASS,DB,TABLE)
            elif int(query) == 4:
                #pc.(BIN,LOGIN,PASS,DB,COL,TABLE)
                print("")
            elif int(query) == 42:
                pc.updateShells(BIN)
            elif int(query) == 69:
                pc.clearScreen()
                break
            elif int(query) == 99:
                pc.clearScreen()
                print('\n\nGoodbye..')
                time.sleep(1)
                exit()
            else:
                print("INCORRECT OPTION")
        except KeyboardInterrupt:
            break