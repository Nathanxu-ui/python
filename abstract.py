from abc import abstractmethod


class People:
    @abstractmethod
    def drive(self):
        print("People can walk")

    def fly(self):
        print("People can fly")


class Place(People):
    def drive(self):
        print("People can drive")


place = Place()
place.drive()
place.fly()

people = People()
people.drive()

print(issubclass(Place, People))
print(isinstance(Place(), People))


