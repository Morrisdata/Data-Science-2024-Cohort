# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 10:03:33 2020

@author: msmorris
"""

###############################################################################
##                      PYTHON FOR DATA I - UNIT 3
##                             FUNCTIONS
## USER-DEFINED FUNCTION BASICS CONCEPT AND SYNTAX
## ANATOMY AND PHYSIOLOGY OF A FUNCTIONS(args)
## RETURN 
## DECOMPOSING A PROCESS
## FUNCTION STUBS
## HELP! USING DOCSTRINGS TO DOCUMENT FUNCTIONS
## PROJECT EXERCISE 
###############################################################################		

#############USER-DEFINED FUNCTION BASICS CONCEPT AND SYNTAX###################
'''
When you start this class over try applying functions to Unit 1 and 2

1) make code more readable
2) modular development
3) reduces redundancy

'''

#define lasagna():
#    mince garlic
#    cut tomato
#lasagna()#oversimplified recipe, will not result in actual lasagna

def ux():
    print ("Here is a function that is listing out printing techniques.")
    print ('Single quotes work too!')
    print ("I'd  'use' double quotes to encapsulate 'single' quotes in your prints.")
    print ('OK "maybe"  one more')
1+1
ux()
 
    
print  ("not part of ux")

## Exercise 
# How did you get here today?
# Create a function Bonus material use what you have learned so far in your
# function.
##



## Exercise
''' 
Take the code you created from the "how you got here" exercise copy and paste it 
below and then put comments in the code to help you understand what you did 
6 months from now
'''
##





## EXERCISE -once  you have finished the unit on loops
''' 
Create a function that opens a new file or creates one called python_skills
then write each skill you have learned and how you rate yourself on a separate 
line next read the file
'''
##





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

# Another way to look at it
def printline(symbol):
    print(symbol * 80)
printline(input('What symbol would you like as a line?'))

## uncomment the Print nose line and see if you can get it to work
# add a another argument and symbol for nose
def print_face(eye, face_char):

   print('  ', eye, ' ', eye)  # Print eyes
#                              # Print nose
   print('  ', face_char*5)    # Print mouth
   return

print_face('o', 'x',)



# Math functions and arguments

# addition
def add(a, b):
   return a + b
add(10, 20)


# subtraction
a=in
b=5
def subtract(a, b):
   return a - b
subtract(a,b)

#division
def divide(a, b):
    a=10
    b=5
    return a/b
divide(a,b)

# EXERCISE:
'''
Remember the formula for Area in unit 2. turn that into a function with,
dynamic inputs and have it use parameters. Hint inputs always take your numbers
and turn them into strings. you will need to fix that piece.
'''
'''your solution here'''



#################################RETURN########################################
'''
Return brings back a one value from a function. That value could be a list and
therefore look like multiple values but its just returning the list. 
'''
def returnexample1():
    return 1+1
returnexample1()

def returnexample2():
    return (1,2,3,4,5)
returnexample2()

'''
To keep it simple the main difference between a return and a print is
a print is for the human user and a return can be used by other functions 
in a program. Again, that is the simple version.
'''

def simpleversion(a,b):
    return a+b

def math():
    y=(int(input('Enter Value one: ')))
    z=(int(input('Enter Value two: ')))
    return simpleversion(y,z)
math()



#Example of return using returning an expression
def height_US_to_cm(feet, inches):
    """Converts height in feet/inches to centimeters"""
    total_inches = (feet * inches_per_foot) + inches # 12 inches_per_foot
    cm = total_inches * 2.54 # 2.56 cm per inch
    return cm # returns a numeric result

feet = int(input('Enter feet: '))
inches = int(input('Enter inches: '))

print('Centimeters:', height_US_to_cm(feet, inches))

# EXERCISE TEMPATURE CONVERSION
"""
Complete the program by writing and calling a function that converts a 
temperature from Celsius into Fahrenheit. Use the formula F = C x 9/5 + 32. 
Test your program knowing that 50 Celsius is 122 Fahrenheit. 
"""
def c_to_f():
    # FIXME
    return  # FIXME: 

temp_c = float(input('Enter temperature in Celsius: '))
temp_f = None

# FIXME: Call conversion function
# temp_f = ??

# FIXME: Print result
# print('Fahrenheit:' , temp_f)


######################DECOMPOSING A PROCESS####################################
'''
When creating functions there is a balance between having to many and to little
the deciding factor is readability. If I were to give instructions on how to 
bake a cake and the instructions said "Bake a cake" and then none of the
instructions were listed out or broken up. Verses "Step 1. get a bag of flour. 
Step2. Get a medium size bowl. Step3. Open the bag of flour. Step4. lift the 
bag of flour above the bowl..." That level of detail is to much. Breaking things
up just enough is what we want to do. Keep it simple. 

A function should be easy to understand and the length should be second. 
Ask yourself can the person your mentoring understand the code, if the answer
is they "should" be able to understand it... its to long. Make is simpler. 

A line of code is non-comment, non-blank and a good rule of thumb if you are
looking for a guidepost its 20 lines of code, optimally less. 

another guide is with 11 font it should all fit easily on your screen without
scrolling. 
'''

###########################FUNCTION STUBS######################################
"""
Pseudo code is code that does not actual run but gives you a framework
you can translate that code into function stubs and begin working and testing
pieces as you develop your program. 

The stub is just a placeholder but could also bring back a print statement.
If you do not want to use a print statement you can simply type pass to have
the function ignored until your ready to start developing. 
"""
#Using the pass statement in a function stub performs no operation.
def steps_to_feet(num_steps):
    feet_per_step = 3
    feet = num_steps * feet_per_step
    return feet

def steps_to_calories(num_steps):
    pass  

steps = int(input('Enter number of steps walked: '))

feet = steps_to_feet(steps)
print('Feet:', feet)

calories = steps_to_calories(steps)
print('Calories:', calories)

"""
Another useful approach is to print a message when a function stub is called, 
thus alerting the user to the missing function statements. Good practice is 
for a stub to return -1 for a function that will have a return value. The 
following function stub could be used to replace the steps_to_calories() stub 
in the program above:
    
"""

# FUNCTIONAL STUB USING A PRINT STATEMENT
def steps_to_calories(steps):
    print('FIXME: finish steps_to_calories')


"""
A NotImplementedError can be used if you want the code to stop when a function 
has not been implemented yet. 
"""

# Stopping the program using NotImplementedError in a function stub.
import math

def get_points(num_points):
    """Get num_points from the user. Return a list of (x,y) tuples."""
    raise NotImplementedError
        
def side_length(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def get_perimeter_length(points):
    perimeter = side_length(points[0], points[1])
    perimeter += side_length(points[0], points[2])
    perimeter += side_length(points[1], points[2])
    return perimeter

coordinates = get_points(3)
print('Perimeter of triangle:', get_perimeter_length(coordinates))


"""
EXERCISE
Define stubs for the functions get_user_num() and compute_avg(). Each stub 
should print "FIXME: Finish function_name()" followed by a newline, and should 
return -1. Each stub must also contain the function's parameters. Example 
output:

FIXME: Finish get_user_num()
FIXME: Finish get_user_num()
FIXME: Finish compute_avg()
Avg: -1
"""
''' Your solution goes here '''

user_num1 = 0
user_num2 = 0
avg_result = 0

user_num1 = get_user_num()
user_num2 = get_user_num()
avg_result = compute_avg(user_num1, user_num2)

print('Avg:', avg_result)




######################################################
## 07.16 HELP! USING DOCSTRINGS TO DOCUMENT FUNCTIONS
######################################################
"""
A programmer should document each function, giving a high-level description. A 
docstring is a string literal placed in the first line of a function body.
"""
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
"""
Run the following program that prints out the response of help(ticket_price). 
Add an additional parameter "vegetarian=False" to ticket_price, augment the 
docstring appropriately, and run the program again.
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

help(ticket_price)

"""
The help() function works with most of the built-in Python names. 
help(str) prints out a description of the string str class methods, 
help(math) prints out all the contents of the math module. 

Use the following interpreter to play with the help function(). 

Try the following: help(str), help(range), and help(max). 
"""

####EXERCISE Design pick your own "Choose your own story game"
'''
This can be a fun pick your own adventure styled game like, Oregon trail, 
House of Danger or any of those text based adventure games. I made one where 
you are my cat and your hunting mice. 

Step 1 what kind of adventure do you want to make? Are you watching a TV show
Do you like board games? Start there. 

Step 2 What is the end goal of your game, write out a basic story line. 
You can keep it very simple, like in my game you must find a good place to 
get lunch. 

Step 3 Have fun, use a white board or scratch notepad to think up scenarios where
things could go wrong or right in your game 

Step 3 Use function stubs and docstrings to create your game outline in python

Step 4 Do not limit yourself to what you know. Design what you want to build
and then we will figure it out from there. 
'''







## PROJECT EXERCISE
'''
Just like you did with, Choose your own story game design out the outline of
your Python skillbuilder/quiz. Do not limit yourself to what you have learned
so far, what do you want to do and we will work backwards from there, or forwards
as we learn new skills. 

HINT: Soon we will learn how to load and read files plus do some basic statistics
over those files. 