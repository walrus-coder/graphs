import math

# Класс для двоичной кучи с указателями на номер индекса из кучи для каждого узла
class BinHeap:
    def __init__(self, l):
        self.heap = l
        self.numOfNodes = len(l)
        self.pointer = [i for i in range(self.numOfNodes)]

# Функция смены местами элементов бинарной кучи с соответствующей заменой в массиве указателей
    def swap(self, i_1, i_2):
        self.heap[i_1], self.heap[i_2] = self.heap[i_2], self.heap[i_1]
        j_1 = self.heap[i_1][1]
        j_2 = self.heap[i_2][1]
        self.pointer[j_1], self.pointer[j_2] = self.pointer[j_2], self.pointer[j_1]

# Функции поднятия/опускания элемента в бинарной куче
    def ShiftUp(self, ind):
        while ind > 0:
            parent = (ind+1)//2-1
            if self.heap[parent][0] > self.heap[ind][0]:
                self.swap(parent, ind)
                ind = parent
            else:
                break

    def ShiftDown(self, ind):
        ind += 1
        length = len(self.heap)
        while 2 * ind  <= length:
            min_ind = ind - 1
            left = 2*ind - 1
            if self.heap[min_ind][0] > self.heap[left][0]:
                min_ind = left
            if 2 * ind + 1 <= length:
                right = 2*ind
                if self.heap[min_ind][0] > self.heap[right][0]:
                    min_ind = right
            ind = ind - 1
            if ind == min_ind:
                break
            else:
                self.swap(min_ind, ind)
                ind = min_ind
                ind += 1

# Достать минимальный элемент за логарифмическое время
    def ExtractMin(self):
        self.swap(0,-1)
        res = self.heap.pop()
        self.pointer[res[1]] = None
        self.ShiftDown(0)
        return res

# Функция восстановления порядка двоичной кучи после изменения одного из ее значений за логарифмическое время
    def ChangePriority(self, ind, old_dist):
        new_dist = self.heap[ind][0]
        if new_dist < old_dist:
            self.ShiftUp(ind)
        else:
            self.ShiftDown(ind)

    def Empty(self):
        return len(self.heap) == 0

# Сам алгоритм Дейкстры
def shortest_path(s):
    dist = [[math.inf, i] for i in range(n)] # В каждом элементе массива другой массив с расстоянием (по умолчанию бесконечным) и номером узла
    dist[s][0] = 0                           # Задание узла, от которого меряется расстояние до других узлов нулевым значением расстояния
    H = BinHeap(list(dist))
    H.swap(0,s)
    while not H.Empty():
        min = H.ExtractMin()
        i = min[1]
        p = min[0]
        # Обход соседей последнего полученного из кучи узла (до которого расстояние точно известно)
        for e in edges[i]:
            if dist[e][0] > p + w[i][e]:
                old = dist[e][0]
                dist[e][0] = p + w[i][e]
                # При изменении элемента массива dist сразу изменяется и соответсвующее значение для расстояния в бинарной куче
                H.ChangePriority(H.pointer[e], old)
    return dist

# Ввод графа и вывод ответа
n,m = tuple(map(int, input().split()))       # Ввод чисел n вершин и m ребер в графе
w = [[0 for i in range(n)] for i in range(n)]
edges = [[] for i in range(n)]   
# Поочередный ввод m ребер направленного графа (начало и конец, целые числа от 0 до n) и веса ребра (вещественное число) через пробел
for i in range(m):
    u, v, k = tuple(map(int, input().split()))
    u = u-1
    v = v-1
    w[u][v] = k
    edges[u].append(v)
a,b = tuple(map(int, input().split()))       # Вершина, из которой идем и вершина, в которую идем (2 целых числа)
ans = shortest_path(a-1)
if ans[b-1][0] == math.inf:
    print(-1)
else:
    print(ans[b-1][0])


