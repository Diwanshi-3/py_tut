#Flatten Nested List
data=[[1,2],[3,4],[5,6]]
data2=[]
for sublist in data:
    for i in sublist:
     data2.append(i)
print(data2)
#Create lists of list which contains number,square,and cube
nested_data=[[(i),(i*i),(i*i*i)] for i in range(1,6)]
print(nested_data)
#Print only strings in List
elements=[1,"apple",2,"banana",3]
string=[]
for i in elements:
   if type(i)==str:
      string.append(i)
print(string)
#Push zeroes of the list at end 
elements=[10,0,9,0,8,0,90,0,0,8,0,6,5,4,3,2]
zeroes=[]
non_zeroes=[]
for i in elements:
    if i==0:
        zeroes.append(i)
    else:
        non_zeroes.append(i)
non_zeroes.extend(zeroes)
print(non_zeroes)
#Print name of students who has marks greater than 80
nested_data=[["Diwanshi",90],["Hanshika",75],["Gururehmat",98],["Harman",63]]
for sublist in nested_data:
  name=sublist[0]
  marks=sublist[1]
  if marks>80:
    print(name)