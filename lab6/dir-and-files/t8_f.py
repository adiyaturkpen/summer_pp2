import os
a=input()
if os.path.exists(a):
  os.remove(a)
else:
  print("The file does not exist")