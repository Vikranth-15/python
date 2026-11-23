#  set is unordered and immutable 



a={1,2,3,2}
print(a)
print(type(a))

# add elements use add method 
a=set()
a.add(22)
a.add(33)
a.add(44)
a.add(22)
print(a)


# can not re assain values 
# a[1]=99
print(a)

for i in a:
    print(i)

# convert string to set 
a="apple"
b=set(a)
print(b)




# can not acess using indexing 

#    b=a[3]


# returns error 

# update set 
a={1,2,3,4}
a.update([2,3,5,6])
print(a)


# remove items 

a={1,2,3,4,5,6}
print(a)

# discard removes if present if not present not raises an error
a.discard(4)
print(a)

# remove it can remove an element if present if not preset raises an error

a.remove(6)
print(a)

# length of set 

print(len(a))


# iterate over set 
for i in a:
    print(i)


# if elements are present in set or not using member ship operators in and not in 

print(2 in a )

s1={1,2,3,4,5,6}

s2={5,6,7,8,9,10}

a=s1-s2
print(a)

# elements from only one set not common elements 

print(s2-s1)

# all elements in both sets 
print(s1| s2)


# not common elements in both sets 
print(s1^s2)


# common elements in both sets

print(s1 & s2) 