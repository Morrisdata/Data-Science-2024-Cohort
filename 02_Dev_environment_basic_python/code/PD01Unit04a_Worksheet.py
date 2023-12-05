# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 08:44:25 2020

@author: msmorris
"""

## 07.08 FUNCTIONS ARE OBJECTS
## 07.09 FUNCTION: COMMON ERRORS
## 07.10 SCOPE OF VARIABLES AND FUNCTIONS
## 07.11 NAMESPACES AND SCOPE RESOLUTION
## 07.12 FUNCTION ARGUMENTS
## 07.13 KEYWORD ARGUMENTS AND DEFAULT PARAMETER VALUES
## 07.14 ARBITRARY ARGUMENT LISTS
## 07.15 MULTIPLE FUNCTION OUTPUTS

###############################
## 07.08 FUNCTIONS ARE OBJECTS
###############################
"""
Functions as objects

A function is also an object in Python, having a type, identity, and value. A 
function definition like def print_face(): creates a new function object with 
the name print_face bound to that object.

All Python code is compiled before being executed by the interpreter. 
Statements entered in an interactive interpreter are compiled immediately, 
then executed. 
Modules are compiled when imported.
Functions are compiled when the interpreter evaluates the function definition.
"""
def print_face():
    # print face statements...
    return

print_face()

func = print_face
func()

"""
The interpreter creates a new function object when the definition 
def print_face() is evaluated. Since a function is just an object, assignment 
operations work the same: func = print_face binds the name func to the same 
object as print_face, thus creating multiple names for a single function. 
Both func() and print_face() perform the same call operation.

Functions can be passed as an argument to another function. here is a fun example
We have a few functions. 
human_head() 
monkey_head()
print_figure() accepts a function as an argument, calling that function to print a head, and then 
printing a body.
"""

def human_head():
    print('   ||||| ')
    print('   o   o')
    print('     >' )
    print('   ooooo')
    return

def monkey_head():
    print('   .-"-.')
    print(' _/.-.-.\\_')
    print('( ( o o ) )')
    print(' |/  "  \\|')
    print('  \\ .-. /')
    print('  /`"""`\\')
    return

def cat_head():
    pass

def dog_head():
    pass

def print_figure(face):
    face()  # Print the face
    print('     |')
    print('   --|--')
    print('  /  |  \\')
    print('@    |    @')
    print('     |')
    print('    /|\\')
    print('   @   @')
    return

choice = int(input('Enter "1" to draw monkey, "2" for human: '))

if choice == 1:
    print_figure(monkey_head)
elif choice == 2:
    print_figure(human_head)


"""
Passing functions as arguments can sometimes improve the readability of code. 
The above example could have been implemented using an if statement to call 
either human_head() or monkey_head() followed by a call to a print_body() 
function. However, the code is simplified by reducing the required number of 
function calls in the first code block to the more simple print_figure(face).

Objects like integers support many operations 
(adding, subtracting, etc.), functions only support the call operation.1
"""


#################################
## 07.09 FUNCTION: COMMON ERRORS
#################################
"""
Common function errors

Copy-and-paste code but then not complete modifications to the pasted code. 
"""
## EXERCISE
"""
A common error stems from copying-and-pasting code but then not modifying the 
copied code correctly. Find the error in the function on the right. 
"""
def cel_to_fah(celsius):
    tmp = (9.0/5.0) * celsius
    fah = tmp + 32

    return fah

def fah_to_cel(fah):
    tmp = fah - 32
    cel = tmp * (5.0/9.0)

    return fah

"""
More common errors
Return the wrong variable
Such as typing return tmp above. 
The function will work and sometimes even return the correct value.

Failing to return a value for a function.
If execution reaches the end of a function's statements, the function returns a 
value of None. If the function is expected to return an actual value, then a 
value of None may be assigned to a variable. This can cause a crash.
"""

def steps_to_feet(num_steps):
    feet_per_step = 3

    feet = num_steps * feet_per_step

feet_per_mile = 5280
steps = int(input('Enter number of steps walked: '))

feet = steps_to_feet(steps)
print("Distance walked in feet:", feet)

## EXERCISE
"""
Using the celsius_to_kelvin function as a guide, create a new function, 
changing the name to kelvin_to_celsius, and modifying the function accordingly.
"""
def celsius_to_kelvin(value_celsius):
    value_kelvin = 0.0

    value_kelvin = value_celsius + 273.15
    return value_kelvin

''' Your solution goes here '''

value_c = 0.0
value_k = 0.0

value_c = 10.0
print(value_c, 'C is', celsius_to_kelvin(value_c), 'K')

value_k = 283.15
print(value_k, 'is', kelvin_to_celsius(value_k), 'C')


##########################################
## 07.10 SCOPE OF VARIABLES AND FUNCTIONS
##########################################
"""
Variable and function scope
There are global and local variables. 
A local variable or function is only visible to the part of the program it is 
contained in. So when a variable is created inside of a function it is only 
available and exists within the bounds of that function hence variable scope

A global varialbe exists outside of functions and can be overwritten within 
functions by local variables.
"""
a = 1 ## Global variable
def add():
    a = 5 #local variable this will overwrite the global variable
    return a + 10 # expected result 5

def sub():
    return a - 1 # expected result 0 because a is differing to global varabiable
add()
sub()
"""
Here is an example of a way to dynamically change a global variable.
"""
"""
The global statement (right) allows modifying a global variable."""

employee_name = 'N/A'

def get_name():
    name = input('Enter employee name:')
    employee_name = name

get_name()
print('Employee name:', employee_name)

employee_name = 'N/A'

def get_name():
    global employee_name
    name = input('Enter employee name:')
    employee_name = name

get_name()
print('Employee name:', employee_name)

## EXERCISE
"""
Can you think of a way to use if then elses to keep the global variable if
it meets a certain critera but if it doesn't to use an input?
"""



#########################################
## NAMESPACES AND SCOPE RESOLUTION
#########################################
"""
Namespace

A namespace maps names to objects. The Python interpreter uses namespaces to 
track all of the objects in a program. For example, when executing z = x + y, 
the interpreter looks in a namespace to find the value of the objects 
referenced by x and y, evaluates the expression, and then updates z in the 
namespace with the expression result.
"""
x = 5             
y = 100
z = x + y

"""
In fact, a namespace is actually just a normal Python dictionary whose keys are 
the names and whose values are the objects. A programmer can examine the names 
in the current local and global namespace by using the locals() and globals() 
built-in functions. 
"""
print('Initial global namespace: ')
print(globals())

my_var = "This is a variable"
print('\nCreated new variable')
print(globals())

def my_func():
    pass

print('\nCreated new function')
print(globals())

"""
Scope is the area of code where a name is visible. Namespaces are used to make 
scope work. Global scope or a local function scope, has its 
own namespace. If a namespace contains a name at a specific location in the 
code, then that name is visible.

There are at least three nested scopes that are active at any point in a 
program's execution: 1

    Built-in scope – Contains all of the built-in names of Python, such as 
    int(), str(), list(), range(), etc.
    Global scope – Contains all globally defined names outside of any 
    functions.
    Local scope – Usually refers to scope within the currently executing 
    function, but is the same as global scope if no function is executing.

When a name is referenced in code, the local scope's namespace is the first 
checked, followed by the global scope, and finally the built-in scope. If the 
name cannot be found in any namespace, the interpreter generates a NameError. 
The process of searching for a name in the available namespaces is called scope 
resolution.


Scopes and namespaces explain how variables can share the same name, but have 
different values. 
"""


########################################################
## KEYWORD ARGUMENTS AND DEFAULT PARAMETER VALUES
########################################################
"""
Keyword arguments

Sometimes a function requires many arguments. In such cases, a function call 
can become very long and difficult to read. It also becomes easy to make a 
mistake when calling such a function if the ordering of the 
arguments is not correct.A function with many arguments.
"""
def print_book_description(title, author, publisher, year, version, num_chapters, num_pages):
    # Format and print description of a book...

print_book_description('The Lord of the Rings', 'J. R. R. Tolkien', 'George Allen & Unwin', 
                       1954, 1.0, 22, 456)
"""
In the example above, a programmer might very easily swap the positions of some 
of the arguments in the function call, potentially introducing a bug into the
 program. Python provides for keyword arguments that allow arguments to map to
 parameters by name, instead of implicitly by position in the argument list. 
 When using keyword arguments, the argument list does not need to follow a specific 
 ordering.
"""
def print_book_description(title, author, publisher, year, version, num_chapters, num_pages):
    # Format and print description of a book...

print_book_description(title='The Lord of the Rings', 
                       publisher='George Allen & Unwin',
                       year=1954, 
                       author='J. R. R. Tolkien', 
                       version=1.0,
                       num_pages=456, 
                       num_chapters=22)
"""
Keyword arguments provide a bit of clarity. Good practice is to use keyword 
arguments for any function containing more than approximately 4 arguments.

Keyword arguments can be mixed with positional arguments, provided that the
keyword arguments come last. A common error is to place keyword arguments 
before all position arguments, which generates an exception.
"""
def split_check(amount, num_people, tax_rate, tip_rate):
    # ...

split_check(125.00, tip_rate=0.15, num_people=2, tax_rate=0.095)


"""
Default parameter values

Sometimes a function may have a parameter that is almost always called with the 
same argument. For example print_time(time, time_zone='PST') might almost always 
be called with the time_zone parameter given the value 'PST'. A programmer can 
assign a default parameter value to a parameter in the function definition, 
allowing calls to the function to omit an argument for that parameter.

The following function prints a date in a particular style, given parameters 
for day, month, and year. The fourth parameter indicates the desired style, 
with 0 meaning American style, and 1 meaning European style. For July 30, 2012, 
the American style is 7/30/2012 and the European style is 30/7/2012.
Figure 7.13.4: Parameter with a default value.
"""
def print_date(day, month, year, style=0):
    if style == 0:  # American
        print(month, '/', day, '/', year)
    elif style == 1:  # European
        print(day, '/', month, '/', year)
    else:
        print('Invalid Style')

print_date(30, 7, 2012, 0)
print_date(30, 7, 2012, 1)
print_date(30, 7, 2012)




##################################
## ARBITRARY ARGUMENT LISTS AFTER COMPLETING CLASS ONCE
##################################
"""
Arbitrary arguments

Sometimes a programmer doesn't know how many arguments a function requires. A 
function definition can include a *args parameter that collects optional 
positional parameters into an arbitrary argument list tuple.
"""
def sandwich(bread, meat, *args): 
    print('%s on %s' % (meat, bread), end=' ') 
    if len(args) > 0: 
        print('with', end=' ') 
    for extra in args: 
        print(extra, end=' ') 
    print("")


sandwich('sourdough', 'turkey', 'mayo')
sandwich('wheat', 'ham', 'mustard', 'tomato', 'lettuce')


"""
Adding a final parameter of **kwargs creates a dictionary containing the 
keyword arguments not assigned to formal parameters 
(kwargs is short for "keyword arguments"). The keys of the dictionary are the 
parameter names specified in the function call.
"""
def sandwich(bread, meat, **kwargs):
    print('%s on %s' % (bread, meat))
    for category, extra in kwargs.items():
        print('   %s: %s' % (category, extra))

sandwich('sourdough', 'turkey', sauce='mayo')
sandwich('wheat', 'ham', sauce1='mustard', veggie1='tomato', veggie2='lettuce')


"""
The * and ** characters in *args and **kwargs are the important symbols. "args" 
and "kwargs" could be changed to any valid identifier 
(like *condiments in the above example).

One or both of *args or **kwargs can be used. They must come last 
(and in that order if both are used) in the parameter list, 
otherwise an error occurs.

Most operating systems, like Windows, Mac OS X, and Linux, have a text-based 
command line that can be used in place of the mouse and graphical user 
interface. To start an application using the command line, a user types in 
the application name followed by some options (sometimes called switches), as 
in "notepad.exe" or 
"firefox.exe --new-window=http://google.com --private-toggle=True". 
The application (.exe) comes first, followed by a list of options in the 
form --option_name=option_value. The formatting of the arguments usually 
depends on the application.

The following gen_command function accepts an application name as the single 
positional argument and an arbitrary number of keyword arguments that detail 
the command line options. The function yields the command line required to 
start the application.
"""

def gen_command(application, **kwargs):
    command = application
    for argument in kwargs:
        command += ' --%s=%s' % (argument, kwargs[argument])
    return command

print (gen_command('notepad.exe'))  # No options
print (gen_command('Powerpoint.exe', file='pres.ppt', start=True, slide=3))



## RUN a program
from sys import exit 

def cont():
    print("What would you like to do next? 1: Another calc 2: exit")
    cont_v = int(input("--->"))
    if cont_v == 1:
        start()
    elif cont_v == 2:
        print("you are now leaving Calculator world, Goodbye.")
        exit()
    else:
        print("invalid entry")
        cont()

def basic_calc():
    print("You can choose 1 for addition or 2 for subtraction")
    bc_value = int(input("--> "))
    if bc_value == 1:
       val1 = int(input("Entervalue 1 : "))
       val2 = int(input("Entervalue 2 : "))
       add(val1,val2)
    elif bc_value == 2:
       val1 = int(input("Entervalue 1 : "))
       val2 = int(input("Entervalue 2 : "))
       sub(val1,val2)
    else:
       print("invalid input try again 1 or 2")
       basic_calc()

def	add(a,b):
    print( a, "+", b,"=", a + b)
    cont()
    

def	sub(a,b):
    print( a, "-", b,"=", a - b)
    cont()

def tipcalc():
    print("not created yet, awesome an exercise!")
    pass

def paycalc():
    print("not created yet, awesome an exercise!")
    pass

def	start():
    print("###############################################")
    print("##           CALCULATOR WORLD                ##")
    print("##   Enter number for calculator you want:   ##")
    print("##      1 - Basic Calculator                 ##")
    print("##      2 - Tip Calculator                   ##")
    print("##      3 - Pay Calculator                   ##")
    print("##      4 - Trip Budget                      ##")      
    print("###############################################")

    next = int(input("---> "))

    if next == 1:
        basic_calc()
    elif next == 2:
        tipcalc()
    elif next == 4:
        paycalc()
    else:
        try_again("This is either invalid input or not developed program yet")
start()


'''PROJECT
Could you use *args or **kwargs to make it easier to relate skills to scores?
How else might you use them. 
Can you take anypart of your skill builder and turn it into a program?