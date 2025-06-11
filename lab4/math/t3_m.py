import math
n=int(input("Number of sides:"))
a=int(input("The length of a side:"))
area = (n * a**2) / (4 * math.tan(math.pi / n))
print("Area:",area)