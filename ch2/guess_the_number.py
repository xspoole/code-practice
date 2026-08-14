import random

secret_number = random.randint(1,20)
print('I am thinking of a number between 1 and 20.')

for guesses_taken in range(1,7): # I think this means I can only make 7 guesses
    print('Make a guess.')
    guess = int(input())

    if guess < secret_number:
        print('Your guess is too low.')
    elif guess > secret_number:
        print('Your guess is too high.')
    else:
        break # this is the correct guess for the number!

if guess == secret_number:
    print('You guessed the number in ' + str(guesses_taken) + ' guesses!')
else:
    print('The number I was thinking of was ' + str(secret_number))
          