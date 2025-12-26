details=("apple",4,"orange")
print(details)
print(type(details))
print(details[0])
print(details[1])

#We cannot directly manipulate the tuple because tuple is immutable hence for manipulating the tuple 
#First we convert the tuple int list and manipulate it then convert it again into tuple
data=list(details)
data.append("Mango")
data.pop(0)
detail=tuple(data)
print(detail)

#We cannot directly manipulate tuple but we can perform some operation directly on tuple
tuple1=(1,2,3,4,5,6,7)
tuple2=(8,9,10)
tuple3=tuple1+tuple2
print(tuple3)

#Find an index 
print(tuple3.index(10))

#length of tuple
print(len(tuple3))