#3.1 Say Goodbye

def say_goodbye(name):
    print("Goodbye,", name)

#3.2 Area of a Circle
def circle_area(radius):
    area = 3.14 * radius * radius
    print(area)

#4.1 Subtract, multiple and divide
def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

#5.1 what shuold I wear?
temps = [50, 53, 56, 57, 60, 62, 64]
def what_to_wear(temps):
    min_temp = min(temps)
    max_temp = max(temps)
    test = (min_temp, max_temp)
    return test



#5.2 is it the weekend

def is_weekend(number):
    if number <= 7 and number == 6 or number == 7:
        return True
    else:
        return False

print(is_weekend(9))

#5.3 fuel efficiency calclulator

def fuel_efficiency(miles, gallons):
    mpg = miles / gallons
    return mpg

print(fuel_efficiency(300, 10))

#5.4 secret code
def secret_code(integer):
    last_digit = integer % 10
    remaining_digits = integer // 10

    num_digits = len(str(remaining_digits))

    new_number = last_digit * (10 ** num_digits) + remaining_digits
    return new_number

print(secret_code(1234))

#6.1 oski stole your power 


def power(x, y):
    result = 1
    for _ in range(y):
        result *= x
    return result

print(power(2, 3))

#6.2 for loops

def min_value(list_of_integers):
    min_val = list_of_integers[0]
    for num in list_of_integers:
        if num < min_val:
            min_val = num
    return min_val

def max_value(list_of_integers):
    max_val = list_of_integers[0]
    for num in list_of_integers:
        if num > max_val:
            max_val = num
    return max_val

#6.2.2 while loops

def min_value_while(list_of_integers):
    min_val = list_of_integers[0]
    index = 0
    while index < len(list_of_integers):
        if list_of_integers[index] < min_val:
            min_val = list_of_integers[index]
        index += 1
    return min_val

def max_value_while(list_of_integers):
    max_val = list_of_integers[0]
    index = 0
    while index < len(list_of_integers):
        if list_of_integers[index] > max_val:
            max_val = list_of_integers[index]
        index += 1
    return max_val

#6.3 calculate the sum
#write a return function that takes an interger as input and returns the sum of its digits

def sum_of_digits(n):
    total = 0
    for digit in str(n):
        total += int(digit)
    return total

print(sum_of_digits(123875412344))
print(f"the result of Calculate the sum with 123875412344 is {sum_of_digits(123875412344)} ")






