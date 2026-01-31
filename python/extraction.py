n=int(input(" "))
digits=[]
temp=n
while temp>0:
    digits.append(temp%10)
    temp=temp//10
print(digits)