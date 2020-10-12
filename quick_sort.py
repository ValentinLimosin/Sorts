import time

def sort(lst, l, r):
    if r > l:
        pivot_i = median(lst, l, r, (l + r) // 2)
        lst[l], lst[pivot_i] = lst[pivot_i], lst[l]
        i = l
        for j in range(l+1, r+1):
            if lst[j] < lst[l]:
                i += 1
                lst[i], lst[j] = lst[j], lst[i]
        lst[i], lst[l] = lst[l], lst[i]
        sort(lst, l, i-1)
        sort(lst, i+1, r)

def median(a, i, j, k):
  if a[i] < a[j]:
    return j if a[j] < a[k] else k
  else:
    return i if a[i] < a[k] else k

def genlst(n):
    c = []
    for i in range(n,0,-1):
        c.append(i)
    return(c)

n = 1000000
lst = genlst(n)
t1 = time.time()
sort(lst, 0, len(lst) - 1)
t2 = time.time()
print("Le programme a trié :",n," valeur(s) en ", t2-t1,"seconde(s)")
