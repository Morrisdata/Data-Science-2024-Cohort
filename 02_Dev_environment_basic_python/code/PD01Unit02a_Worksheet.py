# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 15:18:06 2020

@author: Matthew Morris
"""

###############################################################################
##                      PYTHON FOR DATA I - UNIT 2
##                   MATH. BOOLEAN AND 3 VALUE LOGIC 
## IDENTIFIERS and OBJECTS
## BASIC MATH
## MATH MODULE
## BOOLEAN
## IF THEN ELIF ELSE AND 3 VALUE LOGIC
## PROJECT EXERCISE 
###############################################################################

###############################################################################
# IDENTIFIERS
# - Objects
###############################################################################

''' I like to call these variables. 
there are a few rules that I may break for the sake of speed, training and 
just my shorthand when I speak.'''
"""
Rules for identifiers

An identifier, also called a name, is a sequence of 
letters (a-z, A-Z, 0-9, _ ) 

Rules:
1)    cannot start with a number          003test
2)    cannot have a space in the name     test script
3)    cannnot have a symbol               test#
4)    Python is case sensitive, x is not the same as X 
5)    Avoid underscores _
      double underscores (for example, __init__) have built in use cases
    
Cannot use Reservered words
False      class      finally    is         raise
None       continue   for        lambda     return
True       def        from       nonlocal   try
and        del        global     not        while
as         elif       if         or         with
assert     else       import     pass       yield
break      except     in         print


Style guidelines for identifiers
use lower case for variables
use underscores_between_words
meaningful names, ie age is better than a. 
    
I have been use things like x and a as identifiers in reality you will want
to have identifiers with more meaning. There is a balance between something like
tsrq1 = and Total_Sales_Revenue_Quarter_1 = something in the middle is better and
using acroynms works if they are understandable and standard at your business.
tot_sls_revQ1 or totsales_revq1 gives an idea of the balance
"""


# Objects

x = 10
x =3
"""
Properties of objects
3 defining properties: value, type, and identity.

    Value:    A value  "20", "abcdef", or 55.
    Type:     type of the object, such as integer or string.
    Identity: A unique identifier 
    
    Value: 20 
    type: integer 
    identifier:  125490909 
"""

x = (2 + 2)         # Create a new object with a value of 4, referenced by 'x'.
y = 'ABC'

print("x type is:", type(x))      # Print the type of the object.
print("x id is:",id(x))
print("y type is:", type(y))  # Create and print the type of a string object.
print("y id is: ", id(y))   


# multiple objects and values
x, y, z = 1, 2, 3
print(x)
print(x,y,z)
print(x + y + z)





###############################################################################
# BASIC MATH
# - Order of operation(evaluation)
# - Rounding
# - assignment/reassignment operators  
###############################################################################
print( 2 + 2 )       #addition
print( 2 - 2 )       #subtraction
print( 2 ** 2 )      #power of
print( 5 % 2 )       #modulus
print( 2.1 / 2 )     #division, always results in float
print( 2.1 // 2 )    #division, always results in integer


# Order of operation(evaluation)

'''
Parentheses, Exponents, Multiplication, Division, Addition, Subtraction 
Relational Equality ( <, >), Boolean, assignments
# () ^ * / + - > and ==

Common error: Missing parentheses
It is a good practice to ensure you have explicitly put together your logic
using parentheses. In more complex logic it is easy to forget a parentheses
or lose track and have them set up incorrectly 
'''

## EXERCISE find the area of a room use inputs Length x Width = Area





## What are formulas you use at work?



## Rounding
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
''' in math you often times have a value of x and then you want to add to that
value and have a new total'''
x = 10
x = x + 5
print(x)
'''
in python we can compress this statement down'''
x = 10
x += 5
print(x)


#-assignment/reassignment operators  
x = 10       #assignment
x += 5       #adds
x -= 5       #subtracts
x *= 5       #multiples
x /= 5       #divides



##EXERCISE build an equation or formula that you use at home or work
## use various rounding to bring back various precision






##EXERCISE use math compression to simplify this statement
items = 0
items = items + 42
print(items)



###############################################################################
## MATH MODULE
#  -import what is needed
#  -import 2 needed functions
#  -import entire math module
#  -Common Math functions
###############################################################################

"""
You can bring in the entire math module or just pieces. 
It is good practice to try and bring in just the pieces you will use.
You might be using enough that it is easier to just bring in the entire module
"""
import math as


# import what is needed
from math import sqrt #from the math module import the sqrt function

print(sqrt(4))
print(ceil(4.2))  #this will not work unless you have previously imported math
print(floor(4.2))

# import 2 needed functions
from math import sqrt, ceil
print(sqrt(4))
print(ceil(4.2))
# adding another function will still cause a problem
print(floor(4.2))

#Import entire math module
import math   
print(math.sqrt(4))    # notice the .dot notation
print(math.ceil(4.2))  # 4.2 roundup to whole number
print(math.floor(4.2)) # 4.2 rounddown to whole number
print(math.sqrt(4.2))  # square root of 4.2
print(math.pow(4.2,2)) # 4.2 to the power of 2 (4.2 *4.2)


## Savings Calculator using pow
import math

base = float(input('Enter initial savings: '))
print()

rate = float(input('Enter annual interest % rate: '))
print()

years = int(input('Enter years that pass: '))
print()

total = base * math.pow(1 + (rate / 100), years)

print ('Savings after', years, 'years is', total) 

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

## EXERCISE using from and import together find the square root of 42



###############################################################################
## BOOLEAN
#  - comparison operators 
###############################################################################

'''
BOOLEAN logic bring back TRUE FALSE or UNKNOWN
Which can be extremely valuable in creating actionable reports
'''

print("Is it true that 3 + 2 < 5 - 7?")
answer = (3 + 2 < 5 - 7)
print(answer)

print("Why?")
print("What is 3 + 2?", 3 + 2)
print("What is 5 - 7?", 5 - 7)

print("Oh, that's why it's",answer)


a = 5
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



## EXERCISE using from and import together find the square root of 42



'''
EXERCISE Create several boolian functions:
1) brings back true
2) brings back false
3) uses or and brings back false4) uses and and brings back true
'''



################################
#-comparison operators 
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



# EXERCISE use assign x the value of 10 and then show an example of x 
# not equalling 11 expecte output: True


# Variables and Math and identifiers
'''  A variable is a container to hold a value
# X = 10
# X is a variable that now holds the number 10
# I can say X+1 and get 11
X = 100	
Y = 72	
Z = 14	
	(X-Y)+Z = ? 
'''
 

## EXERCISE
'''
Initial Markup (IMU) is the difference between the cost and selling price of an 
item when it is first introduced for sale. 
It is also called Initial Mark On, Markon or Markup. 

The formula for this calculation is: 
Selling price – cost = Initial Markup Dollars. 

If a buyer brings in a line of jeans with a cost of 25 per pair and initially 
prices them to sell at 55 per pair, the Initial Markup is 30. 

1)Create an IMU calculator so that you can enter the cost of an item the sale
price and see the result

2) using boolean logic evaluate that the price has not exceed a 20% markup
    expected out put: True or False''' 




###############################################################################
# IF THEN ELIF ELSE AND 3 VALUE LOGIC
#  - if-else statements.
#  - Multiple filters and conditionals 
###############################################################################

# if-else statements.
days = 45
if days > 30 and days < 90: 
    print("late fee")


# pineapple pizza debate

people = 100.00
pineapple = 49.00
antip =51.00
paying = "Terry"

# scenerio 1    
if ((pineapple/people) * 100) > 50:  
    print ("pineapple does belong on pizza")
else:
    print ("pineapple does not belong on pizza")

# scenario 2
if ((pineapple / people) * 100) > 50 or paying == "Terry": 
    print ("pineapple does belong on pizza")
else: 
    print ("pineapple does not belong on pizza")


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


    
## EXERCISE 
"""
Write an expression using Boolean operators that prints "Eligible" if user_age 
is greater than 17 and not equal to 25. Ex: 17 prints "Ineligible", 18 prints 
"Eligible".
"""
user_age = 17

if ''' Your solution goes here ''':
    print('Eligible')
else:
    print('Ineligible') 

# Use the "in" operator
nw = ['WA', 'OR', 'ID']
if 'WA' in nw:
    print('Northwest')
else:
    print('not Northwest')
# or try this
'CA' in nw


# Use the "not in" operator
NW = ['WA', 'OR', 'ID']

name = (input('Enter name to check: '))

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

"""
Membership operators can be used to check whether a string is a substring, or 
matching subset of characters, of a larger string. For example, 'abc' in 
'123abcd' returns True because the substring abc exists in the larger string. 
"""
request_str = 'GET index.html HTTP/1.1'

if '/1.1' in request_str:
    print('HTTP protocol 1.1')

if 'HTTPS' not in request_str:
    print('Unsecured connection')
    
    
    
## EXERCISE
'''
Create a function to evaluate IMU and suggest an action
BONUS : use inputs instead of the hard coded values below
Here is a list of products and how much they cost the store to buy
Jean_cost = 25
Shirt_cost = 15
Shoe_cost = 10
Here is a list of what they are being sold for
Jean_price = 60
Shirt_price = 20
Shoe_price = 11
We want to keep our margins begween 2% and 14% 
Create a function that evaluates the cost and the sell price
If it is over 14% bring back directions to markdown
If it is under 2% bring back directions to markup
If it is in range bring back directions to keep same
'''
##
#IMU evaluation and suggestions.






''' PROJECT EXERCISE
Revisit your previous project script and consider how you might use 
Prompts, If then else, Math, and boolean to update your 
scores, find your averages and give recommendations and what you can add to
your resume or what you need to practice.

Could you use input with If then else to create a Quiz? Maybe later you can
begin grading the quiz. A good starting point is to take what you have already 
created and use prompts to make your scores dynamic.
Beyond this is creativity design and your own ideas. 
'''