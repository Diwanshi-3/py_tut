# Arithmetic Operators
a = 10
b = 5
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
print("Floor Division:", a//b)
# Comparision operators
print("Is number a equal to number b?",a==b)
print("Is number a not equal to number b?",a!=b)
print("Is number a greater than equal to number b?",a>=b)
print("Is number a less than equal to number b?",a<=b)
#Logical operators
print(a>b and b<a)
print(a>b or b<a)
print(not a>b)
#Assignment operators
a+=5
a-=3
a/=3
a*=4
a//=5
a%=8
a*=5
print(a)
#Membership operators
nums=[1,2,3,4,5,6]
print(3 in nums)
print(67 not in nums)
#Identity operators(compare the memory object not values )
a=10
b=10
print(a is b) #Output is true due to Integer caching
a=1000
b=1000
print(a is b)
print(a is not b)





