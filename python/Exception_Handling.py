try:
    a=int(input("Enter a number1:"))
    b=int(input("Enter a number2:"))
    print(a/b) 
except ValueError:
    print("Invalid Input")
except ZeroDivisionError:
    print("Division by zero is not defined")
except Exception as e:
    print("Unexpected Error:",e)
else:
    print("I am only executed if exception not occur")
finally:
    print("I am always executed")

# We can also raise a custom errors
n=int(input("Enter a number between 5 and 9"))
if n<5 or n>9:
    raise ValueError("Invalid Input!!")

#Create a CustomeException in Python
class NegativeNumberError(Exception):
    '''Raised when a negative number is occur'''
    pass
try:
    n=int(input("Enter an integer"))
    if n<0:
        raise NegativeNumberError("Error! Number should be positive")
    else:
        print(n)
except NegativeNumberError as e:
    print(e)
except ValueError as e:
    print(e)