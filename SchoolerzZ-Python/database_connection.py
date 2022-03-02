import mysql.connector
import persona, colegio

class SchoolerzDatabase:
    host = '172.16.51.7'
    port = '3306'
    username = 'alvaro'
    password = '1234'
    database = 'schoolerzz'
    miConexion = None
    cursor = None

    def CreateConnection(self):
        try:
            self.miConexion = mysql.connector.connect(host = self.host , user = self.username, passwd = self.password, db = self.database, port = self.port)
            self.cursor = self.miConexion.cursor()
        except Exception as ex:
            print('Fallo de conexión.')

    def ExecuteProcedure(self, procedure):
        self.CreateConnection(self)
        self.cursor.execute(procedure)
        self.cursor.execute("SELECT @out;")
        return self.cursor.fetchone()[0]

    def Login(self, usertype, user, password) -> bool:
        query = f"CALL `pa_LoginAJ`('{usertype}','{user}','{password}',@out);"
        if self.ExecuteProcedure(self, query) == 0:
            return True
        return False

    def CreateNewStudent(self, nombre, ape1, ape2, nacimiento, nacionalidad, pais, ciudad, postCode, direc, email, password) -> bool:

        query = f"CALL `pa_AddStudent`('{nombre}','{nombre}','{ape1}','{ape2}','{nacimiento}','{nacionalidad}','{pais}','{ciudad}','{postCode}','{direc}','{email}','{password}');"
        if self.ExecuteProcedure(self, query) == 0:
            return True
        return False


    def GetManagerData(self, nick):
        ManagerData = []
        query = f"SELECT * FROM SZ_007_SCHOOL_MANAGERS WHERE SZ_007_NICK LIKE '{nick}';"
        self.CreateConnection(self)
        self.cursor.execute(query)
        for data in self.cursor.fetchone():
            ManagerData.append(data)
        manager = persona.Persona(ManagerData[1], ManagerData[2], ManagerData[3], ManagerData[4], ManagerData[5], ManagerData[6], ManagerData[7], ManagerData[8], ManagerData[9], ManagerData[10], ManagerData[11], ManagerData[12])
        return ManagerData

    def GetSchoolData(self, name):
        SchoolData = []
        query = f"SELECT * FROM SZ_006_SCHOOLS WHERE SZ_006_NAME LIKE '{name}';"
        self.CreateConnection(self)
        self.cursor.execute(query)
        for data in self.cursor.fetchone():
            SchoolData.append(data)
        School = colegio.School(SchoolData[1], SchoolData[2], SchoolData[3], SchoolData[4], SchoolData[5], SchoolData[6], SchoolData[7])
        return School