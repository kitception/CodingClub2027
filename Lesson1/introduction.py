# Lesson 1: Introduction to Python

# Print is a function
# () are the arguments
# Think of a function like a factory: the thing you put in the argument () is what gets processed
# As a result, the factory outputs something as a product

print("Hello World!")

# EXERCISE 1: Display your name

# Variables
# There are four main types we're focusing on

# 1. String
# Strings store letters and words
name = "Jerry"

# 2. Integer
# Integers store integers (whole numbers)
age = 16

# 3. Float
# Floats store decimal numbers
price = 3.6

# 4. Boolean
# Booleans store true/false
eaten = True

# Using variables in functions
# Variables are used without quotations, even if it's a string
# Remember that you have to declare a variable before using it!

print(name)

# EXERCISE 2: Make variables for your age and favourite food, then display each in the screen

# Why is it important to have different variable types?
# So the computer knows how to treat values

# Using the addition operator with strings will result in them concatenating (combining)
print("How" + "are" + "you?")

# While using it with integers will result in them adding together
print(1 + 2)

# EXERCISE 3: Make variables for the the price of two grocery items, add them together, then display them

# If statements do something if a statement is true
# Note that = is the assignment operator while == is the equality operator
if age == 16:
    print("You are 16 years old!")
# While else statements do something if the "if" statement is false
else:
    print("You are not 16 years old!")
    
# You can also use different operators like >, <, >=, <=, and !=

# EXERCISE 4: check if the combined price of your two grocery items is over $10

# While loops repeat something until a condition is met
i = 0

#This loop will run until i is greater or equal to 10
while i < 10:
    print(i)
    
    # i += 1 means i = i + 1
    i += 1
    
# EXERCISE 5: count from 1 - 100 in 10 number intervals