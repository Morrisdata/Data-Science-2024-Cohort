# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 07:31:11 2020

CREATE BY Matthew Morris
"""
###############################################################################
##                      PYTHON FOR DATA I Unit 1 Cheat Sheet
###############################################################################
# one line comment
''' multiple line comment'''

print("header1", end=",")
print("header2", end=",")

# Printing a variable
cost = 24.00
print(cost)

# Concating variables an strings using a comma
cost = 24.00
tip = .2
total = cost + (cost * tip)
print("I should tip:",total)


username = input("Enter username: ") #enter a name in the console and hit Enter

# converting input types
int() integer
str() string
float() float

hours = '40'
wage = 20
int(hours) * wage


#convert an input into an integer
wage = int(input("Enter wage :"))


#slicing   
pet = 'Cat'
print(pet[0])
print(pet[0], pet[1],)# complete this to bring back "t"
print(pet[0:3])
print(pet[-1])
print(pet[-2:])



# concatenating ()
print("hello" + "there")
print(str(5) + ' there')   # cast 5 to a string str() in order for this to work


# uppercasing
state = "washington"
state.upper()       # string method (this method doesn't exist for lists)
state = state.title()


## imputing variables into a string 2 methods
# %d Substitute integer
# %f floating point
# %s string
# %x, %X hexadecimal x lower X upper
# %e, %E floating point exponential format e lower E upper
# %r raw
a = 'cats'
b = 'dogs'
c = 5

print("I have %d %r and %d %r") %(c,b,c,a)



# Using format to accomplish the same task
a = 'cats'
b = 'dogs'
c = 5
("I have {} {} and {} {}").format(c,b,c,a)

x = "fun"
print("Mad_libs is a {} game".format(x))

##Example 2
print("Mad_libs is a {1} {0}.".format("fun","game"))
