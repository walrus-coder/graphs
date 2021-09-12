from queue import Queue

# Функция проверки графа на двудольность с помощью обхода в ширину
def BFS():
    dist = ["inf" for i in range(n)]
    color = ["white"  for i in range(n)]
    for start in range(n):
        if dist[start] == "inf":
            dist[start] = 0
            cash = Queue()
            cash.put(start)
            color[start] = True
            while not cash.empty():
                u = cash.get()
                for v in edges[u]:
                    if color[u] == color[v]:
                        return 0
                    if dist[v] == "inf":
                        color[v] = not color[u]
                        cash.put(v)
                        dist[v] = dist[u] + 1
    return 1

if '__main__' == __name__:
    n, m = tuple(map(int, input().split()))
    edges = [[] for i in range(n)]
    for j in range(m):
        e = tuple(map(int, input().split()))
    #    e = (random.randint(1,n), random.randint(1,n))
        if e[0] != e[1]:
            edges[e[0]-1].append(e[1]-1)
            edges[e[1]-1].append(e[0]-1)
    print(BFS())
