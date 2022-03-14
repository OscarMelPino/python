


# LO ESTOY USANDO PARA PROBAR LAS FUNCIONES POR SEPARADO


import pymysql
def DataB():
    miConexion = None
    cursor = None
    miConexion = pymysql.connect(host = 'localhost' , user = 'root', passwd = '7101991a', db = 'schoolerzz', port = 3306, cursorclass=pymysql.cursors.DictCursor)
    cursor = miConexion.cursor()
    return cursor
def GetTeacherSubjects(cursor, teacher):
    sql = f"SELECT sz_017_name from sz_008_teachers join sz_001_groups on sz_008_Id = sz_001_teachers_id join sz_102_groups_students on SZ_001_Id = SZ_102_groups_Id join sz_017_subjects on sz_102_subjects_id = SZ_017_Id where sz_008_nick like '{teacher}';"
    cursor.execute(sql)
    lista = []
    
    for row in cursor.fetchall():
        for column in row:
            lista.append(row[column])
    return lista # Devuelve una lista con las asignaturas de un profesor

for i in GetTeacherSubjects(DataB(), 'TJOY-GUPETOH'):
    print(i)