import random
count=0
points=0
while True:
    options=['Snake','Water','Gun']
    def computer():
        return (random.choice(options))
    computer_choice=computer()
    user_choice=input("Enter your choice (Snake/Water/Gun) : ").capitalize()
    print("Computer choice is " +computer_choice)
    if user_choice==computer_choice:
        print("Draw")
    elif(user_choice=='Gun' and computer_choice=='Snake') or \
        (user_choice=='Snake' and computer_choice=='Water') or\
        (user_choice=='Water' and computer_choice=='Gun'):
        print("User Wins")
        count=count+1
        print("User has ",count,"points")
    elif(user_choice=='Water' and computer_choice=='Snake') or \
        (user_choice=='Gun' and computer_choice=='Water') or \
        (user_choice=='Snake' and computer_choice=='Gun'):
        print("Computer Wins")
        points=points+1
        print("Computer has ",points," points")
    else:
        print("Invalid Input")
    choice=input(("\nDo you want to play again (y/n) : ")).lower()
    if choice=='y':
        continue
    else:
        if count==points:
            print("****Game draw****")
        elif count>points:
            print("*****Overall game is win by User****")
        else:
            print("****Overall game is win by computer****")
        break

