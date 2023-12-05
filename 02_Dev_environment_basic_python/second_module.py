# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 07:00:27 2020

@author: Msmorris
"""
###############################################################################
#--- MULTIPLE VARIABLE DECLERATION  ---  RATE 3
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





###############################################################################
#---  DATA TYPES --- RATE 2
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





###############################################################################
#---  ARITHMATIC OPERATORS  --- RATE 2
###############################################################################
print( 2 + 2 )      #addition
print( 2 - 2 )      #subtraction
print( 2 ** 2 )      #power of
print( 5 % 2 )      #modulus
print( 2.1 / 2 )      #division, always results in float
print( 2.1 // 2 )      #division, always results in integer

10/3
10//3




###############################################################################
#---  assignment/reassignment operators  --- RATE 2
###############################################################################
myAssignment = 10       #assignment
myAssignment += 5       #adds
myAssignment -= 5       #subtracts
myAssignment *= 5       #multiples
myAssignment /= 5       #divides





###############################################################################
#---  comparison operators  --- RATE 4
###############################################################################
myNum = 4
print( myNum < 2 )       #less than
print( myNum > 2 )       #greater than
print( myNum <= 4 )       #less than or equal to
print( myNum >= 2 )       #greater than or equal to
print( myNum == 2 )       #equal to
print( myNum != 2 )       #not equal to
###############################################################################




###############################################################################
#---  string operations  --- RATE 1
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





###############################################################################
#---  function with both input and output  --- RATE 2
###############################################################################
def areaOf(width,height):       #function that accepts two inputs
    return width * height       #function body outputs calculated area

myArea = areaOf(4,6)     #function call provides two arguments and saves return value to a variable
print( myArea )     #displays myArea

###############################################################################





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





###############################################################################
#---  Boolean operations  --- RATE 2
###############################################################################
bool01 = True and False     #Boolean and operation will always be false unless both sides are true
bool02 = True or False     #Boolean
bool03 = not(True and False)     #

###############################################################################





###############################################################################
#---  Lists  --- RATE 2
###############################################################################
myNumbers = [1, 4.8, 7, 9.2, 3, 0]       #creates list
print(myNumbers[3])     #prints the fourth number from the list
print(myNumbers[-1])     #prints the last element from the list

yourNumbers = myNumbers[1:3]        #creates a new list with the second and third values from myNumbers
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





###############################################################################
#---  Sets  --- RATE 1
###############################################################################
idNums = set()      #creates a set
idNums.add(12345)        #adds value to set
idNums.add(12367)        #adds second value to set
idNums.add(12367)        #adds third value to set, but it is duplicate so it will not be added
idNums.discard(12345)       #removes value from set, if found
set(myNumbers)      #converts the list from line 91 above to a set
list(idNums)        #converts the set from line 121 into a list
###############################################################################





###############################################################################
#---  For Loop  --- RATE 2
###############################################################################
cities = ['Albany', 'Chicago', 'Boulder', 'Tampa']
for city in cities:     #performs commands for each item within list
    print('Welcome to the city of ' + city)

sum = 0
for num in range(1,5):      #runs loop for numbers 1 through 4, as range is exclusive of the ending position
    sum += num
###############################################################################
    
    
    
    
    
###############################################################################
#---  While Loop  --- RATE 2
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





###############################################################################
#---  Tuples  --- RATE 3
###############################################################################
myPhone = (877, 435, 7948)      #tuple is created with three sections of a phone number
print( 'Call WGU at {}-{}-{}'.format(myPhone[0], myPhone[1], myPhone[2]) )


###############################################################################






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





###############################################################################
#---  Modules & Python Standard Library--- RATE 2
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