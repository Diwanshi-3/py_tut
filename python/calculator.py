print("CALCULATOR")
print("****MAIN MENU****")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Modulus")
print("6.Floor Division")
a=int(input("Enter a number1:"))
b=int(input("Enter a number2:"))
choice=int(input("Enter your choice:"))
match choice:
    case 1:
        print("Addition of ",a,"and",b,"is",a+b)
    case 2:
         print("Subtraction of ",a,"and",b,"is",a-b)
    case 3:
        print("Multiplication of ",a,"and",b,"is",a*b)
    case 4:
        if b!=0:
         print("Division of ",a,"and",b,"is",a/b)
        else:
            print("Error!")
    case 5:
        if b!=0:
          print("Modulus of ",a,"and",b,"is",a%b)
        else:
            print("Error!")
    case 6:
        if b!=0:
         print("Floor Division of ",a,"and",b,"is",a//b)
        else:
           print("Error!")
    case _:
        print("Invalid choice!!")
    


        


