marks=[32,21,98,65,43]
for index,mark in enumerate(marks): #Enumerate function gives the index with value 
    print(mark)
    if (index==2):
        print("Awesome")

#we can change the starting index also
marks=[32,21,98,65,43]
for index,mark in enumerate(marks,start=1):
    print(mark)
    if (index==3):
        print("Awesome")
