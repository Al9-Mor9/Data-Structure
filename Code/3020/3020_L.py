import sys
sys.stdin = open("input.txt", "r")

n, h = map(int, input().split())
arr = list(map(int, sys.stdin.readlines()))

a = [arr[i] for i in range(n) if not i%2]
b = [h - arr[i] for i in range(n) if i%2]
g = [0] * h
f = [0] * h 
for i in range(len(a)):
    g[a[i] - 1] += 1
for i in range(len(g)-1, 0, -1):
    g[i - 1] = g[i] + g[i - 1]

for i in range(len(b)):
    f[b[i]] += 1

for i in range(len(f)-1):
    f[i + 1] = f[i] + f[i + 1]

cnt = 0
mini = 200000
for i in range(h):
    tmp = f[i] + g[i]
    if tmp < mini:
        mini = tmp
        cnt = 1
    elif tmp == mini:
        cnt += 1
    
print(mini, cnt)