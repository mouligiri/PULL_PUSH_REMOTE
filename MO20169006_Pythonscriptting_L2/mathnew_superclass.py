import math
class sqroot:
    def sqrt(self,a):
        print(math.sqrt(a))

class addition:
    def add(self,a,b):
        print(a+b)

class subtraction:
    def sub(self,a,b):
        print(a-b)

class multiplication:
    def mul(self,a,b):
        print(a*b)

class division:
    def div(self,a,b):
        print(a//b)

class mathnew(sqroot, addition, subtraction, multiplication, division):
    
    def sqrt(self, a):
        return super().sqrt(a)
    def add(self, a, b):
        return super().add(a, b)
    def sub(self, a, b):
        return super().sub(a, b)
    def mul(self, a, b):
        return super().mul(a, b)
    def div(self, a, b):
        return super().div(a, b)
m = mathnew()

m.sqrt(4)
m.add(4,5)
m.sub(5,8)
m.mul(5,6)
m.div(47,2)
