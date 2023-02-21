import sys
sys.stdin = open('input.txt', 'r')
#####
import heapq
n, k = map(int, input().split())
item = []
for _ in range(n):
    item.append(list(map(int, input().split())) + [0])
item = sorted(item, key = lambda X:(-X[1], X[0]))
bag = [int(input()) for _ in range(k)]
bag.sort()

result = 0
heap = []
item.sort(key=lambda x:(x[0], -x[1]))

for i in range(k):
    while item and bag[i] >= item[0][0]:
        heapq.heappush(heap, -item[0][1])
        heapq.heappop(item)
        print(heap)
    if heap:
        result += heapq.heappop(heap)
    if not heap and not item:
        break

print(-result)