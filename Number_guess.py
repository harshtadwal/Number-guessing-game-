low = 0
high = 50

random_num = int(input("Enter the random number b/w 0 and 50: "))

if random_num<0 or random_num>50:
    print("Invalid number!")
    random_num = int(input("Enter again: "))


print("Number Guessing Game! \nYou have five attempts!")  

guess_num = int(input("Ist attempt \nGuess the number: "))

if guess_num == random_num:
    print("Congrats!! you guess the correct number!")  
else:
    print("Wrong number!")
    guess_num = int(input("2nd attempt \nGuess the number: "))
    
    if guess_num==random_num:
        print("Congrats!! you guess the correct number!")  
    else:
        print("Wrong number!")
        guess_num = int(input("3rt attempt \nGuess the number again: "))
        if guess_num==random_num:
            print("Congrats!! you guess the correct number!")   
        else:
            print("Wrong number!")
            guess_num = int(input("4th attempt \nGuess the number again: "))
            if guess_num==random_num:
                print("Congrats!! you guess the correct number!")  
            else:
                print("Wrong number!")
                guess_num = int(input("Last attempt \nGuess the number again: "))
                if guess_num==random_num:
                    print("Congrats!! you guess the correct number!")   
                else:
                    print("You lost!")