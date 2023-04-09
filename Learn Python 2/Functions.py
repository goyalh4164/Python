# to use reduce function
from functools import reduce
# to use reduce function
# function defination
def say_hello():
    print('hello')

# function calling
say_hello()

# function location in memory
print(say_hello)

# parameters
def hello(name,emoji):
    print(name,emoji)

# arguments
hello('Harsh','😊')
# keyword arguments
hello(emoji='😅',name='positional arguments')

# default parameters
def func(emoji='😢',name='Bibi'):
    print(emoji,name)
func()

# return keyword
# after return statement no other execution takes place inside the function body
def sum(num1,num2):
    def another_func(num1,num2):
        return num1+num2
    return another_func(num1,num2)
    print('hello')
total= sum (10,20)
print(total)

# methods are those who work on the objects
# example
print('hello'.capitalize())
print('hell'.upper())

# DOCSTRING are used to provide information about the function... when you hover on it
def test(a):
    '''
    INFO: this will check whether the number is even or not
    '''
    return bool(a%2==0)
print(test(91))
help(test)
print(test.__doc__)

# *args ** kwargs

# def super_func(*args): # this can accept any number of arguments
#     print(args)
#     return sum(args)
# print(super_func(1,2,3,4))
# not working will look into it

# scope exercise
a=1
def parent():
    a=10
    def confusion():
        return a
    return confusion()
print(parent())
print(a)

# scope rules for searching a variable or method or function
#1 -start with local
#2 - Parent local?
#3 - global
#4 -built in python

# GLobal variable

total=0
# def count():
#     # to use the global total we need to add global keyword to this
#     global total
#     total+=1
#     return total
# better way
def count(total):
    total+=1
    return total
print(count(count(count(count(total)))))

# non local keyword
def outer():
    x="local"
    def inner():
        # non local means we do not want to use local x but we want to use the x i.e just outside the current scope
        nonlocal x
        x="nonlocal"
        print("inner:",x)
    
    inner()
    print("outer:",x)
outer()

# pure functions are those functions which do not affect the outside world and will produce the same output as we provide the same input anytime

# some handy and important functions to simplify common tasks
# map , filter , zip and reduce

# map
# it is a pure function
my_list=[1,2,3]
def multiply_by_2(item):
    return item*2
print(map(multiply_by_2,[1,2,3]))  # it return the map object
print(list(map(multiply_by_2,my_list)))
# since map is a pure function so it will not affect the outside list
print(my_list)

# filter
# it filters the iterables on the basis of boolean function
def check_odd(item):
    return item%2!=0

print(list(filter(check_odd,my_list)))

# zip
# we need atleast two iterables
# it makes pair on the basis of index
p1=[1,2,3]
p2=[10,20,30]
p3=[1,11,111]
print(list(zip(p1,p2,p3)))

# reduce
# we need to import it from functools
def accumulator(acc,item):
    print(acc,item)
    return acc+item
print(reduce(accumulator,my_list,0)) # 0 is the starting value of accumulator

# List comprehensions ,set comprehensions or dictionary comprehesions are the quickest way of creating lists by a simple syntax
my_list = [char for char in 'hello']
print(my_list)
my_list2= [num for num in range(0,100)]
print(my_list2)
my_list3=[num*2 for num in range(0,100)]
print(my_list3)
my_list4 =[num for num in range(0,100)
            if num%2==0]
print(my_list4)

# set comprehensions
my_set ={char for char in 'hello'}
print(my_set)

# dictionary comprehensions
simple_dict = {
    'a':1,
    'b':2
}
my_dict = {k:v**2 for k ,v in simple_dict.items()}
print(my_dict)
my_dict2 = {k:v**2 for k ,v in simple_dict.items()
           if v%2==0
           }
print(my_dict2)

# one more way
my_dict3={num:num*2 for num in [1,2,3]}
print(my_dict3)

# simple exercise to remove duplicates
some_list = ['a','b','c','b','d','m','n','n']
duplicates =list(set([item for item in some_list]))
print(duplicates)
print("hello".upper())

