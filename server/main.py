import pymysql
from manager import Manager

# VARIABLES

#user = username
#password = password
#userType = tipe
# if manager:
# 	manager_nick = userType + user
def DataB():
    miConexion = None
    cursor = None
    miConexion = pymysql.connect(host = 'localhost' , user = 'root', passwd = '1234', db = 'schoolerzz', port = 3306, cursorclass=pymysql.cursors.DictCursor)
    cursor = miConexion.cursor()
    return cursor
 
def Log(cursor, t, user, passw):
    # sql = f"SELECT sz_007_name FROM `sz_007_school_managers` where sz_007_Nick like '{user}' and sz_007_password like '{passw}' ;"
    sql = "set @a = -1;" 
    cursor.execute(sql)

    sql = f"call `loginAJ`('{t}','{user}','{passw}', @a);"
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

def GetManagerData(nick, cursor) -> Manager:
    sql = f"SELECT sz_007_nick, sz_007_name, SZ_007_SN1, SZ_007_SN2 FROM `sz_007_school_managers` where sz_007_nick LIKE '{nick}';"
    cursor.execute(sql)
    res = cursor.fetchone()
    retManager = Manager(res['sz_007_nick'],res['sz_007_name'],res['SZ_007_SN1'],res['SZ_007_SN2'], GetSchoolNameFromManager(nick[1:4], cursor))
    return retManager

def GetSchoolNameFromManager(nick, cursor):
    sql = f"SELECT sz_006_name FROM `sz_006_schools` where sz_006_words3 LIKE '{nick}';"
    cursor.execute(sql)
    schoolname = cursor.fetchone()['sz_006_name']
    return schoolname

def GetSchoolData(cursor):
    cole = Manager.RetCole()
    sql = f"SELECT sz_006_name, SZ_006_SchoolCode, SZ_006_Country, SZ_006_City, SZ_006_PostalCode, SZ_006_Address FROM `sz_006_schools` where sz_006_name LIKE '{cole}';"
    cursor.execute(sql)
    school = [cursor.fetchone()['sz_006_name'], cursor.fetchone()['SZ_006_SchoolCode'],
              cursor.fetchone()['SZ_006_Country'], cursor.fetchone()['SZ_006_City'],
              cursor.fetchone()['SZ_006_PostalCode'], cursor.fetchone()['SZ_006_Address']]
    return school # Devuelve una lista con los datos del cole para meterlos en un formulario y 
                  #si los queremos cambiar cambiarlos o borrar dentro del html en el que se cargan

def GetParentData(cursor, parentNick):
    sql = f"SELECT sz_003_name, SZ_003_SN1, SZ_003_SN2, SZ_003_Birth, SZ_003_Nationality, SZ_003_Country, SZ_003_City, SZ_003_PostalCode, SZ_003_Address, SZ_003_Nick, SZ_003_Email, SZ_003_Phone1, SZ_003_Phone2 FROM `sz_003_parents` where sz_003_nick LIKE '{parentNick}';"
    cursor.execute(sql)
    parent = [cursor.fetchone()['sz_003_name'], cursor.fetchone()['SZ_003_SN1'],
              cursor.fetchone()['SZ_003_SN2'], str(cursor.fetchone()['SZ_003_Birth']),
              cursor.fetchone()['SZ_003_Nationality'], cursor.fetchone()['SZ_003_Country'],
              cursor.fetchone()['SZ_003_City'], cursor.fetchone()['SZ_003_PostalCode'],
              cursor.fetchone()['SZ_003_Address'], cursor.fetchone()['SZ_003_Nick'],
              cursor.fetchone()['SZ_003_Email'], cursor.fetchone()['SZ_003_Phone1'],
              cursor.fetchone()['SZ_003_Phone2']]
    return parent # Devuelve una lista con los datos del padre para meterlos en un formulario y 
                  #si los queremos cambiar cambiarlos o borrar dentro del html en el que se cargan

def GetTeacherData(cursor, teacherNick):
    sql = f"SELECT sz_008_name, SZ_008_SN1, SZ_008_SN2, SZ_008_Birth, SZ_008_Nationality, SZ_008_Country, SZ_008_City, SZ_008_PostalCode, SZ_008_Address, SZ_008_Nick, SZ_008_Email, SZ_008_Phone1, SZ_008_Phone2 FROM `sz_008_teachers` where sz_008_nick LIKE '{teacherNick}';"
    cursor.execute(sql)
    teacher = [cursor.fetchone()['sz_008_name'], cursor.fetchone()['SZ_008_SN1'],
              cursor.fetchone()['SZ_008_SN2'], str(cursor.fetchone()['SZ_008_Birth']),
              cursor.fetchone()['SZ_008_Nationality'], cursor.fetchone()['SZ_008_Country'],
              cursor.fetchone()['SZ_008_City'], cursor.fetchone()['SZ_008_PostalCode'],
              cursor.fetchone()['SZ_008_Address'], cursor.fetchone()['SZ_008_Nick'],
              cursor.fetchone()['SZ_008_Email'], cursor.fetchone()['SZ_008_Phone1'],
              cursor.fetchone()['SZ_008_Phone2']]
    return teacher # Devuelve una lista con los datos del teacher para meterlos en un formulario y 
                  #si los queremos cambiar cambiarlos o borrar dentro del html en el que se cargan

def GetStudentData(cursor, studentNick):
    sql = f"SELECT sz_002_name, SZ_002_SN1, SZ_002_SN2, SZ_002_Birth, SZ_002_Nationality, SZ_002_Country, SZ_002_City, SZ_002_PostalCode, SZ_002_Address, SZ_002_Nick, SZ_002_Email, SZ_002_Phone1, SZ_002_Phone2 FROM `sz_002_students` where sz_002_nick LIKE '{studentNick}';"
    cursor.execute(sql)
    student = [cursor.fetchone()['sz_002_name'], cursor.fetchone()['SZ_002_SN1'],
              cursor.fetchone()['SZ_002_SN2'], str(cursor.fetchone()['SZ_002_Birth']),
              cursor.fetchone()['SZ_002_Nationality'], cursor.fetchone()['SZ_002_Country'],
              cursor.fetchone()['SZ_002_City'], cursor.fetchone()['SZ_002_PostalCode'],
              cursor.fetchone()['SZ_002_Address'], cursor.fetchone()['SZ_002_Nick'],
              cursor.fetchone()['SZ_002_Email'], cursor.fetchone()['SZ_002_Phone1'],
              cursor.fetchone()['SZ_002_Phone2']]
    return student # Devuelve una lista con los datos del teacher para meterlos en un formulario y 
                  #si los queremos cambiar cambiarlos o borrar dentro del html en el que se cargan
