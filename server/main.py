from datetime import datetime
from pickle import NONE
import pymysql
from manager import Manager
import random
import hashlib

# VARIABLES

MyManagersList= []
MyStudentsList= []
MyParentsList= []
MyTeachersList= []

#user = username
#password = password
#userType = tipe
# if manager:
# 	manager_nick = userType + user
def DataB():
    miConexion = None
    cursor = None
    miConexion = pymysql.connect(host = '172.16.51.7' , user = 'alvaro', passwd = '1234', db = 'schoolerzz', port = 3306, cursorclass=pymysql.cursors.DictCursor)
    cursor = miConexion.cursor()
    return cursor

def Log(cursor, t, user, passw):
    # sql = f"SELECT sz_007_name FROM `sz_007_school_managers` where sz_007_Nick like '{user}' and sz_007_password like '{passw}' ;"
    sql = "set @a = -1;"
    cursor.execute(sql)

    sql = f"call `pa_loginAJ`('{t}','{user}','{passw}', @a);"
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
    school = []
    for row in cursor.fetchall():
        for column in row:
            school.append(row[column])
    return school # Devuelve una lista con los datos del cole para meterlos en un formulario y
                #si los queremos cambiar cambiarlos o borrar dentro del html en el que se cargan

def GetParentData(cursor, parentNick):
    sql = f"SELECT sz_003_name, SZ_003_SN1, SZ_003_SN2, SZ_003_Birth, SZ_003_Nationality, SZ_003_Country, SZ_003_City, SZ_003_PostalCode, SZ_003_Address, SZ_003_Nick, SZ_003_Email, SZ_003_Phone1, SZ_003_Phone2 FROM `sz_003_parents` where sz_003_nick LIKE '{parentNick}';"
    cursor.execute(sql)
    parent = []
    for row in cursor.fetchall():
        for column in row:
            parent.append(row[column])
    return parent # Devuelve una lista con los datos del padre para meterlos en un formulario y
                    #si los queremos cambiar cambiarlos o borrar dentro del html en el que se cargan

def GetTeacherData(cursor, teacherNick):
    sql = f"SELECT sz_008_name, SZ_008_SN1, SZ_008_SN2, SZ_008_Birth, SZ_008_Nationality, SZ_008_Country, SZ_008_City, SZ_008_PostalCode, SZ_008_Address, SZ_008_Nick, SZ_008_Email, SZ_008_Phone1, SZ_008_Phone2 FROM `sz_008_teachers` where sz_008_nick LIKE '{teacherNick}';"
    cursor.execute(sql)
    teacher = []
    for row in cursor.fetchall():
        for column in row:
            teacher.append(row[column])
    return teacher # Devuelve una lista con los datos del teacher para meterlos en un formulario y
                    #si los queremos cambiar cambiarlos o borrar dentro del html en el que se cargan

def GetStudentData(cursor, studentNick):
    sql = f"SELECT sz_002_name, SZ_002_SN1, SZ_002_SN2, SZ_002_Birth, SZ_002_Nationality, SZ_002_Country, SZ_002_City, SZ_002_PostalCode, SZ_002_Address, SZ_002_Nick, SZ_002_Email FROM `sz_002_students` where sz_002_nick LIKE '{studentNick}';"
    cursor.execute(sql)
    student = []
    for row in cursor.fetchall():
        for column in row:
            student.append(row[column])
    return student # Devuelve una lista con los datos del student para meterlos en un formulario y
                    #si los queremos cambiar cambiarlos o borrar dentro del html en el que se cargan

def GetGroupMarksBySubject(cursor, subject, level, classroom):
    sql = f"SELECT sz002.SZ_002_Name, sz102.SZ_102_Mark_1T, sz102.SZ_102_Mark_2T, sz102.SZ_102_Mark_3T, sz102.SZ_102_Mark_F from sz_102_groups_students as sz102 join sz_001_groups as sz001 on SZ_102_Groups_Id = sz_001_Id join sz_017_subjects as sz017 on SZ_017_Id = SZ_102_Subjects_Id join sz_002_students as sz002 on SZ_102_Students_Id = sz_002_Id where sz_017_name like '{subject}' and sz_001_level = '{level}' and sz_001_class = '{classroom}';"
    cursor.execute(sql)
    lista = []
    fila = []
    for row in cursor.fetchall():
        for column in row:
            fila.append(row[column])
        lista.append(fila)
        fila = []
    return lista # Devuelve una lista con los datos de todos los alumnos en esa en una asignatura

def GetTeacherSubjects(cursor, teacher):
    sql = f"SELECT sz_017_name from sz_008_teachers join sz_001_groups on sz_008_Id = sz_001_teachers_id join sz_102_groups_students on SZ_001_Id = SZ_102_groups_Id join sz_017_subjects on sz_102_subjects_id = SZ_017_Id where sz_008_nick like '{teacher}';"
    cursor.execute(sql)
    lista = []
    for row in cursor.fetchall():
        for column in row:
            lista.append(row[column])
    return lista # Devuelve una lista con las asignaturas de un profesor

def AddStudent(cursor,Snombre, Ssn1, Ssn2, Sbirth, Snation, Scountry, SpostalCode, Saddress, Semail, Smedical, Sobservations, Sschool):
    Snick = CreateNick(cursor,'S',Sschool,Snombre, Ssn1, Ssn2)
    sql=f"INSERT INTO sz_002_Students(SZ_002_Id, SZ_002_Name, SZ_002_SN1, SZ_002_SN2, SZ_002_Birth, SZ_002_Nationality, SZ_002_Country, SZ_002_City, SZ_002_PostalCode, SZ_002_Address, SZ_002_Email, SZ_002_Nick, SZ_002_Password) VALUES (UUID_TO_BIN(UUID()),'{Snombre}', '{Ssn1}', '{Ssn2}', '{Sbirth}', '{Snation}', '{Scountry}', '{SpostalCode}', '{Saddress}', '{Semail}', '{Snick}', '{hashlib.md5(b'1234')}');"
    cursor.execute(sql)
    if Smedical != NONE:
        sql = f"update sz_002_students set SZ_002_Medical = '{Smedical}' where SZ_002_Name = '{Snombre}' and SZ_002_SN1 = '{Ssn1}' and SZ_002_SN2 = '{Ssn2}'"
    cursor.execute(sql)

def AddParent(cursor, Pname, Psn1, Psn2, Pbirth, Pnationality, Pcountry, Pcity, PpostalCode, Paddress, Pemail, Pphone1, Pphone2,  Sschool, Snick):
    Pnick = CreateNick(cursor,'P',Sschool,Pname, Psn1, Psn2)
    if Pphone2 == NONE:
        sql =f"(INSERT INTO sz_003_parents (`SZ_003_Id`,`SZ_003_Name`,`SZ_003_SN1`,`SZ_003_SN2`,`SZ_003_Birth`,`SZ_003_Nationality`,`SZ_003_Country`,`SZ_003_City`,`SZ_003_PostalCode`,`SZ_003_Address`,`SZ_003_Email`,`SZ_003_Nick`,`SZ_003_Password`,`SZ_003_Phone1`)VALUES (UUID_TO_BIN(UUID()),'{Pname}', '{Psn1}', '{Psn2}', '{Pbirth}', '{Pnationality}', '{Pcountry}', '{Pcity}', '{PpostalCode}', '{Paddress}', '{Pemail}','{Pnick}','{hashlib.md5(b'1234')}', '{Pphone1}');"
    else:
        sql =f"(INSERT INTO sz_003_parents (`SZ_003_Id`,`SZ_003_Name`,`SZ_003_SN1`,`SZ_003_SN2`,`SZ_003_Birth`,`SZ_003_Nationality`,`SZ_003_Country`,`SZ_003_City`,`SZ_003_PostalCode`,`SZ_003_Address`,`SZ_003_Email`,`SZ_003_Nick`,`SZ_003_Password`,`SZ_003_Phone1`,`SZ_003_Phone2`)VALUES (UUID_TO_BIN(UUID()),'{Pname}', '{Psn1}', '{Psn2}', '{Pbirth}', '{Pnationality}', '{Pcountry}', '{Pcity}', '{PpostalCode}', '{Paddress}', '{Pemail}', '{Pnick}','{hashlib.md5(b'1234')}', '{Pphone1}', '{Pphone2}');"
    cursor.execute(sql)

    sql=f"INSERT INTO sz_203_students_parents VALUES (UUID_TO_BIN(UUID()), (SELECT SZ_002_Id FROM sz_002_Students WHERE SZ_002_Nick LIKE '{Snick}'), (SELECT SZ_003_Id FROM SZ_003_Parents where SZ_003_Name LIKE '{Pname}' and SZ_003_SN1 LIKE '{Psn1}' and SZ_003_SN2 LIKE '{Psn2}'));"
    cursor.execute(sql)

def AddTeacher(cursor, _Name, _SN1, _SN2, _Birth, _Nacionality, _Country, _City, _PostalCode, _Addres, _Email, _Password, _Phone1, _Phone2, Sschool):
    Tnick = CreateNick(cursor,'T',Sschool,_Name, _SN1, _SN2)
    if _Phone2 == None:
        sql = f"INSERT INTO schoolerzz.sz_008_teachers(SZ_008_Id, SZ_008_Name, SZ_008_SN1, SZ_008_SN2, SZ_008_Birth, SZ_008_Nationality, SZ_008_Country, SZ_008_City, SZ_008_PostalCode, SZ_008_Address, SZ_008_Email, SZ_008_Nick, SZ_008_Password, SZ_008_Phone1) VALUES (UUID_TO_BIN(UUID()), '{_Name}', '{_SN1}', '{_SN2}', '{_Birth}', '{_Nacionality}', '{_Country}', '{_City}', '{_PostalCode}', '{_Addres}', '{_Email}', '{Tnick}','{hashlib.md5(b'1234')}', '{_Phone1}');"
    else:
        sql = f"INSERT INTO schoolerzz.sz_008_teachers(SZ_008_Id, SZ_008_Name, SZ_008_SN1, SZ_008_SN2, SZ_008_Birth, SZ_008_Nationality, SZ_008_Country, SZ_008_City, SZ_008_PostalCode, SZ_008_Address, SZ_008_Email, SZ_008_Nick, SZ_008_Password, SZ_008_Phone1, SZ_008_Phone2) VALUES (UUID_TO_BIN(UUID()), '{_Name}', '{_SN1}', '{_SN2}', '{_Birth}', '{_Nacionality}', '{_Country}', '{_City}', '{_PostalCode}', '{_Addres}', '{_Email}', '{Tnick}', '{hashlib.md5(b'1234')}', {_Phone1}', '{_Phone2}');"
    cursor.execute(sql)

def CreateNick(cursor,t, school, name, sn1, sn2):

    letras = 'TRWAGMYFPDXBNJZSQVHLCKE'
    num = int(random.randint(0,21))
    nick = t + school[0:3].upper() + '-' + name[0:2].upper() + sn1[0:2].upper() + sn2[0:2].upper() + letras[num:num + 1]
    sql = f"SELECT sz_002_name FROM sz_002_students where sz_002_nick LIKE '{nick}';"
    cursor.execute(sql)
    try:
        name = cursor.fetchall()[0]['sz_002_name']
    except Exception as e:
        name = '' 
    while name != '':
        num = int(random.randint(0,21))
        nick = t.upper() + school[0:3].upper() + '-' + name[0:2].upper() + sn1[0:2].upper() + sn2[0:2].upper() + letras[num : num + 1]
        sql = f"SELECT sz_002_name FROM sz_002_students where sz_002_nick LIKE '{nick}';"
        cursor.execute(sql)
        try:
            name = cursor.fetchall()[0]['sz_002_name']
        except Exception as e:
            name = ''
    return nick

# Funciones de modificar
def UpdateTeacher(cursor, _Field, _Data, _Nick):
    sql = f"update from sz_008_teachers set '{_Field}' = '{_Data}' where SZ_008_Nick = '{_Nick}';"
    cursor.execute(sql)

def UpdateSchool(cursor, _Field, _Data, _SchoolCode):
    sql = f"update from sz_006_schools set '{_Field}' = '{_Data}' where SZ_006_SchoolCode = '{_SchoolCode}';"
    cursor.execute(sql)

def UpdateParent(cursor, _Field, _Data, _Nick):
    sql = f"update from sz_003_parents set '{_Field}' = '{_Data}' where SZ_003_Nick = '{_Nick}';"
    cursor.execute(sql)

def UpdateStudent(cursor, _Field, _Data, _Nick):
    sql = f"update from sz_002_students set '{_Field}' = '{_Data}' where SZ_002_Nick = '{_Nick}';"
    cursor.execute(sql)


# insert into sz_203_students_parents values(UUID_TO_BIN(UUID()), (select sz_002_id from sz_002_students where sz_sn1 = 'Melgarejo'), (select sz_003_id from sz_003_parents where SZ_003_Name = 'Padrecito'))
def GetAllParents(cursor, school):
    sql = f"select sz_003_name, sz_003_sn1, sz_003_sn2, sz_003_nick from sz_003_parents join sz_203_students_parents on sz_203_parents_id = sz_003_id join sz_002_students on sz_203_students_id = sz_002_id join sz_102_groups_students on SZ_102_Students_Id = sz_002_id join sz_001_groups on sz_001_id = SZ_102_Groups_Id join sz_006_schools on sz_006_id = SZ_001_Schools_Id where sz_006_name like '{school}';"
    cursor.execute(sql)
    lista = []
    for row in cursor.fetchall():
        lista.append(row)
    return lista

def GetAllTeachers(cursor):
    lastId = 0
    sql = f"select sz_008_name, sz_008_sn1, SZ_008_SN2, SZ_008_Nick from sz_008_teachers;"
    cursor.execute(sql)
    for row in cursor.fetchall():
        lastId += 1
        row['id'] = lastId
        MyTeachersList.append(row)
    return MyTeachersList


#  MANAGERS
def GetAllManagers(cursor):
    lastId = 0
    MyManagersList.clear()
    sql = f"SELECT  sz_007_name, sz_007_sn1, SZ_007_SN2, SZ_007_Nick from sz_007_school_managers;"
    cursor.execute(sql)
    for row in cursor.fetchall():
        lastId += 1
        row['id'] = lastId
        MyManagersList.append(row)
    return MyManagersList

def GetManagerById(cursor, id):
    for manager in GetAllManagers(cursor):
        if manager['id'] == id:
            return manager

def CreateNewManager(cursor, data):
    Mnick = CreateNick(cursor,'S','Joyfe',data['name'], data['sn1'], data['sn2'])
    sql= f"insert into sz_007_school_managers(SZ_007_Id, SZ_007_Name, SZ_007_SN1, SZ_007_SN2, SZ_007_Birth, SZ_007_Nationality, SZ_007_Country, SZ_007_City, SZ_007_PostalCode, SZ_007_Address, SZ_007_Email, SZ_007_Phone1, SZ_007_Nick, SZ_007_Password, SZ_007_Schools_Id) values(BIN_TO_UUID(UUID()), '{data['name']}', '{data['sn1']}', '{data['sn2']}', date('{data['birth']}'), '{data['nationality']}', '{data['country']}', '{data['city']}', '{data['postalcode']}', '{data['address']}', '{data['email']}', '{data['phone1']}', '{Mnick}', '1234', (Select SZ_006_SchoolCode from sz_006_schools where sz_006_name like 'Joyfe'));"
    cursor.execute(sql)

def ModifyManager(cursor, id, data):
    managertomodify = GetManagerById(cursor, id)
    for key in managertomodify.keys():
        managertomodify[key] = data[key]


def GetAllParents(cursor):
    lastId = 0
    sql = f"select sz_003_name, sz_003_sn1, sz_003_sn2, sz_003_nick from sz_003_parents;"
    cursor.execute(sql)
    for row in cursor.fetchall():
        lastId += 1
        row['id'] = lastId
        MyParentsList.append(row)
    return MyParentsList

def GetParentById(cursor, id):
    for parent in GetAllParents(cursor):
        if parent['id'] == id:
            return parent

# Funciones de borrar
def DeleteTeacherfromDataBase(cursor,id):
    MyTeachersList = []
    MyTeachersList = GetAllTeachers(cursor)
    for teacher in MyTeachersList:
        if teacher["id"] == id:
            try:
                sql = f"delete from SZ_008_teachers where SZ_008_Nick = '{teacher['sz_008_nick']}';"
                cursor.execute(sql)
                return True
            except Exception as e:
                print(e)
                return False

def DeleteParent(cursor, id):
    MyParentsList = []
    MyParentsList = GetAllParents(cursor)
    for parent in MyParentsList:
        if parent["id"] == id:
            try:
                sql = f"delete from sz_003_parents where SZ_003_Nick = '{parent['sz_008_nick']}';"
                cursor.execute(sql)
                return True
            except Exception as e:
                print(e)
                return False

def DeleteManager(cursor, id) -> bool:
    return EraseManager(cursor, GetManagerById(id))

def EraseManager(cursor, manager) -> bool:
    try:
        sql = f"delete from sz_007_school_managers where SZ_007_Nick = '{manager['sz_007_nick']}';"
        cursor.execute(sql)
        return True
    except Exception as ex:
        print(str(ex))
        return False







def GetAllTeachers(cursor):
    lastId = 0
    MyTeachersList.clear()
    sql = f"SELECT  SZ_008_Name, sz_008_SN1, SZ_008_SN2, SZ_008_Nick from sz_008_teachers;"
    cursor.execute(sql)
    for row in cursor.fetchall():
        lastId += 1
        row['id'] = lastId
        MyTeachersList.append(row)
    return MyTeachersList

def GetTeacherById(cursor):
    for teacher in GetAllTeachers(cursor):
        if teacher['id'] == id:
            return teacher

def DeleteTeacher(cursor, id) -> bool:
    for teacher in GetAllTeachers(cursor):
        if teacher['id'] == id:
            return EraseManager(cursor, teacher)

def EraseTeacher(cursor, teacher) -> bool:
    try:
        sql = f"delete from sz_008_teachers where SZ_008_Nick = '{teacher['SZ_008_Nick']}';"
        cursor.execute(sql)
        return True
    except Exception as ex:
        print(str(ex))
        return False




def GetAllStudents(cursor):
    lastId = 0
    sql = f"select sz_002_name, sz_002_SN1, sz_002_SN2, sz_002_Nick from sz_002_students;"
    cursor.execute(sql)
    for row in cursor.fetchall():
        lastId += 1
        row['id'] = lastId
        MyStudentsList.append(row)
    return MyStudentsList

def GetStudentById(cursor):
    for student in GetAllStudents(cursor):
        if student['id'] == id:
            return student

def DeleteStudent(cursor, id) -> bool:
    for student in GetAllStudents(cursor):
        if student['id'] == id:
            return EraseStudent(cursor, student)

def EraseStudent(cursor, student) -> bool:
    try:
        sql = f"delete from sz_002_students where SZ_002_Nick = '{student['SZ_002_Nick']}';"
        cursor.execute(sql)
        return True
    except Exception as ex:
        print(str(ex))
        return False