# Tuple is immutable list
my_tuple =(1,2,3,4,5)
print(my_tuple[1])
print(5 in my_tuple)

new_tuple =my_tuple[1:4]
print(new_tuple)

x,y,z,*other =(1,2,3,4,5)
print(other)

# Methods
# it has only two methods
print(my_tuple.count(5))
print(my_tuple.index(3))