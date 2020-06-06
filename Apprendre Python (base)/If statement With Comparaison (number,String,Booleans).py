# if statement with comparaison
# you can compare number, string and booleans
# basic comparator : >= bether tan <= less than 1 == egale != pas egale
# use return ton return the condition

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

biggest_number= max_num(3, 5, 7)
print(biggest_number)

#OR

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1

    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(55, 66, 22))

# Pactice with some input  # CREATE A CALCULATOR    Float is useful to return a floating point number for a number or a string

num1 = float(input("Enter your first number: "))
op = input("Enter the opperator : ")
num2 = float(input("Enter your second number "))

def calculator(num1, op, num2):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2
    else:
        print("Invalid opperator")

print(calculator(num1, op, num2))


