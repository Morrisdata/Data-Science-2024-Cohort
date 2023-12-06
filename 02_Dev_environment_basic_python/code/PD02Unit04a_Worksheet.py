# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 06:48:56 2020

@author: msmorris
"""

######################
## NESTED LOOPS
######################
"""
A nested loop is a loop that appears as part of the body of another loop. The 
nested loops are commonly referred to as the outer loop and inner loop.
"""
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
f = 1
print(A)

for i in range(0,3):
    f *= 10

    for j in range(0,3):
        A[i][j] *= f

print(A)


### EXERCISE COMMENT ###
"""Run the program and inline comment what each line is doing. 
Nested loops have various uses. One use is to generate all combinations of some 
items. Ex: The following program generates all two letter .com Internet domain 
names. 

Review that ord() converts a 1-character string into an integer, and 
chr() converts an integer into a character. Thus, chr(ord('a') + 1) results 
in 'b'.

Program to print all 2-letter domain names.
"""
print('Two-letter domain names:')

letter1 = 'x'
letter2 = '?'
while letter1 <= 'z':  # Outer loop
    letter2 = 'a'
    while letter2 <= 'z':  # Inner loop
        print('%s%s.com' % (letter1, letter2))
        letter2 = chr(ord(letter2) + 1)
    letter1 = chr(ord(letter1) + 1)

## EXERCISE TWO CHARACTER DOTCOM DOMAIN NAMES
"""
Modify the program to include two-character .com names, where the second 
character can be a letter or a number, e.g., a2.com. 
Hint: Add a second while 
loop nested in the outer loop, but following the first inner loop, that 
iterates through the numbers 0-9. 
"""
'''
Program to print all 2-letter domain names.
Note that ord() and chr() convert between text and ASCII/ Unicode encodings.
ord('a') is 97. ord('b') is 98, and so on. chr(99) is 'c', etc.
'''
print('Two-letter domain names:')

letter1 = 'a'
letter2 = '?'
while letter1 <= 'z':  # Outer loop
    letter2 = 'a'
    while letter2 <= 'z':  # Inner loop
        print('%s%s.com' % (letter1, letter2))
        letter2 = chr(ord(letter2) + 1)
    letter1 = chr(ord(letter1) + 1)

## NESTED LOOP HISTOGRAM
"""
Graphically depicts an integer's size by creating a histogram:

Run the program below and observe the output. Modify the program to print one 
asterisk per 5 units. So if the user enters 40, print 8 asterisks.
"""
num = 0
while num >= 0:
    num = int(input('Enter an integer (negative to quit):\n'))

    if num >= 0:
        print('Depicted graphically:')
        for i in range(num):
            print('*', end=' ')
        print('\n')
print('Goodbye.')



## EXERCISE PRINT SEATS
"""
Given num_rows and num_cols, print a list of all seats in a theater. Rows are 
numbered, columns lettered, as in 1A or 3E. Print a space after each seat, 
including after the last. Ex: num_rows = 2 and num_cols = 3 prints:

1A 1B 1C 2A 2B 2C 
"""
num_rows = 2
num_cols = 3

# Note 1: You will need to declare more variables
# Note 2: Place end=' ' at the end of your print statement to separate seats 
# by spaces

''' Your solution goes here '''


############################
## 06.10 BREAK AND CONTINUE
############################
"""
A break statement in a loop causes the loop to exit immediately. - end

In the example below, the nested for loops generate all possible meal options.
The inner loop body calculates the cost of the current meal option. 
If the meal cost == user's amount of money, the search is over, so the break 
statement exits the inner loop. The outer loop body also checks if 
the meal cost and the user's amount of money are equal, and if so, that break 
statement exits the outer loop.

The program could be written without break statements, but the loops' condition 
expressions would be more complex. 
"""
empanada_cost = 3
taco_cost = 4

user_money = int(input('Enter money for meal: '))

max_empanadas = user_money // empanada_cost
max_tacos = user_money // taco_cost

meal_cost = 0
for num_tacos in range(max_tacos + 1):
    for num_empanadas in range(max_empanadas + 1):
        meal_cost = (num_empanadas * empanada_cost) + (num_tacos * taco_cost)

        # Find first meal option that exactly matches user money
        if meal_cost == user_money:
            break

    # Find first meal option that exactly matches user money
    if meal_cost == user_money:
        break

if meal_cost == user_money:
    print('$%d buys %d empanadas and %d tacos without change.' %
        (meal_cost, num_empanadas, num_tacos))
else:
    print('You cannot buy a meal without having change left over.')


"""
Continue statements - go to the next one

A continue statement in a loop causes an immediate jump to the while or for 
loop header statement. A continue statement can improve the readability of a 
loop. 
The example below extends the previous meal finder program to find meal 
options for which the total number of items purchased is evenly divisible by 
the number of diners. In addition, the following program will output all 
possible meal options, instead of reporting the first meal option found.

The program uses two nested for loops to try all possible combinations of tacos 
and empanadas. If the total number of tacos and empanadas is not exactly 
divisible by the number of diners (e.g., num_tacos + num_empanadas) % 
num_diners != 0, the continue statement will immediately proceed to the next 
iteration of the for loop.

Break and continue statements can be helpful to avoid excessive 
indenting/nesting within a loop. However, because someone reading a program 
could easily overlook a break or continue statement, such statements should 
be used only when their use is clear to the reader.
"""
empanada_cost = 3
taco_cost = 4

user_money = int(input('Enter money for meal: '))

num_diners = int(input('How many people are eating: '))

max_empanadas = user_money // empanada_cost
max_tacos = user_money // taco_cost

meal_cost = 0
num_options = 0
for num_tacos in range(max_tacos + 1):
    for num_empanadas in range(max_empanadas + 1):

        # Total items purchased must be equally divisible by number of diners
        if (num_tacos + num_empanadas) % num_diners != 0:
            continue

        meal_cost = (num_empanadas * empanada_cost) + (num_tacos * taco_cost)

        if meal_cost == user_money:
            print('$%d buys %d empanadas and %d tacos without change.' %
                  (meal_cost, num_empanadas, num_tacos))
            num_options += 1

if num_options == 0:
    print('You cannot buy a meal without having change left over.')

"""
"Simon Says" is a memory game where "Simon" outputs a sequence of 10 characters 
(R, G, B, Y) and the user must repeat the sequence. Create a for loop that 
compares the two strings. For each match, add one point to user_score. Upon a 
mismatch, end the game. Ex: The following patterns yield a user_score of 4:

simonPattern: R, R, G, B, R, Y, Y, B, G, Y
userPattern:  R, R, G, B, B, R, Y, B, G, Y
"""
user_score = 0
simon_pattern = 'RRGBRYYBGY'
user_pattern  = 'RRGBBRYBGY'

''' Your solution goes here '''

print('User score:', user_score)


###################
## LOOP ELSE
###################
"""
A loop may optionally include an else clause that executes only if the loop 
terminates normally, not using a break statement. Thus, the complete forms of 
while and for loops are:
"""
while expression:  # Loop expression
    # Loop body: Sub-statements to execute if 
    # the expression evaluated to True
else:
    # Else body: Sub-statements to execute once 
    # if the expression evaluated to False

# Statements to execute after the loop

for name in iterable:
    # Loop body: Sub-statements to execute 
    # for each item in iterable
else:
    # Else body: Sub-statements to execute 
    # once when loop completes

# Statements to execute after the loop

"""
The loop else construct executes if the loop completes normally. In the 
following example, a special message "All names printed" is displayed if the 
entire list of names is completely iterated through. 
"""
names = ['Janice', 'Clarice', 'Martin', 'Veronica', 'Jason']

num = int(input('Enter number of names to print: '))
for i in range(len(names)):
    if i == num:
        break
    print(names[i], end= ' ')
else:
    print('All names printed.')


###############################################################
## GETTING BOTH INDEX AND VALUE WHEN LOOPING: ENUMERATE()
################################################################
"""
The enumerate() function
lets say you have a list and you want to get the index of items in the list
You could run the following code. 
"""
origins = [4, 8, 10]

for index in range(len(origins)):
    value = origins[index]  # Retrieve value of element in list.
    print('Index in list %d: %s' % (index, value))

"""
The enumerate() function retrieves both the index and corresponding element 
value at the same time, providing a cleaner and more readable solution. 
"""
origins = [4, 8, 10]

for (index, value) in enumerate(origins):
    print('Index in list %d: %s' % (index, value))
    
##############################################
## ADDITIONAL PRACTICE: DICE STATISTICS
##############################################
"""
The following program calculates the number of times the sum of 
two dice (randomly rolled) is equal to six or seven.
"""
import random

num_sixes = 0
num_sevens = 0
num_rolls = int(input('Enter number of rolls:\n'))

if num_rolls >= 1:
    for i in range(num_rolls):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        roll_total = die1 + die2

        #Count number of sixes and sevens
        if roll_total == 6:
            num_sixes = num_sixes + 1
        if roll_total == 7:
            num_sevens = num_sevens + 1
        print('Roll %d is %d (%d + %d)' % (i, roll_total, die1, die2))

    print('\nDice roll statistics:')
    print('6s:', num_sixes)
    print('7s:', num_sevens)
else:
    print('Invalid number of rolls. Try again.')

"""
Create a different version of the program that:
Calculates the number of times the sum of the randomly rolled dice equals 
each possible value from 2 to 12.
Repeatedly asks the user for the number of times to roll the dice, quitting 
only when the user-entered number is less than 1. Hint: Use a while loop 
that will execute as long as num_rolls is greater than 1.
Prints a histogram in which the total number of times the dice rolls equals 
each possible value is displayed by printing a character, such as *, that 
number of times. The following provides an example:
"""