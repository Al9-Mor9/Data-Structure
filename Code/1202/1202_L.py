import sys
import heapq
sys.stdin = open('input.txt', 'r')

n, k = map(int, sys.stdin.readline().split())
jewel = []
for _ in range(n):
    heapq.heappush(jewel, list(map(int, sys.stdin.readline().split())))
bag = list(map(lambda x: int(x.replace("\n", "")),list(sys.stdin.readlines())))
bag.sort()
ans = 0

#각 가방에 가능한 가치가 큰 보석을 담는다.
tmp = []
for b in bag:
    while jewel and b >= jewel[0][0]:
        heapq.heappush(tmp, - heapq.heappop(jewel)[1])
    if tmp:
        ans += -heapq.heappop(tmp)
    if not jewel and not tmp: break
print(ans)