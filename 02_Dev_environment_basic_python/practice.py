# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 07:00:27 2020

@author: Msmorris
"""
###############################################################################
#--- MULTIPLE VARIABLE DECLERATION  ---  RATE 4
###############################################################################
var1, var2, var3 = 1, 2, 3      #multiple variable assignment

var1 + var2

bill, ted, adventure = 1, 2, 3
bill + adventure

x, y, z = 1, int('4'), 3
def a():
    return x+y
a()
###############################################################################
''''''''''''''''''
'''   TRY IT   '''
''''''''''''''''''

a, b, c = 1, 2, 3
print( a + b + c)

prompt1, prompt2, prompt3 = int(input('Enter value:')), int(input('Enter value:')), int(input('Enter value:'))

print(prompt1 + prompt2 + prompt3)




###############################################################################
#---  DATA TYPES --- 
###############################################################################
myInteger = 12     #variable assigned an integer
myFloat = 1.2     #variable assigned a float
myString = "twelve"     #variable assigned a string
mySecondString = 'twelve'     #variable assigned a string
myBoolean = False     #variable assigned a Boolean

dateType = type(myFloat)       #determines type of object
convInt = int(myFloat)      #converts float to an integer
convFloat = float(myInteger)        #converts integer to a float
convString = str(myInteger)     #converts integer to string
print(var1)     #print command

###############################################################################
''''''''''''''''''
'''   TRY IT   '''
''''''''''''''''''
name = 'Pat' 
last_name = "Smith"
age = 32
height = 5.4
obese = False

type(height)
height = int(height)
type(height)
height = str(height)
type(height)
''' '''




###############################################################################
#---  ARITHMATIC OPERATORS  --- 
###############################################################################
print( 2 + 2 )      #addition
print( 2 - 2 )      #subtraction
print( 2 ** 2 )      #power of
print( 5 % 2 )      #modulus
print( 2.1 / 2 )      #division, always results in float
print( 2.1 // 2 )      #division, always results in integer

###############################################################################
''''''''''''''''''
'''   TRY IT   '''
''''''''''''''''''
4**3
10//3








###############################################################################
#---  assignment/reassignment operators  --- 
###############################################################################
myAssignment = 10       #assignment
myAssignment += 5       #adds
myAssignment -= 5       #subtracts
myAssignment *= 5       #multiples
myAssignment /= 5       #divides

###############################################################################
''''''''''''''''''
'''   TRY IT   '''
''''''''''''''''''
x = 5
x += 5
(x)




###############################################################################
#---  comparison operators  --- 
###############################################################################
myNum = 4
print( myNum < 2 )       #less than
print( myNum > 2 )       #greater than
print( myNum <= 4 )       #less than or equal to
print( myNum >= 2 )       #greater than or equal to
print( myNum == 2 )       #equal to
print( myNum != 2 )       #not equal to
###############################################################################
''''''''''''''''''
'''   TRY IT   '''
''''''''''''''''''

age = 60
print(age < 55)
print(age > 40 and age < 70)
print (age < 60 or age > 60)




###############################################################################
#---  string operations  --- RATE 1
len()
title()
islower()
count()
format()
split()
###############################################################################
#view all string methods: https://docs.python.org/3/library/stdtypes.html#string-methods
myCourse = "introduction to programming in Python"
courseLength = len(myCourse)        #length operator
courseProper = myCourse.title()     #capitalizes first letter of each word
confirmLower = myCourse.islower()       #determines if the string consists of lowercase characters

statement = "I love Python. Working with Python is amazing because, hello, it's Python!"
countPython = statement.count('Python')

name = 'John Jacob Jingleheimer Schmidt'
name[0:4]        #slice a string


username = "Connie"
code = "C859"
userMessage = "Welcome to {}, {}.".format(code, username)
print( userMessage )

myNewPhrase = "cowabunga dude"
mySplitPhrase = myNewPhrase.split(" ")      #split method
print(mySplitPhrase)
###############################################################################
''''''''''''''''''
'''   TRY IT   '''
''''''''''''''''''

title = "the book thief"
title_length = len(book)
print(title_length)
proper_case = title.title()
print(proper_case)
title_test = proper_case.islower()
print(title_test)
counting = ("blue, blue, orange, blue, red, red, green")
total = counting.count("blue")
print(total)
slicing = "take a bite out of crime"
bite = slicing[7:12]
print(bite)

a = "cats"
b = "dogs"
phrase = "It's raining {} and {}.".format(a,b)
print(phrase)

phrase2 = phrase.split("s")
print(phrase2)

''' '''




###############################################################################
#---  function with both input and output  --- RATE 2
###############################################################################
def areaOf(width,height):       #function that accepts two inputs
    return width * height       #function body outputs calculated area

myArea = areaOf(4,6)     #function call provides two arguments and saves return value to a variable
print( myArea )     #displays myArea

###############################################################################
''''''''''''''''''
'''   TRY IT   '''
''''''''''''''''''

def area(w, h):
    return w * h
area(5,10)




###############################################################################
#---  if / elif / else statements  ---
###############################################################################
age = 16
if age < 16:       #condition will evaluate to either True or False
    print('you are not old enough to drive')      #if condition is True, execute this block
elif age >= 16 and age <= 18:       #second condition will evaluate to either True or False
    print('you may drive with adult supervision')      #if second condition is True, execute this block
else:
    print('you may drive a vehicle')      #if condition is False, execute this block
###############################################################################
''''''''''''''''''
'''   TRY IT   '''
''''''''''''''''''
price = 2000
age = 60
vetern = True
if age >= 60:
    print(price - (price * .2)) 
elif age < 60 and vetern == True:
    print(price - (price * .2))
else:
    print("no discount")





###############################################################################
#---  Boolean operations  --- RATE 2
###############################################################################
bool01 = True and False     #Boolean and operation will always be false unless both sides are true
bool02 = True or False     #Boolean
bool03 = not(True and False)     #

###############################################################################
''''''''''''''''''
'''   TRY IT   '''
''''''''''''''''''




###############################################################################
#---  Lists  --- RATE 2
in
not in
len()
max()
min()
sorted()
sum()
append()
join()
pop()
###############################################################################
myNumbers = [1, 4.8, 7, 9.2, 3, 0]       #creates list
print(myNumbers[3])     #prints the fourth number from the list
print(myNumbers[-1])     #prints the last element from the list

yourNumbers = myNumbers[1:3]    #creates a new list with the second and third values from myNumbers
altNumbers = myNumbers[:3]      #creates a new list with 1st, 2nd, and 3rd values from myNumbers
newNumbers = myNumbers[3:]      #creates a new list with 4th, 5th, and 6th values from myNumbers

matchList = 9.2 in myNumbers        #looks for a match and returns Boolean value
noMatch = 9.3 not in myNumbers      #ensures a match does not exist in list

listLength = len(myNumbers)     #counts items in list
listMax = max(myNumbers)        #returns greatest element of list
listMin = min(myNumbers)        #returns smallest element of list
listSort = sorted(myNumbers)        #returns copy of list ordered smallest to largest
listSortAgain = sorted(myNumbers, reverse=True)        #returns copy of list ordered largest to smallest
listSum = sum(myNumbers)        #returns total sum of list values

myNames = ['Jessica', 'Connie', 'Amy']
myNames.append('Grace')     #new value is added to end of list
myNames.pop()       #removes last item from the list
myNames.pop(1)      #removes second item from the list
listJoined = ", ".join(myNames)     #a string is used to join together values from list
print('Welcome aboard ' + listJoined)
###############################################################################
''' TRY IT '''
food = ['curry', 'thai', 'pizza', 'burger']
food[3]
food[-2:]
newlist = food[0:2]
print(newlist)

shopping = ['chicken', 'spinich', 'tomato', 'potato', 'sausage', 'butter']
costco = shopping[1]
print(costco)

found = input('what are you looking for? :') in shopping
print(found)
''' '''
alpha = sorted(shopping)
print(alpha)
print(len(alpha))
print(max(alpha))
nums = [1,2,3,4,50]
print(sum(nums))
nums.pop(2)
print(nums)
nums.append(4)
print(nums)

color1 = ['red', 'green', 'blue']
color2 = ['red', 'orange', 'purlple']
joined = "blue".join(color2)
print(joined)




###############################################################################
#---  Sets  --- RATE 1
set()
add()
discard()
list()
###############################################################################
idNums = set()      #creates a set
idNums.add(12345)        #adds value to set
idNums.add(12367)        #adds second value to set
idNums.add(12367)        #adds third value to set, but it is duplicate so it will not be added
idNums.discard(12345)       #removes value from set, if found
set(myNumbers)      #converts the list from line 91 above to a set
list(idNums)        #converts the set from line 121 into a list
###############################################################################
''' TRY IT '''
myset= set()
print(myset)
myset.add(12345)
print(myset)
myset.add(345678)
print(myset)
myset.add(78910)
print(myset)
''' '''
food = set()
food.add('thai')
print(food)



###############################################################################
#---  For Loop  --- RATE 2
for in
###############################################################################
cities = ['Albany', 'Chicago', 'Boulder', 'Tampa']
for city in cities:     #performs commands for each item within list
    print('Welcome to the city of ' + city)

sum = 0
for num in range(1,5):      #runs loop for numbers 1 through 4, as range is exclusive of the ending position
    sum += num
###############################################################################
 ''' TRY IT '''
this_bucket = ['fish', 'water', 'stuff', 'things']
for each_run_put_the_next_in_here in this_bucket:
    print('going to read one at a time', each_run_put_the_next_in_here)

counter = 0
for i in range(0,10):
    counter = i+1
print(counter)


''' '''   
    
sum = 0
for i in range(0,10):
    sum = i + 1
print(sum)
    
    
    
###############################################################################
#---  While Loop  --- RATE 2
while
###############################################################################
temp = 34
while temp >= 32:       #while condition is true loop will iterate
    print(temp)
    temp -= 1       #variable must change state, moving towards satisfying condition
print('it is freezing')


startValue = 0
while startValue < 20:
    startValue += 1
    if startValue == 4:     #if statement checks for a specific value
        break       #stops the flow of the while loop prematurely
print(startValue)
###############################################################################
''''''''''''''''''
'''   TRY IT   '''
''''''''''''''''''

startvalue = 0
while startvalue <20:
    startvalue +=1
    if startvalue == 4:
        break
print(startvalue)
        




###############################################################################
#---  Dictionaries  --- RATE 2
###############################################################################
studentGrades = {       #dictionary is created
    'Orfu': 83,     #first entry is added with key of 'Orfu' and value of 83
    'Bismark': 98,
    'Igor': 72
}

if 'Igor' in studentGrades:     #in verifies if key is in dictionary
    print('student is in course')

print( studentGrades.get('Bismark') )       #get method looks up value by key

for student in studentGrades:       #for loop iterates over each entry in dictionary
    print('{}, you earned {} on the final exam'.format(student, studentGrades[student]))
###############################################################################
''''''''''''''''''
'''   TRY IT   '''
''''''''''''''''''

food = {
        'thai': 8.50, 
        'pizza':10.00, 
        'burger':5.50
        }
if 'thai' in food:
    print('it costs')
print(food.get('thai'))

for i in food:
    print ('{}, costs {}'.format(i, [food]))

''' '''




###############################################################################
#---  Tuples  --- RATE 3
###############################################################################
myPhone = (877, 435, 7948)      #tuple is created with three sections of a phone number
print( 'Call WGU at {}-{}-{}'.format(myPhone[0], myPhone[1], myPhone[2]) )


###############################################################################
''''''''''''''''''
'''   TRY IT   '''
''''''''''''''''''
x = (1,2,3,4,5,6,7)
print("Step {}, Step {}, step {}".format(x[3],x[0],x[5]))





###############################################################################
#---  Reading and Writing Files  --- RATE 2
###############################################################################
#f1 = open('/my_path/my_file.txt','r')        #opens a file object for reading (read-mode is default)
#f1 = open('/my_path/my_file.txt','w')        #opens a file object for writing and deletes what is in the file previously
#f1 = open('/my_path/my_file.txt','a')        #opens a file object for appending

#f1.read()        #reads the data from file into a string
#f1.write('hello, friend')        #writes to file
#f1.readline()       #reads the next line of a file
#f1.close()       #closes file

#with open('/my_path/my_file.txt','r') as f:     #opens a file, performs operations and automatically closes file
#    my_lines = []
#    for line in f:
#        my_lines.append(line.strip())       #strip removes newline characters
###############################################################################
''''''''''''''''''
'''   TRY IT   '''
''''''''''''''''''





###############################################################################
#---  Modules & Python Standard Library--- RATE 2
import math
factorial()
floor()
ceil()
exp()
sqrt()

import random
random()
randrange()
randint()
choice()

from datetime import timedelta
timedelta()

###############################################################################
import math     #imports the math module
print('The factorial of 3 is: {}'.format(math.factorial(3)))
print('The largest integer less than or equal to 5.6 is: {}'.format(math.floor(5.6)))
print('The smallest integer less than or equal to 5.6 is: {}'.format(math.ceil(5.6)))
print('The math constant e to the power of 3 equals: {}'.format(math.exp(3)))
print('The square root of 6 is: {}'.format(math.sqrt(6)))


import random       #imports random library
print('a randomly selected element from range(start, stop, step) is: {}'.format(random.randrange(1,10,2)))
print('a random integer is (start,stop): {}'.format(random.randint(1,10)))
print('the next random floating point number in the range [0.0, 1.0) is: {}'.format(random.random()))
word_list = ['apple','banana','orange','pineapple']
print('I have randomly selected: {}'.format(random.choice(word_list)))


# Python standard library: https://docs.python.org/3/library/
# familiarize yourself with modules: csv, collections, random, string, math, os, timedelta

#from collections import defaultdict     #imports individual function from a module
#defaultdict()       #function can now be used by name

#from csv import reader as scvreader     #imports individual function from a module and assigns it a new name
#scvreader()       #function can now be used by new name

from datetime import timedelta
print('The total number of seconds is: {}'.format(timedelta(days=4).total_seconds()))

import datetime as dt  #imports library with new name
print('The current month is: {}'.format(dt.date.today().month))

###############################################################################
''' TRY IT '''
import math
math.factorial(4)

import random
print(' a randomly selected element from range start, stop, step) is :{}'.format(random.randrange(1,10, 2)))




''' '''
###############################################################################
#---  Third-Party Libraries --- RATE 2
###############################################################################
# pip install pytz     #used to install package pytz
#import pytz     #imports the package

#Useful Packages to know:
    #beautiful soup - https://www.crummy.com/software/BeautifulSoup/ - parsing HTML and XML
    #NumPy - http://www.numpy.org/ - scientific computing, multi-dimensional arrays and matrices
    #pandas - http://pandas.pydata.org/ - data manipulation and analysis
    #pillow - https://python-pillow.org/ - work with and manipulate images
    #pyglet - http://www.pyglet.org/ - multimedia library for developing games
    #pytz - http://pytz.sourceforge.net/ - works with time zone data

    
###############################################################################    
###############################################################################
## EXERCISES
###############################################################################
###############################################################################

###############################################################################
# TASK 1 - DONE
###############################################################################
"""Complete the function to return the first two items in the given list"""

def getFirstTwo(mylist):
# Student code goes here
    return(mylist[0:2])
# expected output: [8, 3]
print(getFirstTwo([8,3,5,2,10]))
# expected output: [15, 2]
print(getFirstTwo([15,2,10,12]))

''''''''''''''''''
'''   TRY IT   '''
''''''''''''''''''

def area(w, h):
    h = int(input('What is the hieght?'))
    w = int(input('What is the width?'))
    print('The area is: '+str((w * h)))
area(w,h)





###############################################################################
# TASK 2 - DONE
###############################################################################
"""
Complete the function to return the last two items in the given list
"""
def getLastTwo(mylist):
# Student code goes here
    return(mylist[-2:])
# expected output: [2, 10]
print(getLastTwo([8,3,5,2,10]))  
# expected output: [9, 12]
print(getLastTwo([15,2,9,12]))

''''''''''''''''''
'''   TRY IT   '''
''''''''''''''''''
def shopping(list):
    return list[-2:]
print(shopping(['bread', 'milk', 'carrots', 'pizza']))

###############################################################################
# TASK 3 DONE
# append()
###############################################################################
"""
Complete the function to add num1 to the end of the given list
"""
def addToEnd(mylist, num1):
# Student code goes here list.extend([x])
    mylist.append(num1)
    return mylist
# expected output: [4, 5, 6, 7]
print(addToEnd([4,5,6], 7))
 # expected output: [9, 8, 7, 6]
print(addToEnd([9,8,7], 6))

''''''''''''''''''
'''   TRY IT   '''
''''''''''''''''''

def shopping(mylist,extra):
    mylist.append(extra)
    return mylist
print(shopping(['bread', 'milk', 'carrots', 'pizza'], 'oranges'))





###############################################################################
# TASK 4 DONE
# insert( , )
###############################################################################
"""
# Complete the function to add num2 to the front of the given list
"""
# Complete the function to add num2 to the front of the given list
def addToFront(mylist, num1):
# Student code goes her
    mylist.insert(0,num1)
    return mylist

# expected output: [3, 4, 5, 6]
print(addToFront([4,5,6], 3))
 
# expected output: [10, 9, 8, 7]
print(addToFront([9,8,7], 10))


''''''''''''''''''
'''   TRY IT   '''
''''''''''''''''''
def shopping(mylist, extra):
    mylist.insert(1,extra)
    return mylist
print(shopping([1,2,3,4],5))




###############################################################################
# TASK 5 DONE pop(index)
# pop()
###############################################################################
"""
Complete the function to remove the first item in the given list
"""
# Complete the function to remove the first item in the given list
def removeFirst(mylist):
# Student code goes here
    mylist.pop(0)
    return mylist
# expected output: [7, 8, 9]
print(removeFirst([6,7,8,9]))
 
# expected output: [2, 3, 4]
print(removeFirst([1,2,3,4]))

''''''''''''''''''
'''   TRY IT   '''
''''''''''''''''''
def grocery(mylist):
    mylist.pop(1)
    return mylist
print(grocery(['pizza', 'thai', 'fruit']))




###############################################################################
# TASK 6 Done pop(index)
###############################################################################
"""
Complete the function to remove the third item in the given list
"""
# Complete the function to remove the third item in the given list
def removeThird(mylist):
# Student code goes here
    mylist.pop(2)
    return mylist
# expected output: [6, 7, 9]
print(removeThird([6,7,8,9]))
 
# expected output: [1, 2, 4]
print(removeThird([1,2,3,4]))

###############################################################################
# TASK 7 DONE
# split()
###############################################################################
"""
Complete the function to print all of the words in the given string
"""

def printWords(mystring):
# Student code goes here
    mystring = list(mystring.split(" "))
    return mystring
    
# expected output: ['WGU', 'College', 'of', 'IT']
printWords('WGU College of IT')    
    
# expected output: ['Night', 'Owls', 'Rock']
printWords('Night Owls Rock')
###############################################################################
# TASK 8 DONE
# strip()
###############################################################################
"""
Complete the function to remove trailing spaces from the first string
and leading spaces from the second string and return the combined strings
"""
def removeSpaces(string1, string2):
# Student code goes here
    string1 = string1.strip()
    string2 = string2.strip()
    return (string1, string2)
# expected output: WGU Rocks-You know it!
print(removeSpaces('WGU Rocks    ', '  -You know it!'))
    
# expected output: Welcome WGU-IT Students
print(removeSpaces('Welcome WGU ', ' -IT Students'))

''''''''''''''''''
'''   TRY IT   '''
''''''''''''''''''

def ponum(loc, date, seq):
    location = loc.strip()
    dates = date.strip()
    sequence = seq.strip()
    po = (location + dates + seq)
    return (po)
print(ponum('  110 ', ' 010120 ', '004 '))


###############################################################################
# TASK 9 - DONE
# round()
# round up Ceil()
# round down Floor()
###############################################################################
""""
Complete the function to print the specified hourly rate with two decimals
"""
def displayHourlyRate(rate):
# Student code goes here
    print (round(rate,2))
# expected output: $34.79
displayHourlyRate(34.789123)    
# expected output: $24.12
displayHourlyRate(24.123456)

''''''''''''''''''
'''   TRY IT   '''
''''''''''''''''''
def sales(average):
    print(round(average,2))
sales(578.9876)





###############################################################################
# TASK 10  DONE
# isupper()
###############################################################################
"""
return the number of uppercase letters in the given string
"""
def countUpper(mystring):
# Student code goes here
    countu = 0
    for i in mystring:
     if (i.isupper()):
         countu += 1
    return countu
# expected output: 4
print(countUpper('Welcome to WGU'))
 
# expected output: 2
print(countUpper('Hello, Mary')) 

''''''''''''''''''
'''   TRY IT   '''
''''''''''''''''''

def counter(mystring):
    count = 0
    for i in mystring:
        if (i.isupper()):
            count += 1
    return count
print(counter("Test In Here"))
        


def counter(mystring):
    count = 0
    for i in mystring:
        if (i.isupper()):
            count += 1
    return count
counter("TTTTe")


###############################################################################
# TASK 11  CALENDAR MONTH NAME FROM NUMBER DONE
# import calendar
# calendar.month_name[#])
###############################################################################
"""
Complete the function to print the full name of the month using the calendar 
library
"""
import calendar

def printMonthName(monthNum):
# Student code goes here
    print(calendar.month_name[monthNum])
# expected output: March
printMonthName(3)
 
# expected output: November
printMonthName(11)
import calendar
from datetime import date

def monthname(monthnum):
    return (calendar.month_name[monthnum])
print(monthname(3))

###############################################################################
# TASK 12 DONE get random range
# import random
# random.randrange(start, end)
# range()
###############################################################################
"""
Complete the following function to return a random number between 5 and 8 
exclusive
"""
import random

def getRandom():
# Student code goes here
   return random.randrange(5,8)
# expected output: You should only get 5s, 6s, and 7s
for i in range(10):
    print(getRandom())
 
import random

def getrandom():
    return random.randrange(5,8)
for i in range(20):
    print(getrandom())
    
###############################################################################
# TASK 13 DONE replace a word with another word
# replace()
###############################################################################
"""
Complete the function to replace the word WGU with Western Governors University 
and print the new string
"""
def replaceWGU(mystring):
# Student code goes here
    mystring = mystring.replace('WGU', 'Western Governors University')
    print(mystring)
# expected output: Western Governors University Rocks
replaceWGU('WGU Rocks')
    
# expected output: Hello, Western Governors University
replaceWGU('Hello, WGU')

def replacemilk(item):
    item = item.replace("Milk", "Tequila")
    return(item)
print(replacemilk("Milk tastes great"))



###############################################################################
# TASK 14 DONE replace a word if found
###############################################################################
"""
Complete the function to remove the word WGU from the given string
ONLY if it's not the first word and return the new string
"""

def removeWGU(mystring):
# Student code goes here
   
    if mystring[:3] != 'WGU':
        mystring = mystring.replace('WGU','')
        return(mystring)
    else:
        return('do nothing')

# expected output: WGU Rocks
print(removeWGU('WGU Rocks'))
    
# expected output: Hello, John
print(removeWGU('Hello, WGUJohn'))


###############################################################################
# TASK 15 print first X number of  a string
###############################################################################
"""
Complete the function to print the first X number of characters in the 
given string
"""
def printFirst(mystring, x):
# Student code goes here
    mystring = mystring[0:x]
    print(mystring)
# expected output: WGU
printFirst('WGU College of IT', 3)    
 
# expected output: WGU College
printFirst('WGU College of IT', 11)

''''''''''''''''''
'''   TRY IT   '''
''''''''''''''''''
def printFirst(mystring,x):
    mystring = mystring[0:x]
    return mystring
printFirst("Test",2)
###############################################################################
# TASK 16 find a word in a string return True
# in
# not in
###############################################################################
"""
Complete the function to return True if the word WGU exists in the given string 
otherwise return False
"""
def containsWGU(mystring):
# Student code goes here
    if 'WGU' in mystring:
        return True
    else:
        return False
# expected output: True
print(containsWGU('WGU College of IT'))
    
# expected output: False
print(containsWGU('Night Owls Rock'))

''''''''''''''''''
'''   TRY IT   '''
''''''''''''''''''

def test(mystring):
    if 'test' in mystring:
        print('found it')
    else:
        print('keep looking')
test('testing')


###############################################################################
# TASK 17
###############################################################################
"""
Complete the function to return the last X number of characters in the given 
string
"""
def getLast(mystring, x):
# Student code goes here
    return(mystring[-x:])
   
# expected output: IT
print(getLast('WGU College of IT', 2))
 
# expected output: College of IT
print(getLast('WGU College of IT', 13))


###############################################################################
# TASK 18 integer for days and prints number of seconds in those days
# import datetime
# from datetime import timedelta
# timedelta(days = x).total_seconds()
###############################################################################
'''
Complete the function that takes as input an integer for a number of days and 
prints the total number of seconds in that number of days
'''
import datetime

def currentDate(x):
# Student code goes here
 from datetime import timedelta
 print(timedelta(days=x).total_seconds())

#print('The total number of seconds is: {}'.format(timedelta(days=4).total_seconds()))

currentDate(4) #expected outcome: The total number of seconds is 345600.0.
currentDate(7) #expected outcome: The total number of seconds is 604800.0.

''''''''''''''''''
'''   TRY IT   '''
''''''''''''''''''



###############################################################################
# TASK 19
# import calendar
# isleap()
###############################################################################
"""
Complete the function to return the number of leap years in the list
"""
import calendar

# Complete the function to return the number of leap years in the list
def countLeapYears(yearList):
    
    j=0
    for i in yearList:
        if calendar.isleap(int(i)):
            j += 1
    return j
# Student code goes here
 
# expected output: 2
print(countLeapYears([2001, 2018, 2020, 2090, 2233, 2176, 2200, 2982]))
 
# expected output: 4
print(countLeapYears([2001, 2018, 2020, 2092, 2204, 2176, 2200, 2982]))


''''''''''''''''''
'''   TRY IT   '''
''''''''''''''''''



###############################################################################
# TASK 20 Done timedelta
# import datetime
# (somedate + datetime.timedelta(days = x))
###############################################################################
"""
Complete the function to add 90 days to the given date and return the new date
"""
import datetime

# Complete the function to add 90 days to the given date and return the 

def add90Days(someDate):
# Student code goes here
   return(someDate + datetime.timedelta(days = 90))
# expected output: 2018-12-30
print(add90Days(datetime.date(2018, 10, 1)))
 
# expected output: 2015-05-12
print(add90Days(datetime.date(2015, 2, 11)))

###############################################################################
# TASK 21
# from math import e, ceil
# ceil()
###############################################################################
"""
Complete the function that takes an integer as input, multiplies by e, and 
returns result rounded up. e = eulers number 2.71828
"""
from math import e,ceil

def mathCalculation(x):
# Student code goes here
    return  ceil(x*e)
    
#expected outcome: 9
print(mathCalculation(3))    


#expected outcome: 25
print(mathCalculation(9))

# check it
ceil(3*2.71828)
ceil(9*2.71828)
###############################################################################
# TASK 22
# import random as r
###############################################################################
"""
Complete the function that takes a list as input and returns a randomized item 
from that list
"""
import random as r

def selection(x):
# Student code goes here

    x = r.choice(x)
    return(x)
print(selection(['apple','banana','orange','grape']))
print(selection([7,5,3,9,12,4,8,10]))

###############################################################################
# TASK 23   DONE Factorial
###############################################################################
"""
Complete the function that takes an integer as input and returns the factorial 
of that integer
"""

from math import factorial

def calculate(x):
# Student code goes her
#    for i in range(1, x):
#        x *= i
    return(math.factorial(x))
   # return x

 
print(calculate(3)) #expected outcome: 6
print(calculate(9)) #expected outcome: 362880


###############################################################################
# TASK 24 - DONE print list as a sentance
###############################################################################
"""
Complete the function to combine the words into a sentence and return a string
""" 
def combineWords(words):
# Student code goes here
    return (' '.join(words))
# expected output: WGU College of IT
print(combineWords(['WGU', 'College', 'of', 'IT']))
    
# expected output: Night Owls Rock
print(combineWords(['Night', 'Owls', 'Rock']))


###############################################################################
# TASK 25 DONE print key=value from dictionary
###############################################################################
"""
Complete the function to print every key and value
"""
# Complete the function to print every key and value
def printDict(mydict):
# Student code goes here num_calories = dict(Coke=90, Coke_zero=0, Pepsi=94)
    for x in mydict:
        print( x+"="+mydict[x])
# expected output: 
#        tomato=red
#        banana=yellow
#        lime=green
printDict({'tomato': 'red', 'banana': 'yellow', 'lime': 'green'})
 
# expected output: 
#        Brazil=Brasilia
#        Ireland=Dublin
#        Indonesia=Jakarta
printDict({'Brazil': 'Brasilia', 'Ireland': 'Dublin', 'Indonesia': 'Jakarta'})

###############################################################################
# TASK 26 remove dictionary item if it exists
###############################################################################
"""
Complete the function to remove a dictionary item if it exists
"""
# Complete the function to remove a dictionary item if it exists
def removeDictItem(mydict, key):
    mydict.pop(key)
    return mydict
           

# expected output: {'tomato': 'red', 'lime': 'green'}
print(removeDictItem({'tomato': 'red', 'banana': 'yellow', 'lime': 'green'} , 'banana'))
 
# expected output: {'Brazil': 'Brasilia', 'Ireland': 'Dublin', 'Indonesia': 'Jakarta'}
print(removeDictItem({'Brazil': 'Brasilia', 'Ireland': 'Dublin', 'Indonesia': 'Jakarta'},'Cameroon'))


###############################################################################
# TASK 27  Done print if value exists otherwise print string
###############################################################################
"""
Complete the function to return a dictionary value if it exists or return 
Not Found if it doesn't existWhen get() is called, Python checks if the 
specified key exists in the dict. If it does, then get() returns the value of 
that key. If the key does not exist, then get() returns the value specified in 
the second argument to get().
"""
def findDictItem(mydict, key):
 #   mydict = mydict.get(key)
      
    if key in mydict.keys(): 
       return(mydict[key]) 
    else: 
        return("Not present") 

# expected output: yellow
print(findDictItem({'tomato': 'red', 'banana': 'yellow', 'lime': 'green'} , 'banana'))
 
# expected output: Not Found
print(findDictItem({'Brazil': 'Brasilia', 'Ireland': 'Dublin', 'Indonesia': 
    'Jakarta'},'Cameroon'))
    
###############################################################################
# TASK 28 combine 2 lists into 1
###############################################################################
"""
Complete the function to return a new list containing the first two and last 
two items in the given list
"""
def getFirstTwoAndLastTwo(mylist):
# Student code goes here
   return (mylist[:2] + mylist[-2:])
# expected output: [8, 3, 19, 1]
print(getFirstTwoAndLastTwo([8,3,7,15,2,10,19,1]))
 
# expected output: [7, 15, 3, 5]
print(getFirstTwoAndLastTwo([7,15,2,10,19,1,3,5]))


###############################################################################
# TASK 29 sorting list based on conditions True or False
###############################################################################
"""
Complete the function to order the values in the list. If ascending is true 
then order lowest to highest otherwise sort highest to lowest
"""
# Complete the function to order the values in the list
# if ascending is true then order lowest to highest
# if ascending is false then order highest to lowest
def sortList(mylist, ascending):
# Student code goes here
    if ascending == True:
        return sorted(mylist)
        
    else:
        return sorted(mylist, reverse = True)
 
# expected output: [4, 12, 19, 33]
print(sortList([19,4,33,12], True))
 
# expected output: [33, 19, 12, 4]
print(sortList([19,4,33,12], False))

###############################################################################
# TASK 30 create a dictionary 
###############################################################################
"""
Complete the function to return a dictionary using list1 as the keys and list2 
as the values
"""
def createDict(list1, list2):
# Student code goes here
    x = dict(zip(list1, list2))
    print(x)
               
# expected output: {'tomato': 'red', 'banana': 'yellow', 'lime': 'green'}  
print(createDict(['tomato', 'banana', 'lime'], ['red','yellow','green']))        
 
# expected output: 
{'Brazil': 'Brasilia', 'Ireland': 'Dublin', 'Indonesia': 'Jakarta'}
print(createDict(['Brazil', 'Ireland', 'Indonesia'], ['Brasilia','Dublin','Jakarta']))


###############################################################################
# TASK 31 
###############################################################################
"""
Complete the function to print the full name of the day of the week
"""
import calendar, datetime

def printWeekdayName(year, month, day):
    
# Student code goes here
    days =["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] 
    dayNumber = datetime.date(year, month, day).weekday()
    return (days[dayNumber]) 
# expected output: Friday    
printWeekdayName(2001, 8, 31)
 
# expected output: Monday
printWeekdayName(2018, 10, 1)