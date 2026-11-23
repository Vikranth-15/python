#    tuples represented in open brackets 


#    ordered

#    immutable

a=(1,2,3)
print(type(a))


# we can not use append method use + (plus) operator 
b=(2,)
b=b+(5,6)
print(b)

# element re assainment can not be done
b[2]==99
print(b)

# convert string to tuple 
a='RED'
b=tuple(a)
print(b)  

# o/p ('R', 'E', 'D')

# tuple packing
c=2,3,4
print(type(c))


# access elements using indexing 
print(c[0])

# we can modify list inside the tuple
t=(2,3,4,[55,66,77,78])
t[3][3]=88
print(t)

#  Packing: Assigning multiple values to a tuple.
student = ("Rahul", 22, "Java")
print(student)


# Unpacking: Assigning tuple elements to separate variables.
student = ("Rahul", 22, "Java")

name, age, course = student

print(name)
print(age)
print(course)