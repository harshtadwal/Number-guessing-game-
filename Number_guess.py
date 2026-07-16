import random

random_num = random.randint(0,100)
user_attempt = 5

print("Welcome to Number Guessing Game!\nYou have 5 attempts.")
while user_attempt>0:

    guess_num = int(input("Guess the number between 0 and 100: "))

    if guess_num == random_num:
        print("Congratulations, You won the Game!!")
        break
    
    elif guess_num>random_num:
        user_attempt-=1
        print("Too high!\nAttempts left:", user_attempt)
    elif guess_num<random_num:
        user_attempt-=1
        print("Too low!\nAttempts left:", user_attempt)
     
     
if user_attempt==0:
    print("Game Over!")
    print("The correct number is: ",random_num)
    print("Better luck next time!")
