import pymysql

# VARIABLES

#user = username
#password = password
#userType = tipe
# if manager:
# 	manager_nick = userType + user
def DataB():
    miConexion = None
    cursor = None
    miConexion = pymysql.connect(host = 'localhost' , user = 'root', passwd = '7101991a', db = 'schoolerzz', port = 3306, cursorclass=pymysql.cursors.DictCursor)
    cursor = miConexion.cursor()
    return cursor
 
def Log(cursor, t, user, passw):
    # sql = f"SELECT sz_007_name FROM `sz_007_school_managers` where sz_007_Nick like '{user}' and sz_007_password like '{passw}' ;"
    sql = "set @a = -1;" 
    cursor.execute(sql)

    sql = f"call `pa_LoginAJ`('{t}','{user}','{passw}', @a);"
    cursor.execute(sql)

    sql = "select @a;"
    cursor.execute(sql)
    
    data = cursor.fetchone()
    
    return data['@a']
 
def Parents(cursor):
    sql = "SELECT sz_003_name, sz_003_nick FROM `sz_003_parents`;"
    cursor.execute(sql)
    lista = [] 
    for result in cursor.fetchall():
        for columna in result:
            lista.append(result[columna])
    return lista
