class Animal:
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return "Woof!"
class Cat(Animal):
    def speak(self):
        return "Meow!"
    
def animal_sound(animal):
    return animal.speak()

my_dog = Dog()
my_cat = Cat()

print(animal_sound(my_dog))
print(animal_sound(my_cat))

#speak method is overwritten by both the dog and cat class