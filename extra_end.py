Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> #2.Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.
... 
>>> 
>>> def extra_end(str):
...     if len(str) < 2:
...         return str
...     print(str[-2:]*3)
... 
...     
>>> extra_end("Hello")
lololo
>>> extra_end("ab")
ababab
>>> extra_end("hi")
hihihi
>>> extra_end("H")
'H'
