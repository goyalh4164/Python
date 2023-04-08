is_old = True
is_licenced =True

if is_old and is_licenced:
    print('you can drive the car')
elif is_old:
    print('you are old make a license')
else:
    print('not now')

# indentaion helps in fast execution of program and make the code more readable
# indentation has 4 spaces between blocks

# Truthy and Falsey
print(bool(''))
print(bool(0))
print(bool(None))

# Ternary Operator
is_friend =False
can_message = "message allowded" if is_friend else "not allowded"
print(can_message)

# Logical operators
# > < >= <= == !=
# ASCII comparision
print('a'>'A')
print(1<2>3)
print(1<2<3<5<8)
print(0!=0)
print(not(True))

# is vrs ==
# == checks for equality of value not the datatype you are comparing
print(True == 1)
print('' == 1)
print([] == 1)
print(10 == 10.0)
print([] == [])

# it checks whether the address in memory is same or not
print(True is 1)
print('' is 1)
print([] is 1)
print('1' is '1')
print(10 is 10.0)
print([] is [])
