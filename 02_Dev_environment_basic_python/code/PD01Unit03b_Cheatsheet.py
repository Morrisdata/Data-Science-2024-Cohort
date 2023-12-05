# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 08:45:10 2020

@author: msmorris
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 10:03:33 2020

@author: msmorris
"""

###############################################################################
##                      PYTHON FOR DATA I - UNIT 3
##                       FUNCTIONS- CHEAT SHEET
## USER-DEFINED FUNCTION BASICS CONCEPT AND SYNTAX
## ANATOMY AND PHYSIOLOGY OF A FUNCTIONS(args)
## RETURN 
## DECOMPOSING A PROCESS
## FUNCTION STUBS
## HELP! USING DOCSTRINGS TO DOCUMENT FUNCTIONS
## PROJECT EXERCISE 
###############################################################################		

#############USER-DEFINED FUNCTION BASICS CONCEPT AND SYNTAX###################

def ux():
    print ("Here is a function that is listing out printing techniques.")
    print ('Single quotes work too!')
    print ("I'd  'use' double quotes to encapsulate 'single' quotes in your prints.")
    print ('OK "maybe"  one more')
1+1
ux()
    
print  ("not part of ux")


############A&P OF FUNCTIONS( Use of arguments or arg!)#######################

# We will define 3 functions with examples of arguments:
# print_none, print_one, print_two

def print_none():
    print ("Even though this has no arguments it is still important")
print_none()

#This function will take 1 argument
def print_one(x):
    print (x) # 
print_one("x allows me to pass in a usable variable")
print_one()

# This function will take 2 arguments
def print_two(x, y):
    print (x,y)
print_two(2+3, "< that number is the x variables/argument. This is the y")


# Math functions and arguments

# addition
def add(a, b):
   return a + b
add(10, 20)


# subtraction
a = 10
b = 5
def subtract(a, b):
   return a - b
subtract(a,b)

#division
def divide(a, b):
    a = 10
    b = 5
    return a/b
divide(a,b)



#################################RETURN########################################
def returnexample1():
    return 1+1
returnexample1()

def returnexample2():
    return (1,2,3,4,5)
returnexample2()



###########################FUNCTION STUBS######################################
#Using the pass statement in a function stub performs no operation.
def steps_to_calories(num_steps):
    pass  

# FUNCTIONAL STUB USING A PRINT STATEMENT
def steps_to_calories(steps):
    print('FIXME: finish steps_to_calories')

# Stopping the program using NotImplementedError in a function stub.
def get_points(num_points):
    """Get num_points from the user. Return a list of (x,y) tuples."""
    raise NotImplementedError
get_points(1)        



######################################################
## 07.16 HELP! USING DOCSTRINGS TO DOCUMENT FUNCTIONS
######################################################
def function_name(parameter_list):
    """This is a docstring"""
    # Function body statements
"""
A docstring starts and ends with three consecutive quotation marks. Keep the 
docstring of a simple function as a single line, including the quotes. 
Furthermore, there should be no blank lines before or after the docstring.

Multi-line docstrings should use consistent indentation for each line, 
separating the ending triple-quotes by a blank line. The following function 
definition illustrates a multi-line docstring.
"""
def ticket_price(origin, destination, coach=True, first_class=False):
    
    """Calculates the price of a ticket between two airports.
    Only one of coach or first_class must be True.

    Arguments:
    origin -- string representing code of origin airport
    destination -- string representing code of destination airport

    Optional keyword arguments:
    coach -- Boolean. True if ticket cost priced for a coach class ticket 
    (default True)
    first_class -- Boolean. True if ticket cost priced for a first class ticket 
    (default False)

    """
    #Function body statements ...

"""
The help() function can help a programmer by giving all the 
documentation associated with an object ie docstring.
help(ticket_price) would print out the docstring for the ticket_price function, 
providing the programmer with information about how to call that function.
"""



### EXERCISE
def ticket_price(origin, destination, coach=True, first_class=False):
    """Calculates the price of a ticket between two airports.
    Only one of coach or first_class must be True.

    Arguments:
    origin -- string representing code of origin airport
    destination -- string representing code of destination airport

    Optional keyword arguments:
    coach -- Boolean. True if ticket cost priced for a coach class ticket 
    (default True)
    first_class -- Boolean. True if ticket cost priced for a first class ticket 
    (default False)

    """
    #Function body statements ...

help(ticket_price)

