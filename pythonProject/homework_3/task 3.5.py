from random import randint

player = input('камень (к), ножници (н), бумага (б): ')
print(player, 'против', end=' ')
chosen = randint(1,3)

if chosen == 1:
    computer = 'к'
elif chosen == 2:
    computer = 'н'
else:
    computer = 'б'
print(computer)

if player == computer:
    print()
elif player == 'к' and computer == 'н':
    print('Победил игрок')
elif player == 'к' and computer == 'б':
    print('Победил компьютер')
elif player == 'н' and computer == 'б':
    print('Победил игрок')
elif player == 'н' and computer == 'к':
    print('Победил компьютер')
elif player == 'б' and computer == 'к':
    print('Победил игрок')
elif player == 'б' and computer == 'н':
    print('Победил компьютер')


