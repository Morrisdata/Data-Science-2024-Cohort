# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 20:41:27 2021

@author: Matth
"""





##########################################
## PRACTICES WITH LISTS AND DICTIONARIES 
##########################################
    
#Task 1
"""
Complete the function to return the first two items in the given list

# Complete the function to return the first two items in the given list
def getFirstTwo(mylist):
# Student code goes here
 
# expected output: [8, 3]
print(getFirstTwo([8,3,5,2,10]))  
 
# expected output: [15, 2]
print(getFirstTwo([15,2,10,12]))
"""

#Task 2
"""
Complete the function to return the last two items in the given list

# Complete the function to return the last two items in the given list
def getLastTwo(mylist):
# Student code goes here
 
# expected output: [2, 10]
print(getLastTwo([8,3,5,2,10]))  
 
# expected output: [9, 12]
print(getLastTwo([15,2,9,12]))
"""

#Task 3
"""
Complete the function to add num1 to the end of the given list

# Complete the function to add num1 to the end of the given list
def addToEnd(mylist, num1):
# Student code goes here
 
# expected output: [4, 5, 6, 7]
print(addToEnd([4,5,6], 7))
 
# expected output: [9, 8, 7, 6]
print(addToEnd([9,8,7], 6))
"""

#Task 4
"""
Complete the function to add num2 to the front of the given list

# Complete the function to add num2 to the front of the given list
def addToFront(mylist, num1):
# Student code goes here
 
# expected output: [3, 4, 5, 6]
print(addToFront([4,5,6], 3))
 
# expected output: [10, 9, 8, 7]
print(addToFront([9,8,7], 10))
"""
#Task 5
"""
Complete the function to return a new list containing the first two and last 
two items in the given list

# Complete the function to return a new list containing 
# the first two and last two items in the given list
def getFirstTwoAndLastTwo(mylist):
# Student code goes here
 
# expected output: [8, 3, 19, 1]
print(getFirstTwoAndLastTwo([8,3,7,15,2,10,19,1]))
 
# expected output: [7, 15, 3, 5]
print(getFirstTwoAndLastTwo([7,15,2,10,19,1,3,5]))
"""
#Task 6
"""
Complete the function to remove the first item in the given list

# Complete the function to remove the first item in the given list
def removeFirst(mylist):
# Student code goes here
 
# expected output: [7, 8, 9]
print(removeFirst([6,7,8,9]))
 
# expected output: [2, 3, 4]
print(removeFirst([1,2,3,4]))
"""
#Task 7
"""
Complete the function to remove the third item in the given list

# Complete the function to remove the third item in the given list
def removeThird(mylist):
# Student code goes here
 
# expected output: [6, 7, 9]
print(removeThird([6,7,8,9]))
 
# expected output: [1, 2, 4]
print(removeThird([1,2,3,4]))
"""
#Task 8
"""
Complete the function to order the values in the list. If ascending is true 
then order lowest to highest otherwise sort highest to lowest

# Complete the function to order the values in the list
# if ascending is true then order lowest to highest
# if ascending is false then order highest to lowest
def sortList(mylist, ascending):
# Student code goes here
 
# expected output: [4, 12, 19, 33]
print(sortList([19,4,33,12], True))
 
# expected output: [33, 19, 12, 4]
print(sortList([19,4,33,12], False))
"""
#Task 9
"""
Complete the function to return a dictionary using list1 as the keys and list2 
as the values

# Complete the function to return a dictionary using 
# list1 as the keys and list2 as the values
def createDict(list1, list2):
# Student code goes here
        
# expected output: {'tomato': 'red', 'banana': 'yellow', 'lime': 'green'}  
print(createDict(['tomato', 'banana', 'lime'], ['red','yellow','green']))        
 
# expected output: 
{'Brazil': 'Brasilia', 'Ireland': 'Dublin', 'Indonesia': 'Jakarta'}
print(createDict(['Brazil', 'Ireland', 'Indonesia'], ['Brasilia','Dublin','Jakarta']))
"""
#Task 10
"""
Complete the function to return a dictionary value if it exists or return 
Not Found if it doesn't exist

# Complete the function to return a dictionary value 
# if it exists or return Not Found if it doesn't exist
def findDictItem(mydict, key):
# Student code goes here
        
# expected output: yellow
print(findDictItem({'tomato': 'red', 'banana': 'yellow', 'lime': 'green'} , 'banana'))
 
# expected output: Not Found
print(findDictItem({'Brazil': 'Brasilia', 'Ireland': 'Dublin', 'Indonesia': 
    'Jakarta'},'Cameroon'))
"""
#Task 11
"""
Complete the function to remove a dictionary item if it exists

# Complete the function to remove a dictionary item if it exists
def removeDictItem(mydict, key):
# Student code goes here
 
# expected output: {'tomato': 'red', 'lime': 'green'}
print(removeDictItem({'tomato': 'red', 'banana': 'yellow', 'lime': 'green'} , 'banana'))
 
# expected output: {'Brazil': 'Brasilia', 'Ireland': 'Dublin', 'Indonesia': 'Jakarta'}
print(removeDictItem({'Brazil': 'Brasilia', 'Ireland': 'Dublin', 'Indonesia': 'Jakarta'},'Cameroon'))
"""
#Task 12
"""
Complete the function to print every key and value

# Complete the function to print every key and value
def printDict(mydict):
# Student code goes here
        
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
"""
