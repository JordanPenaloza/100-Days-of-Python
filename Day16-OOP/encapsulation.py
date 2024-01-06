class Car:
    def __init__(self, make, model):
        self.__make = make  # Encapsulated attribute
        self.__model = model  # Encapsulated attribute

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model
    
car1 = Car(make="Toyota", model="Corolla")
car2 = Car(make="Toyota", model="Prius")
print(car1.get_make())

#make and model controlled by getter methods
