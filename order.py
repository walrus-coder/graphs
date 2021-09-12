import random
from datetime import datetime
import time

# Нахождение postorder порядка элементов в графе с помощью обхода в глубину
def explore(i):
    if visited_const[i]:
        return
    if visited_temp[i]:
        dag[0] = False
        return
    visited_temp[i] = True
    for ed in edges[i]:
        explore(ed)
    visited_temp[i] = False
    order.append(i+1)
    visited_const[i] = True
    return


if '__main__' == __name__:
    n, m = tuple(map(int, input().split()))
    start = datetime.now()
    edges = [[] for i in range(n)]
    for j in range(m):
        e = tuple(map(int, input().split()))
    #    e = (random.randint(1,n), random.randint(1,n))
        if e[0] != e[1]:
            edges[e[0]-1].append(e[1]-1)
    order = []
    visited_temp = [False] * n
    visited_const = [False] * n
    dag = [True]
    next = 0
    while ((next < n) & (dag[0])):
        explore(next)
        next += 1
    order.reverse()
    end = datetime.now()
    if dag[0]:
        #print("Done, execute time equals ", end - start)
        print(" ".join(map(str,order)))
    else:
        print("Not a DUG")

