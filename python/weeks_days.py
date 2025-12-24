while True:
    print("DAYS OF THE WEEK")
    choice=int(input("Enter the day you want to print:"))
    match choice:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
        case _:
            print("Invalid choice!!")
    user_choice=input("Do you want to continue?")
    if user_choice=='yes' or user_choice=='Yes':
        continue
    else:
        print("Exit...")
        break


