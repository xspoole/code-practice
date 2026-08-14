import random, sys

print('ROCK, PAPER, SCISSORS')

wins = 0
losses = 0
ties = 0

while True: # main loop for the game
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties)) # the % thing keeps the number of wins, losses, and ties updated
    while True: # this is what the player will input
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        player_move = input()
        if player_move == 'q':
            sys.exit()
        if player_move == 'r' or player_move == 'p' or player_move == 's': # I can use or in if statements to define multiple inputs at once
            break # leaves the player input loop
        print('Type one of r, p, s, or q')

    # display the player's choice, which was defined in above while loop
    if player_move == 'r':
        print('ROCK versus...')
    elif player_move == 'p':
        print('PAPER versus...')
    elif player_move == 's':
        print('SCISSORS versus...')

    # display what computer chose
    random_number = random.randint(1,3) # 3 choices for rps
    if random_number == 1:
        computer_move = 'r'
        print('ROCK')
    elif random_number == 2:
        computer_move = 'p'
        print('PAPER')
    elif random_number == 3:
        computer_move = 's'
        print('SCISSORS') # it seems like else isn't always needed in if statement

    # define what actually happens in the game
    if player_move == computer_move:
        print('It is a tie!')
        ties = ties + 1 # update number of ties
    elif player_move == 'r' and computer_move == 's':
        print('You win!')
        wins = wins + 1
    elif player_move == 'p' and computer_move == 'r':
        print('You win!')
        wins = wins + 1
    elif player_move == 's' and computer_move == 'p':
        print('You win!')
        wins = wins + 1
    else: # yay I made this program better than the book
        print('You lose!')
        losses = losses + 1
