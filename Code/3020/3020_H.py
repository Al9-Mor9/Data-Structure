import sys
sys.stdin = open('text.txt', 'r')
#--------------------------#
# 누적합 사용
import sys
input = sys.stdin.readline
n, h = map(int, input().split())    # 길이, 높이
up, down = [0] * (h + 1), [0] * (h + 1) # 종유석, 석순
# up, down : (index)길이 갯수
for i in range(n):
    if i % 2 == 0:
        up[int(input())] += 1
    else:
        down[int(input())] += 1
# print(up, down)   # [0, 1, 0, 1, 0, 1, 0, 0] [0, 1, 0, 1, 0, 1, 0, 0]
for i in range(h - 1, 0, -1):
    down[i] += down[i + 1]
    up[i] += up[i + 1]
# 역순으로 누적합 적용
print(up, down)   # [0, 3, 2, 2, 1, 1, 0, 0] [0, 3, 2, 2, 1, 1, 0, 0]

up.reverse() # up은 위에 붙어있으므로 역순으로 바꿔줘야함
print(up, down)   # [0, 0, 1, 1, 2, 2, 3, 0] [0, 3, 2, 2, 1, 1, 0, 0]
minCnt = 0
breakFree = n   # 부수는 갯수
'''
  0  1  2  3  4  5  6  7        # 8개
 -8 -7 -6 -5 -4 -3 -2 -1        # -8 + 1
  7  6  5  4  3  2  1  0
'''
for i in range(1, h + 1):
    print(up[i-1], down[i])
    breakCnt = up[i - 1] + down[i]  # i번째 줄에서 진행 시 부수는 갯수
    if breakFree > breakCnt:    # 크기 비교
        breakFree = breakCnt    # 작은 수 입력
        minCnt = 1              # 갯수 초기화
    elif breakFree == breakCnt:
        minCnt += 1

print(breakFree, minCnt)
