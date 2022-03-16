import persona

class Student(persona.Persona):
    def __init__(self, medical, observations) -> None:
        super().__init__()
        self.Medical = medical
        self.Observations = observations

    # SETTERS
    def SetMedical(self, value):
        self.Medical = value
    def SetObservations(self, value):
        self.Observations = value
    
    # GETTERS
    def GetMedical(self):
        return self.Medical
    def GetObservations(self):
        return self.Observations