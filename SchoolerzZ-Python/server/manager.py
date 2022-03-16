import persona

class Manager(persona.Persona):
    def __init__(self, telep1, telep2, colegio) -> None:
        super().__init__()
        self.Telefono1 = telep1
        self.Telefono2 = telep2
        self.Colegio = colegio.name

    # SETTERS
    def SetTelefonoUno(self, value):
        self.Telefono1 = value
    def SetTelefonoDos(self, value):
        self.Telefono2 = value
    def SetColegio(self, value):
        self.Colegio = value
    
    # GETTERS
    def GetTelefonoUno(self):
        return self.Telefono1
    def GetTelefonoDos(self):
        return self.Telefono2
    def GetColegio(self):
        return self.Colegio