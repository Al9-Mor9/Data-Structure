import sys
#sys.stdin = open('input.txt', 'r')
from heapq import heappush, heappop
n = int(sys.stdin.readline())
heap = []
for i in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        print(heappop(heap)) if heap else print(0)
    else:
        heappush(heap, num)