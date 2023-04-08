# set is a collection of unordered unique values
my_set = {2,1,2,3,4,4,5,5,5,5}
my_set.add(100)
my_set.add(2)
print(my_set)

# convert a list of duplicate values to unique value list
my_list = [1,2,2,3,3,3,4,5,5,5]
print(list(set(my_list)))

# indexing does not work with sets
print(1 in my_set)
print(7 in my_set)

# some useful methods
new_set = my_set.copy()
my_set.clear()
print(new_set);

# very very useful methods
a ={1,2,3,4,5}
b ={4,5,6,7,8,9,10}

# difference a-b
print(a.difference(b))

# discard it removes the element
a.discard(5)
print(a)

# difference update it updates the set
a.difference_update(b)
print(a)

# intersection
print(a.intersection(b))
print(a & b)
# one more way

# disjoint .. is anything common between two sets.if nothing is common then it returns true
print(a.isdisjoint(b))

# union 
print(a.union(b))
# oe more way
print(a | b)

# subset
a={4,5}
b={4,5,6,7,8,9,10}
print(a.issubset(b))

# issuperset
print(b.issuperset(a))