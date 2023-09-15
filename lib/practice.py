class Human:
    species = "Homo sapiens"

    def __init__(self, name):
        self.name = name
        self._age = 0 # private member of the class

    def get_age(self):
        print("Retrieving age")
        return self._age

    def set_age(self, age):
        if (type(age) in (int, float)) and (0 <=age <= 120):
            print(f"Setting age to {age}")
            self._age = age
        else:
            print("Age must be a number between 0 and 120")

    age = property(get_age, set_age)

joel = Human("joel")
print(joel.age)

joel.age = False

joel.age = 24
print(joel.age)

# print(joel.species)
# print(joel.name)


# # Changing species using dot notation
# joel.species = "Python programmer"
# joel.name = "Guido van Rossum"

# print(joel.species)
# print(joel.name)

# # Adding new attributes using dot notation
# joel.nationality = "Kenyan"
# print(joel.nationality)


# # inbuilt functions to manipulat attributes include:
# # getattr()
# # setattr()
# # hasattr()
# # delattr()

# # An example 
# print(getattr(joel, "name"))

# setattr(joel, "nationality", "African")
# print(getattr(joel, "nationality"))