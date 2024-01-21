import math
def factorial(x):
    
    factorial = 1
    if int(x) >= 1:
      for i in range (1,int(x)+1):
         factorial = factorial * i
    return( factorial)
    
def log_ten(x):
    
     y=math.log(x,10)
     return(y)
def degreetorad(x):
     z=x * (math.pi / 180)
     return(z)

def trigonmetry(x):
    k=degreetorad(x)
    l=(math.sin(k)) 
    m=(math.tan(k))
    n=(math.cos(k))
    return(l,m,n)

    


