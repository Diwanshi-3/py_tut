num=[1,2,3,4,5,6,7,8,9,10]
count=0
target=int(input("Enter the number whose index you want to find:"))
for i in num:
    if i==target:
        print("Index is",count)
        break
    count+=1
else:
    print("Element not found")
    
