# Functions

def add_numbers(a, b):
    return a+b

print(add_numbers(2, 3))

def list_function(list1):
    sum = 0
    for item in list1:
        sum = sum + item

    return sum

list1 = [1, 2, 3, 4]
print(list_function(list1))