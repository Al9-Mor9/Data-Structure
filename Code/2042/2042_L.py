import sys
sys.stdin = open("input.txt", "r")
#-------------------------------------
# Segment Tree

# Time-complexity
# construct O(n)
# update    O(log n)
# query     O(log n)

import math
N, m, k = map(int, sys.stdin.readline().rstrip().split())
arr = [int(sys.stdin.readline()) for _ in range(N)]
idx = pow(2, int(math.log2(N)) + 1)

class Node:
    def __init__(self, n):
        self.n = n
        self.v = None

# value를 반환하는 재귀함수, 함수가 호출 될 때 노드 객체가 생성되고, tree 딕셔너리에 저장됨.
def init(n):
    # 구하고 싶은 depth 까지 모든 노드 생성
    if n - idx < N:
        node = Node(n)
        node.v = init(n*2) + init(n*2 + 1) if n < idx else arr[n-idx]        
        tree[n] = node
        return node.v
    else:
        return 0

def query(now, s, e):
    if s == e:
        return int(tree[s].v)
    else:
        l, r = lr[now]
        mid = (s + e)//2
        if l == s and r == e:
            return int(tree[now].v)
        else:
            return query(now*2, s, mid) + query(now*2 + 1, mid + 1, e)
            
def update(n, new):
    n += idx - 1
    chg = tree[n].v - new
    while n != 1:
        tree[n].v -= chg
        n = n//2
    tree[n].v -= chg

#left, right list for query index
lr = {i+ idx : [i + idx, i + idx] for i in range(idx)}
for i in range(idx - 1, 0, -1):
    lr[i] = [lr[i*2][0], lr[i*2 + 1][1]]
#print(lr)

#initialize O(n)
tree = {}
init(1)

for _ in range(m + k):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    if a == 1:
        update(b, c)
    elif a == 2:
        print(query(1, b + idx - 1, c + idx - 1))