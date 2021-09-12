from queue import Queue

# Нахождение расстояния в графе от опорного элемента с помощью поиска в ширину
def BFS(start, end):
    dist = ["inf" for i in range(n)]
    dist[start] = 0
    cash = Queue()
    cash.put(start)
    while not cash.empty():
        u = cash.get()
        for v in edges[u]:
            if dist[v] == "inf":
                cash.put(v)
                dist[v] = dist[u] + 1
                if v == end:
                    return dist[v]
    return -1

if '__main__' == __name__:
    n, m = tuple(map(int, input().split()))
    edges = [[] for i in range(n)]
    for j in range(m):
        e = tuple(map(int, input().split()))
    #    e = (random.randint(1,n), random.randint(1,n))
        if e[0] != e[1]:
            edges[e[0]-1].append(e[1]-1)
            edges[e[1]-1].append(e[0]-1)
    start, end = tuple(map(int, input().split()))
    print(BFS(start-1,end-1))
    


