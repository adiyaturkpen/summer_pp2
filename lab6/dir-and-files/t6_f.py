for i in range(65,91):
    f=chr(i)+ ".txt"
    with open(f, 'w') as file:
        file.write("Hello world!")