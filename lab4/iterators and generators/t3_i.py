a = int(input())
b = (i for i in range(12, a + 1, 12))
print(*b, sep=", ")
