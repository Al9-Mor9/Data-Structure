# ‘()’ 인 괄호열의 값은 2이다.
# ‘[]’ 인 괄호열의 값은 3이다.
# ‘(X)’ 의 괄호값은 2×값(X) 으로 계산된다.
# ‘[X]’ 의 괄호값은 3×값(X) 으로 계산된다.
# 올바른 괄호열 X와 Y가 결합된 XY의 괄호값은 값(XY)= 값(X)+값(Y) 로 계산된다.


# ( ), [ ] - pop, 연속으로 pop되면 계속 곱하고 pop 끊기면 곱한 값 더하는 곳에 넣음
# ( (, ( [, [ [, [ (
# ( ], [ ) - 안 됨
import sys

sys.stdin = open('input.txt', 'r')
parentheis = list(input())

stack = []
mul = 1
ans = 0

for i, p in enumerate(parentheis):
    if p == '(':
        stack.append(p) # stack에 쌓기
        mul *= 2 # ( 시작할 때 2곱하기
    elif p == '[':
        stack.append(p) # stack에 쌓기
        mul *= 3 # [ 시작할 때 3곱하기
    elif p == ')':
        if stack == [] or stack[-1] == '[': # )를 넣을 때 스택이 비어있거나 스택 맨 위가 [일 떄
            ans = 0
            break
        elif parentheis[i-1] == '(': # 가장 안쪽이 ()일 때
            ans += mul # 여태까지 계산한 값을 답에 더해줌
        stack.pop() # ()이든 (())이든 pop
        mul //= 2 # 빠져나올 때마다 괄호 풀었을 때의 값으로 복귀, 열린 괄호가 남아있으면 1이 안 됨

    else: # ']'
        if stack == [] or stack[-1] == '(': # ]를 넣을 때 스택이 비어있거나 스택 맨 위가 (일 떄
            ans = 0
            break
        elif parentheis[i-1] == '[': # 가장 안쪽이 []일 때
            ans += mul # 여태까지 계산한 값을 답에 더해줌
        stack.pop() # []이든 [[]]이든 pop
        mul //= 3 # 빠져나올 때마다 괄호 풀었을 때의 값으로 복귀, 열린 괄호가 남아있으면 1이 안 됨

print(ans)