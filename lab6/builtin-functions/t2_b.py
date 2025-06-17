a=input()
u=0
l=0
for i in a:
    for j in i:
        if j==" ":
            continue
        elif j==j.lower():
            l+=1
        else:
            u+=1
print("u=",u,"l=",l)