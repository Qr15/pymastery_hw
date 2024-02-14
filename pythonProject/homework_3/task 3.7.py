from random import randint

win_numbers = []

for chosen in range(7):
    chosen = randint(0, 9)
    win_numbers.append(chosen)

print(win_numbers)