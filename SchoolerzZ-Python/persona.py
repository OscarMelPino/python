class Persona:

    def __init__(self, name, sn1, sn2, birth, nationality, country, city, postalcode, address, email, nick, password) -> None:
        self.Name = name
        self.Sn1 = sn1
        self.Sn2 = sn2
        self.Birth = birth
        self.Nationality = nationality
        self.Country = country
        self.City = city
        self.PostalCode = postalcode
        self.Address = address
        self.Email = email
        self.Nick = nick
        self.Password = password
        pass


    # SETTERS
    def SetName(self, value):
        self.Name = value
    def SetFirstSurname(self, value):
        self.Sn1 = value
    def SetSecondSurname(self, value):
        self.Sn2 = value
    def SetBirthDate(self, value):
        self.Birth = value
    def SetNationality(self, value):
        self.Nationality = value
    def SetCountry(self, value):
        self.Country = value
    def SetCity(self, value):
        self.City = value
    def SetPostalCode(self, value):
        self.PostalCode = value
    def SetAddress(self, value):
        self.Address = value
    def SetNick(self, value):
        self.Nick = value
    def SetPassword(self, value):
        self.Password = value

    # GETTERS
    def GetName(self):
        return self.Name
    def GetFirstSurname(self):
        return self.Sn1
    def GetSecondSurname(self):
        return self.Sn2
    def GetBirthDate(self):
        return self.Birth
    def GetNationality(self):
        return self.Nationality
    def GetCountry(self):
        return self.Country
    def GetCity(self):
        return self.City
    def GetPostalCode(self):
        return self.PostalCode
    def GetAddress(self):
        return self.Address
    def GetNick(self):
        return self.Nick
    def GetPassword(self):
        return self.Password