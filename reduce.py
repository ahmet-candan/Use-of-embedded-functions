from functools import reduce
"""def toplama(x,y):
    return x + y
print(reduce(toplama,[1,2,3,4]))"""

print(reduce(lambda x,y: x*y,[1,2,3,4,5]))

def max(x,y):
    if(x>y):
        return x
    else:
        return y
print(reduce(max,[-2,5,7,-7]))
