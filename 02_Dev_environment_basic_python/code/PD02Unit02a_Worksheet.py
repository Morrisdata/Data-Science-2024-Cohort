# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 20:35:31 2021

@author: Matth
"""
######################################
## ITERATING OVER A DICTIONARY
######################################
"""
Dictionaries can contain objects of arbitrary type, even other containers such 
as lists and nested dictionaries. For example, my_dict['Jason'] = ['B+', 'A-'] 
creates an entry in my dict whose value is a list containing the grades of the 
student 'Jason'. 
"""
student_grades = {}  # Create an empty dict
grade_prompt = "Enter name and grade (Ex. 'Bob A+'):"
menu_prompt = ("1. Add/modify student grade\n"
                "2. Delete student grade\n"
                "3. Print student grades\n"
                "4. Quit\n")

while True:  # Exit when user enters no input
    command = input(menu_prompt).lower().strip()
    if command == '1':
        name, grade = input(grade_prompt).split()
        # ...
    elif command == '2':
        # ...
    elif command == '3':
        # ...
    elif command == '4':
        break
    else:
        print('Unrecognized command.')

## EXERCISE Delete from Dictionary
# Delete Prussia from country_capital. Sample output for the given program:        

country_capital = {'Spain': 'Madrid', 'Togo': 'Lome', 'Prussia': 'Konigsberg'}
''' Your solution goes here '''

print('Prussia deleted?', end=' ')
if 'Prussia' in country_capital:
    print('No.')
else:
    print('Yes.')
    

"""
As usual with containers, a common programming task is to iterate over a 
dictionary and access or modify the elements of the dictionary. 
A for loop can be used to iterate over a dictionary object, the loop variable 
being set to a key of an entry in each iteration. The ordering in which the 
keys are iterated over is not necessarily the order in which the elements were 
inserted into the dictionary. The Python interpreter creates a hash of each 
key. A hash is a transformation of the key into a unique value that allows 
the interpreter to perform very fast lookup. Thus, the ordering is actually 
determined by the hash value, but such hash values can change depending on the 
Python version and other factors.
"""
'''EXAMPLE a for loop over a dictionary retrieves each key in a dictionary'''
for key in dictionary:  # Loop expression
    # Statements to execute in the loop

#Statements to execute after the loop
    
"""
The dict type also supports the useful methods items(), keys(), and values() 
methods, which produce a view object. A view object provides read-only access 
to dictionary keys and values. A program can iterate over a view object to 
access one key-value pair, one key, or one value at a time, depending on the 
method used. A view object reflects any updates made to a dictionary, even if 
the dictionary is altered after the view object is created. 


    dict.items() – returns a view object that yields (key, value) tuples.
    dict.keys() – returns a view object that yields dictionary keys.
    dict.values() – returns a view object that yields dictionary values.

The following examples show how to iterate over a dictionary using the above 
methods: 
"""
## dict.items()
num_calories = dict(Coke=90, Coke_zero=0, Pepsi=94)
for soda, calories in num_calories.items():
    print('%s: %d' % (soda, calories))
## dict.keys()
num_calories = dict(Coke=90, Coke_zero=0, Pepsi=94)
for soda in num_calories.keys():
    print(soda)
## dict.values()
num_calories = dict(Coke=90, Coke_zero=0, Pepsi=94)
for soda in num_calories.values():
    print(soda)
"""
When a program iterates over a view object, one result is generated for each 
iteration as needed, instead of generating an entire list containing all of the 
keys or values. Such behavior allows the interpreter to save memory. Since 
results are generated as needed, view objects do not support indexing. 
A statement such as my_dict.keys()[0] produces an error. Instead, a valid 
approach is to use the list() built-in function to convert a view object into 
a list, and then perform the necessary operations. The example below converts 
a dictionary view into a list, so that the list can be sorted to find the first 
two closest planets to Earth. 
"""

''' EXAMPLE use list() to convert view objects into lists '''
solar_distances = dict(mars=219.7e6, venus=116.4e6, jupiter=546e6, pluto=2.95e9)
list_of_distances = list(solar_distances.values())  # Convert view to list

sorted_distance_list = sorted(list_of_distances)
closest = sorted_distance_list[0]
next_closest = sorted_distance_list[1]

print('Closest planet is %.4e' % closest)
print('Second closest planet is %.4e' % next_closest)

"""
The dict.items() method is particularly useful, as the view object that is 
returned produces tuples containing the key-value pairs of the dictionary. 
The key-value pairs can then be unpacked at each iteration, similar to the 
behavior of enumerate(), providing both the key and the value to the loop body 
statements without requiring extra code. 
"""

'''EXAMPLE iterating over a dictionary:Grade book'''
"""
 Write a program that uses the keys(), values(), and/or items() dict methods to 
 find statistics about the student_grades dictionary. Find the following:

    Print the name and grade percentage of the student with the highest total 
    of points.
    Find the average score of each assignment.
    Find and apply a curve to each student's total score, such that the best 
    student has 100% of the total points.

"""
# student_grades contains scores (out of 100) for 5 assignments
student_grades = {
    'Andrew': [56, 79, 90, 22, 50],
    'Nisreen': [88, 62, 68, 75, 78],
    'Alan': [95, 88, 92, 85, 85],
    'Chang': [76, 88, 85, 82, 90],
    'Tricia': [99, 92, 95, 89, 99]
}

# Print each key in the dictionary my_dict()
for key in my_dict.keys():
    print key()
#Change all negative values in my_dict() to 0
for key, value in my_dict.items():
    if value < 0:
        my_dict[key] = 0
# Print twice the value of every value in my_dict
for v in my_dict.values():
    print(2 * v)
    
###EXERCISE REPORT COUNTRY POPULATION###
"""
Write a loop that prints each country's population in country_pop. Sample 
output for the given program:

United States has 318463000 people.
India has 1247220000 people.
Indonesia has 252164800 people.
China has 1365830000 people.
"""
country_pop = {
    'China':         1365830000,
    'India':         1247220000,
    'United States': 318463000,
    'Indonesia':     252164800
} # country populations as of 2014

''' Your solution goes here '''

    print(country, 'has', pop, 'people.')   


#############################
## DICTIONARY NESTING
#############################

"""
A dictionary may contain one or more nested dictionaries, in which the 
dictionary contains another dictionary as a value. Consider the following code: 
"""
students = {}
students ['Jose'] = {'Grade': 'A+', 'StudentID': 22321}
(students)
print('Jose:')
print(' Grade: %s' % students ['Jose']['Grade'])
print(' ID: %d' % students['Jose']['StudentID'])

"""


The variable students is first created as an empty dictionary. An indexing 
operation creates a new entry in students with the key 'Jose' and the value of 
another dictionary. Indexing operations can be applied to the nested dictionary 
by using consecutive sets of brackets []: 
    The expression students['Jose']['Grade'] first obtains the value of the key 
    'Jose' from students, yielding the nested dictionary. The second set of 
    brackets indexes into the nested dictionary, retrieving the value of the 
    key 'Grade'.

Nested dictionaries also serve as a simple but powerful data structure. A data 
structure is a method of organizing data in a logic and coherent fashion. 
Actually, container objects like lists and dicts are already a form of a data 
structure, but nesting such containers provides a programmer with much more 
flexibility in the way that the data can be organized. Consider the simple 
example below that implements a gradebook using nested dictionaries to organize 
students and grades.
"""
''' EXAMPLE storing grades '''
grades = {
    'John Ponting': {
        'Homeworks': [79, 80, 74],
        'Midterm': 85,
        'Final': 92
    },
    'Jacques Kallis': {
        'Homeworks': [90, 92, 65],
        'Midterm': 87,
        'Final': 75
    },
    'Ricky Bobby': {
        'Homeworks': [50, 52, 78],
        'Midterm': 40,
        'Final': 65
    },
}

user_input = input('Enter student name: ')

while user_input != 'exit':
    if user_input in grades:
        # Get values from nested dict
        homeworks = grades[user_input]['Homeworks']
        midterm = grades[user_input]['Midterm']
        final = grades[user_input]['Final']

        # print info
        for hw, score in enumerate(homeworks):
            print('Homework %d: %d' % (hw, score))

        print('Midterm: %s' % midterm)
        print('Final: %s' % final)

        # Compute student total score
        total_points = sum([i for i in homeworks]) + midterm + final
        print('Final percentage: %f%%' % (100*(total_points / 500.0)))

    user_input = input('Enter student name: ')

"""
Note the whitespace and indentation used to layout the nested dictionaries. 
Such layout improves the readability of the code and makes the hierarchy of the 
data structure obvious. The extra whitespace does not affect the dict elements, 
as the interpreter ignores indentation in a multi-line construct.

A benefit of using nested dictionaries is that the code tends to be more 
readable, especially if the keys are a category like 'Homeworks'. Alternatives 
like nested lists tend to require more code, consisting of more loops 
constructs and variables.

Dictionaries support arbitrary levels of nesting; for example, the expression 
students['Jose']['Homeworks'][2]['Grade'] might be applied to a dictionary that 
has four levels of nesting.
"""

'''EXAMPLE music library'''
"""
The following example demonstrates a program that uses 3 levels of nested 
dictionaries to create a simple music library.

The following program uses nested dictionaries to store a small music library. 
Extend the program such that a user can add artists, albums, and songs to the 
library. First, add a command that adds an artist name to the music dictionary. 
Then add commands for adding albums and songs. Take care to check that an 
artist exists in the dictionary before adding an album, and that an album 
exists before adding a song.
"""
music = {
    'Pink Floyd': {
        'The Dark Side of the Moon': {
            'songs': [ 'Speak to Me', 'Breathe', 'On the Run', 'Money'],
            'year': 1973,
            'platinum': True
        },
        'The Wall': {
            'songs': [ 'Another Brick in the Wall', 'Mother', 'Hey you'],
            'year': 1979,
            'platinum': True
        }
    },
    'Justin Bieber': {
        'My World':{
            'songs': ['One Time', 'Bigger', 'Love Me'],
            'year': 2010,
            'platinum': True
        }
    }
}
(music)
# Get user input

# While user input != 'exit'
    # ...

