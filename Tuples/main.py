mytuple = ('banana', 'blue', 'apple', 'green', 7, False)
print(mytuple)
address = (1234, 'Dobie Rd', 'United States', 48864)
for i in address:
    print(i)
#unpacking
hnumber, streetname, country, zipcode = address
print(streetname)
mytuple2 = ('red', 3, 0.3, True, [1, 2, 3], [9, 10, 11], 'happy')
print(mytuple2[3])
print(mytuple2[4][1])
#slicing
print(mytuple2[5:])
#changing items

mytuple2[5][1]=8
print(mytuple2)