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
            while _type not in ["cat", "dog"]:
                print('======= Oops, type dog or cat =======')
                _type = input()
                if _type == "dog" or _type == "cat":
                    self.printPetProfile()
                    return True

    def printPetProfile(self):
        print(str(self.petProfile))

class Menu():
    def __init__(self):
        self.show()

    def show(self):
        print('============ Welcome to the Shelter Dashboard ============' "\n"
              '1) Show pets' "\n"
              '2) Create a new pet' "\n")
        self.exec()

    def exec(self):
        menu_option = input()
        if menu_option == "1":
            print('show pets')
        elif menu_option == "2":
            # name = input("Type the name of the pet" "\n")
            # age = input("Type the age" "\n")
            # pet_type = input("Type the type" "\n")
            # newPet = Pet(name, age, pet_type)
            newPet = Pet('rhuan', '10', 'fsafas')
        else:
            while menu_option not in ["1", "2"]:
                print('this is not a valid option, please choose 1 or 2')
                menuoption = input()
                return True