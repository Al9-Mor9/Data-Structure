# 아직 못 품 한 시간으론 택도 없네
import sys
import math
sys.stdin = open('input.txt', 'r')

n = int(sys.stdin.readline().strip())
h = int(math.log2(n))
start_node = 2 ** (h + 1)
visit = []
seg_tree = [0] * (start_node * 2)

# init
for i in range(n):
    x, y = map(int, sys.stdin.readline().strip().split())
    visit.append((x, y))
    seg_tree[start_node + i] = y

print(seg_tree)

for i in range(start_node - 1, 0, -1):
    seg_tree[i] = max(seg_tree[i * 2], seg_tree[i * 2 + 1])
print(seg_tree)
print(visit)
m = int(sys.stdin.readline().strip())

def binary_search(v, f):
    l = 0
    r = n
    while l <= r:
        mid = (l + r)//2
        if visit[mid][0] == v:
            return mid, 1
        elif visit[mid][0] < v:
            l = mid + 1
        else:
            r = mid - 1

    if f == "l":
        return l
    else:
        return r
x = 2006
print(binary_search(x, "l") - 1)
print(binary_search(x, "r") + 1)

def query(x, y):
    x_idx, x_t = binary_search(x)
    y_idx, y_t = binary_search(y)

    