class FirstClass:
    def testMethod(self):
        print("First Class")
      
class SecondClass(FirstClass):
    def testMethod(self):
        print("Second Class")
        super().testMethod()
    
class ThirdClass(FirstClass):
    def testMethod(self):
        print("Third Class")
        super().testMethod()
     
class FourthClass(SecondClass, ThirdClass):
    def testMethod(self):
        print("Fourth Class")
        super().testMethod()





obj = FourthClass()
obj.testMethod()
 
