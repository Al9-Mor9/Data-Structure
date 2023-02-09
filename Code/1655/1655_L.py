import sys
sys.stdin = open("input.txt", "r")
import heapq
n = int(sys.stdin.readline())
l, r = [], []
# 일단 넣고, 좌 상단과 우 하단을 비교해서 바꿔주자. 출력은 항상 좌 상단
for _ in range(n):
    tmp = int(sys.stdin.readline())
    if (len(l) == len(r)):
        heapq.heappush(l, -tmp)
    else:
        heapq.heappush(r, tmp)
    
    if r and -l[0] > r[0]:
        l_large = heapq.heappop(l)
        heapq.heappush(r, -l_large)
        r_small = heapq.heappop(r)
        heapq.heappush(l, -r_small)
    print(-l[0])

