Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> #1.Given a string, return the string made of its first two chars, so the String "Hello" yields "He". If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "".
>>> 
>>> def first_two(str):
...     if len(str) < 2:
...         return str
...     print(str[0:2])
... 
...     
>>> first_two("Hello")
He
>>> first_two("x")
'x'
>>> first_two()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    first_two()
TypeError: first_two() missing 1 required positional argument: 'str'
>>> first_two("")
''
