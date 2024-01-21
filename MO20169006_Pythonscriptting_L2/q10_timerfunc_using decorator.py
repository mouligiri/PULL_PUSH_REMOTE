from time import time
  
  
def timer_func(func):
    # This function shows the execution time of 
    # the function object passed
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {t2-t1}s' )#func._name_!r is used for printting which function is executed
        
    return (wrap_func)
  
  
@timer_func
def long_time(n):
    for i in range(n):
        for j in range(10):
            i*j
  
  
long_time(6)
