# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

import sys
sys.stdin = open('input.txt', 'r')

n = int(sys.stdin.readline())
stack = []

for i in range(n):
    input_string = sys.stdin.readline().split()
    cmd = input_string[0]
    
    if cmd == 'push':
        num = input_string[1]
        stack.append(num)
    
    elif cmd == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    elif cmd == 'size':
        print(len(stack))

    elif cmd == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    
    elif cmd == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])