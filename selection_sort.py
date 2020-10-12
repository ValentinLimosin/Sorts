from random import randrange
import time

def selection(lst) :
    for j in range(0,len(lst)-1):
        Min = j
        for k in range(j+1,len(lst)) :
            if lst[k] < lst[Min] :
                Min = k
        lst[j],lst[Min]=lst[Min],lst[j]

def genlst(n):
    c = []
    for i in range(n,0,-1):
        c.append(i)
    return(c)

lst = genlst(10000)
t1 = time.time()
selection(lst)
t2 = time.time()
print("Le programme a trié :",len(lst)," valeur(s) en ", t2-t1,"seconde(s)")
