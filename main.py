import random


class NumberGame:

    def __init__(self, minimum=0, maximum=100):
        self.attemptlist = []
        self.running = True
        self.number = random.randint(int(minimum), int(maximum))
        self.minimum = int(minimum)
        self.maximum = int(maximum)

    def guesshiddennumber(self, number):
        if self.number == int(number):
            print("Вы угадали загаданное число!")
            print("История ваших попыток:", self.attemptlist)
            self.running = False

        else:
            self.attemptlist.append(int(number))
            if int(number) > self.number:
                print("Введённое число больше загаданного")
            else:
                print("Введённое число меньше загаданного")


print("Игра: Угадай загаданное число")
minval = input("Введите минимум: ")
maxval = input("Введите максимум: ")

game = NumberGame(minval, maxval)

print("Игра: угадайте число от ", game.minimum, " до ", game.maximum)

while game.running:
    print("Введите предполагаемое число: ")
    value = input()
    game.guesshiddennumber(value)
