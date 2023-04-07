# List Decalaration
li = [1,2,3,4,5]
li2 = ['a','b','c']
li3 = [1,2,'a',True,[31,31]]

# printing the list
print(li3)

# amazon cart
amazon_cart =['notebooks','sunglasses']
print(amazon_cart[0])
print(amazon_cart[1])
# length on the list
print(len(amazon_cart))

# List Slicing
l=['a','b','c','d']
print(l[0:3])

# List are mutable unlike the strings
l=['a','b','c','d']
l[1]=7
print(l)

# Decalaration of the list using the string slicing
new_list = l[0:2]
new_list[0]="pointer"
print(new_list)

# listing pointing concept
a=[1,2,3,4,5]
b=a
print(a)
b[0]=7
print(a)
print(b)
# if you copy the whole list then the new list points to the old list only
# so changes reflect in both
# take it as a concept of pointer in c++
# if you want to avoid this then do in this manner
c=[1,2,3]
# this will remove the pointer concept
d=c[:]
print(c)
d[0]=7
print(c)
print(d)

# Everything in python is object
# matrix
# these are used in image processing
matrix =[
    [1,2,3],
    [2,4,6],
    [7,8,9]
]
print("matrix")
print(matrix)
print(matrix[1][1])

# List Methods
basket = [1,2,3,4,5]

# length
print(len(basket))

# append
basket.append(6) # it does not return anything 

# insert to insert at a particular index
basket.insert(5,100)
print(basket)

# extent
basket.extend([313,414,431])
print(basket)

# pop
# IMP pop returns the removed value from the list
basket.pop();
print(basket)
# you can also remove by it's index
basket.pop(2) 
print(basket)

# remove
# if you want to remove by the value
# it will throw error if the value you are trying to remove is not present in the list
basket.remove(414)
print(basket)

# clear
# it will clear the entire list
basket.clear()
print(basket)

# index
# it will also throw error if the value is not present in the list
bag = ['a','b','c','d','e','f','f','g']
print(bag.index('d'))
# if you want to search the index in an range
print(bag.index('b',0,3))

# in operator
# if you just want to check whether the value is present in the list or not 
print('b' in bag)
print('x' in bag)
print('h' in 'harsh goyal')

# count
# to count the occurence
print(bag.count('f'))
print((('harsh').count('h')))

# sort
exp = [5,4,2,5,7,88,1,2]
print(exp)
exp.sort()
print(exp)

# sorted
# if you want that your original list should not modify

lt =[53,53,34,3,52442,5,62,4,14,25,24,2]
print(sorted(lt)) # it returns the copy of the list
print(lt)

# reverse
p=[1,2,3,4,5,6]
p.reverse();
print(p)

# some useful tricks in practice
prac = ['a','b','c','d','e','f','g','h']
prac.sort()
prac.reverse()
print(prac[:])
print(prac[::-1])
print(prac)

# range 
print(list(range(1,100)))
print(list(range(100)))

# join

sentence ='--'
new_sentence = sentence.join(['hi','my','name','is','JOJO'])
print(new_sentence)

# list unpacking
a,b,c=[1,2,3]
print(a)
print(b)
print(c)
a,b,c,*other,d=[1,2,3,931,3193,139139]
print(a)
print(b)
print(c)
print(other)

# None keyword is similar to NULL in c++


