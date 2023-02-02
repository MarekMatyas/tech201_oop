# Initialisation
#
# Initialisation ->  Relates to setting a particular data for an instance of a class.
# Instantiation -> the creation of an instance of an object.

class Dog:

    def __init__(self, name, colour):
        self.animal_kind = "canine"
        self.name = name
        self.colour = colour
        self.bark()

    def bark(self): ##Method
        return "woof"

# __innit__ (Initialize)

fido = Dog("Fido", "Brown")
print(fido.colour)  #Brown
print(fido.name) #Fido
#  Initializing a class with class variables is good practice. It is possible to set variables
