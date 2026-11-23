# to store collection of values 

a=[1,2,3,4,5]
print(a)

# access a particular value use indexing 

a=[1,2,3,4,5]
print(a[3])

print(a[-1])

print()

for i in a:
    print(i)

# print max value 
print(max(a))

# print min value 
print(min(a))

# add a new value to list in last use append 

a=[1,2,3,4,5]
a.append(99)
print(a)

# add a  value to list in particular index use insert

a=[1,2,3,4,5]
a.insert(0,99)
print(a)


# add two list use extend 
a=[1,2,3]
b=[4,5,6]
a.extend(b)
print(a)

# remove first matching value 
a=[1,2,3,4,5,3,2,1]
a.remove(1)
print(a) 

# remove last element 

a=[1,2,3,4,5]
a.pop()
print(a)

# remove particular  element use indexing 

a=[1,2,3,4,5]
a.pop(3)
print(a)

# remove all elements
# remove last element 

a=[1,2,3,4,5]
a.clear()
print(a)




# index of first occur element

a=[1,2,3,4,5,6,7,8,9,5,1,2,3,5]

print(a.index(5))

# number of times element occured use count

a=[1,2,3,4,5,6,7,8,9,5,1,2,3,5]

print(a.count(5))

# sort list use sort

a=[1,2,3,4,5,6,7,8,9,5,1,2,3,5]
a.sort()
print(a)

# reverse list use reverse

a=[1,2,3,4,5,6,7,8,9,5,1,2,3,5]
a.reverse()
print(a)


# sum of list use sum

a=[1,2,3,4,5,]

print(sum(a))


# max in list

a=[1,2,3,4,5,]

print(max(a))

# min in list

a=[1,2,3,4,5,]

print(min(a))

# to see particular value in list

# membership operators are  ----  in and not in  


print(88 in a )

print(1 not in a)


# double the list of same items use * (star) operator 

a=[1,2,3]

print(a*2)



# print a list 
z=[9,8,7,6]
for i in z:
    print(i)

for i in range(0,len(z)):
    print(z[i])


# shallow copy 
b=[1,2,4]
c=b.copy()
print(c)


# remove a value based on value 
a=[1,2,3,4,5,6,4,3,2,1]
a.remove(5)
print(a)