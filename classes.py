# Object-oriented programming (OOP)

# OOP is about making the code more readable.
# Everything in OOP is an object. And objects are modeled against real world objects
# Attributes ( things about it's state, variables)
# Behaviours (methods)

# Classes are the templates we use to create objects.
# Classes are a way of bringing both data and functionality of our code together.
# Functions inside the class is called a method.
#Create a class (template)
# Don't use underscores, each word needs to be capitalised
class Dog:

    animal_kind = "Canine" # class variable (Attributes)
    animal_kind2 = "Octopus"

    def bark(self): # method (Behaviour)
        return "woof"

# self - I'm referring to the current class.

# print(Dog.animal_kind)
#print(Dog.bark())
# Objects need to be made
# Instantiation creating or making object from a class

fido = Dog()
lasie = Dog()

# print(type(fido)) #  The output: <class '__main__.Dog'>
# print(type(lasie)) # The output: <class '__main__.Dog'>
print(fido.animal_kind)  # The output: Canine
print(lasie.animal_kind) # The output: Canine
# print(fido.bark()) #The output: woof

Dog.animal_kind = "Dolphin" # We can overwrite the template as well to change's attributes of objects
# fido.animal_kind = "Big dog" # We can change the variable for certain objects
print(fido.animal_kind) # Big dog  # Output for fido
print(lasie.animal_kind) # the output for lasie :Canine
print(lasie.animal_kind2) #  This is the output when we add a variable: Octopus




