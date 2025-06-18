a = ['a', 'bb', 'ccc', 'dddd']
f = open('list.txt', 'w')
for i in a:
    f.write(i + '\n')
f.close()
