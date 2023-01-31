# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

import sys
sys.stdin = open('input.txt', 'r')

n = int(sys.stdin.readline())
queue = []

for i in range(n):
    input_string = sys.stdin.readline().split()
    cmd = input_string[0]
    
    if cmd == 'push':
        num = input_string[1]
        queue.append(num)
    
    elif cmd == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))

    elif cmd == 'size':
        print(len(queue))

    elif cmd == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    
    elif cmd == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])

    elif cmd == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])