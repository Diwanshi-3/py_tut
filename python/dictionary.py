info={'Name':'Diwanshi','Age':18,'Email':'diwanshichhabra5@gmail.com'}
print(info)
print(type(info))
print(info['Name'])
print(info.get('Name'))
#print(info['Contact']) gives error because contact is not present in dictionary
print(info.get('Contact')) #But get method not gives error it return None
print(info.values()) #give all values of dictionary
print(info.keys())   #give all keys of  dictionary
#access key value pair using keys method
for key in info.keys():
    print(f"The value corresponding to {key} is {info[key]}")
#access key value pairs using items() method 
for key,value in info.items():
    print(f"The value corresponding to {key} is {value}")
print(info.items()) #give key value pairs

#Dictionary Methods

#1.update()
dict1={122:45,123:28,124:54,897:345}
dict1.update({128:89})
print(dict1)
dict2={'Name':'Diwanshi','Age':18,'Email':'diwanshichhabra5@gmail.com'}
dict1.update(dict2)
print(dict1)

#2.clear()
dict1={122:45,123:28,124:54,897:345}
dict1.clear()
print(dict1)

#3.del
dict1={122:45,123:28,124:54,897:345}
#del(dict1) #delete entire dictionary
del dict1[122]
print(dict1)

#4.pop()
dict1={122:45,123:28,124:54,897:345}
dict1.pop(122)
print(dict1)

#5.popitem()
dict1={122:45,123:28,124:54,897:345}
dict1.popitem()
print(dict1)





