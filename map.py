"""def double(x):
    return x*2

print(list(map(double,[1,2,3,4,5,6])))"""

#print(list(map(lambda x: x**2,[1,2,3,4,5,6,7])))

liste1 = [1,2,3,4]
liste2 = [5,6,7,8]
liste3 = [9,10,11,12]

print(list(map(lambda x,y: x*y,liste1,liste2)))



