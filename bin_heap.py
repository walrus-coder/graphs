import random

# Расстановка элементов массива в порядке двоичной кучи с последовательным выводом всех изменений
def toHeap(arr):
    l = len(arr)
    k = 0
    swaps = []
    for i in range(l,1,-1):
        stop = False
        while not stop:
            stop = True
            j = i
            while (j != 1):
                if (arr[j-1] < arr[j//2 - 1]):
                    stop = False
                    k += 1
                    swaps.append([j//2 - 1, j-1])
                    arr[j-1], arr[j//2 - 1] = arr[j//2 - 1], arr[j-1]
                j = j//2
    return swaps, k
 

n = int(input())
arr = list(map(int, input().split()))
swaps, k = toHeap(arr)
print(k)
for ans in swaps:
    ans = map(str, ans)
    print(" ".join(ans))
print(arr)
