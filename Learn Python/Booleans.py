#booleans
is_cool =False
is_cool=True
# they are used to control the flow of program

print(bool(-1))
print(bool(0))
print(bool(1))

# everything in python when you take input is a string 
birth_year = input('what year were you born: ')
age=2022-int(birth_year)
print(f'your age is : {age}')

# some tricky
print(2000 -bool(2000))
print(2000 -bool(""))

# commenting must be least 
# simple exercise
password="hello"
print(f'{len(password)}')
