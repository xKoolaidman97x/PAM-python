###### QUERY CHECKS #########
def queryNumb(query):
    while True:
        venida = input(f"{query}")
        check = venida.isnumeric()
        if check:
            break
        else:
            print("INCORRECT INPUT")
    salida = venida
    return salida
def queryStr(query):
    while True:
        venida = input(f"{query}")
        if venida == '':
            print("INCORRECT INPUT")
        else:
            break
    salida = venida
    return salida
def queryStr_secure(query):
    from getpass import getpass
    while True:
        venida = getpass(f"{query}")
        if venida == '':
            print("INCORRECT INPUT")
        else:
            break
    salida = venida
    return salida
def clearScreen():
    import os
    # Clearing the Screen
    os.system('clear')
###### QUERIES ######### 
def selectPass(BIN,LOGIN,PASS,DB,COL,TABLE):
    import os
    try:
        #print(COL) 
        #print(BIN,LOGIN,PASS,DB,COL,TABLE)
        db_column = DB_COLUMN_CHECK(COL)
        db_siteName = queryStr('Site-name to search: ')
        #print(f"{BIN}/shell/selectPass {LOGIN} {PASS} {db_siteName} {DB} '{COL}' {TABLE}")
        clearScreen()
        os.system(f"bash {BIN}/shell/selectPass {LOGIN} {PASS} {db_siteName} {DB} '{COL}' {TABLE} {db_column}")
    except KeyboardInterrupt:
        return
def updatePass(BIN,LOGIN,PASS,DB,COL,TABLE):
    import os
    try:
        #COL_raw = ['name','username','password']
        #COL = ','.join(COL_raw)
        # db_column = DB_COLUMN_CHECK(COL)        
        db_siteName = queryStr('Site-name to update: ')
        os.system(f"bash {BIN}/shell/selectPass {LOGIN} {PASS} {db_siteName} {DB} '{COL}' {TABLE}")
        db_siteUser = queryStr('Username to update: ')
        db_pass_UPDATE = queryStr('New Pass: ')
        clearScreen()
        os.system(f"bash {BIN}/shell/updatePass {LOGIN} {PASS} {db_pass_UPDATE} {db_siteName} {DB} {TABLE} '{db_siteUser}'")
        #os.system(f'bash /Users/leo/dev/sql/shell/selectPass {login}')
        #print('Updating..')
        #print('Updated.')
    except KeyboardInterrupt:
        return
def deletePass(BIN,LOGIN,PASS,DB,COL,TABLE):
    import os
    try:
        db_column = DB_COLUMN_CHECK(COL)
        db_siteName = queryStr('Site-name to delete: ')
        os.system(f"bash {BIN}/shell/selectPass {LOGIN} {PASS} {db_siteName} {DB} '{COL}' {TABLE} {db_column}")
        db_userName = queryStr('Specify username to delete: ')
        clearScreen()
        os.system(f'bash {BIN}/shell/delPass {LOGIN} {PASS} {db_siteName} {DB} {TABLE} {db_userName} {COL} {db_column}')
    except KeyboardInterrupt:
        return
def newPass(BIN,LOGIN,PASS,DB,COL,TABLE):
    import os
    try:
        db_newPass_form = []
        db_columns_output = []
        db_columns_input = COL.split(",")
        os.system(f'bash {BIN}/shell/latestIndex {LOGIN} {PASS} {DB}')
        for x in db_columns_input:
            output = queryStr(f"NEW {x}: ")
            db_newPass_form.append(f"'{output}'")
            db_columns_output.append(f"'{x}'")
        newColumns = ', '.join(db_columns_output) 
        newPasswd = ', '.join(db_newPass_form)
        #print(newPasswd)
        clearScreen()
        os.system(f'bash {BIN}/shell/newPass {LOGIN} {PASS} {DB} "{newColumns}" {TABLE} "{newPasswd}"')
    except KeyboardInterrupt:
        return
###### DB COMMANDS ######### 
def DB_CREATE_BACKUP(BIN,LOGIN,PASS,DB,TABLE):
    import os
    try:
        db_backUpName = queryStr('Backup Name: ')
        #db_table = queryStr('Table Name: ') 
        os.system(f'bash {BIN}/shell/createBackup {LOGIN} {PASS} {BIN} {db_backUpName} {DB} {TABLE}')
    except KeyboardInterrupt:
        return
def DB_GET_COLUMNS(BIN,LOGIN,PASS,TABLE):
    import subprocess
    try:
        #db_table = queryStr('Table Name: ') 
        output = subprocess.check_output(f'bash {BIN}/shell/db_get_columnName {LOGIN} {PASS} {TABLE}', shell=True)
        columns_raw = output.decode('utf-8')
        columns_raw = columns_raw.strip("'").strip(" ")
        columns_raw = columns_raw.split('\n')
        columns_raw.remove("")
        columns = ','.join(columns_raw)
        #print(columns_raw)
        #print(type(columns))
        #print(columns_raw)
        #print(columns)
        return columns
    except KeyboardInterrupt:
        return
def DB_COLUMN_CHECK(COL):
    col_index = COL.split(",")
    columnNames = ['name','login','url']
    for x in col_index:
        #print(x)
        if x in columnNames:
            db_colSpec = x
            #print(f'special column is {db_colSpec}')
            break
    return db_colSpec
def DB_LOAD_BACKUP(BIN,LOGIN,PASS,DB,TABLE):
    import os
    try:
        db_backUpName = queryStr('Backup Name: ')
        #db_table = queryStr('Table Name: ') 
        print(f"{BIN}/shell/loadBackup {LOGIN} {PASS} {BIN} {db_backUpName} {DB} {TABLE}")
        os.system(f"bash {BIN}/shell/loadBackup {LOGIN} {PASS} {BIN} {db_backUpName} {DB} {TABLE}")
    except KeyboardInterrupt:
        return
def DB_DESTROY_ALL(BIN,LOGIN,PASS,DB,TABLE):
    import os
    try:
        #backup = venida('Backup Name: ')
        #db_table = queryStr('Table Name: ')
        os.system(f'bash {BIN}/shell/destroyAll {LOGIN} {PASS} {DB} {TABLE}')
    except KeyboardInterrupt:
        return
def DB_SHOW_ALL(BIN,LOGIN,PASS,DB,TABLE):
    import os
    try:
        #backup = venida('Backup Name: ')
        #db_table = queryStr('Table Name: ')
        os.system(f'bash {BIN}/shell/showallPass {LOGIN} {PASS} {DB} {TABLE}')
    except KeyboardInterrupt:
        return
def DB_SET_TABLE(BIN,LOGIN,PASS,DB):
    import os
    try:
        #backup = venida('Backup Name: ')
        os.system(f'mysql -u {LOGIN} --password={PASS} -D {DB} -e "SHOW TABLES;"')
        db_table = queryStr('Table Name: ')
        db_columns = DB_GET_COLUMNS(BIN,LOGIN,PASS,db_table)
        return db_table,db_columns
    except KeyboardInterrupt:
        return
def DB_TEST_CON(login,passwd):
    import MySQLdb
    import MySQLdb.Error
    db = MySQLdb.connect('127.0.0.1', login, passwd)
    cursor = db.cursor() 
    try:
        cursor.execute("SELECT VERSION()")
        results = cursor.fetchone()
        # Check if anything at all is returned
        if results:
            return True
        else:
            return False               
    except MySQLdb.Error as e:
        print("ERROR %d IN CONNECTION: %s" % (e.args[0], e.args[1]))
    return False
############# ADVANCED COMMANDS #############
def DB_CREATE_USER(BIN):
    import os
    username = queryStr('Username: ')
    password = queryStr('Password: ')
    os.system(f'bash {BIN}/shell/db_create_user {username} {password}')
def updateShells(BIN):
    import os
    SH_BIN=f'{BIN}/shell'
    print("/Users/leo/dev/projects/PAM/bin/shell")
    updateFolder = queryStr('\nPlease type path from where to update shells from: ')
    print('')
    os.system(f'sudo cp -rvf {updateFolder}/* {SH_BIN}')