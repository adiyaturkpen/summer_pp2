import os
a=input()
if os.path.exists(a):
    print("path exist")
    if os.access(a, os.R_OK):
        print("readable")
    else:
        print("not readable")
    if os.access(a, os.W_OK):
        print("writable")
    else:
        print("not writable")
    if os.access(a, os.X_OK):
        print("executable")
    else:
        print("not executable")
else:
    print('path does not exist')
    