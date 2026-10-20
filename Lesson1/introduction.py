# Lesson 1: Introduction to Python

# Print is a function
# () are the arguments
# Think of a function like a factory: the thing you put in the argument () is what gets processed
# As a result, the factory outputs something as a product

print("Hello World!")

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

# Why is it important to have different variable types?
# So the computer knows how to treat values

# Using the addition operator with strings will result in them concatenating (combining)
print("How" + "are" + "you?")

# While using it with integers will result in them adding together
print(1 + 2)

# Using variables in functions
# Variables are used without quotations, even if it's a string
# Remember that you have to declare a variable before using it!

print(name)

# If statements do something if a statement is true
if age == 16:
    print("You are 16 years old!")
# While else statements do something if the "if" statement is false
else:
    print("You are not 16 years old!")

# While loops repeat something until a condition is met
i = 0

#This loop will run until i is greater or equal to 10
while i < 10:
    print(i)
    
    # i += 1 means i = i + 1
    i += 1