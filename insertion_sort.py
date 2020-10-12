import time

def insertion(lst=None):
    for i in range(len(lst)):
        c = lst[i]
        j = i
        while j > 0 and lst[j-1] > c:
            lst[j] = lst[j-1]
            j -= 1
        lst[j] = c


def genlst(n):
    c = []
    for i in range(n, 0, -1):
        c.append(i)
    return c

lst = genlst(10000)
t1 = time.time()
insertion(lst)
t2 = time.time()
print("Le programme a trié :", 1000000, " valeur(s) en ", t2-t1, "seconde(s)")
