from collections import Counter
from functools import cmp_to_key


lines = [l.strip() for l in open("zad7_data").readlines()]

def typ(reka):
    counter = Counter(reka)
    powtarz = counter.most_common()
    if powtarz[0][1] == 5:
        return 7
    elif powtarz[0][1] == 4:
        return 6
    elif powtarz[0][1] == 3 and powtarz[1][1] == 2:
        return 5
    elif powtarz[0][1] == 3:
        return 4
    elif powtarz[0][1] == 2 and powtarz[1][1] == 2:
        return 3
    elif powtarz[0][1] == 2:
        return 2
    return 1

def cmp(pierw, drug):
    mozliwe = {'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7,'9':8,'T':9,'J':10,'Q':11,'K':12,'A':13}
    pierw = pierw[0]
    drug = drug[0]
    t1 = typ(pierw)
    t2 = typ(drug)
    if t1 != t2:
        if t1 < t2:
            return -1
        else:
            return 1
    else:
        for i in range(0,5):
            if mozliwe[pierw[i]] < mozliwe[drug[i]]:
                return -1
            elif mozliwe[pierw[i]] > mozliwe[drug[i]]:
                return 1
    return 0


reka = []
for line in lines:
    linia = line.split()
    reka.append((linia[0], int(linia[1])))
reka.sort(key=cmp_to_key(cmp))
odp=0
for i in range(len(reka)):
    odp+=(i+1)*(reka[i][1])
print(odp)