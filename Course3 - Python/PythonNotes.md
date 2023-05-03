# Python Notes

### Basics

- Naming: snake_case
- Syntax: no `;`, no `{}`, indentation + `:`, `#`
- defining function: `def func:`
- Data type:
  - Numeric: int, float, complex
  - Sequence: str, list`[]`, tuple `()`
  - Boolean: bool
  - Dictionary: dict `{}`
  - Set: set`{}`
- Scope resolution: LEGB

### Useful built-in functions

- round(num, 2)
- split("\n")
- `import random` random.choice(list)
- Slicing and reverse `str[::-1]`
- `map(func, list)`, returns a map object
- `filter(func, list)` but only contains true values, "none" are "filtered"
- `for (key, value) in zip(list1, list2)`
- `str.replace("a","b")`

### Class

- class name in CamelCase
- constructor: `__init__(self) -> None`; using `self` keyword
- ABC and `mro()`, `help()`

### Comparing diff languages

- Java, JS, React, Python
- Naming convention (folder, module, class, variables)
- scope
- variable declaration / type
- Built-in data types
- function definition
- class definition
  - constructor, `this`
  - private / static members
- importing & exporting modules

### Comprehensions

- List comprehension
  - `[ <expression> for x in <sequence> if <condition>] `
- Dictionary comprehension
  - `dict = { key:value for key, value in <sequence> if <condition> } `
- Set's: similar to list but with `{}`
- Generator: similar to list but with `()`

### In / Outputs

- print(), print(f"{str:<8} is ...")
- input(), exit()

### File handling

- with open(filename or location, mode='r') as file
  - (automatically calls close())
  - open() default mode 'r'
  - mode: 'r', 'rb', 'r+', 'w' overrides!, 'a'
  - file default is a list
- Create new file, set mode='w'
  - file.write("sth")
  - file.writelines(["Line1", "\nLine2"])
- Read
  - readline(): first line or n charaters;
  - readlines(): return all as a list
  - read(): return all as string or first n characters

### Paths

- Absolute paths: leading forward slash `/` or drive label
- Relative paths: `file.txt`, or `./file.txt`

### Exceptions

- try: expect:
- Exceptions:
  - IndexError,
  - ZeroDivisionError,
  - FileNotFoundError,
- base class for user-defined exceptions: Exception
