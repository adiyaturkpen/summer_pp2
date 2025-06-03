#1
'''print("Hello, World!")'''
#2
'''import sys
print(sys.version)'''
#3
'''if 1 > 0:
 print("1 is greater than 0!") '''
#4
'''asdfghjkl;'''
#5
'''x = 1
y = "abc"
print(x)
print(y)'''
#6
'''x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)'''
#7
'''x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0'''
#8
'''x = 1
y = "abc"
print(type(x))
print(type(y))'''
#9
'''a = 4
A = "Sally"
#A will not overwrite a'''
#10
'''myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"'''
#11
'''x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)'''
#12
'''x = y = z = "Orange"
print(x)
print(y)
print(z)'''
#13
'''fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)'''
#14
'''x = "Python is awesome"
print(x)'''
#15
'''x = "Python"
y = "is"
z = "awesome"
print(x, y, z)'''
#16
'''x = "Python "
y = "is "
z = "awesome"
print(x + y + z)'''
#17
'''x = 5
y = 10
print(x + y)'''
#18
'''x = 5
y = "John"
print(x, y)'''
#19
'''x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()'''
#20
'''x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)'''
#21
'''x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)'''
#22
'''x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(type(x))
print(type(y))
print(type(z))'''
#23
'''x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))'''
#24
'''x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))'''
#25
'''x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))'''
#26
'''x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))'''
#27
'''x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))'''
#28
'''x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3'''
#29
'''x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2'''
#30
'''x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be "3.0"'''
#31
'''print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')'''
#32
'''a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)'''
#33
'''a =\'''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.\'''
print(a)'''
#34
'''a = "Hello, World!"
print(a[1])'''
#35
'''for x in "banana":
  print(x)'''
#36
'''a = "Hello, World!"
print(len(a))'''
#37
'''txt = "The best things in life are free!"
print("free" in txt)'''
#38
'''txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
'''
#39
'''txt = "The best things in life are free!"
print("expensive" not in txt)'''
#40
'''txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
'''
#41
'''b = "Hello, World!"
print(b[2:5])'''
#42
'''b = "Hello, World!"
print(b[:5])'''
#43
'''b = "Hello, World!"
print(b[2:])'''
#44
'''b = "Hello, World!"
print(b[-5:-2])'''
#45
'''a = "Hello, World!"
print(a.upper())'''
#46
'''a = "Hello, World!"
print(a.lower())'''
#47
'''a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"'''
#48
'''a = "Hello, World!"
print(a.replace("H", "J"))'''
#49
'''a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']'''
#50
'''a = "Hello"
b = "World"
c = a + b
print(c)'''
#51
'''a = "Hello"
b = "World"
c = a + " " + b
print(c)'''
#52
'''age = 36
txt = f"My name is John, I am {age}"
print(txt)'''
#53
'''price = 59
txt = f"The price is {price} dollars"
print(txt)'''
#54
'''price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)'''
#55
'''txt = f"The price is {20 * 59} dollars"
print(txt)'''
#56
'''txt = "We are the so-called \"Vikings\" from the north."'''