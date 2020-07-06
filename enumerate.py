liste =["kavun","karpuz","kiraz"]
liste2 = ["a","b","c","d","f","g"]

#örenk1
"""i = 0
sonuc = list()

for a in liste:
    sonuc.append((i,a))
    i+=1
print(sonuc)"""


#örenk2
print(list(enumerate(liste)))


#örenk3
for index,a in enumerate(liste2):
    if index%2 == 0:
        print(a)
    


