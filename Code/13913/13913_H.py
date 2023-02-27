import sys
sys.stdin = open('text.txt', 'r')


def pathfind(now):
    data = []
    tmp = now
    for _ in range(visited[now] + 1):   # 경로 역추적
        data.append(tmp)    # 새로운 리스트 만들어서 append
        tmp = check[tmp]
    for i in range(len(data)):
        print(data.pop(), end=' ')  # 걍 pop 반복,,


n, m = map(int, input().split())
# 최댓값 저장
visited = [0] * 100001  # 방문 확인 & 걸리는 시간 저장
check = [0] * 100001    # 출처 번호 기록용

# bfs
q = [n]
while q:
    num = q.pop(0)
    if num == m:    # 탈출조건
        ans = visited[num]
        break
    # n-1, n+1, n*2 append
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

# visited에 0으로 고정을 못함 그래서 루프 나와서 0으로 고정
visited[n] = 0
check[n] = 0
print(ans)
# 경로 추적 레쓰고
pathfind(num)