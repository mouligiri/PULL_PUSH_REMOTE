import sys
try:
    x = input("Enter your dob or press ctrl+c to trigger exception")
    
except KeyboardInterrupt:
    print ('KeyboardInterrupt exception is caught')
else:
    print('dob is printed')
finally:
      print("first finally block has executed")
try:
    A=10
    print("Value of number is",a)
except NameError:
    print ("NameError:  'a' is not defined")
else:
    print ("No exception has occured")
finally:
      print("second finally block has executed")    
try:
    
    a= 75/0
    print (a)
except ZeroDivisionError:
    print ("Zero Division Exception Raised.")
else:
    print (" No error!")
finally:
      print("third finally block has executed")    
    
