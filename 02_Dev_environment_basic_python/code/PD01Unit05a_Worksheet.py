

###############################################################################
##                       PYTHON FOR DATA I - UNIT 5
##                          WORKING WITH FILES                               ##
# Covered in this Unit
# mkdir()
# import
# getcwd()
# chdir()
# open file
# Read file
# write to file
# append to file
# write to multiple lines
# write to multiple columns
# close()
# listdir()
# shutil(source,destination)

###############################################################################

'''
First step in working with files is being able to navigate to your files or 
save your files using python programing rather than your file explorer.
We are going to:
    Make a directory
    Change our directory
    Create, open, write to and read a file
    Move files from 1 folder to another)
lets first start by reading some files in. You will need some files to load. 
There are several files online to pick from. This can cause lots of errors
troubleshooting and can be frustrating at times. Keep working at it you will get
it.  
'''

# Set your OS path where your files are stored

# getcwd() What is your Current Working directory 
import os
os.getcwd()

# chdir() Change your default working directory - you dont want to do this often
import os
from pathlib import Path

path = Path('//Users//Matthew//Desktop//GA//00_DATA_SETS//DEV')
os.chdir(path)

## EXERCISE
# Get Current working directory
# Create a new directory called TEST *instead of copy paste use the prior code
# as reference.
##





# Make a directory
import os
dirName = '/Users/Matthew/Desktop/GA/00_DATA_SETS/DEV'
os.mkdir(dirName)


'''
Homework - how would you: Delete, Rename or move a Directory
use google or python.org to research and figure this out
'''




# listdir() List all of the files in your directory


# time to create files, read files and write to files

a = open("new_file.csv","w+") # Open a file to write to 'W' or create one '+'

# open your folder and see if the file was created

a.write("First line in my doc.") # Write a line to the document
a.close() # Close file


#Open file into variable
b = open("new_file.csv","r")
lines = b.readlines() # use readlines to readlines into a variable
b.close()
print(lines) # output results to the screen

# Iterate over each line - Once you have completed the entire course
print('\nCalculating average...')
total = 0
for ln in lines:
    total += int(ln)
# Compute result
avg = total/len(lines)
print('Average value:', avg)

# Remove files
my_file = open('myfile.txt', 'r')
# ...
file_info = os.stat('myfile.txt')
# ...
os.remove('myfile.txt')

##############################
## 12.06 THE 'with' STATEMENT
##############################
"""
A with statement can be used to open a file, execute a block of statements, 
and automatically close the file when complete. 
"""
with open('myfile.txt', 'r') as myfile:
    # Statement-1
    # Statement-2
    # ...
    # Statement-N




# Write several lines to a file and read them
		
with open("multiline.csv", 'w+') as t:			

# Use Raw_inputs to create 3 lines of in your file
line1 = "line 1"
line2 = "line 2"
line3 = "line 3"

t.write(line1)
t.write("\n")   # \n is a carriage return that we are writing to file
t.write(line2)
t.write("\n")
t.write(line3)
t.write("\n")
t.close()

a = open("multiline.csv","r")
b = a.readlines()
a.close()
(b)



# Find your file using windows manually

''' Results should look like this
line1 = "line 1"
line2 = "line 2"
line3 = "line 3"

Rewrite and update your code putting commas and more information after each line
Then review your file again to see how it behaves
Example

line1 = "line 1,Red"
line2 = "line 2,Blue"
line3 = "line 3,Green, 4.52"

'''

## EXERCISE
# Create a file called names with names of friends family actors or fictional characters
# column for First Name, Last Name, age, Notes
##



# 'a+' Next append a line to the end of the file
# Open the file for appending text to the end
t= open("multiline.csv","a+")
t.write("append_test, 4")
t.close()
(t)

## EXERCISE
# Reopen your name file and add a new name to the file 
##




# shutil(src,dst) Move files
'''
1. Create a two folders on your desktop 1 called Hotel and 1 called Conference. 
2. Create a file in your hotel folder called passenger.txt
3. Use shutil to move your passenger file back and forth from your Hotel to Conference
4. Check your folders to validate the file has moved, then try moving it back
'''
import shutil
shutil.move('C://Users//Matthew//Desktop//Hotel//passenger.txt', 'C://Users//Matthew//Desktop//Conference//passenger.txt')



'''
We will be using a lot of variables in our code loading your file path into a
variable will make it more flexible
'''

import shutil
hotel = 'C://Users//Matthew//Desktop//Hotel//passenger.txt'
conference = 'C://Users//Matthew//Desktop//Conference//passenger.txt'
shutil.move(conference,hotel)

## EXERCISE
# Move sales.csv, products.csv, stores.csv, counties.csv into the folder
# Iowa Liquor Sales'
##
shutil.move('C://Users//Matthew//Desktop//GA//00_DATA_SETS//counties.csv',
            'C://Users//Matthew//Desktop//GA//00_DATA_SETS//iowaliquor//counties.csv')

shutil.move('C://Users//Matthew//Desktop//GA//00_DATA_SETS//sales.csv',
            'C://Users//Matthew//Desktop//GA//00_DATA_SETS//iowaliquor//sales.csv')

shutil.move('C://Users//Matthew//Desktop//GA//00_DATA_SETS//products.csv',
            'C://Users//Matthew//Desktop//GA//00_DATA_SETS//iowaliquor//products.csv')



# open readlines 
a = open("titanic.csv") # you may need to work with your path
a.readlines()




## EXERCISE
# open and read each of the files in the iowa liquor sales database
##
import os
os.getcwd()
os.chdir
a = open("products.csv")
a.readlines()


"""
A programmer can also use the csv module to write text into a csv file, using 
a writer object. The writer object's writerow() and writerows methods can be 
used to write a list of strings into the file as one or more rows. 
"""
import csv

row1 = ['100', '50', '29']
row2 = ['76', '32', '330']

with open('grades.csv', 'w') as csvfile:
    grades_writer = csv.writer(csvfile)

    grades_writer.writerow(row1)
    grades_writer.writerow(row2)

    grades_writer.writerows([row1, row2])

# Reading each row of a csv file after completing course
import csv

with open('grades.csv', 'r') as csvfile:
    grades_reader = csv.reader(csvfile, delimiter=',')

    row_num = 1
    for row in grades_reader:
        print('Row #{}:'format.row_num, row)
        row_num += 1
        
        
Below is a sample exercise. You should copy the entire code snippet into your 
Python editor. Your code should be placed in the area that says "student code 
goes here" highlighted in yellow. This is inside the function. When you run 
this entire code snippet, there are test cases below your code. Your output 
should match the expected output.

# Complete the function to print the first X number of characters in the 
given string
def printFirst(mystring, x):
# Student code goes here
 
# expected output: WGU
printFirst('WGU College of IT', 3)    
 
# expected output: WGU College
printFirst('WGU College of IT', 11)

############################################
## ADDITIONAL EXERCISES
############################################

# EXERCISE
'''return the directory name only from the given file name'''

import os

# Complete the function to return the current working directory
def getCurrentDirectory():
# Student code goes here
 
# expected output: /tmp

print(getCurrentDirectory())


# EXERCISE
'''return the directory name only from the given file name '''

import os

# Complete the function to return the directory name only from the given file 
name
def getDirectoryName(fileName):
# Student code goes here
 
# expected output: /var/www
print(getDirectoryName("/var/www/test.html"))
 
# expected output: /var/www/apple
print(getDirectoryName("/var/www/apple/test.html"))

# EXERCISE
'''return the file name part only from the given file name'''

import os

# Complete the function to return the file name part only from the given file 
name
def getFileName(fileName):
# Student code goes here
 
# expected output: test.html
print(getFileName("/var/www/test.html"))
 
# expected output: names.txt
print(getFileName("/var/www/apple/names.txt"))

# EXERCISE
'''return the directory name only from the given file name '''

import os

# Complete the function to create the specified file and return the file name
def createFile(filename):
# Student code goes here
 
# expected output: True
createFile("test.txt")
print(os.path.exists("test.txt"))

# EXERCISE

'''print all files in the given directory'''

import os

# Complete the function to print all files in the given directory
def printFiles(someDirectory):
# Student code goes here
    
# expected output: main.py    
# if using PyFiddle.io otherwise it varies
printFiles(os.getcwd())

# EXERCISE
'''return FILE if the given path is a file or return DIRECTORY if the given 
path is a directory or return NEITHER is it's not a file or directory
'''
import os

# Complete the function to return FILE if the given path is a file
# or return DIRECTORY if the given path is a directory
# or return NEITHER is it's not a file or directory
def whatIsIt(somePath):
# Student code goes here
 
# expected output: DIRECTORY
print(whatIsIt(os.getcwd()))
 
# expected output: FILE
print(whatIsIt(os.listdir(os.getcwd())[0]))
 
# expected output: NEITHER
print(whatIsIt('apple.pie.123.txt'))

# EXERCISE

''' read the contents of the specified file and print the contents'''

import os

# Complete the function to read the contents of the specified file and print 
the contents
def printFileContents(filename):
# Student code goes here
 
# expected output: Hello
with open("test.txt", 'w') as f: 
f.write("Hello")
printFileContents("test.txt")

# EXERCISE
''' append the given new data to the specified file then print the contents of 
the file '''

import os

# Complete the function to append the given new data to the specified file 
then print the contents of the file
def appendAndPrint(filename, newData):
# Student code goes here
 
# expected output: Hello World
with open("test.txt", 'w') as f: 
f.write("Hello ")



''' PROJECT EXERCISE 
Remember the first exercise. We are going to do this again but this time
load that information into a file. Use this unit to help you:
    
Create a file that lists all the skills you have learned so far
rate yourself for each skill in a seperate column next to the skill
0 = Don't know
1 = Aquiring knowledge
2 = Can apply with 80% help from Google
3 = Can apply with 20% help from Google
4 = Can teach <20% help from Google
5 = Can design, review, optimize


As you code you will think "there has to be a faster way!!!" There is but 
practice the syntax
You may also come up with additional ideas like" what is my average score?"
Or what is my total average score by unit?"
We will continue to address various topics to help you code ideas like these
but be sure to log all ideas as you code for later enhancements. 

This Project will grow and be designed and redesigned several different ways
as you progress and revist.'''




###############################################################################
##                               BONUS                                       ## 
## Pandas reading files  , Connecting to AWS                                 ##
###############################################################################
'''
Pandas is something we will explore more in Python for Data III
However here is a small look into how Pandas can read files

Read Data From a file
Lets take a look at what the code is going to do. with most code you have to 
be able to read it backwards. Yoda talk. so reading this backwards we are : 
taking a counties.csv file and reading it using a read_csv functions from 
pd(pandas) and then loading that data into a variable called a. 
a = pd.read_csv('~/Desktop/DataSets/counties.csv')
You will want to adjust the link to navigate to where your file is located.'''

# read in the drinks data
import pandas as pd
a = pd.read_csv('~Matthew\Desktop\Datasets\counties.csv')
a
## 
# Read in the data sets products, sales, stores
##

'''
After completing this course try working with this code to create a folder
import os

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
        

# Example
createFolder('./data/')
# Creates a folder in the current directory called data




###############################################################################
##                   Connect to AWS and Perform a Select                     ##       
## you may need to install psycopg2 using anaconda prompt  and               ##
## conda install psycopg2      
## Connection to AWS is available per General Assembly                       ##
###############################################################################
''' This example shows how to connect to a database, and then obtain and use a 
cursor object to retrieve records from a table.'''

import psycopg2
import sys
import pprint
import pandas as pd 
 

#Define our connection stri
conn_string = "host='analyticsga.cuwj8wuu6wbh.us-west-2.rds.amazonaws.com'dbname='iowa_liquor_sales_database' user='analytics_student' password='analyticsga'"
 
# print the connection string we will use to connect
 
# get a connection, if a connect cannot be made an exception will be raised here
conn = psycopg2.connect(conn_string)
 
# conn.cursor will return a cursor object, you can use this cursor to perform queries
cursor = conn.cursor()
print ("Connected!\n")
 
df = pd.read_sql_query('select item_no from products', conn)
df



