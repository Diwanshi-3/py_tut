#MAP 
l=[1,2,3,4,5,6,7,8,9,10]
#suppose you have to return a new list which cotains cube of the list l
'''
def cube(x):
    return x*x*x
new=[]
for i in l:
    new.append(cube(i))
print(new)
'''
#But using map function you do this all in one line
#new=map(cube,l)
#print(list(new))
#You can also use lambda function to make it more shorter 
new=map(lambda x:x*x*x,l)
print(list(new))
#you can use this map function with tuple also
t=(1,2,3,4,5,6,7,8,9,10)
new=map(lambda x:x*x*x,t)
print(tuple(new))
#We can also input a new tuple or list using map
new_list=map(int,input().split())
print (list(new_list))
new_tuple=map(int,input().split())
print(tuple(new_tuple))
#FILTER 
#Suppose you have a list l which contains numbers and you have to print a new list which contains only numbers greater than 2 in l
#You make for loop write conditions make new list then append that too much but filter function make your work shorter 
new_filter=filter(lambda x:x>2,l)
print(list(new_filter))
#REDUCE 
#For using reduce function it is necessary to import reduce 
from functools import reduce
#Suppose you have to do the sum of elements of  list then you can use reduce function
sum1=reduce(lambda x,y:x+y,l)
print(sum1)