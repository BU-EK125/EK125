# Class 13: User-Defined Functions, Arguments, and Scope

## Learning Objectives
By the end of this reading, you should understand:
- How to write and call your own functions
- How arguments get passed to functions (parameters, defaults, keyword arguments)
- Where variables "live" in your program (scope)
- When changes inside a function affect the original data
- How to structure modular programs using functions

## Part 1: User-Defined Functions (Morning)

We have seen many built-in functions in Python. You can also write your own functions, which are called user-defined functions. Related user-defined functions can be stored in user-defined modules, which can then be imported into programs for use.

When we write a function, we write the function definition. The function can then be called, much like built-in functions.

The general form of a function definition is:

```python
def functionname(parameters):
    """ Documentation string. """
    # Function body
```

The first line is called the function header. It consists of the reserved word `def`, the name of the function, parameters (if any) in parentheses, followed by a colon. The rest of the function, which is indented, is the function body. This typically begins with a documentation string (docstring), in triple quotes. The docstring should be sentence(s) describing what the function does, beginning with a capitalized word and ending with a period. After the docstring there are the statements in the body of the function. It is common to indent the body of the function 4 spaces.

The function is called by giving the name of the function, and passing arguments in parentheses that will correspond to the parameters in the function header:

```python
functionname(arguments)
```

Sometimes the arguments in the function call are referred to as actual parameters and the parameters in the function header are referred to as formal parameters.

Two main reasons for writing our own functions are:

- To be able to reuse code by calling the function whenever it is needed
- To write modular programs

If there is code that will be repeated at different times, perhaps using different values, it can be made into a function and then called whenever needed.

Modular programs are programs that consist of a series of functions that do the actual work. The functions are called by a main program, which can be implemented as either a script or function.

### Functions with Return

We have seen examples of built-in functions that calculate and return a value, such as the `round` function. User-defined functions can also accomplish this using the `return` statement.

As an example, we will write a function that returns the area of a square. In order to calculate the area of a square, the function needs the length of each side of the square, so the side length must be passed as an argument to the function. Here is a function definition for a function named sqrarea that accomplishes this:

```python
def sqrarea(sidelen):
    """This function calculates the area of a square."""
    sqar = sidelen**2
    return sqar
```

The function can then be called by using the name of the function and passing a number for the length of a side of the square:

```python
>>> sqrarea(3)
9
```

In the function call, the side length, 3, was passed to the parameter `sidelen` in the function. The function then squared this, and returned the result. We say that when the function is called, control is sent to the function, and the function begins executing. The return statement not only returns the value (in this case, 9), but also sends control out of the function.

In general a docstring describes what a function does and can be displayed using the help function:

```python
>>> help(sqrarea)
Help on function sqrarea in module __main__:
```

```
sqrarea(sidelen)
    This function calculates the area of a square.
```

The variable `sqar`, which was used in the function body, was not necessary. The return statement could just return an expression:

```python
def sqrarea(sidelen):
    """This function calculates the area of a square."""
    return sidelen**2
```

The value returned from the function would normally be stored in a variable, e.g.

```python
>>> mysquare = sqrarea(3)
>>> mysquare
9
```

In this example, one argument was passed to the function. For a function to calculate the area of a rectangle, both the length and width of the rectangle must be passed to the function, so there will be two parameters in the function header and two arguments passed in the function call:

```python
def rectarea(rlen, rwid):
    """This function calculates the area of a rectangle."""
    return rlen * rwid
```
```
>>> rectarea(2, 4)
8
```

The values of the arguments are passed to the corresponding parameters in the function, so the first argument, 2, is passed to the first parameter `rlen`, and the second argument 4 is passed to the second parameter `rwid`.

Notice that the `return` statement returned the result of an expression; an intermediate variable could be used but is not necessary.

In Python, the `return` statement can only return one object. If it is desired to have a function return more than one thing, they can be stored in one data structure (such as a tuple or list), and that can be returned. In the following example, a function calculates and returns both the area and the perimeter of a square, by storing both in a list.

```python
def sqrarea_perim(sidelen):
    """Calculates the area and perimeter of a square."""
    sqar = sidelen**2
    sqperim = 4 * sidelen
    results = [sqar, sqperim]
    return results
```
```
>>> sqrarea_perim(11)
[121, 44]
```

Using a tuple instead of a list is perhaps easier to understand, and it is easier to use the results.

```python
def sqrarea_perim(sidelen):
    """Calculates the area and perimeter of a square."""
    sqar = sidelen**2
    sqperim = 4 * sidelen
    return sqar, sqperim
```
```
>>> area, perim = sqrarea_perim(11)
>>> print(area, perim)
121 44
```

### Functions with no Return

In many cases functions calculate and return values, but in some cases functions just accomplish a task, such as printing.

For example, the following function receives as parameters a string and an integer `n`, and prints the string n times in a row on one line. After that, it moves the cursor down.

```python
def printstrs(instr, n):
    """This function prints instr n times."""
    for i in range(n):
        print(instr,end='')
    print()
```

Here are two examples of calling the function:

```python
>>> printstrs('x',3)
xxx
```
```python
>>> printstrs("Hi", 5)
HiHiHiHiHi
```

Notice that the function does not have a `return` statement, since it is not calculating anything. However, all functions return something regardless of whether there is a return statement or not. The default value that is returned is a special value `None`, as we can see by passing a call to the function `printstrs` to the print function. In the following example, `aa` and then the newline gets printed by the function, and then the result returned by the function call, `None`, is printed once the function stops executing and returns control.

```python
>>> print(printstrs('a',2))
aa
None
```

The `printstrs` function prints the line `aa` and returns `None`. The print function then prints the returned value, `None`. This is equivalent to:

```python
>>> x = printstrs('a',2)
>>> print(x)
```

It is not always necessary to pass arguments to functions (whether they explicitly return something or not). For example, we may wish to have a function that just prints a set of instructions.

```python
def printinstruct():
    """This function just prints stuff."""
    print('Please sit up')
    print('Do not slouch!')
    print('Chew with your mouth closed')
```
```
>>> printinstruct()
Please sit up
Do not slouch!
Chew with your mouth closed
```

A function like this that just prints helps to facilitate modular programs. Of course, the instructions printed by a function would normally refer to actions that the user must take when running a program!

### Lambda Functions

Anonymous functions, called lambda functions in Python, are very short one line functions that do not require a formal function definition using `def`. Lambda functions are created using the keyword `lambda`. The general form is:

```python
lambda argument(s): expression
```

The function begins with the reserved word `lambda`, then argument(s) followed by a colon and then an expression that uses the arguments; the result of the expression is returned.

If the lambda function is stored in a variable, the variable can be used to call the function. For example,

```python
>>> times3 = lambda num: num * 3
>>> times3(11)
33
```

One advantage of a lambda function is that it is shorter than a function definition and does not require the header with `def` or the `return` statement. A disadvantage is that the "body" of the function is confined to one simple expression.

## Part 2: Function Arguments and Parameter Passing (Morning/Afternoon)

### How Arguments Get Into Functions

When you call a function, Python doesn't copy your data. Instead, it gives the function access to your original data by creating a new name (the parameter name) that refers to it:

```python
def processData(data):
    # 'data' is a new name that gives access to whatever was passed in
    print(f"Parameter 'data' has id: {id(data)}")
    
myList = [1, 2, 3]
print(f"Original 'myList' has id: {id(myList)}")
processData(myList)

# Output shows they have the SAME id - it's the same object!
```

Think of it like giving someone a nickname:
- You have a friend named "Elizabeth"
- You start calling her "Liz"
- Both names refer to the same person
- If "Liz" gets a haircut, "Elizabeth" has a new haircut too (same person!)

### Default Parameter Values

Parameters can have default values that are used when no argument is provided:

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")           # Uses default: "Hello, Alice!"
greet("Bob", "Hi")       # Overrides default: "Hi, Bob!"
```

**Order matters:** Parameters with defaults must come after parameters without defaults:

```python
# CORRECT
def makeProfile(name, age, country="USA"):
    return f"{name}, {age}, {country}"

# WRONG - SyntaxError!
def makeProfile(name, country="USA", age):
    return f"{name}, {age}, {country}"
```

### Keyword Arguments

You can specify arguments by name, which gives you powerful flexibility. **This is one of Python's most useful features** because it lets you:
1. **Skip over defaults you want to keep** - you don't have to provide every argument in order
2. **Provide arguments in any order** - as long as you use names, Python knows what goes where
3. **Make your function calls more readable** - the names document what each value means

```python
def createAccount(username, email, role="user", active=True):
    return f"{username} ({email}): {role}, active={active}"

# Positional arguments - must be in exact order
createAccount("alice", "alice@example.com", "admin", False)

# Keyword arguments - can be in ANY order!
createAccount(username="bob", role="admin", email="bob@example.com")
# Notice: role came before email, which is NOT the definition order

# Mix positional and keyword (positional must come first)
# This is especially useful to skip middle parameters
createAccount("charlie", "charlie@example.com", active=False)
# We skipped 'role' and kept its default, while still setting 'active'

# Without keyword arguments, you'd have to do:
createAccount("charlie", "charlie@example.com", "user", False)
# Must provide "user" explicitly even though it's the default!
```

**Why this matters:** Imagine a function with many optional parameters:
```python
def analyzeData(data, normalize=False, removeOutliers=False, 
                fillMissing=False, scale=True, verbose=False):
    # Implementation
    pass

# Want to only set verbose=True, keeping all other defaults?
# With keyword arguments (EASY):
analyzeData(myData, verbose=True)

# Without keyword arguments (TEDIOUS):
analyzeData(myData, False, False, False, True, True)
# Have to remember the order and provide every single value!
```

### The Confusing Case: Same Names Inside and Outside

Sometimes the variable name outside the function matches the parameter name inside the function. This can be confusing at first:

```python
def processGrades(grades):
    # The parameter 'grades' is a NEW name
    # It refers to whatever was passed in
    grades.append(100)
    print(f"Inside: {grades}")

# Our variable is also called 'grades'
grades = [85, 90, 78]
processGrades(grades)  # Pass 'grades' to parameter 'grades'
print(f"Outside: {grades}")
# Outside: [85, 90, 78, 100] - Modified!
```

Even though both are named `grades`, they're different names that happen to refer to the same object. The parameter `grades` inside the function is created fresh when you call the function.

**This gets really confusing with keyword arguments:**
```python
def analyzeScores(scores, threshold):
    print(f"Analyzing {len(scores)} scores with threshold {threshold}")
    # ... implementation ...

scores = [85, 90, 78, 92]
threshold = 80

# This looks bizarre but is perfectly valid!
analyzeScores(scores=scores, threshold=threshold)
#             ^^^^^^ parameter name
#                    ^^^^^^ variable name (different!)
```

The pattern `scores=scores` means "assign the value of the variable `scores` to the parameter `scores`." The first `scores` is the parameter name, the second is the variable name. They're different names that happen to be spelled the same way.

### The Two Types of Data: Mutable and Immutable

Python data types fall into two categories:

**Immutable (Cannot be changed):**
- Numbers: `int`, `float`
- Strings: `str`
- Tuples: `tuple`

**Mutable (Can be changed):**
- Lists: `list`
- Dictionaries: `dict`
- Sets: `set`

This distinction determines what happens in functions.

### Immutable Objects: Always Safe

With immutable objects, any "change" creates a new object:

```python
def tryToModify(x, s, t):
    x = x + 1      # Creates NEW number
    s = s.upper()  # Creates NEW string
    t = t + (4,)   # Creates NEW tuple
    print(f"Inside: x={x}, s={s}, t={t}")

num = 10
string = "hello"
tup = (1, 2, 3)

tryToModify(num, string, tup)
print(f"Outside: num={num}, string={string}, tup={tup}")
# Outside: num=10, string=hello, tup=(1, 2, 3) - All unchanged!
```

### Mutable Objects: Changes Affect the Original

With mutable objects, the function can modify your original data:

```python
def modifyList(lst):
    lst.append(999)        # Modifies the original
    lst[0] = "changed"     # Modifies the original
    print(f"Inside: {lst}")

myData = [1, 2, 3]
modifyList(myData)
print(f"Outside: {myData}")
# Outside: ['changed', 2, 3, 999] - Changed!
```

**The key insight:** Methods like `append()`, `remove()`, and index assignment modify the list in place. But reassignment (`lst = []`) creates a new local variable.

```python
def resetList(lst):
    lst = []  # Creates NEW local variable, doesn't affect original
    print(f"Inside: {lst}")

myData = [1, 2, 3]
resetList(myData)
print(f"Outside: {myData}")
# Outside: [1, 2, 3] - Unchanged!
```

## Part 3: Variable Scope (Afternoon)

### What is Scope?

The scope of a variable or object is where that object is valid. Variables defined in a function are `local` to that function, meaning that their scope is the function. Formally, what happens is that every function has its own symbol table, which contains the names of the variables and their values. Once a function is called and control is sent to the function, its symbol table is created. The function's symbol table only exists while the function is executing.

For example, for the `sqarea` function, the symbol table contains the local variable `sqar`, as well as the parameter `sidelen`.

```python
def sqrarea(sidelen):
    """This function calculates the area of a square."""
    sqar = sidelen**2
    return sqar
```

After the function is called, attempting to reference either `sqar` or `sidelen` will result in an error. This is because after the function stops executing, the symbol table, the variable `sqar`, and the parameter `sidelen` no longer exist.

```python
>>> area = sqrarea(4)
>>> print(sqar)

NameError: name 'sqar' is not defined
```

### The LEGB Rule

When Python looks up a variable name, it searches in this order:

1. **Local** - Inside the current function
2. **Enclosing** - In any enclosing functions (for nested functions)
3. **Global** - At the module level (outside all functions)
4. **Built-in** - Python's built-in names

```python
x = "global"  # Global scope

def outer():
    x = "enclosing"  # Enclosing scope
    
    def inner():
        x = "local"  # Local scope
        print(x)
    
    inner()
    print(x)

outer()
print(x)

# Output:
# local
# enclosing
# global
```

### Reading vs. Modifying Variables

You can read variables from outer scopes without any special syntax:

```python
taxRate = 0.08  # Global

def calculateTotal(price):
    # Can read taxRate from global scope
    return price * (1 + taxRate)

print(calculateTotal(100))  # 108.0
```

But if you try to modify a global variable, Python creates a new local variable instead:

```python
count = 0

def increment():
    count = count + 1  # ERROR! Can't read global 'count' before assigning
    print(count)

increment()  # UnboundLocalError
```

### The `global` Keyword

To modify a global variable from inside a function, use the `global` keyword:

```python
count = 0

def increment():
    global count  # Now refers to the global variable
    count = count + 1
    print(count)

increment()  # 1
increment()  # 2
print(count)  # 2
```

**Use cases for `global`:**
```python
# Configuration that changes during runtime
debugMode = False

def enableDebug():
    global debugMode
    debugMode = True

# Maintaining state across function calls
requestCount = 0

def logRequest():
    global requestCount
    requestCount += 1
    print(f"Request #{requestCount}")
```

**Better alternatives when possible:**
```python
# Instead of global, use return values
def incrementCounter(count):
    return count + 1

counter = 0
counter = incrementCounter(counter)

# Or use a class to group related data
class RequestLogger:
    def __init__(self):
        self.count = 0
    
    def logRequest(self):
        self.count += 1
        print(f"Request #{self.count}")
```

### The `nonlocal` Keyword

For nested functions that need to modify variables in the enclosing function:

```python
def outerFunction():
    count = 0
    
    def increment():
        nonlocal count  # Refers to count in outerFunction
        count += 1
    
    increment()
    increment()
    print(count)  # 2

outerFunction()
```

## Part 4: Modular Programs and Function Stubs (Afternoon)

### Modular Programs

In general in programming, a modular program is one in which the program is broken down into separate tasks, and each task is implemented as a function. This facilitates the top-down design approach of taking a problem, breaking it down into pieces, and implementing each as a function. The program then consists basically of calling the functions to complete each of the tasks.

A basic algorithm for many programs is:

- Get input(s)
- Calculate result(s), using the input(s)
- Print and/or display the result(s)

So, a simple outline of many programs would be to have:

- Function(s) to get the input(s)
- Function(s) to calculate result(s) using the input(s)
- Function(s) to display the result(s)

As an example, we will write a program that will prompt the user for the cost of an item in a store, and then calculate and print the total cost with a tax of 3%. The program will call 3 functions:

- A function to prompt for and return the cost
- A function to calculate the total cost including the tax
- A function to print the total cost

Here are the function definitions.

```python
def getcost():
    """ Prompts for item cost. """
    cost = float(input('Enter the item cost: '))
    return cost

def calctax(cost):
    """ Calculates and returns cost plus tax. """
    tax = cost * .03
    return cost + tax

def printtotcost(totcost):
    """ Prints cost plus tax. """
    print(f'The total cost is ${totcost:.2f}')
```

The functions could be called from a script, which is frequently called a main program. The program consists of calls to the functions. We will discuss scripts in future lectures. Other times the main program is implemented as a function rather than a script.

```python
# main program
cost = getcost()
totalcost = calctax(cost)
printtotcost(totalcost)
```

The output might look like this:

```
Enter the item cost: 11.11
The total cost is $11.44
```

Of course, to be more complete, the `getcost` function would error-check to make sure that the user enters a valid cost.

### Function Stubs

When writing a program that consists of a script calling multiple functions, the best practice is not to write the entire program and then execute it to see the results. Frequently, there are errors. When an error is encountered in a particular function, the problem may be in that function, or it might be the result of an incorrect argument passed to the function, that was obtained from another function. A more effective method for constructing the program is to use function stubs, which are place-holders for the actual functions.

The approach is:

- Sketch out the algorithm
- Decide what the functions are going to do
- Write the script, consisting of the calls to the functions (including the arguments that will get passed back and forth)
- Write function stubs for the individual functions
- Change each function stub to the actual function, one at a time

This methodical method of writing a program helps cut down on mistakes, and makes it easier to find bugs when they occur.

Function stubs should mimic what the function is eventually going to do, including using the arguments and returning the correct type(s).

For example, let's say we are going to write a program that will prompt the user for a temperature in degrees Celsius, convert that to Fahrenheit, and print the results.

We might have functions to:

- Prompt the user for degrees C, error-checking to make sure it's valid, and return the result
- Receive the degrees C and from that calculate and return degrees F
- Print both degrees C and degrees F in a nice sentence format

The script for the main program might look like this:

```python
# Convert C to F
degC = getdegc()
degF = c2f(degC)
printCF(degC, degF)
```

Example function stubs might look like this:

```python
def getdegc():
    """Prompts user for degrees Celsius."""
    return 33

def c2f(degreesc):
    """Converts degrees C to degrees F"""
    return degreesc + 5

def printCF(degreesc, degreesf):
    """Prints degrees C and degrees F"""
    print(degreesc, degreesf)
```

The idea is to execute the program with the function stubs and make sure that values are being passed back and forth correctly. Eventually, after prompting the user and error-checking, the `getdegc` function will return a positive number. So, for now, we just return a positive number. Eventually, once we figure out the conversion, the `c2f` function will convert C to F. For now, we'll just add 5 so we know that this function is correctly receiving the degrees C and using this number to calculate and return degrees F. Then, the `printCF` function will eventually print in a nice sentence format, but for now it will just print the values.

The headers for the functions should not change. Putting the actual doc strings in the function stubs is a good idea.

Then, once that is working, modify the stubs one at a time. For example, you might start by modifying the `getdegc` function to prompt the user. Then, modify that function to include the error-checking. Going about this systematically really does cut down on errors and makes it easier to find them.

## Part 5: Making Copies When You Need Them (Afternoon)

### The Problem: Multiple Names, Same Object

Assignment doesn't copy - it creates another name:

```python
original = [1, 2, 3]
alias = original  # NOT a copy!

print(original is alias)  # True - same object
alias.append(4)
print(original)  # [1, 2, 3, 4] - Changed!
```

### Solution 1: Shallow Copy

Use `.copy()` for a new list with the same contents:

```python
original = [1, 2, 3]
shallowCopy = original.copy()

shallowCopy.append(4)
print(original)  # [1, 2, 3] - Unchanged
print(shallowCopy)  # [1, 2, 3, 4]
```

**Warning:** Shallow copy only copies the outer container:

```python
original = [1, 2, [3, 4]]
shallowCopy = original.copy()

shallowCopy[2].append(5)  # Modifying the inner list
print(original)  # [1, 2, [3, 4, 5]] - Inner list changed!
```

### Solution 2: Deep Copy

For complete independence with nested structures:

```python
import copy

original = [1, 2, [3, 4]]
deepCopy = copy.deepcopy(original)

deepCopy[2].append(5)
print(original)  # [1, 2, [3, 4]] - Completely unchanged
print(deepCopy)  # [1, 2, [3, 4, 5]]
```

### When to Use Each Type of Copy

**Use shallow copy when:**
- Your list contains only immutable items (numbers, strings)
- You're copying simple structures
- Performance matters (shallow copy is faster)

```python
def processScores(scores):
    # Make a copy so we don't modify the original
    localScores = scores.copy()
    localScores.sort()
    return localScores[len(localScores)//2]  # Median
```

**Use deep copy when:**
- Your list contains other lists, dicts, or mutable objects
- You need complete independence
- You're okay with the performance cost

```python
def backupStudentData(students):
    # students is a list of dicts with nested lists
    # Need deep copy to protect all levels
    return copy.deepcopy(students)
```

**Don't copy when:**
- The function only reads data (no modifications)
- You want changes to persist (that's the point!)
- Working with huge datasets (copying is expensive)

```python
def calculateAverage(numbers):
    # No copy needed - just reading
    return sum(numbers) / len(numbers)

def sortInPlace(data):
    # No copy needed - we WANT to modify original
    data.sort()
```

## Putting It All Together

### Example: Understanding a Complex Case
```python
def processGrades(grades, bonusPoints=5):
    # 'grades' refers to the original list (mutable)
    # 'bonusPoints' has value 5 (immutable)
    
    # This modifies the original grades
    for i in range(len(grades)):
        grades[i] += bonusPoints
    
    # This creates a new local variable
    bonusPoints = 10  # Doesn't affect anything outside
    
    return grades

# First call
class1 = [85, 90, 78]
result1 = processGrades(class1)
print(class1)  # [90, 95, 83] - Modified!
print(result1 is class1)  # True - same object

# Second call with protection
class2 = [88, 92, 86]
result2 = processGrades(class2.copy())  # Pass a copy
print(class2)  # [88, 92, 86] - Original unchanged!
```

### Common Pitfalls and Solutions

| Problem | Why It Happens | Solution |
|---------|----------------|----------|
| Function modifies your list | Lists are mutable, function gets original | Pass `myList.copy()` |
| Can't modify global in function | `=` creates local variable | Use `global` keyword |
| Nested lists change unexpectedly | Shallow copy shares inner objects | Use `copy.deepcopy()` |
| Can't modify enclosing variable | Assignment creates new local | Use `nonlocal` keyword |

## Appendix: The Mutable Default Parameter Trap

This is an advanced topic that won't affect most of your code, but you should be aware of it.

### The Problem

Default parameter values are created once when Python first reads the function definition:

```python
def addItem(item, itemList=[]):
    print(f"List id: {id(itemList)}")
    itemList.append(item)
    return itemList

# Call it multiple times without providing a list
result1 = addItem("apple")
print(result1)  # ['apple']

result2 = addItem("banana")  
print(result2)  # ['apple', 'banana'] - WHAT?!

result3 = addItem("cherry")
print(result3)  # ['apple', 'banana', 'cherry'] - It keeps growing!

# They're all the SAME list object!
print(result1 is result2 is result3)  # True
```

### Why This Happens

1. Python read the function definition and created ONE empty list
2. Every call without providing `itemList` uses that SAME list
3. Each call modifies the SAME list
4. This list persists between function calls

### The Solution

Use `None` as the default and create a new list inside the function:

```python
def addItem(item, itemList=None):
    if itemList is None:
        itemList = []  # Create a NEW list each time
    itemList.append(item)
    return itemList

# Now each call gets its own list
print(addItem("apple"))   # ['apple']
print(addItem("banana"))  # ['banana'] - Correct!
```

This pattern works for any mutable default (lists, dicts, sets).

## Key Concepts Summary

- **Parameters**: Names defined in function definition
- **Arguments**: Values passed when calling the function
- **Default values**: Parameter values used when no argument provided
- **Keyword arguments**: Arguments specified by parameter name
- **Docstring**: Documentation string describing what a function does
- **Return statement**: Returns a value and sends control out of function
- **Scope**: Where a variable exists and can be accessed (LEGB rule)
- **Local variables**: Variables defined inside a function
- **Global variables**: Variables defined at module level
- **Mutable**: Can be modified (lists, dicts, sets)
- **Immutable**: Cannot be modified (numbers, strings, tuples)
- **Shallow copy**: Copies container but shares nested objects
- **Deep copy**: Complete independent copy of all levels
- **Function stubs**: Placeholder functions for testing program structure
- **Modular program**: Program broken down into separate functions

## Check Your Understanding

1. What's the difference between a parameter and an argument?
2. Why does `lst.append(x)` modify the original list but `lst = []` doesn't?
3. What's the difference between `list2 = list1` and `list2 = list1.copy()`?
4. When should you use shallow copy vs. deep copy?
5. Why does Python search Local, Enclosing, Global, Built-in in that order?
6. When is it better to return a value rather than use `global`?
7. What happens if you define a function with `def func(a, b=5, c)`?
8. How can you call a function with many parameters but only set one optional parameter?
9. What are function stubs and why are they useful?
10. Why should parameters with default values come after parameters without defaults?
