                            #JOINING METHODS OF SETS

cities1={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Seoul","Kabul","Madrid"}
 
 #1.union() and update() method
cities3=cities1.union(cities2)
print(cities3) #Union combine both sets and return new set
print(cities1) #unchanged
print(cities2) #unchanged
cities1.update(cities2) #update method add data item in the existing set
print(cities1) #changed
 
 #2.intersection() and intersection_update() method
cities1={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Seoul","Kabul","Madrid"}
cities3=cities1.intersection(cities2)
print(cities3)
print(cities1) #unchanged
cities1.intersection_update(cities2)
print(cities1)  #updated

#3.symmetric_difference() and symmetric_difference_update() method
cities1={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Seoul","Kabul","Madrid"}
cities3=cities1.symmetric_difference(cities2)
print(cities3)
print(cities1) #unchanged
cities1.symmetric_difference_update(cities2)
print(cities1) #updated

#4.difference() and difference_update() method
cities1={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Seoul","Kabul","Madrid"}
cities3=cities1.difference(cities2)
print(cities3)
print(cities1) #unchanged
cities1.difference_update(cities2)
print(cities1) #updated

                               #SET METHODS

#1. isdisjoint() method
cities1={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Seoul","Kabul","Madrid"}
print(cities1.isdisjoint(cities2))
cities1={"Tokyo2","Madrid2","Berlin","Delhi"}
cities2={"Tokyo","Seoul","Kabul","Madrid"}
print(cities1.isdisjoint(cities2))

#2.issuperset()
cities1={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Madrid"}
print(cities1.issuperset(cities2))

#3.issubset()
cities1={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Madrid"}
print(cities2.issubset(cities1))
cities1={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Madrid","Shahabad"}
print(cities2.issubset(cities1))

#4.add()
cities1={"Tokyo","Madrid","Berlin","Delhi"}
cities1.add("Kurukshetra")
print(cities1)

#5.update()
cities1={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Madrid"}
cities1.update(cities2)
print(cities1)

#6.remove() and discard()
cities1={"Tokyo","Madrid","Berlin","Delhi"}
cities1.remove("Tokyo")
cities1.discard("Tokyo")

#cities1.remove("Shahabad")  it gives error because shahabad is not present in set
cities1.discard("Shahabad")  #but discard doesnot give error as item is not present in set

#7.del
cities1={"Tokyo","Madrid","Berlin","Delhi"}
del (cities1)

#8. clear()
cities1={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Madrid"}
cities1.clear()
print(cities1)

#9.pop()
cities1={"Tokyo","Madrid","Berlin","Delhi"}
item=cities1.pop()
print(item)

