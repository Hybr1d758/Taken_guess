import random
print("Hey!")
print('What is your name?')
name = input()
secretNumber = random.randint(1, 20)
print('Alright ' + name + ' Can you guess the number I am thinking about')

def generate_three_number_hint():
    hints = [secretNumber]
    hints.append(7,17)
    return hints

for guessesTaken in range(1, 7):
    print('Take a guess')
    guess = int(input())
    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break

if (guess % 2) == 0:
    print("The answer is even")
else:
    print("The answer is odd")


if guess == secretNumber:
    print('Well done ' + name)
else:
    print('Nope, the number i was thinking was ' + str(secretNumber))

print('It took you ' + str(guessesTaken))
print('thank you' + name)