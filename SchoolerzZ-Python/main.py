from subprocess import REALTIME_PRIORITY_CLASS
import database_connection

# VARIABLES
MyDB = database_connection.SchoolerzDatabase
userType = ''
user = ''
usuario = ''
def Welcome():
    print("*******************************")
    print("***      MENU PRINCIPAL     ***")
    print("*******************************")
    print("*** 1. ENTRAR               ***")
    print("*** 2. VOLVER AL INICIO     ***")
    print("*******************************")
    WelcomeActions(SelectOption(2))

def SelectOption(max) -> int:
    valid = False
    while not valid:
        try:
            option = int(input("Elige una opción.\n> "))
            if option > 0 and option < max + 1:
                return option
        except:
            print("Eso no es un número, bobo.")

def MainLogin() -> bool:
    global user
    user = input("Introduce tu nombre de usuario.\n> ")
    password = input("Introduce tu contraseña.\n> ")
    return MyDB.Login(MyDB, userType, user, password)

def WelcomeActions(cosa):
    global usuario
    if cosa == 1:
        if not MainLogin():
            print("Datos incorrectos.")
            Welcome()
        usuario = userType + user #Concatenamos el tipo de usuario con el nick
        if userType == 'M':
            ManagerActionsMenu()
        # Login valido, hacer cosas de después
    if cosa == 2:
        UserType()
        print("Nos vemos pronto.")
        exit

def ManagerActionsMenu():
    print("*******************************")
    print("*** ¿QUE QUIERES HACER?     ***")
    print("*** 1. REGISTRAR            ***")
    print("*** 2. MODIFICAR            ***")
    print("*** 3. BORRAR               ***")
    print("*** 4. SALIR                ***")
    print("*******************************")
    manageraction = SelectOption(4)
    if manageraction == 4: userType()
    print("*** ¿SOBRE QUIÉN?           ***")
    print("*** 1. ESTUDIANTE           ***")
    print("*** 2. DOCENTE              ***")
    print("*** 3. TUTOR                ***")
    print("*** 4. ADMINISTRADOR/A      ***")
    print("*** 5. SALIR                ***")
    target = SelectOption(5)
    if target == 5: userType()
    ManagerActions(manageraction, target)

def ManagerActions(action, targetType):
    if action == 1: Registrar(targetType)
    if action == 2: Modificar(targetType)
    if action == 3: Borrar(targetType)

def Registrar(targetType):
    if targetType == 1: RegistrarEstudiante()
    if targetType == 2: RegistrarDocente()
    if targetType == 3: RegistrarTutor()
    if targetType == 4: 
        print("No se puede registrar otro administrador de esta manera.")
        return
    

def RegistrarEstudiante():
    nombre = input("Introduce un nombre.\n> ")
    ape1 = input("Introduce primero apellido.\n> ")
    ape2 = input("Introduce segundo apellido.\n> ")
    nacimiento = input("Introduce fecha de nacimiento.\n> ")
    nacionalidad = input("Introduce nacionalidad.\n> ")
    pais = input("Introduce país de residencia.\n> ")
    ciudad = input("Introduce ciudad de residencia.\n> ")
    postCode = input("Introduce código postal.\n> ")
    direc = input("Introduce dirección.\n> ")
    email = input("Introduce dirección de correo electrónico.\n> ")
    password = input("Introduce una contraseña.\n> ")
    # MyDB.CreateNewStudent( más todo lo de arriba)
    if not MyDB.CreateNewStudent(MyDB, usuario, nombre, ape1, ape2, nacimiento, nacionalidad, pais, ciudad, postCode, direc, email, password, '', '', ''):
        print("Algo ha fallado, revise los datos.")
        ManagerActionsMenu()
        return
    print("Estudiante registrado con éxito.")
    ManagerActionsMenu()

        
def RegistrarDocente():
    pass

def RegistrarTutor():
    pass

def Modificar(targetType):
    if targetType == 1: ModificarEstudiante()
    if targetType == 2: ModificarDocente()
    if targetType == 3: ModificarTutor()
    if targetType == 4: ModificarAdministrador()

def ModificarEstudiante():
    pass

def ModificarDocente():
    pass

def ModificarTutor():
    pass

def ModificarAdministrador():
    pass

def Borrar(targetType):
    if targetType == 1: BorrarEstudiante()
    if targetType == 2: BorrarDocente()
    if targetType == 3: BorrarTutor()
    if targetType == 4: BorrarAdministrador()

def BorrarEstudiante():
    pass

def BorrarDocente():
    pass

def BorrarTutor():
    pass

def BorrarAdministrador():
    pass

def UserType():
    global userType
    print("*******************************")
    print("*** BIENVENIDO A SCHOOLERZZ ***")
    print("*******************************")
    print("*** ¿QUIÉN ERES?            ***")
    print("*** 1. ESTUDIANTE           ***")
    print("*** 2. DOCENTE              ***")
    print("*** 3. TUTOR                ***")
    print("*** 4. ADMINISTRADOR/A      ***")
    print("*** 5. SALIR                ***")
    print("*******************************")
    useroption = SelectOption(5)
    if useroption == 1: userType = 'S'
    if useroption == 2: userType = 'T'
    if useroption == 3: userType = 'P'
    if useroption == 4: userType = 'M'
    if useroption == 5: exit()
    Welcome()

# MAIN
if __name__ == "__main__":
    UserType()
