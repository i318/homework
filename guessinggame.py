import random






def User_guess():
    def guess(x):
        random_number = random.randint(1,x)
        guess = 0 
        while guess != random_number:
            guess = int(input(f'Try to find the number by guessing a number between 1 and {x}:   '))
            if guess < random_number:
                print("Sorry, guess again. Too low buddy.")
            elif guess > random_number:
                print("'Sorry, guess is too high there buddy.")
        print(f'Yay, you guessed {random_number}')
    guess(100)

def computer1():
    def terminal_guess(x):
        lowestno = 1
        highestno = x
        storage1 = ''
        while storage1 != 'c':
            if lowestno != highestno:
                guess = random.randint(lowestno,highestno)
            else:
                guess = lowestno
            storage1 = input(f"Would you say {guess} is too high 'H', low 'L', or correct 'C'").lower()
            if storage1 == 'h':
                highestno = guess - 1
            elif storage1 == 'l':
                lowestno = guess + 1
        print(f"Woohoo, your number {guess} was guessed.")
    terminal_guess(100)


gametype = input("Which game would you like to play? Computer or User? ")

if gametype == "Computer":
    computer1()
elif gametype == "User":
    User_guess()
else:
    print("Invalid")