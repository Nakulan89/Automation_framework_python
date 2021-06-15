class Parrot:
    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now dancing".format(self.name)


# instantiate the parrot class
blu = Parrot("Blu", 10)


# call our instance methods
print(blu.sing("Happy"))
print(blu.dance())
