class utilities:
    def __init__(self):

        def avg(self):
            return 'this is your avg'

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

        print('from print profile')

class Menu():
    def __init__(self):
        self.show()

    def show(self):
        print('============ Welcome to the Shelter Dashboard ============' "\n"
              '1) Show pets' "\n"
              '2) Create a new pet' "\n")
        self.exec()

    def exec(self):
        menuoption = input()
        if menuoption == "1":
            print('show pets')
        elif menuoption == "2":
            print('option 2')
        else:
            while menuoption not in ["1", "2"]:
                print('this is not a valid option')
                menuoption = input()
        return True


def main():
    menu = Menu()

if __name__ == "__main__": main()




# Create a new pet
# name = input("Type the name of the pet")
# age = input("Type the age")
# petType = input("Type the type")
# newPet = Pet(name, age, petType)


# newPet = Pet('rhuan', '10', 'cat')

#
# print(newPet.validation())
