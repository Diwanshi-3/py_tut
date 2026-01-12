#Lambda functions are anonymous functions
#Lambda function describes whole function as a single expression 
#for example you write function for get sum it write as :
# def sum(x,y):
#   return x+y
# print(sum(5,6))
sum=lambda x,y:x+y   #Lambda function expression your function in single expression
print(sum(3,5))
square=lambda x:x*x
print(square(5))
cube=lambda y:y*y*y
print (cube(9))
sum=lambda x,y:x+y
print(sum(3,5))
average=lambda x,y,z:(x+y+z)/2   #It can also take multiple arguments 
print(average(4,5,6))

#Mainly Lambda function used when function passed as an argument
def apply(fx,value):
     return value+fx(value)
print(apply(cube,6))  #Here cube is a function passed as an argument 
print(apply(lambda x:x*x*x,6))  #You can use lambda function as this also 
