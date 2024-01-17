Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #1.Given a string, return the string made of its first two chars, so the String "Hello" yields "He". If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "".
>>> 
>>> 
>>> def first_two(str):
...     if len(str) < 2:
...         return str
...     print(str[0:2])
... 
...     
>>> first_two("Hello")
He
>>> first_two("abcdefg")
ab
>>> first_two("ab")
ab
>>> 
>>> 
>>> 
>>> #2.Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.
>>> 
>>> def extra_end(str):
...     if len(str) < 2
...     
SyntaxError: expected ':'
>>> 

... 
>>>    if len(str) < 2:
...        
SyntaxError: unexpected indent
>>> 
... def extra_end(str):
...     if len(str) < 2:
...         return str
...     print (str[-2:]*3)
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
>>> 
>>> 
>>> #3.Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".
>>> 
>>> def first_half(str):
...     iflen(str) % 2 != 0:
...         
SyntaxError: invalid syntax
>>> def first_half(str):
...     iflen(str) % 2 != 0:
...         
SyntaxError: invalid syntax
>>> def first_half(str):
    if len(str) % 2 != 0:
        print("the length of the string is odd.")
        middle =int(len(str) /2)
        print(str[:middle])

        
first_half("WooHoo")

def first_half(str):
    if len(str) % 2 != 0:
        print("the length of the string is odd.")
        middle =int(len(str) /2)
        return (str[:middle])

    
first_half("WooHoo")

def first_half(str):
    middle = len(str) // 2
    return str[0:middle]

data = input("enter the string:")
enter the string:WooHoo
print("first half of the string is:",first_half(data))
first half of the string is: Woo
first half of the string is: Woo
SyntaxError: invalid syntax
data = input("enter the string:")
enter the string:HelloThere
print("first half of the string is:",first_half(data))
first half of the string is: Hello


#4Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.


def without_end(str):
    if len(str) < 2:
        return str
    
    # If the num is even,
    if len(str) % 2 == 0:
        half_len_str = int(len(str)/2)
        front = str[1:half_len_str]
        rear = str[-half_len_str:-1]
        print(front + rear)
    
    # If the num is odd,
    else:
        half_len_str = int(len(str)/2)
        front = str[1:half_len_str]
        rear = str[-half_len_str-1:-1]
        print(front + rear)

        

without_end('Hello')
ell
without_end('hello world')
ello worl
len('hello world')
11


def without_end(str):
    if len(str) < 2:
        return str
    
    # If the num is even,
    if len(str) % 2 == 0:
        half_len_str = int(len(str)/2)
        front = str[1:half_len_str]
        rear = str[-half_len_str:-1]
        print(front + rear)
    
    # If the num is odd,
    else:
        half_len_str = int(len(str)/2)
        front = str[1:half_len_str]
        rear = str[-half_len_str:-1]
        print(front + rear)

        
without_end('Hello')
el
without_end('Helo')
el
KeyboardInterrupt
without_end('Hllo')
ll


#5 Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".

def make_abba(a,b):
    print(a+b+b+a)

    
make_abba('Hi','Bye')
HiByeByeHi
make_abba('Yo','Alice')
YoAliceAliceYo
make_abba('What','up')
WhatupupWhat


#6 Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. The strings will not be the same length, but they may be empty (length 0).


def combo_string(a,b)
SyntaxError: expected ':'
def combo_string(a,b):
    if len(a) < len(b):
        print(a + b + a)

        
elif len(a) == len(b) or len(a) == len(b) == 0:
    
SyntaxError: invalid syntax
def combo_string(a,b):
    if len(a) < len(b):
        print(a + b + a)

      elif  len(a) == len(b) or len(a) == len(b) == 0:
          
SyntaxError: unindent does not match any outer indentation level
def combo_string(a,b):
    if len(a) < len(b):
        print(a + b + a)
        elif len(a) == len(b) or len(a) == len(b) == 0:
            
SyntaxError: invalid syntax
def combo_string(a,b):
    if len(a) < len(b):
        print(a + b + a)
        elif len(a) == len(b) or len(a) == len(b) == 0 :
            
SyntaxError: invalid syntax
def combo_string(a,b):
    if len(a) < len(b):
        print(a + b + a)

        
else:
    
SyntaxError: invalid syntax
def combo_string(a, b):
  if len(a) < len(b):
        print(a + b + a)
        elif len(a) == len(b) or len(a) == len(b) == 0:
            
SyntaxError: invalid syntax
def combo_string(a, b):
  short = ""
  long = ""
  if len(a) < len(b):
      short = a
      long = b
      print(short + long + short)

      
eli len(a) == len(b) or len(a) == len(b) ==0:
    
SyntaxError: invalid syntax
def combo_string(a, b):
  short = ""
  long = ""
  if len(a) < len(b):
      short = a
      long = b
      print(short + long + short)
      elif len(a) == len(b) or len(a) == len(b) ==0:
          
SyntaxError: invalid syntax
def combo_string(a, b):
  short = ""
  long = ""
  if len(a) < len(b):
      short = a
      long = b
      print(short + long + short)
      else:
          
SyntaxError: invalid syntax
def combo_string(a, b):
  short = ""
  long = ""
  if len(a) < len(b):
      short = a
      long = b
      print(short + long + short)

      
combo_string('Hello','hi')

def combo_string(a, b):
    short = ""
    long = ""
    
    if len(a) < len(b):
        short = a
        long = b
        print(short + long + short)

        
