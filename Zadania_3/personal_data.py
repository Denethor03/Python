import json

class dataclass:
    def __init__(self,name=None,surname=None,address=None,postalCode=None,pesel=None):
        self.name = name
        self.surname = surname
        self.address = address
        self.postalCode = postalCode
        self.pesel = pesel

    def __str__(self):
        return ("Name: "+ self.name+"\nSurname: "+ self.surname +
        "\nAddress: "+self.address+"\nPostal code: "+self.postalCode+
        "\nPesel: "+self.pesel)
    def write_Json(self):
        with open("personalData",'w') as f:
            json.dump(self.__dict__,f)
    def read_Json(self,file):
        with open(file,'r') as f:
            data = json.load(f)
        self.__dict__.update(data)

if __name__ == "__main__":
    person1 = dataclass()
    person1.read_Json("personalData")
    print(person1)
