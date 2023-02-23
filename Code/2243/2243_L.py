import sys
import math
sys.stdin = open('input.txt', 'r')

# 숫자가 낮을 수록 맛이 좋은 사탕 -> 맛조사

# 사탕의 순위와 개수를 넣고, 
# 뺄 때는 가지고 있는 사탕 중에서 몇 번째를 뺄껀지를 기준으로 뺌.

# 만약 최고 존엄 사탕 1이 4개, 3이 1개, 5가 2개 라면,
# 1111355 식으로 담긴다.
# 여기서 3번째 사탕은 1 이다. 
# 힙큐로 풀려고 했으나, 특정 순위의 사탕을 탐색하려면, 
# 그만큼 빼줘야 한다. 하지만 20 억개의 사탕. -> 다 못 뺀다.

# 사탕의 수를 value로 가지고 있으며, k번 째 사탕의 순위를 알고 있어야한다.
# -> 세그먼트 트리

# 맛조사 종류 100만개 -> 수정이 동생 사탕 기계임?
# 세그 트리의 높이 h = logn, 2^(h+1) 만큼 노드가 필요하다. 
n = 1000_000
h = int(math.log2(n))
start_node = 2 ** (h + 1) # i 번째는 2 ** (h + 1) + i - 1 번째에 담긴다.
seg_tree = [0] * (2 ** (h + 2) + 1) # 정확한 범위이므로 1을 더해 주자. 

# k 번째 찾아서 출력, 그리고 빼기
def search_pop(k):
    node = 1
    depth = 0
    seg_tree[node] -= 1
    while depth < h + 1:
        left_v = seg_tree[node * 2]
        if k <= left_v:
            node = 2 * node
        else: 
            k -= seg_tree[node * 2] # 왼쪽 노드를 빼줘야 왼쪽 끝 부터의 순서를 기준으로 삼을 수 있다.
            node = 2 * node + 1
        seg_tree[node] -= 1
        depth += 1
    print(node - start_node + 1)

# n번째 사탕 v개 추가해주기, 구간합도 추가해 주자.
def update(n, v):
    cur = start_node + n - 1
    while cur > 0:
        seg_tree[cur] += v
        cur //= 2

#넣을 건지 뺄건지에 따라 나눠줘. 
c = int(sys.stdin.readline())
for i in range(c):
    inputs =  list(map(int, sys.stdin.readline().split()))
    if inputs[0] == 1:
        search_pop(inputs[1])
    else:
        update(inputs[1], inputs[2])

# print(1)
# for i in range(h + 2):
#     dis = '-' * i
#     print(2**i, dis, 2**(i+1) - 1)
# seg_tree = [0] * (1000000 * 4)