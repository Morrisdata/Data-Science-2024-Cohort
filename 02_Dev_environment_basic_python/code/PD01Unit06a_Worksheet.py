############################################################################### 
##                    PYTHON FOR DATA I - UNIT 5
##                  LISTS [ ] TUPLES () DICTIONARIES{}      
## You have been creating a list of skills and scores lets look at this more
## formally.
###############################################################################
''' 
List can contain integers, characters or a mix of both

list1 = [1,2,3,4,5,6]
list1

list2 = ["soy", "bread", "eggs"]

list3 = [1,5.2,"bread"]

* Lists can contain lists

list4 = ["soy", "bread", "eggs",["corn", "kale", "carrots"]]
list4

* List of things you can do with lists

Delete, Append, Extend, Insert, Populate, Remove, Reverse, 
Sort, Add lists together. 

For now we will focus on creating lists and :

* adding lists together
* append values
* replace a list element
* remove list elements
* exploring data
* sorting data
* slicing data

This is just an intro later you will begin to see how lists can be used with 
data.
'''
### creating
a = [1, 2, 3, 4, 5]     # create lists using brackets
a
		


### slicing
a[0]        # returns 1 (Python is zero indexed)
a[0:3]      # returns [2, 3] (inclusive of first index but exclusive of second)
a[-2]       # returns 5 (last element)


## EXERCISE
'''
1. Bring back the first animal
2. Bring back the two middle animals
3. Bring back the last animal
'''
a = ['duck', 'goose', 'fox', 'ox']
       0        1       2      3
a[1:2]


#appending
a = [1, 2, 3, 4, 5] 
a[5] = 6       # error because you can't assign outside the existing range

a.append(6)     # list method that appends 6 to the end
a
a = a + [0, .5]     # use plus sign to combine lists
a
#checking length
len(a)      # returns 7

#checking type
type(a)     # returns list
type(a[0])  # returns int

#sorting
sorted(a)               # sorts the list
sorted(a, reverse=True) # reverse=True is an 'optional argument'
sorted(a, True)         # error because optional arguments must be named

## EXERCISE
'''
1. Make a list of your favorite foods, or bands
2. display your list
3. add a new value to your list
4. sort your list 
'''
##

###EXERCISE###
"""
1. Modify the program to print the correct ordinal number 
("1st", "2nd", "3rd", "4th", "5th") 
instead of "1th", "2th", "3th", "4th", "5th".
2. For the oldest person, remove the ordinal number (1st) from the print 
statement to say, "The oldest person lived 122 years".

Reminder: List indices begin at 0, not 1, thus the print statement uses 
oldest_people[nth_person-1], to access the nth_person element 
(element 1 at index 0, element 2 at index 1, etc.). 
"""
oldest_people = [122, 119, 117, 117, 116]  # Source: Wikipedia.org

nth_person = int(input('Enter N (1-5): '))

if (nth_person >= 1) and (nth_person <= 5):
    print('The {}th oldest person lived {}d years'.format(nth_person, oldest_people[nth_person-1]))

### PRACTICE AND MORE EXAMPLES

my_list1 = ['ac110','ac113','da250','da500'] # creates a list
my_list1[0] #Get an element from a list
my_list1[0:] # Get a new list from a range of another list
my_list2 = ['ac099', 'da580', 'in001']
master_list = my_list1 + my_list2 # my_list2 is added to then end of my_list1
new_account = 'ac999'
master_list[5] = new_account # change the value of the ith element 
master_list
master_list.append(new_account)# Add the elements in [x] to the end of my-list 
                         
del master_list[5] # Delete an element from a list
       
'''EXAMPLE'''
my_teams = ['Raptors', 'Heat', 'Nets']
your_teams = my_teams  # Create a shared reference to same list
my_teams[1] = 'Lakers'  # Modify list element
print('My teams are:', my_teams)  # Both variables have changed
print('Your teams are:', your_teams)  # Both variables have changes

'''EXAMPLE'''
my_songs = ['your song', 'read my mind', 'karma police']
karaoke = my_songs[:]  
my_songs[1] = 'Your Song'  # Modify list element
print('My songs are:', my_songs)  # List element has changed
print('Your songs are:', karaoke)  # List element has not changed                 


######## EXERCISE
'''
Modify short_names by deleting the first element and changing the last element 
to Joe. Sample output from given program:
'''
short_names = ['Gertrude', 'Sam', 'Ann', 'Joseph']
''' Your solution goes here '''
print(short_names)


#######################
## LIST METHODS
## list.append(x) # Add an item to the end of a list
## list.extend([x]) # Add all items in [x] to list
## list.insert(i,x) # insert x into list before position i
#  Remove Elements
## list.remove(x) #Remove first item from list with value x
## list.pop() # Remove and return last item in list
## list.pop(i) # Remove and return item at position i in list
#  Modify elements
## list.sort() #sort the items of list in-place
## list.reverse() #Reverse the elements of list in place
#  Miscellaneous
## list.index(x) #Return index of first item in list with value x
## list.count(x) #Count the number of times value x is in the list
#######################
"""
A list method can perform a useful operation on a list such as adding or 
removing elements, sorting, reversing, etc.
The table below shows the available list methods. Many of the methods perform 
in-place modification of the list contents — a programmer should be aware that 
a method that modifies the list in-place changes the underlying list object, 
and thus may affect the value of a variable that references the object.
"""
# Add elements
list.append(x) # Add an item to the end of a list
list.extend([x]) # Add all items in [x] to list
list.insert(i,x) # insert x into list before position i

# Remove Elements
list.remove(x) #Remove first item from list with value x
list.pop() # Remove and return last item in list
list.pop(i) # Remove and return item at position i in list

# Modify elements
list.sort() #sort the items of list in-place
list.reverse() #Reverse the elements of list in place

# Miscellaneous
list.index(x) #Return index of first item in list with value x
list.count(x) #Count the number of times value x is in the list

''' EXAMPLE'''
vals = [1,4,16]
vals.append(7)
(vals)
vals.insert(0,32)
(vals)
vals.pop()
(vals)
vals.pop()
(vals)
vals.pop(0)
(vals)
vals.remove(16)
(vals)




###EXERCISE###

'''Sort short_names in reverse alphabetic order. 
Sample output from given program:
['Tod', 'Sam', 'Joe', 'Jan', 'Ann'] '''

short_names = ['Jan', 'Sam', 'Ann', 'Joe', 'Tod']

''' Your solution goes here '''

print(short_names)






## EXERCISE:
'''Create a list of the first names of your family members.
Print the name of the last person in the list.
add a new person to your family make it a celebrity
Change the name of the new person to lowercase using the string method 'lower'.
Sort the list in reverse alphabetical order. '''



########################
## 09.05 LIST STRIDE

##Stride
"""
An optional component of slice notation is the stride, which indicates how many 
elements are skipped between extracted items in the source list. For example, 
the expression my_list[0:5:2] has a stride of 2, thus skipping every other 
element, and resulting in a slice that contains the elements in positions 
0, 2, and 4. 
The default stride value is 1 (the expressions my_list[0:5:1] 
and my_list[0:5] being equivalent). 
"""
my_list[start:end]
my_list[start:end:stride]
my_list[start:]
my_list[:end]
my_list[:]




# Tuple() is the same as a list but it cannot be changed


# Dictionary{}

family = {'dad':'Goerge Sr.', 'mom':'Gangi', 'size':2}
family


# check the length
len(family) # returns 3 (number of key-value pairs)

# use the key to look up a value (fast operation regardless of dictionary size)
family['dad'] # returns 'Dr.Venture'

# add a new entry
family['pet'] = 'mother'
family

# keys must be unique, so this edits an existing entry
family['pet'] = 'ostrich'
family['pet']

# delete an entry
del family['pet']

# keys can be strings or numbers or tuples, values can be any type
family['kids'] = ['michael', 'lindsey','gob'] # value can be a list
family

# useful methods
family.keys() # returns list: ['dad', 'kids', 'mom', 'size']
family.values() # returns list: ['Goerge Sr.', ['Michael', 'Lindsey','Gob'], 'unknown', 2]
family.items() # returns list of tuples:
# [('dad', 'Goerge Sr.'), ('kids', ['Michael', 'Lindsey','Gob']), ('mom', 'Gangi'), ('size', 2)]

#1. Print the name of the mom.

#2. Change the size to 5.

#3. Add 'Tobias' to the list of kids. 


#4 Add to the family dictionary grandkids 'Goerge Michael and Maeby'

#Writing Dictionaries to .csv



"""
Practicle example
"""
my_dict = {
    'Bobby': 'A+',
    'Alan': 67,
    10: 5.0
}


"""
one way to create a dictionary a programmer first creates a dictionary and then adds entries, 
perhaps by reading user-input or text from a file. Dictionaries are mutable, 
so entries can be added, modified, or removed in-place. 
"""


my_dict[key] 	#Indexing operation – retrieves the value associated with key. 	
jose_grade = my_dict['Jose']

my_dict[key] = value #Adds an entry if the entry does not exist, else modifies 
                     #the existing entry. 	
my_dict['Jose'] = 'B+'
del my_dict[key] 	#Deletes the key entry from a dict. 	
del my_dict['Jose']
key in my_dict #Tests for existence of key in my_dict. 	
if 'Jose' in my_dict: # ...





#######################
## 09.11  DICTIONARIES
## {key:values}
#######################
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
    
    
#############################
## 09.12  DICTIONARY METHODS
## my_dict.clear() # removes all items from the dictionary
## my_dict.get(key, default) # Reads the value of the key entry from the 
                          # dictionary. If the key does not exist in the 
                          # dictionary, then returns default.

## my_dict1.update(my_dict2) # Merges dictionary my_dict1 with another dictionary 
                          # my_dict2. Existing entries in my_dict1 are 
                          # overwritten if the same keys exist in my_dict2.
## my_dict.pop(key, default) # Removes and returns the key value from the 
                          # dictionary. If key does not exist, then default is 
                          # returned.
#############################

"""
A dictionary method is a function provided by the dictionary type (dict) that 
operates on a specific dictionary object. Dictionary methods can perform some 
useful operations, such as adding or removing elements, obtaining all the keys 
or values in the dictionary, merging dictionaries, etc.

Modification of dictionary elements using the above methods is performed 
in-place. Ex: Following the evaluation of the statement my_dict.pop('Ahmad'), 
any other variables that reference the same object as my_dict will also reflect 
the removal of 'Ahmad'. As with lists, a programmer should be careful not to 
modify dictionaries without realizing that other references to the objects 
may be affected. 
"""                          










''' Project Exercise
Review your project code and notes. 
can you implement Data structures to help you with your studying?
As you try to write these lists or dictionaries to a file you may have difficulty
without loops

How do you write this to EXCEL?
Uou could attempt export and that is worth a look and you could explore data frames
but that is another story for another time. For now just use this unit to practice
after the next units you may get some ideas how to populate excel with your 
Dictionaries, Lists and Tuples

'''

