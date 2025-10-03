# 3 Lists
fav_foods = ['mango', 'chocolate', 'sushi', 'avocado', 'yogurt']
print(fav_foods[1])
print(fav_foods[-1])
fav_foods.append('cookies')
fav_foods.insert(0, 'apple')
fav_foods.remove('sushi')
print(len(fav_foods))

for i in fav_foods:
    print(i.upper())

first_last_foods = fav_foods[0:5:4]
print(first_last_foods)

if 'potato' in fav_foods:
    print("A Potato!")
else:
    print("No Potato! :(")

#3.2 Slicing and Striding
numbers = list(range(0, 21))

def get_first_15(numbers):
    first_15_list = numbers[0:15]
    return first_15_list


def get_ever_5th(first):
    every_5th_list = first[0:15:5]
    return every_5th_list

def reverse_and_stride(first):
    reverse_stride_list = first.reverse()
    reverse_stride_list = first[0:15:3]
    return reverse_stride_list

step1 = get_first_15(numbers)
print(step1)
step2 = get_ever_5th(step1)
print(step2)
step3 = reverse_and_stride(step2)
print(step3)

# 3.3 Nested Lists
numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]           
]
#print the thrid row

print(numbers[2])

#print the second element of the second row
print(numbers[1][1])
numbers.append([10, 11, 12])
def sum_nested():
    total = 0
    for row in numbers:
        for num in row:
            total += num
    return total

print(sum_nested())

# 3.4 create a 5x5 list of numbers 1 to 25

def create_5x5():
    grid = []
    for i in range(5):
        row = []
        for j in range(5):
            row.append(i * 5 + j + 1)
        grid.append(row)
    return grid

print(create_5x5())

# 4.1 Dictionaries

ages = {
    "Katie": 30,
    "Mariam": 42,
    "Safia": 25,
    "Mira": 48  
}

print(ages["Katie"])
ages["Mira"] = 100
del ages["Mariam"]
ages["Milana"] = 52

for name, age in ages.items():
    print(f"{name} is {age} years old.") 