a = int(input())
b = (i for i in range(2, a + 1, 2))
print(*b, sep=", ")
