import random

generated_num = random.randint(1,50)

while True:
    try:
        user_input = int(input("Guess the number (1 to 50) :"))
        if generated_num > user_input:   
            print ("Number guessed is less than actual number")
        elif generated_num < user_input:
            print ("Number guessed is more than actual number")
        elif user_input > 50:
            print ("The number is between 1 - 50 only")
        else:
            print ("Woah !! Correct")
            break
    except ValueError:
        print("Please enter a valid number")
