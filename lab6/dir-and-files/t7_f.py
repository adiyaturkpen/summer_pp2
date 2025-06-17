f=open(r"C:\Users\Lenovo\pp2\pp2-summer\lab6\dir-and-files\lab6.txt")
with open("lab6_2.txt", 'w') as file:
        file.write(f.read())