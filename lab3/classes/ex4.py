import math
class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x=new_x
        self.y=new_y

    def dist(self, other):
        return math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2)

x1=float(input("x1: "))
y1=float(input("y1: "))
p1=Point(x1, y1)
x2=float(input("x2: "))
y2=float(input("y2: "))
p2=Point(x2, y2)
new_x=float(input("new x1: "))
new_y=float(input("new y1: "))
p1.move(new_x, new_y)
print("new point1:")
p1.show()
print("point2:")
p2.show()
print("distance:", p1.dist(p2))
