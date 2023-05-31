import random
print('what is your name?')
name = input()
secretNumber = random.randint(1, 20)
print('Alright ' + name + ' Can you guess the number I am thinking about')

for guessesTaken in range(1, 7):
    print('Take a guess')
    guess = int(input())
    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print(' Your guess is too high')
    else:
        break

if guess == secretNumber:
    print('Well done ' + name)
else:
    print('Nope, the number i was thinking was ' + str(secretNumber))

print('It took you ' + str(guessesTaken))