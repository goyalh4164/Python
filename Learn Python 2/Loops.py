for item in 'Harsh Goyal':
    print(item)
for item in [1,2,3,4,5]:
    print(item)
for item in (1,2,3,4,5):
    print(item)
for item in {1,2,3,4,5}:
    print(item)
print(item)
print("================================================")
for item in (1,2,3,4,5):
    for x in ['a','b','c']:
        print(item,x)

# Iterable can be list,dictionary,tuple,set string
# iterated -> one by one check each item in the collection

user ={
    'name':'Golen',
    'age' : 5006,
    'can_swim' :False
}

for item in user:
    print(item)

for item in user.items():
    print(item)

for item in user.items():
    key,value=item
    print(key,value)

for key,value in user.items():
    print(key,value)

for item in user.values():
    print(item)

for item in user.keys():
    print(item)

# Range function 
print(range(100))

for i in range(0,100):
    print(i)

for i in range(0,100,2):
    print(i)

for i in range(0,10,2):
    print(list(range(i)))

# enumerate is used to have index counter
for i,char in enumerate('Helllooo'):
    print(i,char)

# while loop
i=0
while i<50:
    print(i)
    i+=1
else:
    print('done with all the work')
# incase of break statement else part of the while loop does not execute

i=0
my_list=[1,2,3]
while i<len(my_list):
    print(my_list[i])
    i+=1
    break
else:
    print('else will not execute')

for item in my_list:
    continue
    print(item)
# pass is used to pass in the next line

# simple exercise
picture = [
[0,0,0,1,0,0,0],
[0,0,1,1,1,0,0],
[0,1,1,1,1,1,0],
[1,1,1,1,1,1,1],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0]
]
fill='*'
empty=' '
for image in picture:
    for pixel in image:
        if pixel:
            print(fill,end="") # no need of new line
        else:
            print(empty,end="")
    print('') #need a new line after each inner loop

# Duplicate exercise
some_list = ['a','b','b','c','d','e','f','d','f']
duplicate =[]
for value in some_list:
    if some_list.count(value)>1:
        if value not in duplicate:
            duplicate.append(value)
print(duplicate)
