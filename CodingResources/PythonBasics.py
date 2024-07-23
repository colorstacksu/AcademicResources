# creating variables in python
number = 1 #this is an int
precise_number = 4.8663 #this is a float
name = "Colorstack" #this is a string
location = 'Marietta' #this is a string
isValid = True # this is a boolean

# how to print
# run this code to see what it prints out
# this should print out "1" in your console. Try replacing number with another variable from the top and see what it prints
print(number)

# if you want to print text typed directly
print("Hello Tech Scholar")

# and if you want to print both text and variables, use a comma to separate the literal string and variable:
print("My name is", name)

# taking in input. This is how you would store new in put into a variable
# using input, you can take in data from the user. Using the parentheses
name = input("Enter a new name: ")
print(name)

# if the input you are taken in should be stored in a data type for example int, it should be done this way
number = int(input("What is your age?"))

# if you want the length of a string, you can use len()
print(len(name)) # this will print out the length of the current value of the variable "name"

# if you want to print out a specific text a specific amount of times, you can do it this way
print("Yessir " * 6)

# traditionally, we can also use a for loop to achieve this and so much more
# if only one value is passed to range, it will iterate from 0 by default to the value right before the number passed
# its default increment is 1 and you can only change that if it has all 3 parameters: beginning, end and increment
# this will print out values 0 to 3 with a default increment of 1.
for i in range(4):
    print(i)



