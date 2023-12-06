###############################################################################
##                       PYTHON FOR DATA II - UNIT 1
##                          WORKING WITH FILES                               ##
## LOOPS AND LISTS
## ITERATING OVER A LIST
## LIST NESTING
## LOOPS MODIFYING LISTS
## LIST COMPREHENSIONS
## SORTING LISTS
###############################################################################


###EXERCISE###
"""
The following (unfinished) program implements a digital line queuing system for
an amusement park ride. The system allows a rider to reserve a place in line 
without actually having to wait. The rider simply enters a name into a program 
to reserve a place. Riders that purchase a VIP pass get to skip past the common 
riders up to the last VIP rider in line. VIPs board the ride first. 
(Considering the average wait time for a Disneyland ride is about 45 minutes, 
this might be a useful program.) For this system, an employee manually selects 
when the ride is dispatched (thus removing the next riders from the front of 
the line).

Complete the following program, as described above. Once finished, add the 
following commands:
    The rider can enter a name to find the current position in line. 
    (Hint: Use the list.index() method.)
    The rider can enter a name to remove the rider from the line.
"""
riders_per_ride = 3  # Num riders per ride to dispatch

line = []  # The line of riders
num_vips = 0  # Track number of VIPs at front of line

menu = ('(1) Reserve place in line.\n'  # Add rider to line
        '(2) Reserve place in VIP line.\n'  # Add VIP
        '(3) Dispatch riders.\n'  # Dispatch next ride car
        '(4) Print riders.\n'
        '(5) Exit.\n\n')

user_input = input(menu).strip().lower()

while user_input != '5':
    if user_input == '1':  # Add rider 
        name = input('Enter name:').strip().lower()
        print(name)
        line.append(name)

    elif user_input == '2':  # Add VIP
        print('FIXME: Add new VIP')
        # Add new rider behind last VIP in line
        # Hint: Insert the VIP into the line at position num_vips.
        #Don't forget to increment num_vips.

    elif user_input == '3':  # Dispatch ride
        print('FIXME: Remove riders from the front of the line.')
        # Remove last riders_per_ride from front of line.
        # Don't forget to decrease num_vips, if necessary.

    elif user_input == '4':  # Print riders waiting in line
        print('%d person(s) waiting:' % len(line), line)

    else:
        print('Unknown menu option')

    user_input = input('Enter command: ').strip().lower()
    print(user_input)


################################
## ITERATING OVER A LIST
## split() and tokens
## all(list) # True if every element in list is True
## any(list) # True if any element in the list is True
## max(list) # Get the max of the list
## min(list) # Get the min of the list
## sum(list) # Get the sum of the list
################################
"""
A programmer commonly wants to access each element of a list. Thus, learning 
how to iterate through a list using a loop is critical.

Looping through a sequence such as a list is so common that Python supports a 
construct called a for loop, specifically for iteration purposes. The format of 
a for loop is shown below.
"""
for my_var in my_list:
    # Loop body statements go here
"""
Each iteration of the loop creates a new variable by binding the next element 
of the list to the name my_var. The loop body statements execute during each 
iteration and can use the current value of my_var as necessary. 

Programs commonly iterate through lists to determine some quantity about the 
list's items. For example, the following program determines the value of the 
maximum even number in a list:
"""

'''EXAMPLE: FINDING THE MAXIMUM NUMBER '''
''' If the user enters the numbers 7, -9, 55, 44, 20, -400, 0, 2, then the 
program will output Max even #: 44. The code uses three for loops. The first 
loop converts the strings obtained from the split() function into integers. The 
second loop prints each of the entered numbers. Note that the first and second 
loops could easily be combined into a single loop, but the example uses two 
loops for clarity. The third loop evaluates each of the list elements to find 
the maximum even number.

Before entering the first loop, the program creates the list nums as an empty 
list with the statement nums = []. The program then appends items to the list 
inside the first loop. Omitting the initial empty list creation would cause an 
error when the nums.append() function is called, because nums would not 
actually exist yet.

The main idea of the code is to use a variable max_num to maintain the largest 
value seen so far as the program iterates through the list. During each 
iteration, if the list's current element value is even and larger than max_num 
so far, then the program writes that value to max_num. Using a variable to 
track a value while iterating over a list is very common behavior.
'''

# User inputs string w/ numbers: '203 12 5 800 -10'
user_input = input('Enter numbers:')

tokens = user_input.split()  # Split into separate strings

# Convert strings to integers
nums = []
for token in tokens:
    nums.append(int(token))

# Print each position and number
print()  # Print a single newline
for index in range(len(nums)):
    value = nums[index]
    print('%d: %d' % (index, value))

# Determine maximum even number
max_num = None
for num in nums:
    if (max_num == None) and (num % 2 == 0):
        # First even number found
        max_num = num
    elif (max_num != None) and (num > max_num ) and (num % 2 == 0):
        # Larger even number found
        max_num = num

print('Max even #:', max_num)

## Built in functions
all(list) # True if every element in list is True
any(list) # True if any element in the list is True
max(list) # Get the max of the list
min(list) # Get the min of the list
sum(list) # Get the sum of the list



###EXERCISE Using Built in functions with lists ###
"""
Complete the following program using functions from the table above to find 
some statistics about basketball player Lebron James. The code below provides 
lists of various statistical categories for the years 2003-2013. Compute and 
print the following statistics:

    Total career points
    Average points per game
    Years of the highest and lowest scoring season

Use loops where appropriate.
"""
#Lebron James: Statistics for 2003/2004 - 2012/2013
games_played = [79, 80, 79, 78, 75, 81, 76, 79, 62, 76]
points = [1654, 2175, 2478, 2132, 2250, 2304, 2258, 2111, 1683, 2036]
assists = [460, 636, 814, 701, 771, 762, 773, 663, 502, 535]
rebounds = [432, 588, 556, 526, 592, 613, 554, 590, 492, 610]

# Print total points

# Print Average PPG

# Print best scoring year

# Print worst scoring year


###EXERCISE guesses###
"""
Write a loop to populate user_guesses with num_guesses integers. Read integers 
using int(input()). Ex: If num_guesses is 3 and user enters 9 5 2, then 
user_guesses is [9, 5, 2].
"""
num_guesses = 3
user_guesses = []

''' Your solution goes here '''

print(user_guesses)

### EXERCISE Sum Extra Credit ###
"""
num_guesses = 3
user_guesses = []

''' Your solution goes here '''

print(user_guesses)
"""

test_grades = [101, 83, 107, 90]
sum_extra = -999 # Initialize 0 before your loop

''' Your solution goes here '''

print('Sum extra:', sum_extra)



### EXERCISE Hourly tempature reporting ###
"""
Write a loop to print all elements in hourly_temperature. Separate elements 
with a -> surrounded by spaces. Sample output for the given program:
90 -> 92 -> 94 -> 95 
Note: 95 is followed by a space, then a newline. 
"""
hourly_temperature = [90, 92, 94, 95]

''' Your solution goes here '    




''

#######################
## 09.04  LIST NESTING
## [[]]
## enumerate
#######################
"""
Since a list can contain any type of object as an element, and a list is itself 
an object, a list can contain another list as an element. Such embedding of a 
list inside another list is known as list nesting. For example, the code 
my_list = [[5, 13], [50, 75, 100]] creates a list with two elements that are 
each another list. 
"""
'''EXAMPLE'''
my_list = [[10, 20], [30, 40]]
print('First nested list:', my_list[0])
print('Second nested list:', my_list[1])
print('Element 0 of first nested list:', my_list[0][0])

"""
A list is a single-dimensional sequence of items, like a series of times, data 
samples, daily temperatures, etc. List nesting allows for a programmer to also 
create a multi-dimensional data structure, the simplest being a two-dimensional 
table, like a spreadsheet or tic-tac-toe board. The following code defines a 
two-dimensional table using nested lists:
"""    
tic_tac_toe = [
    ['X', 'O', 'X'],
    [' ', 'X', ' '],
    ['O', 'O', 'X']
]

print(tic_tac_toe[0][0], tic_tac_toe[0][1], tic_tac_toe[0][2])
print(tic_tac_toe[1][0], tic_tac_toe[1][1], tic_tac_toe[1][2])
print(tic_tac_toe[2][0], tic_tac_toe[2][1], tic_tac_toe[2][2])


'''EXAMPLE Two dimensional list'''
"""
The following example illustrates the use of a two-dimensional list in a 
distance between cities example.
Run the following program, entering the text '1 2' as input to find the 
distance between LA and Chicago. Try other pairs. Next, try modifying the 
program by adding a new city, Anchorage, that is 3400, 3571, and 4551 miles 
from Los Angeles, Chicago, and Boston, respectively.

Note that the styling of the nested list in this example makes use of 
indentation to clearly indicate the elements of each list -- the spacing does 
not affect how the interpreter evaluates the list contents.

The following example illustrates the use of a two-dimensional list in a 
distance between cities example.

Run the following program, entering the text '1 2' as input to find the 
distance between LA and Chicago. Try other pairs. Next, try modifying the 
program by adding a new city, Anchorage, that is 3400, 3571, and 4551 miles 
from Los Angeles, Chicago, and Boston, respectively.

Note that the styling of the nested list in this example makes use of 
indentation to clearly indicate the elements of each list -- the spacing does 
not affect how the interpreter evaluates the list contents.
"""
# direct driving distances between cities, in miles
# 0: Boston    1: Chicago    2: Los Angeles

distances = [
    [
        0,  
        960,  # Boston-Chicago
        2960 # Boston-Los Angeles
    ],
    [
        960,  # Chicago-Boston
        0,
        2011  # Chicago-Los Angeles
    ],
    [
        2960,  # Los Angeles-Boston
        2011,  # Los-Angeles-Chicago
        0
    ]
]

user_input = input('Enter city pair (Ex: 1 2) -- ').strip()
city1, city2 = user_input.split()

print('Distance: %d miles' % distances[int(city1)][int(city2)])

"""
As always with lists, a typical task is to iterate through the list elements. 
A programmer can access all of the elements of nested lists by using nested for 
loops. The first for loop iterates through the elements of the outer list 
(rows of a table), while the nested loop iterates through the inner list 
elements (columns of a table). The code below defines a 3x2 table and iterates 
through each of the table entries: 
"""

currency = [

        [1.00, 5.00, 10.0], # US Dollars
        [0.75, 3.77, 7.53], # Euros
        [0.65, 3.25, 6.50]  # British pounds
for row in currency:
    for cell in row:
        print(cell, end=' ')
    print()

##Enumerate
"""
Combining nested for loops with the enumerate() function gives easy access to 
the current row and column: 
"""
''' EXAMPLE Iterating through Multi-dimensional lists using Enumerate() '''

currency = [
   [1, 5, 10 ],  # US Dollars
   [0.75, 3.77, 7.53],  #Euros
   [0.65, 3.25, 6.50]  # British pounds
]
for row_index, row in enumerate(currency):
   for column_index, item in enumerate(row):
       print('currency[%d][%d] is %.2f' % (row_index, column_index, item))

## EXERCISE Print Multiplication Table
"""
Print the two-dimensional list mult_table by row and column. Hint: Use nested 
loops. Sample output for the given program:
"""

1 | 2 | 3
2 | 4 | 6
3 | 6 | 9

mult_table = [
    [1, 2, 3],
    [2, 4, 6],
    [3, 6, 9]
]

''' Your solution goes here '''

################################
## LOOPS MODIFYING LISTS
################################
"""
The below example of changing element's values combines the len() and range() 
functions to iterate over a list and increment each element of the list by 5. 
"""
my_list = [3.2, 5.0, 16.5, 12.25]

for i in range(len(my_list)):
    my_list[i] += 5
(my_list)


## Changing List Size
"""
A common error is to add or remove a list element while iterating over that 
list. Such list modification can lead to unexpected behavior if the programmer 
is not careful. For example, consider the following program that reads in two 
sets of numbers and attempts to find numbers in the first set that are not in 
the second set. 
"""
nums1 = []
nums2 = []

user_input = input('Enter first set of numbers: ')
tokens = user_input.split()  # Split into separate strings

# Convert strings to integers
for pos, val in enumerate(tokens):
    nums1.append(int(val))
    print('%d: %s' % (pos, val))

user_input = input('Enter second set of numbers:')
tokens = user_input.split()

# Convert strings to integers
print()
for pos, val in enumerate(tokens):
    nums2.append(int(val))
    print('%d: %s' % (pos, val))
    
# Remove elements from nums1 if also in nums2
print()
for val in nums1:
    if val in nums2:
        print('Deleting %d' % val)
        nums1.remove(val)

# Print new numbers
print('\nNumbers only in first set:', end=' ')
for num in nums1:
    print(num, end=' ')
"""
The above example iterates over the list nums1, deleting an element from the 
 list if the element is also found in the list nums2. The programmer expected a 
 certain result, namely that after removing an element from the list, the next 
 iteration of the loop would reference the next element as normal. However, 
 removing the element shifts the position of each following element in the list 
 to the left by one. In the example above, removing 15 from nums1 shifts the 
 value 20 left into position 2. The loop, having just iterated over position 2 
 and removing 15, moves to the next position and finds the end of the list, 
 thus never evaluating the final value 20.

The problem illustrated by the example above has a simple fix: Iterate over a 
copy of the list instead of the actual list being modified. Copying the list 
allows a programmer to modify, swap, add, or delete elements without affecting 
the loop iterations. The easiest way to copy the iterating list is to use slice 
notation inside of the loop expression, as in
"""
for item in my_list[:]:
    # Loop statements.

'''EXERCISE SLICE Notation'''
"""   
Modify the program using slice notation to iterate over a copy of the list. 
"""

user_input = input('Enter second set of numbers:')
tokens = user_input.split()

# Convert strings to integers
print()
for pos, val in enumerate(tokens):
    nums2.append(int(val))
    print('%d: %s' % (pos, val))
    
# Remove elements from nums1 if also in nums2
print()
for val in nums1:
    if val in nums2:
        print('Deleting %d' % val)
        nums1.remove(val)

# Print new numbers
print('\nNumbers only in first set:', end=' ')
for num in nums1:
    print(num, end=' ')

##############################
## LIST COMPREHENSIONS
## new_list = [expression for name in iterable]
##############################

"""
The Python language provides a convenient construct, known as 
list comprehension, that iterates over a list, modifies each element, and 
returns a new list consisting of the modified elements.
A list comprehension construct has the following form: 
"""
new_list = [expression for name in iterable]


"""
A list comprehension has three components:

    An expression component to evaluate for each element in the iterable 
        object.
    A loop variable component to bind to the current iteration element.
    An iterable object component to iterate over 
    (list, string, tuple, enumerate, etc).

A list comprehension is always surrounded by brackets, which is a helpful 
reminder that the comprehension builds and returns a new list object. 
The loop variable and iterable object components make up a normal for loop 
expression. The for loop iterates through the iterable object as normal, and 
the expression operates on the loop variable in each iteration. The result is a 
new list containing the values modified by the expression. The below program 
demonstrates a simple list comprehension that increments each value in a list 
by 5.
"""
my_list = [10, 20, 30]
list_plus_5 = [(i + 5) for i in my_list]

print('New list contains:', list_plus_5)
"""
Programmers commonly prefer using a list comprehension rather than a 
for loop in many situations. Such preference is due to less code and due 
to more-efficient execution by the interpreter. The table below shows various 
for loops and equivalent list comprehensions. 
"""
'''EXAMPLE for loops and equivelent comprehension'''

# 01 Add 10 to every element
my_list = [5, 20, 50]
for i in range(len(my_list)):
    my_list[i] += 10
print(my_list)

my_list = [5, 20, 50]
my_list = [(i+10) for i in my_list]
print(my_list)

# 02 Convert every element to a string. 
my_list = [5, 20, 50]
for i in range(len(my_list)):
    my_list[i] = str(my_list[i])
print(my_list)

my_list = [5, 20, 50]
my_list = [str(i) for i in my_list]
print(my_list)


# 03 Convert user input into a list of integers.
inp = input('Enter numbers:')
my_list = []
for i in inp.split():
    my_list.append(int(i))
print(my_list)

inp = input('Enter numbers:')
my_list = [int(i) for i in inp.split()]
print(my_list)

# 04 Find the sum of each row in a two-dimensional list.
my_list = [[5, 10, 15], [2, 3, 16], [100]]
sum_list = []
for row in my_list:
    sum_list.append(sum(row))
print(sum_list)

my_list = [[5, 10, 15], [2, 3, 16], [100]]
sum_list = [sum(row) for row in my_list]
print(sum_list)

# 05 Find the sum of the row with the smallest sum in a two-dimensional table.
my_list = [[5, 10, 15], [2, 3, 16], [100]]
sum_list = []
for row in my_list:
    sum_list.append(sum(row))
min_row = min(sum_list)
print(min_row)

my_list = [[5, 10, 15], [2, 3, 16], [100]]
min_row = min([sum(row) for row in my_list])
print(min_row)

"""
list comprehension is not an exact replacement of for loops, because list 
comprehensions create a new list object, whereas the typical for loop is able 
to modify an existing list.

The third row of the table above has an expression in place of the iterable 
object component of the list comprehension, inp.split(). That expression is 
evaluated first, and the list comprehension will loop over the list returned by 
split().

The last example from above is interesting because the list comprehension is 
wrapped by the built-in function min(). List comprehension builds a new list 
when evaluated, so using the new list as an argument to min() is allowed – 
conceptually the interpreter is just evaluating the more familiar code: 
    min([30, 21, 100]). 
"""

## Conditional list comprehension
"""
A list comprehension can be extended with an optional conditional clause that 
filters out elements from the resulting list.
"""
new_list = [expression for name in iterable if condition]

'''EXAMPLE filters out odd numbers'''
# Get a list of integers from the user
numbers = [int(i) for i in input('Enter numbers:').split()]

#Filter out odd numbers
even_numbers = [i for i in numbers if (i % 2) == 0]
print('Even numbers only:', even_numbers)

########################
## SORTING LISTS
## sort(my_list, key=...)
## sorted(my_list, key=...)
########################
"""
One of the most useful list methods is sort(), which performs an in-place 
rearranging of the list elements, sorting the elements from lowest to highest. 
The normal relational equality rules are followed: numbers compare their 
values, strings compare ASCII/Unicode encoded values, lists compare 
element-by-element, etc. The following illustrates. 
"""
my_list = [ 150, 47, 500, -37, 0]

my_list.sort()

"""
The sort() method performs element-by-element comparison to determine the final
ordering. Numeric type elements like int and float have their values directly 
compared to determine relative ordering, i.e., 5 is less than 10.

The below program illustrates the basic usage of the list.sort() method, 
reading book titles into a list and sorting the list alphabetically.
"""

books = []
prompt = 'Enter new book: '
user_input = input(prompt).strip()

while (user_input.lower() != 'exit'):
    books.append(user_input)
    user_input = input(prompt).strip()

books.sort()

print('\nAlphabetical order:')
for book in books:
    print(book)

"""
The sort() method performs in-place modification of a list. Following execution
of the statement my_list.sort(), the contents of my_list are rearranged. The 
sorted() built-in function provides the same sorting functionality as the 
list.sort() method, however, sorted() creates and returns a new list instead 
of modifying an existing list. 
"""
numbers = [int(i) for i in input('Enter numbers: ').split()]

sorted_numbers = sorted(numbers)

print('\nOriginal numbers:', numbers)
print('Sorted numbers:', sorted_numbers)

## Key argument
"""
Both the list.sort() method and the built-in sorted() function have an optional
 key argument. The key specifies a function to be applied to each element prior 
 to being compared. Examples of key functions are the string methods 
 str.lower, str.upper, or str.capitalize.

Consider the following example, in which a roster of names is sorted 
alphabetically. If a name is mistakenly uncapitalized, then the sort 
algorithm places the name at the end of the list, because lower-case letters 
have a larger encoded value than upper-case letters. Ex: 'a' maps to the ASCII 
decimal value of 97 and 'A' maps to 65. Specifying the key function as 
str.lower (note the absence of parentheses) automatically converts the elements 
to lower-case before comparison, thus placing the lower-case name at the 
appropriate position in the sorted list.
"""
names = []
prompt = 'Enter name: '

user_input = input(prompt)

while user_input != 'exit':
    names.append(user_input)
    user_input = input(prompt)

no_key_sort = sorted(names)
key_sort = sorted(names, key=str.lower)

print('Sorting without key:', no_key_sort)
print('Sorting with key: ', key_sort)

## Key argument .sort() .sorted() can be applied to any function
my_list = [[25], [15, 25, 35], [10, 15]]

sorted_list = sorted(my_list, key=max)

print('Sorted list:', sorted_list)
"""
Sorting also supports the reverse argument. The reverse argument can be set to 
a Boolean value, either True or False. Setting reverse=True flips the sorting 
from lower-to-highest to highest-to-lowest. Thus, the statement 
sorted([15, 20, 25], reverse=True) produces a list with 
the elements [25, 20, 15]. 
"""

   

