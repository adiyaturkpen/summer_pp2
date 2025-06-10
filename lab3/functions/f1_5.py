def permutations(st):
    if len(st) == 1:
        return [st]  
    perm_l = []
    for i in range(len(st)):
        rem = st[:i] + st[i+1:]
        for perm in permutations(rem):
            perm_l.append(st[i] + perm) 
    return perm_l

st = input()
perms = permutations(st)
print(perms)
