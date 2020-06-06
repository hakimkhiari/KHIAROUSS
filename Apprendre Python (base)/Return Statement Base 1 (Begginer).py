# Use the return Statement
# That's the thing you can't do

def cube(num):
    str(num * num * num)
cube(3)
#or
def cube(num):
    num*num*num
cube(3)
#or
def cube(num):
    num*num*num
print(cube(3))
# if you try to run All this code it don't work

# Thats why you need to use a Return Statement

def cube(num):
    return num*num*num               #This type of code work
print(cube(3))

# You can also store The value of the return Function in a variable
#like the code bellow

def cube(num):                          #after a return statement in a function you can't type code bellow
    return num * num * num
result = cube(5)       #storing the value
print(result)          # after print this variable that store the return of the function