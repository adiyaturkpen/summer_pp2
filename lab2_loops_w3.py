#1
'''print(10 > 9)
print(10 == 9)
print(10 < 9)'''
#2
'''a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")'''
#3
'''print(bool("Hello"))
print(bool(15))'''
#4
'''x = "Hello"
y = 15

print(bool(x))
print(bool(y))'''
#5
'''bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])'''
#6
'''bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})'''
#7
'''class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))'''
#8
'''def myFunction() :
  return True

print(myFunction())'''
#9
'''def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")'''
#10
'''x = 200
print(isinstance(x, int))'''
#11
'''thislist = ["apple", "banana", "cherry"]
print(thislist)'''
#12
'''thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)'''
#13
'''thislist = ["apple", "banana", "cherry"]
print(len(thislist))'''
#14
'''list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]'''
#15
'''mylist = ["apple", "banana", "cherry"]
print(type(mylist))'''
#16
'''thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)'''
#17
'''thislist = ["apple", "banana", "cherry"]
print(thislist[1])'''
#18
'''thislist = ["apple", "banana", "cherry"]
print(thislist[-1])'''
#19
'''thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])'''
#20
'''thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])'''
#21
'''thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])'''
#22
'''thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])'''
#23
'''thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")'''
#24
'''thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)'''
#25
'''thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)'''
#26
'''thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)'''
#27
'''thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)'''
#28
'''thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)'''
#29
'''thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)'''
#30
'''thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)'''
#31
'''thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)'''
#32
'''thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)'''
#33
'''thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)'''
#34
'''thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)'''
#35
'''thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)'''
#36
'''thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)'''
#37
'''thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)'''
#38
'''thislist = ["apple", "banana", "cherry"]
del thislist'''
#39
'''thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)'''
#40
'''thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)'''
#41
'''thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])'''
#42
'''thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1'''
#43
'''thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]'''
#44
'''fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)'''
#45
'''fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)'''
#46
'''newlist = [x for x in fruits if x != "apple"]'''
#47
'''newlist = [x for x in fruits]'''
#48
'''newlist = [x for x in range(10)]'''
#49
'''newlist = [x for x in range(10) if x < 5]'''
#50
'''newlist = [x.upper() for x in fruits]'''
#51
'''newlist = ['hello' for x in fruits]'''
#52
'''newlist = [x if x != "banana" else "orange" for x in fruits]'''
#53
'''thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)'''
#54
'''thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)'''
#55
'''thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)'''
#56
'''thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)'''
#57
'''def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)'''
#58
'''thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)'''
#59
'''thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)'''
#60
'''thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)'''
#61
'''thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)'''
#62
'''thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)'''
#63
'''thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)'''
#64
'''list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)'''
#65
'''list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)'''
#66
'''list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)'''
#67
'''thistuple = ("apple", "banana", "cherry")
print(thistuple)'''
#68
'''thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)'''
#69
'''thistuple = ("apple", "banana", "cherry")
print(len(thistuple))'''
#70
'''thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))'''
#71
'''tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)'''
#72
'''tuple1 = ("abc", 34, True, 40, "male")'''
#73
'''mytuple = ("apple", "banana", "cherry")
print(type(mytuple))'''
#74
'''thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)'''
#75
'''thistuple = ("apple", "banana", "cherry")
print(thistuple[1])'''
#76
'''thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])'''
#77
'''thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])'''
#78
'''thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])'''
#79
'''thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])'''
#80
'''thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])'''
#81
'''thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")'''
#82
'''x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)'''
#83
'''thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)'''
#84
'''thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)'''
#85
'''thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)'''
#86
'''thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) 
#this will raise an error because the tuple no longer exists'''
#87
'''fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)'''
#88
'''fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)'''
#89
'''fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)'''
#90
'''thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)'''
#91
'''thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])'''
#92
'''thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1'''
#93
'''tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)'''
#94
'''fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)'''
#95
'''thisset = {"apple", "banana", "cherry"}
print(thisset)'''
#96
'''thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)'''
#97
'''thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)'''
#98
'''thisset = {"apple", "banana", "cherry"}

print(len(thisset))'''
#99
'''myset = {"apple", "banana", "cherry"}
print(type(myset))'''
#100
'''thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)'''
#101
'''thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)'''
#102
'''thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)'''
#103
'''thisset = {"apple", "banana", "cherry"}

print("banana" not in thisset)'''
#104
'''thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)'''
#105
'''thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)'''
#106
'''thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)'''
#107
'''thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)'''
#108
'''thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)'''
#109
'''thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)'''
#110
'''thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)'''
#111
'''thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)'''
#112
'''thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)'''
#113
'''set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)'''
#114
'''set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)'''
#115
'''set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)'''
#116
'''set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)'''
#117
'''x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)'''
#118
'''set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)'''
#119
'''set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)'''
#120
'''set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)'''
#121
'''set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)'''
#122
'''set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3)'''
#123
'''set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)'''
#124
'''set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)'''
#125
'''set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)'''
#126
'''set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)'''
#127
'''set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)'''
#128
'''set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)'''
#129
'''thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)'''
#130
'''thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])'''
#131
'''thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
print(len(thisdict))'''
#132
'''thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))'''
#133
'''thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)'''
#134
'''thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]'''
#135
'''x = thisdict.get("model")'''
#136
'''x = thisdict.keys()'''
#137
'''car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change'''
#138
'''car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change'''
#139
'''car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["color"] = "red"

print(x) #after the change'''
#140
'''car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change'''
#141
'''car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["color"] = "red"

print(x) #after the change'''
#142
'''thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")'''
#143
'''thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018'''
#144
'''thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})'''
#145
'''thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)'''
#146
'''thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})'''
#147
'''thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)'''
#148
'''thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)'''
#149
'''thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)'''
#150
'''thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists.'''
#151
'''thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)'''
#152
'''for x in thisdict:
  print(x)'''
#153
'''for x in thisdict:
  print(thisdict[x])'''
#154
'''for x in thisdict.values():
  print(x)'''
#155
'''for x in thisdict.keys():
  print(x)'''
#156
'''for x, y in thisdict.items():
  print(x, y)'''
#157
'''thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)'''
#158
'''thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)'''
#159
'''child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}'''
#160
'''print(myfamily["child2"]["name"])'''
#161
'''for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])'''
#162
'''a = 33
b = 200
if b > a:
  print("b is greater than a")'''
#163
'''a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")'''
#164
'''a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")'''
#165
'''a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")'''
#166
'''if a > b: print("a is greater than b")'''
#167
'''a = 2
b = 330
print("A") if a > b else print("B")'''
#168
'''a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")'''
#169
'''a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")'''
#170
'''a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")'''
#171
'''a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")'''
#172
'''x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")'''
#173
'''a = 33
b = 200

if b > a:
  pass'''
#174
'''i = 1
while i < 6:
  print(i)
  i += 1'''
#175
'''i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1'''
#176
'''i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)'''
#177
'''i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")'''
#178
'''fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)'''
#179
'''for x in "banana":
  print(x)'''
#180
'''fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break'''
#181
'''fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)'''
#182
'''fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)'''
#183
'''for x in range(6):
  print(x)'''
#184
'''for x in range(2, 6):
  print(x)'''
#185
'''for x in range(2, 30, 3):
  print(x)'''
#186
'''for x in range(6):
  print(x)
else:
  print("Finally finished!")'''
#187
'''for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")'''
#188
'''adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)'''
#189
'''for x in [0, 1, 2]:
  pass'''