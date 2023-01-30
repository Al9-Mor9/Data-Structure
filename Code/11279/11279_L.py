import sys
sys.stdin = open("input.txt", "r")
#----------------------------------
import sys
from heapq import heappush, heappop
n = int(sys.stdin.readline())

heap = []
for _ in range(n):
    order = -int(sys.stdin.readline())
    if order != 0 :
            heappush(heap, order)
    else:
        print(-heappop(heap)) if heap else print(0)