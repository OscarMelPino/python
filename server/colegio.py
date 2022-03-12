class School:
    def __init__(self, nombre, codigo, letras, pais, ciudad, postal, direccion) -> None:
        self.name = nombre
        self.schoolCode = codigo
        self.words3 = letras
        self.country = pais
        self.city = ciudad
        self.postalCode = postal
        self.address = direccion

    # GETTERS
    def GetName(self):
        return self.name
    def GetSchoolCode(self):
        return self.schoolCode
    def GetWords3(self):
        return self.words3
    def GetCountry(self):
        return self.country
    def GetCity(self):
        return self.city
    def GetPostalCode(self):
        return self.postalCode
    def GetAddress(self):
        return self.address

    #SETTERS
    def SetName(self, value):
        self.name = value
    def SetSchoolCode(self, value):
        self.schoolCode = value
    def SetWords3(self, value):
        self.words3 = value
    def SetCountry(self, value):
        self.country = value
    def SetCity(self, value):
        self.city = value
    def SetPostalCode(self, value):
        self.postalCode = value
    def SetAddress(self, value):
        self.address = value