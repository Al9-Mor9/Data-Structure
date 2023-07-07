import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
# --------------------------------------
# 소수는 541보다 작음.
# 정답은 2^31 보다 작음.
# 

# 2 3 5 7 
# 2 
# 3 

# 2 3 5 7 4 6 10 14
# 

from queue import PriorityQueue


k, n = map(int, input().split()) 
q = PriorityQueue()
arr = list(map(int, input().split()))
for g in arr: q.put(g)

for i in range(n):
    qq = PriorityQueue()
    a = []
    while not q.empty():
        tmp = q.get()
        a.append(tmp)
        qq.put(tmp)
    print("\n",a)
    q = qq
    cur = q.get()
    for j in range(k):
        new = cur * arr[j]
        q.put(new)
        print("cur arr[j] new is ..",cur, arr[j],new)

        if not cur % arr[j]:
            print("stop when", cur, arr[j])
            break

print(cur)




