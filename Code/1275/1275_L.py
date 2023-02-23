import sys
import math
sys.stdin = open('input.txt', 'r')

n, q = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

# get segtree
h = int(math.log2(n))
start_node = 2 ** (h + 1)
arr = arr + [0] * (2 ** (h + 1) - n)
print(arr)

seg_tree = [0] * (start_node) + arr 
l_idx = [start_node] * (2 * start_node)
r_idx = [0] * (2 * start_node)

# initialize segment tree
for i in range(1, start_node + 1):
    cur = start_node + i - 1
    l_idx[cur] = i
    r_idx[cur] = i
    cur //= 2
    while cur > 0:
        seg_tree[cur] += arr[i-1]
        if l_idx[cur] > i:
            l_idx[cur] = i
        if r_idx[cur] < i:
            r_idx[cur] = i
        cur //= 2

# print(seg_tree)
# print(l_idx)
# print(r_idx)

def search(cur, l, r):
    if l > r: return 0
    if l_idx[cur] == l and r_idx[cur] == r: return seg_tree[cur]
    elif l_idx[cur] <= l and r_idx[cur] >= r:
        mid = (l_idx[cur] + r_idx[cur])//2
        if l <= mid <= r:
            return search(cur * 2, l, mid) + search(cur * 2 + 1, mid + 1, r) 
        elif mid > r:
            return search(cur * 2, l, r)
        elif mid <= l:
            return search(cur * 2 + 1, l, r)
    else:
         return 0
#print(search(1, 1, 4))

def update(n, v):
    cur = n + start_node - 1 
    dis = seg_tree[cur] - v
    while cur > 0:
        seg_tree[cur] -= dis
        cur//=2

#print(seg_tree)

for i in range(q):
    l, r, n, v =  map(int, sys.stdin.readline().split())
    if r < l: r, l = l, r
    print(search(1, l, r))
    update(n, v)