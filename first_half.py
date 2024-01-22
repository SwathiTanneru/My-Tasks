Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #3.Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".
... 
... def first_half(str):
...     first_half_str = len(str) // 2
...     return str[0:first_half_str]
... 
>>> first_half("WooHoo")
'Woo'
>>> first_half("HelloThere")
'Hello'
>>> first_half("Hello")
'He'
