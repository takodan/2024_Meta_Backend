# Programming in Python
## Module 1 Getting started with Python
### welcome to python programming
1. programming: A set of instructions that a computer uses to perform a specific function.
2. Python pro:
    1. multi platform
    2. easy to read and learn
3. `print("hello world")`
4. Basic syntax
    1. use `;` or next line to separate statement
    2. use `\` to force line
    3. indentation matters
    4. use `#` to start a comment
5. Variables
    1. give variables a meaningful names
    2. camelCase
    3. snack_case
    4. multiple assignments is available
    5. delete a variable by `del varName`
6. Data type
    1. Numeric (Integer, Float, Complex Number)
    2. Sequence (String, List, Tuples)
    3. Dictionary
    4. Boolean
    5. Set
7. Type casting: implicit and explicit
    - `ord()`: character to unicode code
    - `hex()`, `oct()`
8. `print()` https://docs.python.org/3/library/functions.html#print
9. formatting https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals

### control flow and conditionals
1. Math and logical operators
2. If, else, elif
3. Match statement (new in python 3.10) https://www.geeksforgeeks.org/python-match-case-statement/
```py
http_status = 200
match http_status:
    case 200 | 201: #200 or 201
        print("Success")
    case 400:
        print("Not Found")
    case 500 | 501:
        print("Server Error")
    case _: # else
        print("Unknow")
```

4. Looping constructs
    1. use `enumerate()` with `for`
    2. `Break`, `Continue`, `Pass`
    3. nested loop

## Module 2 Basic programming with Python
1. Define a function `def`
    1. args `def fn(*args_name):`
        1. `args_name` will become a **tuple**
        2. pass arguments like `fn(value1, value2)`
    2. keyword args (kwargs) `def fn(*kwargs_name):`
        1. `kwargs_name` will become a dictionary
        2. pass arguments like `fn(key1 = value1, key2 = value2)`
    3. ordering arguments `def fn(a, b, *args_c, **kwargs_d):`
    4. more with unpacking operator `*` https://realpython.com/python-kwargs-and-args/
2. Variable scope: built-in > global > enclosing > local
3. Data structures: mutable or immutable
4. List 
    1. methods https://www.w3schools.com/python/python_ref_list.asp
    2. print without brackets and comma `list1 = [1, 2, 3, 4]; print(*list1) # 1 2 3 4 `
5. Tuple: immutable list
6. Sets
    1. unordered collection with no duplicate elements, cannot get a item by index
    2. mathematical operations like `difference()`, `union()`, or `intersection()` https://www.w3schools.com/python/python_ref_set.asp
7. Dictionary
    1. methods https://www.w3schools.com/python/python_ref_dictionary.asp
    2. delete `del dictionary[keyName]`
    3. `.get(keyName, value)` `.items()`

8. exercise at "2_ordering_system.py"

### Errors, exceptions and file handling
1. Syntax error, Exception errors (during code execution)
```py
try:
    # code you want to try
    pass
except:
    # run this block if error happened in try
    # if this except has run, other except won't trigger
    pass
except Exception as exception: 
    # run this block if the specific error happened
    # Exception: all exceptions class
    print(exception) # print the error message in the exception class
    print(exception.__class__) # print exception class name
else:
    # if no error happened, run this block
finally:
    # always run this block
```
2. more exceptions https://docs.python.org/3/library/exceptions.html
3. open() https://docs.python.org/3/library/functions.html#open
```py
# remember to close file
file = open(<file_path>, <mode>)
file.close()

# with open, automatically close()
with open(<file_path>, <mode>) as file:
    data = file.read() # return the entire file as a string
    data_line = file.readline() # return a line as a string
    data_lines = file.readlines() # return the entire file as a list

    file.write(string)
    file.writelines(sequence) # remember to add "\n" if needed

    # file can be iterate line by line
    for line in file:
        print(line, end='')
```
3. use `open()` with `try:` `expect:` in case file not found
4. exercise in "2_file_ops"


## Module 3 Programming paradigms
1. **Procedural programming**: Create functions (subroutines/procedures) that can be reused.
2. don't repeat yourself (DRY)
3. **Algorithms**: Break the problem into smaller parts and build up a series of steps to resolve the problem.
4. Algorithms types:
    1. Recursion: Recursion refers to a method or a function that will call itself
    2. Divide and conquer: breaking the problem into smaller sub-problems and solving the final solution.
    3. Dynamic programming: This is mainly used for optimization problems.
    4. Greedy algorithm: This one finds the best solution in each and every step instead of approaching optimization in a global way.
5. Refactoring: rewrite the code to make it easier to manage or to run more efficiently.
6. Refactoring: rewrite the code to make it easier to manage or to run more efficiently.
6. Big O notation (order by time complexity):
    1. O(1) Constant: Best / Fastest 
        1. It does not depend on the size of the input data.
        2. It's like finding your favorite book on a perfectly organized bookshelf – it takes the same amount of time whether you have 10 books or 1,000 books.
        3. dictionary
    2. O(log(n)) Logarithmic: Good / Pretty Fast
        1. It grows slowly / logarithmically as you add more data.
        2. Think of it as finding a name in a phone book by repeatedly splitting it in half – it gets faster even if the phone book gets bigger.
        3. **Binary search**
    3. O(n) Linear: Fair / Moderate
        1. It grows linearly with the size of the input data. If you have twice as much data, it takes about twice as long.
        2. It's like looking through a list of names one by one to find a match.
        3.  `for i in range(n):`
    4. O(nlog(n)) Linearithmic: Bad / Slower
        1. It's faster than quadratic but slower than linear.
        2. Heap Sort, Merge Sort
    6. O(n^2) Quadratic
        1. It is proportional to the square of the input size.
        2. Like checking every combination of items on a list against each other
        3. **Bubble Sort**
    6. O(n^3) Cubic
    7. O(n^c)
    8. O(2^n) Exponential
        1. It doubles with each addition to the input data set.
        2. Imagine a puzzle where you have to try every possible combination
        3. **Fibonacci**, generating all subsets of a set
    9. O(c^n)
    10. O(n!)
        1. It grows factorially with the size of the input.
        2. Practically unusable for large problems.
7. steps of analyzing code with Big O Notation
    1. Identify the Input Size: "n"
    2. Identify Loops and Iterations: They often determine the primary factors affecting time complexity.
    3. Count Operations Inside Loops: inside each loop that depends on the input size "n."
    4. Combine Complexity: If you have nested loops, multiply their complexities.
    5. Choose the Dominant Term: Focus on the term with the highest growth rate
    6. Simplify: Simplify the expression as much as possible by removing constant factors.


### Functional programming
1. In functional programming, functions are considered standalone or independent.
2. Functions in Python have the same level of numbers and strings
3. print the whole string in reverse order `print(String[::-1])`
4. Pure function: no effect beyond its own scope. Its output depends on input.
5. be careful of Deep Copy and Shallow Copy.
6. Recursion: a function that calls itself.
    1. example 1: factorial
    ```py
    def find_factorial_recursive(n):
        # Base Condition
        if n == 1:
            return 1
        # Recursive calls
        else
            return n * find_factorial_recursive(n-1)
    ```

    2. example 2: Tower of Hanoi
    - at "2_tower_of_hanoi"

7. Reversing a string
    1. example 1: Slice
    ```py
    # str[start:stop:step]
    trial = "reversal"
    new_trial = trial[::-1]
    print(trial)
    ```

    2. example 2: Recursion
    ```py
    def str_reverse(string):
        if len(string) == 0:
            return string
        else:
            return str_reverse(string[1:]) + string[0]
    
    string = "reversal"
    new_string = str_reverse(string)
    print(new_string)
    ```

8. map()
    1. `map(function, iterable, *iterables)`
    2. Return an iterator that applies `function` to every item in a `iterable`. 
9. filter()
    1. `filter(function, iterable)`
    2. Construct an iterator from those elements of `iterable` for which `function` is true.
10. List comprehension 
    - `list1 = [<expression> for x in <sequence> if <condition>]` 
11. Dictionary comprehension 
    - `dict1 = {x:x for x in <sequence> if <condition> }`
    - `dict2 = {x:y for x, y in zip(list1, list2) if <condition> }`
12. exercise at "2_comprehensions.py"

### Object Oriented Programming
1. Class: a blue print for creating a object / instance
    1. Attributes: variable
    2. Behavior: function
2. Inheritance: creating a new class (Child/Subclass) which is derivative of a existing class (Parent/Super Class).
3. Polymorphism: a function can change its behavior when called by different object.
4. Encapsulation: bind/encase methods and variables in a single unit of scope to limit access.
```py
# Encapsulation
class Alpha():
    print("This line always run no matter there is a instance or not!")
    print()
    def __new__(cls):
        pass

    def __init__(self) -> None:
        self._a = 2.  # Protected member 'a', can still be accessed by the class and its subclasses
        self.__b = 2.  # Private member 'b', can only be accessed from within the class
```

5. Abstraction: 
    1. abstract class abstract cannot create an instance.
    2. child of abstract class must overwrite every methods in the abstract class.
    3. for interoperability, consistency, and/or avoiding code duplication.
    1. example in "2_inheritance.py"

6. Inheritance
    1. types
        1. simple: `Parent_1 < Child_1`
        2. multiple: `Parent_1 < Child_1` && `Parent_2 < Child_1`
        3. multi level: `Parent_1 < Child_1 < Child_2`
        4. hierarchical: `Parent_1 < Child_1` && `Parent_1 < Child_2`
    2. Method resolution order (MRO)
        1. Python use the C3 linearization algorithm to determine the MRO.
        2. `Class_A.mro()`
        3. `help(Class_A)` will also shows info about MRO
    3. example in "2_inheritance.py"
        1. `__init__` and `super()`
        2. `issubclass()`, `isinstance()`


## Module 4 Modules, packages, libraries and tools
### Modules
1. `sys.path`: list of directories that the interpreter will search in for the required module.
2. `sys.path.append()` or `sys.path.insert()` to add a path (`sys.path` return a list).
3. import
```py
import math
import math as m
from math import sqrt
from math import *
```
4. Namespaces and Scope
    1. `globals()` returns a reference to the current global namespace dictionary
    2. `locals()` returns a current copy of the local namespace dictionary
    3. An **immutable** argument can never be modified by a function.
    4. A **mutable** argument can’t be redefined wholesale, but it can be modified in place.
    5. to access and modify an object in the global scope `global x`
    6. to access and modify an object in the enclosing scope `nonlocal x`
5. example in "2_import_and_scope"
6. reload a module
```py
import importlib
importlib.reload(module_name)
```
### testing tools
1. testing steps: planning -> preparation -> execution -> reporting
2. white box, black box
3. functional, non-functional, maintenance
4. levels of testing:
    1. unit/ component: tests specific individual components by isolating them. can be done when writing code
    2. integration: combines the unit tests and tests the flow of data from one component to another.
    3. system: Test all the software.
    4. acceptance: This involves a few end users. Alpha, beta, and regression tests.
5. testing early and testing frequently; the goal is early detection
6. PyTest
    1. `python -m pytest test.py` to run test.py with PyTest
    2. `python -m pytest test.py::test_fn_name` to run a single function in test.py
    3. example in "2_pytest"
7. Test-driven development (TDD): write the test first, and then the code.

## Module 5 Graded assessment
1. some recap

