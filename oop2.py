import random


class Toys:

    def __init__(self, toy1, toy2, toy3):
        self.toy1 = toy1
        self.toy2 = toy2
        self.toy3 = toy3

    def choose_toy(self):
        all_toys = [self.toy1, self.toy2, self.toy3]
        print("No. Baby wants to play {}".format(random.choice(all_toys)))


class Sleep:

    def __init__(self):
        self.answers = ["Yes", "No"]
        self.answer = str

    def choose_answer(self):
        self.answer = random.choice(self.answers)
        if self.answer == "No":
            toys = Toys("Car", "Chew", "Squeeze")
            toys.choose_toy()
        if self.answer == "Yes":
            print("Yes. Baby wants to sleep! Good bye")


class Game:

    def start(self):
        print("Do you want to sleep?")
        sleep = Sleep()
        sleep.choose_answer()


if __name__ == "__main__":
    game = Game()
    game.start()
