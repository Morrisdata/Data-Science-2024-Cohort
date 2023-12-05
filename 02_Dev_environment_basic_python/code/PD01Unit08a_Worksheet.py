###############################################################################
## 06    LOOPS
## 06.01 LOOPS(GENERAL)
## 06.02 WHILE LOOPS
## 06.03 MORE WHILE EXAMPLES
## 06.04 COUNTING
## 06.05 FOR LOOPS
## 06.06 COUNTING USING THE RANGE() FUNCTION
## 06.07 WHILE VS. FOR LOOPS
## 06.08 NESTED LOOPS
## 06.09 DEVELOPING PROGRAMS INCREMENTALLY
## 06.10 BREAK AND CONTINUE
## 06.11 LOOP ELSE
## 06.12 GETTING BOTH INDEX AND VALUE WHEN LOOPING: ENUMERATE()
## 06.13 ADDITIONAL PRACTICE: DICE STATISTICS
###############################################################################
########################
## 06.01 LOOPS(GENERAL)
########################
"""
Loop concept

People who have children may be familiar with looping around the block until a 
baby falls asleep.

A loop is a program construct that repeatedly executes the loop's statements 
(known as the loop body) while the loop's expression is true; when false, 
execution proceeds past the loop. Each time through a loop's statements is 
called an iteration. 

Let's say you have a grocery list and you have nothing so far. You look at the
list see the first item and pick it up look at the list again and pick up next
item look at list again no more items on list you are done shopping. Here is 
how that looks as a loop. 
"""
grocery = 0
buy = 0
while grocery <3: # 3 items on grocery list
    buy = buy +1
    grocery = buy
print('I had', grocery, 'items on my list')


'''A loop can be used to compute the average of a list of numbers. '''
sum = 0
num = 0
val = 5
while val > -1:
    sum = sum + val
    num = num + 1
avg = sum/num


#####################
## 06.02 WHILE LOOPS
#####################
"""
While loop: Basics
A while loop is a construct that repeatedly executes an indented block of code 
(known as the loop body) as long as the loop's expression is True. 
At the end of the loop body, execution goes back to the while loop statement 
and the loop expression is evaluated again. If the loop expression is True, the 
loop body is executed again. But, if the expression evaluates to False, then 
execution instead proceeds to below the loop body. Each execution of the 
loop body is called an iteration, and looping is also called iterating.
"""

while expression:  # Loop expression
    # Loop body: Sub-statements to execute
    # if the loop expression evaluates to True

# Statements to execute after the expression evaluates to False
curr_power = 2
user_char = 'y'

while user_char == 'y':
   print(curr_power)
   curr_power = curr_power * 2
   user_char = input()
print('Done') 


x = 3
while x >= 1:
    # Do something
    x = x - 1

'''Example: While loop with a sentinel value
The following example uses the statement while user_value != 'q': to allow a 
user to end a face-drawing program by entering the character 'q'. The letter 
'q' in this case is a sentinel value, a value that when evaluated by the loop 
expression causes the loop to terminate.

The code print(user_value*5) produces a new string, which repeats the value of 
user_value 5 times. In this case, the value of user_value may be "-", thus the 
result of the multiplication is "-----". Another valid 
(but long and visually unappealing) method is the statement print '%s%s%s%s%s' 
% (user_value, user_value, user_value, user_value, user_value).

Note that input may read in a multi-character string from the user, so only the 
first character is extracted from user_input with user_value = user_input[0].

Once execution enters the loop body, execution continues to the body's end 
even if the expression becomes False midway through.
Figure 6.2.1: While loop example: Face-printing program that ends when user 
enters 'q'.
'''
nose = '0'  # Looks a little like a nose
user_value = '-'

while user_value != 'q':
    print(' {} {} '.format(user_value, user_value))  # Print eyes
    print('  {}  '.format(nose))  # Print nose
    print(user_value*5)  # Print mouth
    print('\n')

    # Get new character for eyes and mouth
    user_input = input("Enter a character ('q' for quit): \n")
    user_value = user_input[0]

print('Goodbye.\n')

"""
Example: While loop: Iterations

Each iteration of the program below prints one line with the year and the 
number of ancestors in that year. 

The program checks for year_considered >= user_year rather than for 
year_considered != user_year, because year_considered might be reduced 
past user_year without equaling it, causing an infinite loop. An infinite 
loop is a loop that will always execute because the loop's expression is always 
True. A common error is to accidentally create an infinite loop by assuming 
equality will be reached. Good practice is to include greater than or less than 
along with equality in a loop expression to help avoid infinite loops.

A program with an infinite loop may print output excessively, or just seem to 
stall (if the loop contains no printing). A user can halt a program by pressing 
Control-C in the command prompt running the Python program. Alternatively, 
some IDEs have a "Stop" button.
"""
year_considered = 2020  # Year being considered
num_ancestors = 2  # Approx. ancestors in considered year
years_per_generation = 20  # Approx. years per generation

user_year = int(input('Enter a past year (neg. for B.C.): '))
print()

while year_considered >= user_year:
    print('Ancestors in %d: %d' % (year_considered, num_ancestors))

    num_ancestors = num_ancestors * 2
    year_considered = year_considered - years_per_generation
    
   
## EXERCISE
"""
Write an expression that executes the loop body as long as the user enters a 
non-negative number.
Also note: If the submitted code has an infinite loop, the system will stop 
running the code after a few seconds and report "Program end never reached." 
The system doesn't print the test case that caused the reported message.
"""
user_num = 9;
while ''' Your solution goes here ''':
  print('Body')
  user_num = int(input())

print('Done.')

## EXERCISE
"""
Write a while loop that prints user_num divided by 2 until user_num is less 
than 1. The value of user_num changes inside of the loop. Sample output for 
the given program:
10.0
5.0
2.5
1.25
0.625

Also note: If the submitted code has an infinite loop, the system will stop 
running the code after a few seconds and report "Program end never reached." 
The system doesn't print the test case that caused the reported message. 
"""
user_num = 20

''' Your solution goes here '''

#############################
## 06.03 MORE WHILE EXAMPLES
#############################
"""
Example: GCD
The following is an example of using a loop to compute a mathematical quantity. 
The program computes the greatest common divisor (GCD) among two user-entered
integers num_a and num_b, using Euclid's algorithm: 
If num_a > num_b, 
set num_a to num_a - num_b, 
else set num_b to num_b - num_a
Repeat until num_a equals num_b, 
then num_a and num_b both equal the GCD.
"""
num_a = int(input('Enter first positive integer: '))
print()

num_b = int(input('Enter second positive integer: '))
print()

while num_a != num_b:
    if num_a > num_b:
        num_a = num_a - num_b
    else:
        num_b = num_b - num_a

print('GCD is %d' % num_a)

### EXERCISE CHAT WITH YOUR COMPUTER'''
'''
Uses elif branching and a random number to mix up the program's responses.
review the code below and see if you can alter the code to grow the 
conversation. There is a detail of the code and what it is doing below the code
'''
import random  # Import a library to generate random numbers

print('Tell me something about yourself.')
print('You can type \'Goodbye\' at anytime to quit.\n')

user_text = input()

while user_text != 'Goodbye':
    random_num = random.randint(0, 2)  # Gives a random number between 0 and 2
    if random_num == 0:
        print('\nPlease explain further.\n')
    elif random_num == 1:
        print("\nWhy do you say: '%s'?\n" % user_text)
    elif random_num == 2:
        print('\nWhat else can you share?\n')
    else:
        print('\nUh-oh, something went wrong. Try again.\n')

    user_text = input()

print('It was nice talking with you. Goodbye.\n')

"""
Each time through the while loop, the program will check if the user-entered 
string user_text is equal to the string literal "Goodbye". If the two strings 
are not equal, the while loop contents will execute. Within the while loop, the 
program obtains a random number between 0 and 2 by using the random library. 
The randint() function provides a new random number each time the function is 
called. The arguments to randint(), 0 and 2, provide the minimum and maximum 
values that the function may return. Using the number given by randint(), the 
program's elif statements branch to a particular response. 
"""

'''
Outputs average of list of positive integers
List ends with 0 (sentinel)
Ex: 10 1 6 3 0  yields (10 + 1 + 6 + 3) / 4, or 5
'''

values_sum = 0
num_values = 0

curr_value = int(input())
   
while curr_value > 0: # Get values until 0 (or less)
    values_sum += curr_value
    num_values += 1
    curr_value = int(input())

print('Average: %d\n' % (values_sum / num_values))

## EXERCISE WHILE LOOP WITH SENTINEL
user_value = int(input())

max_value = user_value

while user_value > 0:
    if user_value > max_value:
        max_value = user_value
    user_value = int(input())

print('Max value:', max_value, end='')

## EXERCISE BIDDING EXAMPLE
"""Write an expression that continues to bid until the user enters 'n'."""
import random
random.seed(5)

keep_going = '-'
next_bid = 0

while ''' Your solution goes here ''':
   next_bid = next_bid + random.randint(1, 10)
   print('I\'ll bid $%d!' % (next_bid))
   print('Continue bidding?', end=' ')
   keep_going = input()
   
##################
## 06.04 COUNTING
##################
"""
Counting with a while loop

Commonly, a loop should iterate a specific number of times, such as 10 times. 
The programmer can use a variable to count the number of iterations, called a 
loop variable. To iterate N times using an integer loop variable i, a loop1 
with the following form is used:
"""
# Iterating N times using a loop variable
i = 1
while i <= N:
    # Loop body statements go here
    i = i + 1

"""
A common error is to forget to include the loop variable update 
(e.g., i = i +1) at the end of the loop, causing an unintended infinite loop.

The following program outputs the amount of money in a savings account each 
year for the user-entered number of years, with $10,000 
initial savings and 5% yearly interest:
"""
initial_savings = 10000
interest_rate = 0.05

print('Initial savings of $%d' % initial_savings)
print('at %d%% yearly interest.\n' % (interest_rate*100))

years = int(input('Enter years: '))
print()

savings = initial_savings
i = 1  # Loop variable
while i <= years:  # Loop condition
    print(' Savings in year %d: $%f' % (i, savings))
    savings = savings + (savings*interest_rate)
    i = i + 1  # Increment loop variable

print('\n')

"""
Counting down is also common, as in counting down from 5 to 1. The loop body 
executes when i is 5, 4, 3, 2, and 1, but does not execute when i reaches 0.
"""
# COUNTS DOWN
i = 5
while i >= 1:
    i = i - 1   # Loop body statements go here

# INCREASED BY 2 PER ITERATION
i = 0
while i <= 100:
    i = i + 2   # Loop body statements go here

## LOOP OVER US PRESIDENTIAL ELECTION YEARS
year = 1792
current_year = ?

while year ? ??:
    # Print the election year
    year = year + ?

"""
Shorthand operators

Because assignments such as i = i + 1 are so common in programs, the 
programming language provides a shorthand version: i += 1. Similar operators 
include +=, -=, *=, and /=. For example, num *= x is shorthand for num = num * 
x. The item on the right can be an expression, so num *= x + y is shorthand for 
num = num * (x + y). Usage of such operators is common in loops.
"""
i = 0
while i < N:
    i += 1  # Loop body statements go here

## EXERCISE PRINT 1 TO N
"""
Using Shorthand, write a while loop that prints from 1 to user_num. Sample output for the given 
program:
1
2
3
4
"""
i = 1
user_num = 4 # Assume positive

''' Your solution goes here '''

  
## EXERCISE PRINT OUTPUT USING A COUNTER
"""
Retype and run, note incorrect behavior. Then fix errors in the code, which 
should print num_stars asterisks.
Sample output for the correct program when num_stars is 3:
*
*
*
"""
while num_printed != num_stars:
    print('*')
num_stars = 3
num_printed = 0

''' Your solution goes here '''   


###################
## 06.05 FOR LOOPS
###################
"""
A common task is to access all of the elements in a container. 
Ex: Printing every item in a list. A for loop statement loops over each element 
in a container one at a time, assigning the next element to a variable that can 
then be used in the loop body. 
The container in the for loop statement is typically a list, tuple, or string. 
Each iteration of the loop assigns the next element in the container to the 
name given in the for loop statement. 
"""
#ITERATING OVER A LIST USING A FOR LOOP
for name in ['Bill', 'Nicole', 'John']:
    print('Hi %s!' % name)

"""
Iterating over a dictionary using a for loop assigns the keys of the dictionary 
to the loop variable. The values can then be accessed using the key.
"""
channels = {
    'MTV': 35,
    'CNN': 28,
    'FOX': 11,
    'NBC': 4,
    'CBS': 12
}

for c in channels:
    print('%s is on channel %d' % (c, channels[c]))

"""
A for loop can also iterate over a string. Each iteration assigns the next 
character of the string to the loop variable.
"""
my_str = ''
for character in "Red Curry":
    my_str += character + '_'
print(my_str)

"""
For loops can be used to perform an action during each iteration. 
The program below uses an additional variable to sum list elements and 
and calculate average daily revenue.
"""
daily_revenues = [
    2356.23,  # Monday
    1800.12,  # Tuesday
    1792.50,  # Wednesday
    2058.10,  # Thursday
    1988.00,  # Friday
    2002.99,  # Saturday
    1890.75   # Sunday
]

total = 0
for day in daily_revenues:
    total += day

average = total / len(daily_revenues)

print('Weekly revenue: $%f' % total)
print('Daily average revenue: $%f' % average)

"""Reversed()
By using the reversed() function you can start at the last position and work
backwords through the elements.
"""
names = [
    'Biffle',
    'Bowyer', 
    'Busch',
    'Gordon',
    'Patrick'
]
# print them normal
for name in names:
    print(name, '|', end=' ') # Review what does end= ' ' accomplish?

# print them in reverse
print('\nPrinting in reverse:')
for name in reversed(names):
    print(name, '|', end=' ')

## EXERCISE
"""
Write an expression to print each price in stock_prices. Sample output  
$ 34.62
$ 76.30
$ 85.05
"""
# Apple (APPL) stock prices 2005-2007
stock_prices = [34.62, 76.30, 85.05]
for ''' Your solution goes here ''':
    print('$', price)


## EXERCISE PRINTING A DICTIONARY
"""
Write a for loop to print each contact in contact_emails. Sample output:
mike.filt@bmail.com is Mike Filt
s.reyn@email.com is Sue Reyn
narty042@nmail.com is Nate Arty
"""

contact_emails = {
    'Sue Reyn' : 's.reyn@email.com',
    'Mike Filt': 'mike.filt@bmail.com',
    'Nate Arty': 'narty042@nmail.com'
}

''' Your solution goes here '''  

#############################################
## 06.06 COUNTING USING THE RANGE() FUNCTION
#############################################
"""
The range() function

While loops are commonly used for counting a specific number of iterations, 
and for loops are commonly used to iterate over all elements of a container. 
The range() function allows counting in for loops as well. range() generates 
a sequence of numbers, starting at zero and ending before a value given inside 
the parentheses. Ex: for i in range(3) sets i to 0 during the first iteration 
of the for loop, i to 1 during the second iteration, and finally i to 2 on the 
third iteration. The value within the parentheses is not included in the 
generated sequence.

The range() function can take up to three arguments to indicate the starting 
value of the sequence, the ending value of the sequence minus 1, and the 
interval between numbers.
"""
Range 	       Sequence 	Explanation
range(5) 	    0 1 2 3 4 	Every integer from 0 to 4.
range(0, 5) 	0 1 2 3 4	Every integer from 0 to 4.
range(3, 7) 	3 4 5 6	    Every integer from 3 to 6.
range(0, 5, 1)  0 1 2 3 4	Every 1 integer from 0 to 4.
range(0, 5, 2)  0 2 4	    Every 2 integers from 0 to 4.
range(5, 0, -1)
range(5, 0, -2) 5 3 1	    Every 2 integers from 5 down to 1
    
"""
Evaluating the range() function creates a new "range" type object.  
The range type is a sequence type like lists and tuples, but are immutable. 
In general, range objects are only used as a part of a for loop statement. 
"""

''' CALCULATING YEARLY SAVINGS '''
'''Program that calculates savings and interest, using rangs for years'''

initial_savings = 10000
interest_rate = 0.05

years = int(input('Enter years: '))
print()

savings = initial_savings
for i in range(years):
    print(' Savings in year %d: $%f' % (i, savings))
    savings = savings + (savings*interest_rate)

print('\n')

#############################
## 06.07 WHILE VS. FOR LOOPS
#############################
"""
General Rules
for loop with range() is better than while loop with range() the later can 
cause an infinite loop.

for loop when the number of iterations is computable before the loop starts 
example counting down from x to 5

for loop when accessing the elements of a container, as when adding 1 to items
in a list

while loop when the number of iterations is not computable before entering the 
loop, as when iterating until a user enters a particular character.
"""

######################
## 06.08 NESTED LOOPS
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


## EXERCISE PRINT RECTANGLE
"""
Write nested loops to print a rectangle. Sample output for given program:

* * *  
* * *
"""

num_rows = 2
num_cols = 3

''' Your solution goes here '''

        print('*', end=' ')
    print()


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

############################################
## 06.09 DEVELOPING PROGRAMS INCREMENTALLY
############################################
"""
Incremental programming
3x4 keypad that has letters under a given number. 
 2
abc

As programs increase in complexity, a programmer's development process becomes 
more important. A programmer should not write the entire program and then run 
the program—hoping the program works. If, as is often the case, the program 
does not work on the first try, debugging at that point can be extra difficult 
because the program may have many distinct bugs.

Experienced programmers practice incremental programming, starting with a 
simple version of the program, and then growing the program little-by-little 
into a complete version.
"""
"""

Example: Phone number program

The following program allows the user to enter a phone number that includes 
letters, which appear on phone keypads along with numbers and are commonly used 
by companies as a marketing tactic (e.g., 1-555-HOLIDAY). The program then 
outputs the phone number using numbers only.

The first program version simply prints each element of the string to ensure 
the loop iterates properly through each string element.
"""
user_input = input('Enter phone number: ')

index = 0
for character in user_input:
    print('Element %d is: %s' % (index, character))
    index += 1
"""
The second program version outputs the numbers (0 - 9) of the phone number and 
outputs a '?' for all other characters. A FIXME comment attracts attention to 
code that needs to be fixed in the future. Many editors automatically highlight 
FIXME comments. Large projects with multiple programmers might also include a 
username and date, as in FIXME(01/22/2018, John). 
"""
user_input = input('Enter phone number: ')
phone_number = ''

for character in user_input:
    if '0' <= character <= '9':
        phone_number += character
    else:
        #FIXME: Add elif branches for letters and hyphen
        phone_number += '?'

print('Numbers only: %s' % phone_number)

"""
The third version completes the elif branch for the letters A-C (lowercase and 
uppercase, per a standard phone keypad). The code also modifies the if branch 
to echo a hyphen in addition to numbers. 
"""
user_input = input('Enter phone number: ')
phone_number = ''

for character in user_input:
    if ('0' <= character <= '9') or (character == '-'):
        phone_number += character
    elif ('a' <= character <= 'c') or ('A' <= character <= 'C'):
        phone_number += '2'
    #FIXME: Add remaining elif branches
    else:
        phone_number += '?'

print('Numbers only: %s' % phone_number)


"""
The fourth version can be created by filling in the if-else branches similarly 
for other letters and adding more instructions for handling unexpected 
characters. The code is not shown below, but sample input/output is provided. 

Enter phone number (letters/- OK, no spaces): 1-555-HOLIDAY       
Numbers only: 1-555-4654329
...
Enter phone number (letters/- OK, no spaces): 1-555-holiday
Numbers only: 1-555-4654329
...
Enter phone number (letters/- OK, no spaces): 999-9999
Numbers only: 999-9999
...
Enter phone number (letters/- OK, no spaces): 9876zywx%$#@
Numbers only: 98769999????

Complete the phone number program.

Complete the program by providing the additional if-else branches for decoding 
other letters in a phone number. Try incrementally writing the program by 
adding one "else if" branch at a time, testing that each added branch works 
as intended.
"""

user_input = input('Enter phone number:\n')
phone_number = ''

for character in user_input:
    if ('0' <= character <= '9') or (character == '-'):
        phone_number += character
    elif ('a' <= character <= 'c') or ('A' <= character <= 'C'):
        phone_number += '2'
    #FIXME: Add remaining elif branches
    else:
        phone_number += '?'

print('Numbers only: %s' % phone_number)

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
## 06.11 LOOP ELSE
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
## 06.12 GETTING BOTH INDEX AND VALUE WHEN LOOPING: ENUMERATE()
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
## 06.13 ADDITIONAL PRACTICE: DICE STATISTICS
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

