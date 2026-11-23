a='hello'
print(a)
print(type(a))

 # access string slicing or indexing for some part

print(a[0])

# reverse a string 

print(a[::-1])

# convert upper case 

s1='abc'
s1=s1.upper()
print(s1)

# convert lower case 

s1='ABC'
print(s1.lower())

# first letter capital

s1='abc'
print(s1.capitalize())

# every word first letter capital 

s1="the quick brown fox"

print(s1.title())

# every word capital 
print(s1.upper())

# remove spaces 
s1='   abc'

s1=s1.strip()
print(s1)

# starts with 
s1='aabbcc'
print(s1.startswith('aabb'))

# ends with 
s1='aabbcc'

print(s1.endswith('cc'))

# replace characters 

s1='abba'
s1=s1.replace('a','x')
print(s1)

#  Find first occurrence

s1='hello  i am  vikky i is programmer'

a=s1.find('hello')
print(a)

# find how may times it occur 
a='he drives,he sings,he drives'
b=a.count('he')
print(b)


# split string 

a='he is a good boy'
b=a.split(" ")
print(b)

# iterate over string 
a='he is good at maths'
for i in a:
    print(i,end=" ")

print()
for i in range(0,len(a)):
    print(a[i],end=" ")


print()
# concatination 
a="hello "
b="world"
a=a+b
print(a)


# multiply strings use * (star) operator

a='hello '
print(a*3)