class Shape():
    def area(self):
        return 0
class Square(Shape):
    def __init__(self,l):
        self.l=l
    def area(self):
        return self.l ** 2
a = float(input("a="))
s=Square(a)
print("S=",s.area())
