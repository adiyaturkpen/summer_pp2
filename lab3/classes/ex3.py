class Shape():
    def area(self):
        return 0
class Rectangle(Shape):
    def __init__(self,l,w):
        self.l=l
        self.w=w
    def area(self):
        return self.l * self.w
a=float(input("a="))
b=float(input("b="))
s=Rectangle(a,b)
print("S=",s.area())
