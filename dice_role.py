import random

count = 0
while True :
    ans = input("Do you want to play ? (Y/N)")
    if (ans=="Y" or ans == "y"):
        print("Playing")
        d1 = random.randint(1,2)
        d2 = random.randint(2,3)
        print(f'({d1},{d2})')
        count = count + 1
    elif (ans=="N" or ans =="n"):
        print ("Quit. Thankyou for playing !")
        print (f'Dice rolled till date : {count}')
        break
    else:
        print ("Invalid choice")
