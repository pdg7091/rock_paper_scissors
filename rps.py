import random

while(True):
    player_one = input('Please enter rock(r), paper(p) or scissors(s): ')
    player_two = random.randint(1, 3)

    if player_two == 1:
        player_two = 'r'
    if player_two == 2:
        player_two = 'p'
    if player_two == 3:
        player_two = 's'

    print()

    print(f'Your choice: {player_one}\n')
    print(f'Computer\'s choice: {player_two}\n')

    if (player_one == player_two):
        print('It\'s a tie!')
    elif player_one == 'r':
        if player_two == 's':
            print('Player one wins! Rock blunts Scissors!')
        else:
            print('Player two wins!')

    elif player_one == 'p':
        if player_two == 'r':
            print('Player one wins! Paper covers Rock!')
        else:
            print('Player two wins!')

    elif player_one == 's':
        if player_two == 'p':
            print('Player one wins! Scissors cut Paper!')
        else:
            print('Player two wins!')

    print()

    print('Would you like to play again? (Y?N)\n')
    answer = input()

    if answer == 'n' or answer == 'N':
        break
