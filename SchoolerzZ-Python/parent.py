import persona

class Parent(persona.Persona):
    def __init__(self, telep1, telep2) -> None:
        super().__init__()
        self.Telefono1 = telep1
        self.Telefono2 = telep2

    # SETTERS
    def SetTelefonoUno(self, value):
        self.Telefono1 = value
    def SetTelefonoDos(self, value):
        self.Telefono2 = value
    
    # GETTERS
    def GetTelefonoUno(self):
        return self.Telefono1
    def GetTelefonoDos(self):
        return self.Telefono2