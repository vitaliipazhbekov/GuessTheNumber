import random

random.randrange(0, 100)
number = random.randrange(0, 100)
Running = True

while Running:
    guess = int(input('Введите целое число, без дробей, пи'))

    if guess == number:
        print('Ты угадал!')
        Running = False

    elif number > guess:
        print('Загаданное число больше того, что вы ввели')
    else:
        print('Загаданное число меньше того, что вы ввели')


print('Game Over. Хотите еще?')