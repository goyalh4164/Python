# Dictionary

# dict keyword  # it is used to declare the dictionary
# key-value pair
# it stores in unordered manner i.e not sorted
# dictionary declaration
dictionary = {
    'x' : [1,2,3],
    'a' : 1,
    'b' : True
}

print(dictionary)
print(dictionary['x'][1])

# Dictionary keys
# keys must be imutable
dic2 ={
    123:[1,2,3],
    True : 'hello',
    True :"ok"
}
# if key is repeated then it contains the latest value
print(dic2[True])

# Dictionary Methods
user ={
    'basket' : [1,2,3],
    'greet' : 'hello'
}
# get will give None if value is not present
print(user.get('age'))
# you can also provide default value if the age is not present
print(user.get('age',55))

# one more way to create dictionary
user2 = dict(name='John')
print(user2)

# in operator in dictionary
print('basket' in user)
print('hello' in user.values())
print('greet' in user.keys())
print(('greet','hello') in user.items()) # it uses tuple as a key value pair

# clear and copy
user2= user.copy()
user.clear()
print(user2)

# pop here pop needs atleast one argument i.e key
print(user2.pop('greet'))
print(user2.popitem()) # it removes the random key value pair from the dictionary

# update : if value not present then it adds the value pair to the dictionary
user ={'age':18}
print(user.update({'age':55}))
print(user.update({'ages':25}))
print(user)
