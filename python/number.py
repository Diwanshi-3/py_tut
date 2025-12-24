while True:
    print("1.To check whether a number is positive,Negative or Zero")
    print("2.To check whether a number is even or odd")
    choice=int(input("Enter your choice:"))
    match choice:
        case 1:
            n=int(input("Enter the number:"))
            if n<0:
                print(n,"is negative number")
            elif n>0:
                print(n,"is positive number")
            else:
                print("number is zero")
        case 2:
            n=int(input("Enter the number:"))
            if n%2==0:
                print(n,"is even number")
            else:
                print(n,"is odd number")
    user_choice=input("Do you want to continue?")
    if user_choice=='yes' or user_choice=='Yes':
        continue
    else:
        print("Exit!!")
        break