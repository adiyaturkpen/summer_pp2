import os
a=input()
if os.path.exists(a):
    print("path exist")
    print("filename:", os.path.basename(a))
    print("directory:", os.path.dirname(a))
else:
    print("path does not exist")
