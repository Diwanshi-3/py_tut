n=int(input(" "))
count=0
temp=n
while temp>0:
    count+=1
    temp=temp//10
print(count)