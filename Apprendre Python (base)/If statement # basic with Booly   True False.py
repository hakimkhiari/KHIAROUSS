# if statement you have a condition true you bring but if it false you have otherwise
# True or False

# Booly statement with if statement #one variable

is_male = True               #the variable have to reffer with a true or a false
if is_male:
    print("you are a male")
else:
    print("You are not a male")
                                                                #you need to write where the indentation is

    # Booly statement with if statement # Multy  variable
is_male = True
is_tall = True
# you can use !AND! or !OR!

bleu = True
grosse = True

if bleu and grosse:                               # alway us : after if,else and elif
    print("Ta voiture est grosse et bleue")
else:
    print("Ta voiture n'est pas grosse et bleue")

# With elif more complex           #ADD not(variable) to a variable for telling if this condition is false
is_male = True
is_tall = False

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You are not a male and not tall")

