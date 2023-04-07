print(type("this is a string"))
# way to write string in python
username = 'coolcoder'
password = 'coolsecret'
long_string_msg='''
ROBOT
o  o
 ||
----
'''
print(long_string_msg)

# string concatenation
print('Harsh'+' '+'Goyal')

# Type conversion
print(type(float(int(str(100)))))

# Escape Sequence
# tab spacing
weather = "\tIt\'s \"kind of\" sunny!\\ \n"
print(weather)

# Formatted string
name ='John'
age=10
print('hi '+ name + ' . You are '+ str(age) + ' years old')
# convert the above in formated string
print(f'hi {name}. You are {age} years old')
# one more way
print('hi {}. You are {} years old'.format(name,age))
# fi you want to change the position of the variables
print('hi {1}. You are {0} years old'.format(name,age))

# string indexing
selfish = '01234567'
        # '01234567'
# [start:stop]
print(selfish[0:7])
print(selfish[0:2])
print(selfish[0:9])
# step over
print(selfish[0:6:2])
# will it work
print(selfish[1:])
print(selfish[:])
print(selfish[::1])
# negative index
print(selfish[-1])
print(selfish[-3])
# reverse the string
print(selfish[::-1])

# Immutability
# string are immutable
# i.e string in python can't change
# this will not work
# selfish[0]='8' 
# but you can do this
selfish='hello'

# will it work
selfish=selfish+'8'
print(selfish)
# it works

# some important builtin functions
print(len('bfhwkndjendwk'))
quote='to be or not to be'
print(quote.upper())
print(quote.capitalize())
# find
print(quote.find('be'))
print(quote.find('bef'))
# replace
print(quote.replace('be','me'))
# remember nothing changes because all these methods returns the copy of the string