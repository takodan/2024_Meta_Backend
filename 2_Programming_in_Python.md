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


## Module 4 Modules, packages, libraries and tools
## Module 5 Graded assessment