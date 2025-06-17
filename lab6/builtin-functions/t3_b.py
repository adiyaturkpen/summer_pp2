a=input()
b=''.join(reversed(a))
s=0
for i in range(len(a)):
    if a[i]==b[i]:
        s+=1
if s==len(a):
    print("polindrome")
else:
    print("not polindrome")