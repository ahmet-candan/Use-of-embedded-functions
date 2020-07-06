#print(list(filter(lambda x: x % 2 == 0,[1,2,3,4,5,6,7,8])))

def asal(x):
    i = 2
    if x==1:
        return False
    elif x==2:
        return True

    else:
        while i<x:

            if(x%i==0):
                return False
            i+=1
            return True
            
print(list(filter(asal,range(0,100))))
             
