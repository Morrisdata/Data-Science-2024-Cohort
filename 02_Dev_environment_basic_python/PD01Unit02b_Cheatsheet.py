# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 15:18:06 2020

@author: Matthew Morris
"""

###############################################################################
##              FUNCTIONS, PRINTING, MATH, VARIABLES, 3 VALUE LOGIC          ##
###############################################################################
###############################################################################
#--- BASIC MATH
###############################################################################
print( 2 + 2 )       #addition
print( 2 - 2 )       #subtraction
print( 2 ** 2 )      #power of
print( 5 % 2 )       #modulus
print( 2.1 / 2 )     #division, always results in float
print( 2.1 // 2 )     #division, always results in integer

## ROUNDING
x = (1000000 / 3)
print(x)
print(round(x, 5))
print(round(x, 4))
print(round(x, 3))
print(round(x, 2))
print(round(x, 1))
print(round(x))
print(round(x,-1))
print(round(x,-2))
print(round(x,-3))
print(round(x,-4))
print(round(x,-5))


## MATH COMPRESSION
x = 10       #assignment
x += 5       #adds
x -= 5       #subtracts
x *= 5       #multiples
x /= 5       #divides


#####################
## 03.09 MATH MODULE
#####################

import math   
print(math.sqrt(4))    # notice the .dot notation
print(math.ceil(4.2))  # 4.2 roundup to whole number
print(math.floor(4.2)) # 4.2 rounddown to whole number
print(math.sqrt(4.2))  # square root of 4.2
print(math.pow(4.2,2)) # 4.2 to the power of 2 (4.2 *4.2)

"""
Common math module functions
http://docs.python.org/3.7/library/math.html has a complete listing.
"""
#Function 	Description
#ceil  	    Round up value 		
#factorial 	factorial (3! = 3 * 2 * 1) 		
#fmod 	    Remainder of division 		
#exp 	    Exponential function ex 		
#pow 	    Raise to power 		
#acos 	    Arc cosine 	asin 	
#atan 	    Arc tangent 	atan2 	
#cos 	    Cosine 	sin 	Sine
#hypot 	    Length of vector from origin 		
#radians 	Convert degrees to radians 		
#cosh 	    Hyperbolic cosine 		
#gamma 	    Gamma function 		
#pi         (constant) 	
#fabs 	    Absolute value
#floor 	    Round down value
#fsum 	    Floating-point sum
#log 	    Natural logarithm
#sqrt 	    Square root
#Arc        sine
#Arc        tangent with two parameters
#degrees    Convert from radians to degrees
#tan 	    Tangent
#sinh 	    Hyperbolic sine
#erf 	    Error function


## BOOLEAN

print("Is it true that 3 + 2 < 5 - 7?")
answer = (3 + 2 < 5 - 7)
print(answer)

a= 5
b = -2
print("Is it greater?", a > b)
print("Is it greater or equal?", a >= b)
print("Is it less or equal?", a <= b)
print("what if we add 1 to b then is  b equal or greater?",a <= (b + 1))


## AND OR NOT
a = 5
b = 10
c = 15
# this is different then chaining, you can control the comparisions
a < 5 and a == 1 # and - if either compariasions are false then false
a < 5 or a == 1 # or - if either comparisions are true then true
a < 5 and not a == 1
a < 5 or not a == 1

################################
#---  comparison operators  --- 
################################
x = 4
print( x < 2 )       # less than
print(x > 2 )        # greater than
print( x <= 4 )      # less than or equal to
print(x >= 2 )       # greater than or equal to
print( x == 2 )      # equal to
print( x != 2 )      # not equal to
print(x in [1,2,3,4]) # Membership And identity operators
print(x not in [1,2,3,4]) 

# if-else statements.
days = 45
if days > 30 and days < 90: 
    print("late fee")

# Multiple filters and conditionals 
weather = "Sunny"
day = "Monday"
time = "5am"
season = "SUMMER"


if weather == "Sunny" and day == "Monday" and time == "5am" and season == "Winter": 
    print("dont garden")
elif weather == "Sunny" and day == "Saturday" and time == "10am" and season == "Spring": 
    print("Garden")
else: print("Need more data")


###########################################
##  IF THEN ELIF ELSE AND 3 VALUE LOGIC
###########################################
# Use the "in" operator
nw = ['WA', 'OR', 'ID']
if 'CA' in nw:
    print('Northwest')
else:
    print('not Northwest')
# or try this
'CA' in nw


# Use the "not in" operator
NW = ['WA', 'OR', 'ID']

name = input('Enter name to check: ')

if name not in NW:
    print('Could not find', name, 'in region')
else:
    print('Found', name, 'in region')

# parse through a string
request_str = 'GET index.html HTTP/1.1'

if '/1.1' in request_str:
    print('HTTP protocol 1.1')

if 'HTTPS' not in request_str:
    print('Unsecured connection')
    
    
