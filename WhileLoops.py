### Part Two -- your code goes here. 
import random

def main():
    #gets random number
    random_number = random.randint(1,100)
    print ('Guess number between 1 and 100.')
    #iterates and checks guess until correct
    while True:
        if check_guess(random_number, input('Enter guess >')) == True:
            break
    ()

def check_guess(correct, guess):
    #checks to see if valid input and compares guess to correct number
    try:
        guess = int(guess)
        if guess < correct:
            print ('Too low.')
        elif guess > correct:
            print ('Too high.')
        else:
            print ('Correct guess!')
            return True
    except ValueError:
        print ('Invalid input.')

main()