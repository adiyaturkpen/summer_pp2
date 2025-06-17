a=list(map(int,input().split()))
b=1
for i in range(len(a)):
    b*=a[i]
print(b)