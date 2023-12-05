# Python for Data I
# Matthew Morris 
# Matthewmorris.da@gmail.com

############################################################################### 
##                    PYTHON FOR DATA I - UNIT 5
##                      lOOPS
###############################################################################
'''
You don't have to do loops but you will eventually want to in order
to avoid hand cramps from so much typing and headaches from the mental
math of basically doing loops manually. 

Loops are a way to reduce code and automate tasks that you would 
repeat over and over. 
A loop is a sequence of instructions that are continually repeated until
a certain condition is reached. 

There are 2 types of loops in python the FOR loop and the WHILE loop
For loops and While loops both allow us to perform an action over and over 
and over and over and over. 

FOR loops will iterate through list and perform its action once for each of 
those items. Lists and strings have a finite length.
So we know how many times a for loop will run based on the length of the list.

WASH
RINSE
repeat twice

A WHILE loop however will continue running and will check conditions to 
determine whether it should run the loop 1 more time. 
WASH
RINSE
until clean
'''



###############################################################################
# FOR LOOP                                                                   ##
###############################################################################
''' 
for x in n:
    do y
x

FOR container IN values:
        do something
In these values we are going to do something and put them in the container
'''
# Using a loop to Upper case your values
for color in ['red', 'blue', 'green']:
    print (color.upper())
color

for color in ['red', 'blue', 'green']:
    print (color.capitalize())

# What is this Loop doing?
for color in ['red', 'blue', 'green']:
    print (str.title(color))
color


# Using Count to see how a loop works
for count in [1, 2, 3]:
    print(count)
    print('Yes' * count)
print('Done counting.')


#In your own words what is happening below run the code and look at output
for color in ['red', 'blue', 'green']:
    if (color) is 'red':
        print ('Red')
    elif(color) == 'blue':
        print ('Blue')
    else: print('Green')
    print(color)


    

## EXERCISE
''' 
1. Run the code below
2. Why did the second for loop not bring back the entire phrase?
3. Change the code to bring back the entire phrase.
'''

for letter in "Python for Data":
    print (letter)
    
print() # what is this doing?
print()

loop = "Loops iterate"

for letter in loop:
    # Only print out the letter i
    if letter == "i":
        print (letter)


## EXERCISE
'''
Remember that list of family members you created 
Try using a loop to put all of their names in upper case
Bonus put the entire loop in a function and call the function.
Could you use input prompts to make this more dynamic?
Would psuedocode help in design and planning? 
'''




#Ranges
# We will be using ranges, randint, and importing to assist with loop examples 

# You can create a list of numbers using range 
list(range(4))
list(range(10))


# Comment up this codes to explain what is happening    
n=(range(6))
for count in n: 
    print(count) 
    print('Yes' * count)




# FOR work an 8 hour day
for count in range(1,9):
    print "Start of hour"
    print "End of hour"
    print str(count) +" hours"
print "Go home you have worked a full 8 hour day."

# Writing results into a list
''' 
Randint will randomly choose 1 of two numbers 0 or 1 for us
The code below is a coin flip simulator. 
This one is using 2 for loops and compressing some code. 
It may take a few passes to read through
this and manipulate it. Keep this as an extra credit assignment'''


from random import randint
num = 100
flips = [randint(0,1) for r in range(num)]
results = []
for object in flips:
        if object == 0:
            results.append('Heads')
        elif object == 1:
            results.append('Tails')
print results

## CHALLENGE 
'''
Count how many flips, how many heads, how many tails
Create a calculation that displays the % of times heads to tails
'''
##




###############################################################################
##                     LOOPS and LISTS                                       ##
###############################################################################        

# refresher on Loops
counts = [1,2,3,4,5]	
lunches = ['thai', 'deli', 'pcc', 'sandwich']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters'] # you can put different data types in a list
	
for count in counts:
    print (count)
	
for i in lunches:
	print ("Lunch options: %s" % i)

for i in change:
    print ("I have %r" % i)
	

# Building a list from a loop
'''
1. Create an empty list that will feed into a variable
2.	Use range to get a 0 thru 10 iteration
3.  Append new values to the ist
4. print the list out
'''    
# Example 1

values = []
for i in range(0, 6):
    print ("Adding %d to the list." % i)
    values.append(i)

for i in elements:
    
	print ("Value was: %d" % i)

# Example two less code	
values2 = range(6)
for i in elements2:
    print ("elements item was: %d" % i)
    


## EXERCISE
'''
1. create a random list of numbers
2. Bring back only the odd numbers
3. Write into a seperate list called odd
'''
##


##EXERCISE
'''
1. Run the code below
2. Use what you have learned to document what this code is doing
'''
##
def count(numbers):
    total = 0
    for n in numbers:
        if n == 'WA':
            total = total + 1
    return total

x = ['WA', 'ID', 'OR', 'WA','NOTWA','wa', 'WASHINGTON','OR','CA','WA' ]
y = count(x)
print (y)



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
   

###############################################################################
# WHILE LOOP                                                                 ##
###############################################################################
'''Loop concept

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


grocery = 0
buy = 0
while grocery <3: # 3 items on grocery list
    buy = buy +1
    grocery = buy
print('I had', grocery, 'items on my list')
'''

# WHILE  Work until boss leaves!
''' 
You are not sure when your boss leaves so you complete a task and then look 
over at thier desk to see if they are gone. 
Once they are gone your weekend starts!!!!
'''
while expression:  # Loop expression
    # Loop body: Sub-statements to execute
    # if the loop expression evaluates to True

x = 3
while x >= 1:
    # Do something
    x = x - 1

curr_power = 2
user_char = 'y'

while user_char == 'y':
   print(curr_power)
   curr_power = curr_power * 2
   user_char = input()
print('Done') 


# Examples
nums = [1,2,3,4,5]
i = 0
while (i < 4):
    print (nums)
    i +=1

# Why is this different?  
nums = [1,2,3,4,5]
i = 0
while (i < 4):
    print (i)
    i +=1

# Get the average of a list of numbers. Document what you think is happening
sum = 0
num = 0
val = 5
while val > -1:
    sum = sum + val
    num = num + 1
avg = sum/num



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


# Using random with While

import random
#variables
boss_is_still_working_on_your_review = True
count = 0
#stay at work as long as your boss is working on your review
while boss_is_still_working_on_your_review:	
    print ("Heads down and complete a task!"	)
    print ("When task is finished see if they are gone!")	
    count +=1
    print (str(count) +" task(s) complete, good job!")
    print
    
    #Boss will randomly leave
    if random.randrange(0,10) ==0:
        boss_is_still_working_on_your_review = False
        print ("Go home you hard worker, boss is gone")




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

''' Summary loops and lists
There are for loops and that is what you want to use 9 times out of 10 because 
they have an end. While loops can go on into oblivion. 
You use loops when you have a repeatable process and you want to reduce code. 
Not sure when you would use a loop? Just code away and when you hit 
something where you think, "I wish there was a way to reduce this code and 
only code it once"...probably going to be a loop. 
For more information on loops checkout the documentation: 
    http://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/loops.html
    
 We will go deeper into loops and lists in the next unit with
# iterating over a list
# iterating over a dictionary
# nested lists
# list and loop comprehensions
# sorting lists
# dictionaries and loops
# Dictionary nesting 
    
 '''


''' PROJECT EXERCISE
something that has been repeating in the project is if then else reviewing scores 
and recommendations. Can you think of how you might use loops and lists to reduce
the code to review scores and give recommendations?"
Take a look at unit one and working with files. 
Wouldn't it be great if you could use inputs into calculators then have that in
loops and lists to update these files. 
Yes this entire course is a loop, keep running it with your Skills assesment/Quiz/TrainingTracker/...
'''






