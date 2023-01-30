# import sys
# sys.stdin = open("input.txt", "r")

stack = []

lst = list((input().strip()))
ans = 0
num = 1     # num에 계산을 누적해갈거임
# () : 2, [] : 3
# 괄호안에 괄호 존재하면 값을 곱해갑
for i in range(len(lst)):
    if lst[i] == '(':
        stack.append('(')
        num *= 2
    elif lst[i] == '[':
        stack.append('[')
        num *= 3

    # 닫았을 때
    elif lst[i] == ')':
        # 스택에 남은게 없거나 바로전에 [ 있으면 [)이니까 0 출력
        if not stack or stack[-1] == '[':
            ans = 0
            break
        # 바로전에 열었었으면 11줄 반복문안에서 이미 계산 했으므로 지금까지 계산값 더하고
        elif lst[i-1] == '(':
            ans += num
        #다시 2로 나눠줌
        num //= 2
        stack.pop()

    elif lst[i] == ']':
        # (]이면 안되니까 ans = 0
        if not stack or stack[-1] == '(':
            ans = 0
            break
        # 바로전에 열었었으면 마찬가지로 11번줄에서 곱했었으니 지금까지 계산값 더하고
        elif lst[i-1] == '[':
            ans += num
        # 다시 3으로 나눠줌
        num //= 3
        stack.pop()

# print(ans)        이거 왜 안되는지 모르겠음
if stack:
    print(0)
else:
    print(ans)
