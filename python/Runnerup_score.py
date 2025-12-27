n=int(input(""))
list1 = list(map(int, input().split()))
largest=max(list1)
secondlargest=-10**10
for i in list1:
    if i<largest and i>secondlargest:
        secondlargest=i
print(secondlargest)