num1 = 42 # variable declaration - Data type - Primitive: Numbers
num2 = 2.3 # variable declaration - Data type - Primitive: Numbers
boolean = True # variable declaration - Data type - Primitive: Boolean 
string = 'Hello World' # variable declaration - Data type - Primitive: String
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration - Data type - Composite: List
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # variable declaration - Data type - Composite: Dictionary
fruit = ('blueberry', 'strawberry', 'banana') # variable declaration - Data type - Composite: Tuple
print(type(fruit)) # access type of Data
print(pizza_toppings[1]) # List - access value
pizza_toppings.append('Mushrooms') # List - add value
print(person['name']) # Dictionary - access value
person['name'] = 'George' # Dictionary - update or change value
person['eye_color'] = 'blue' # Dictionary - add value
print(fruit[2]) # Dictionary - access and print(console) value

if num1 > 45:
    print("It's greater") # Conditional - if
else:
    print("It's lower") # Conditional - else

if len(string) < 5:
    print("It's a short word!") # Conditional - if
elif len(string) > 15:
    print("It's a long word!") # Conditional - else if 
else:
    print("Just right!") # Conditional - else

for x in range(5): 
    print(x) # for loop - stop
for x in range(2,5):
    print(x) # for loop - start & stop
for x in range(2,10,3):
    print(x) # for loop - start, increment & stop
x = 0
while(x < 5):
    print(x)
    x += 1 # while loop - start, stop & increment
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
pizza_toppings.pop() # List - delete value
pizza_toppings.pop(1) # List - remove specific value

print(person) # Dictionay - access value
person.pop('eye_color') # Dictionay - delete value
print(person) # Dictionay - access value

pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
for topping in pizza_toppings:
    if topping == 'Pepperoni': # for loop - start
        continue # for loop - continue
    print('After 1st if statement')
    if topping == 'Olives':
        break # for loop - break

def print_hello_ten_times(): # function
    for num in range(10): # for loop inside of a function
        print('Hello') # function - return

print_hello_ten_times() # function - call

def print_hello_x_times(x): # function - parameter
    for num in range(x): # function - argument
        print('Hello') # function - return

print_hello_x_times(4) # function - call

def print_hello_x_or_ten_times(x = 10): # function - parameter
    for num in range(x): # for loop inside of a function
        print('Hello') # function - return

print_hello_x_or_ten_times() # function - argument predifined
print_hello_x_or_ten_times(4) # function - argument


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)