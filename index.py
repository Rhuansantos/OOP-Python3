class Shelter:
    def __init__(self):
        self.shelterId = 0
        self.shelterLocation = 'Orlando-Fl'
        return Shelter


class Pet(Shelter):
    def __init__(self, _name, _age, _type):
        self.name = _name
        self.age = _age
        self.type = _type
        Pet.validation(_type)

    def validation(self):
        #if self.age == "dog"
        yield 'hello pet'


# Create a new pet
# name = input("Type the name of the pet")
# age = input("Type the age")
# age = input("Type the type")

newPet = Pet('rhuan', '10', 'dog')
print(newPet)

a = Pet.validation

print(a)