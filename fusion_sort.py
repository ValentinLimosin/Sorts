from random import randrange
import time

def merge(left, right):
    left_i, right_i = 0, 0
    res = []
    while left_i < len(left) and right_i < len(right):
        if left[left_i] < right[right_i]:
            res.append(left[left_i])
            left_i += 1
        else:
            res.append(right[right_i])
            right_i += 1
    res += left[left_i:]
    res += right[right_i:]
    return res

def sort(lst):
    if len(lst) <= 1:
        return lst
    middle = len(lst)//2
    left = sort(lst[:middle])
    right = sort(lst[middle:])
    return merge(left, right)

def genlst(n):
    c = []
    for i in range(n,0,-1):
        c.append(i)
    return(c)


n = 1000000
lst = genlst(n)
t1 = time.time()
lst = sort(lst)
t2 = time.time()
print("Le programme a trié :",n," valeur(s) en ", t2-t1,"seconde(s)")
