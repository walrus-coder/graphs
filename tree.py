import queue

# Создание класса узла бинарного дерева
class Node:
    def __init__(self,key = None):
        self.key = key
        self.childs = []

    def AddChild(self, node):
        if self.key == None:
            self = node
        else:
            self.childs.append(node)

#Создание класса самого дерева
class Tree:
    def __init__(self,n):
       self.nodes = [Node(i) for i in range(n)]
       self.root = None

    def AddChild(self, child, parentKey):
        self.nodes[parentKey].AddChild(child)

    def setRoot(self,i):
        self.root = tree.nodes[i]

n = int(input())
seq = tuple(map(int, input().split()))

# Заполнение дерева
tree = Tree(n)
for i in range(n):
    if seq[i] != -1:
        tree.AddChild(tree.nodes[i], seq[i])
    else:
        tree.setRoot(i)

# Рекурсивный алгоритм для нахождения высоты дерева
def Height(tree):
    if tree.root == None:
        return 0
    h = 0
    for leaf in tree.root.childs:
        tree.root = leaf
        h = max(h, Height(tree))
    return h + 1

#Итеративный алгоритм для нахождения высоты дерева
def HeightIter(tree):
    buffer = queue.Queue()
    buffer.put(tree.root)
    dist = [None for i in range(n)]
    dist[tree.root.key] = 1
    while not buffer.empty():
        cur = buffer.get()
        for leaf in cur.childs:
            dist[leaf.key] = dist[cur.key] + 1
            ans = dist[leaf.key]
            buffer.put(leaf)
    return ans
        



print(HeightIter(tree))





