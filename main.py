cost = 10
tax_percent = 25
tax = cost * tax_percent/ 100

price = cost + tax

print(price)


name = "Abdul Basit"
print(name + " chicken")


# Going to change the name variables

"""
chicken comments
"""


name = "chicken"
print (name)

''' 
String formatter
'''

formatter_string = "hi {}"
lastname_formatter_string = "hi {} {}"

print(formatter_string.format(name))
print(lastname_formatter_string.format(name, name))

''' 
input name
'''
# first_name = input('Enter your first name')
# print(first_name)

'''
take days an input and convert it to week
'''

# days = int(input("Enter days"))
# weeks = days / 7
# print(round(weeks))

'''
make a list of interger and string
'''
my_list = [1, 2, 3, "chicken", "basit"]
my_list.append("new item")
my_list.remove(2)
my_list.insert(2, "removed")
print(my_list)

print(my_list[3])
print(len(my_list))


for x in my_list:
    print(x)




'''
using set
'''

my_set = {1, 2, 3, 4, 5, 5, 5}
my_set.add(6)
my_set.remove(3)
print(my_set)
print(len(my_set))
print(2 in my_set)
print(10 in my_set)


'''
- Create a list of 5 animals called zoo

- Delete the animal at the 3rd index.

- Append a new animal at the end of the list

- Delete the animal at the beginning of the list.

- Print all the animals

- Print only the first 3 animals
'''
print()
print()
print()
zoo = ["lion", "tiger", "elephant", "giraffe", "zebra"]
zoo.pop(3)
zoo.append("monkey")
zoo.pop(0)
print(zoo)
print(zoo[:3])


print( 1 == 2)
print( 1 != 2)
print( 1 > 2)
print( 1 < 2)
print( 1 >= 2)
print( 1 <= 2)

# logical operators
print(1 < 2 and 2 < 3)
print(1 < 2 or 2 > 3)
print(not(1 < 2 and 2 < 3))
print(not(1 < 2 or 2 > 3))  

if 1 < 2:
    print("1 is less than 2")
elif 1 == 2:
    print("1 is equal to 2")
else:
    print("1 is not less than 2")


'''
- Create a variable grade holding an integer between 0 - 100

- Code if, elif, else statements to print the letter grade of the number grade variable

Grades:

A = 90 - 100

B = 80 - 89

C = 70-79

D = 60 - 69

F = 0 - 59


Example:

if grade = 87 then print('B') 
'''


# Grade evaluation
grade = 87  # Change this value to test other grades

if 90 <= grade <= 100:
    print('A')
elif 80 <= grade <= 89:
    print('B')
elif 70 <= grade <= 79:
    print('C')
elif 60 <= grade <= 69:
    print('D')
elif 0 <= grade <= 59:
    print('F')
else:
    print('Invalid grade')

i =0
while i < 5:
    print(i)
    i += 1
else:
    print("i is no longer less than 5")


'''
user_Dictionary
'''

user_Dictionary = {
    "name": "Abdul Basit",
    "age": 25,
    "is_student": True,
    "courses": ["Math", "Science", "History"],
}

print(user_Dictionary)
print(user_Dictionary["name"])
print(len(user_Dictionary))
print(user_Dictionary.values())

user_Dictionary2 = user_Dictionary.copy()
user_Dictionary2["name"] = "New Name"
print(user_Dictionary2)
print(user_Dictionary)


'''
Based on the dictionary:

    my_vehicle = {
        "model": "Ford",
        "make": "Explorer",
        "year": 2018,
        "mileage": 40000
    }

- Create a for loop to print all keys and values

- Create a new variable vehicle2, which is a copy of my_vehicle

- Add a new key 'number_of_tires' to the vehicle2 variable that is equal to 4

- Delete the mileage key and value from vehicle2

- Print just the keys from vehicle2 
'''

my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}
for key, value in my_vehicle.items():
    print(f"{key}: {value}")
vehicle2 = my_vehicle.copy()
vehicle2["number_of_tires"] = 4
# vehicle2.pop("mileage")
print(vehicle2.keys())
print()
print()
print(vehicle2)

def print_function(first_name, last_name):
    print(f"Hello {first_name} {last_name}")

print_function("Abdul", "Basit")
print_function("John", "Doe")
print_function("Jane", "Smith")

def print_number(lower_number, higher_number):
    print(f"Numbers between {lower_number} and {higher_number}:")

print_number(1, 10)
print_number(higher_number=20, lower_number=10)

'''
- Create a function that takes in 3 parameters(firstname, lastname, age) and

returns a dictionary based on those values
'''

def create_user_dict(firstname, lastname, age):
    return {
        "firstname": firstname,
        "lastname": lastname,
        "age": age
    }       

user1 = create_user_dict("Abdul", "Basit", 25)
user2 = create_user_dict("John", "Doe", 30)
print(user1)
print(user2)



home_assignment = {
    "assignment_1": 85,
    "assignment_2": 90,
    "assignment_3": 78
}
def grading(assignments):
    sum_of_grades = 0
    for grade in assignments.values():
        sum_of_grades += grade
    average = sum_of_grades / len(assignments)

    return round(average, 2)
print(grading(home_assignment))


# from Dog import *

# dog1 = Dog()
# dog1.name = "Buddy"
# dog1.color = "Brown"


from enemy import *
enemy1 = Enemy("Goblin")

# enemy1.type_of_enemy = "Orc"
enemy1.talk()
# print(f"Enemy Type: {enemy1.type_of_enemy}, Health: {enemy1.health}, Attack Power: {enemy1.attack_power}")

from animal import *
cat1 = Cat("Whiskers", "Black", 4, True, 2, 2)
cat1.talk()