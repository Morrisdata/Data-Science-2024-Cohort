# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 09:26:17 2020

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

## EXERCISE 
# How did you get here today?
# Create a function Bonus material use what you have learned so far in your
# function.
##



## EXERCISE
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

# EXERCISE:
'''
Remember the formula for Area in unit 2. turn that into a function with,
dynamic inputs and have it use parameters. Hint inputs always take your numbers
and turn them into strings. you will need to fix that piece.
'''
'''your solution here'''



#################################RETURN########################################

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


###########################FUNCTION STUBS######################################

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
''' 