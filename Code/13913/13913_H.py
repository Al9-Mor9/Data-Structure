import sys
sys.stdin = open('text.txt', 'r')


def pathfind(now):
    data = []
    tmp = now
    for _ in range(visited[now] + 1):   # 경로 역추적
        data.append(tmp)
        tmp = check[tmp]
    for i in range(len(data)):
        print(data.pop(), end=' ')


n, m = map(int, input().split())
visited = [0] * 100001
check = [0] * 100001
q = [n]
while q:
    num = q.pop(0)
    if num == m:
        ans = visited[num]
        break
    if 0 <= num-1 < len(visited) and not visited[num - 1]:
        q.append(num - 1)
        visited[num - 1] = visited[num] + 1
        check[num - 1] = num
    if 0 <= num+1 < len(visited) and not visited[num + 1] :
        q.append(num + 1)
        visited[num + 1] = visited[num] + 1
        check[num + 1] = num
    if 0 <= num*2 < len(visited) and not visited[num * 2]:
        q.append(num * 2)
        visited[num*2] = visited[num] + 1
        check[num * 2] = num
visited[n] = 0
check[n] = 0
# print(check[:30])
# print(visited[:30])
print(ans)
pathfind(num)