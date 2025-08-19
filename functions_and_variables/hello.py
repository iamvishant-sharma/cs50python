#print ("Hello, world")

# print = built-in function
# ("Hello, world") = argument
# Output = Hello, world --> Side effect

# print ("Hello, world" --> SyntaxError: '(' was never closed --> Bug

# name = input("what your name? ")

## use case of end in print means how we want to end our print statement
## by default it '\n' as per the python documentation
## print(*objects, sep=' ', end='\n', file=None, flush=False)

# print("Hello ", end="")
# print(name)
# Output: Hello, Vishant

## use case of sep in print means how we want to seperate our print statement
## by default it ' ' as per the python documentation

# print("Hello ", name, sep="&&&&&")
# Output: Hello &&&&&abc

# print(f"Hello, {name}") ##--> f is a special indicator for Python to treat this string a special way,

# By utilizing the strip method on name (for example, name = name.strip()), 
# you will remove any whitespace from the left and right of the user’s input.
# name = input("what your name? ").strip().capitalize()

# first, last = name.split(" ")
# print(f"Hello, {first}")