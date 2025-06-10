def unique(lst):
    unique_l=[]
    for i in lst:
        if i not in unique_l:
            unique_l.append(i)
    return unique_l
list_= input()
lst = list_.split()  
print(unique(lst))
