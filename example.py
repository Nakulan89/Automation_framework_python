# parent class
class Bird:

    def __init__(self):
        print("Bird is ready")

    def whoisthis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")


#child class
class Penguin(Bird):

    def __init__(self):
        # call super() function
        super().__init__()
        print("Penguin is ready")

    def whoisthis(self):
        super().whoisthis()
        print("Penguin")

    def run(self):
        super().swim()
        print("Run faster")


peggy = Penguin()
peggy.swim()
