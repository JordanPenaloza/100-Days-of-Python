class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("moving in water")

nemo = Fish()
nemo.swim()
nemo.breathe()

#the fish class can inherit features of the animal class since it is also an animal
#the fish can breathe even though the breath method isn't specifically in it's class
