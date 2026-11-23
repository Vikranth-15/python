#   Keys must be of immutable type and must be unique.

#  Values can be of any data type and can repeat.

# keys are set 

# values are list 

# dictonary key value pairs


a={1:"a",2:"b",3:"c"}
print(a[3])

age={"vikky":25,"sam":30,"ram":33,"krishna":33}
print(age["ram"])

val=age.get("ram")
print(val)

# if key not found 

val=age.get("hari","not found")
print(val)



keys=["tata","audi","bmw"]
values=[2,3,5]
dict1=dict(zip(keys,values))
print(dict1)

# update data 
dict1['tata']=99

print(dict1)

#remove items 

dict1.pop("bmw")
print(dict1)

del dict1["tata"]

print(dict1)