class Shelter:
    def __init__(self):
        self.shelterId = '0'
        self.shelterLocation = 'Orlando-Fl'

class Pet(Shelter):
    def __init__(self, _name, _age, _type):
        super().__init__()
        self.name = _name
        self.age = _age
        self.type = _type
        self.validation(self.type)
        self.petProfile = [_name, _age, _type, self.shelterLocation]

    def validation(self, _type):
        if _type == "dog" or _type == "cat":
            print('everything looks fine')
        else:
            while _type is not "dog" or _type is not "cat":
                print('======= Oops, type dog or cat =======')
                _type = input()
                if _type == "dog" or _type == "cat":
                    self.printPetProfile()
                    return True

    def printPetProfile(self):
        print()




# Create a new pet
# name = input("Type the name of the pet")
# age = input("Type the age")
# petType = input("Type the type")
# newPet = Pet(name, age, petType)


newPet = Pet('rhuan', '10', 'fas')

#
# print(newPet.validation())
