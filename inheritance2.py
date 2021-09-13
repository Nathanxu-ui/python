class Dog:

    def food_dog(self):
        print("dog eat")


class Cat(Dog):

    def food_cat(self):
        print("cat eat")

    def food_cat2(self):
        super().food_dog()


cat = Cat()
cat.food_cat2()

cat = Dog()
cat.food_dog()