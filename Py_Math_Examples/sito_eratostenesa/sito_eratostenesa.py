#Sito Eratostenesa - poszukiwanie liczb pierwszych

from math import sqrt

def od_do(od, do):
    zw=[]
    while od!=do+1:
        zw.append(od)
        od+=1
    return zw

def sito(do):
    sq = int(sqrt(do)) 
    obecnie=1           
    tab=od_do(1, do)   
    while True:
        if obecnie>sq:
            return tab

        for i in tab:  
            if (not(i%obecnie) and not(obecnie==i)) and obecnie!=1: 
                tab.remove(i)

        i = tab.index(obecnie)+1
        obecnie = tab[i]
        
n = int(input("Podaj gorny zakres dzialania sita: "))
pierwsze = sito(n)
for pierwsza in pierwsze:
        print (pierwsza)
