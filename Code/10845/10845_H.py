import sys
#sys.stdin = open("input.txt", "r")
#---------------------------------------
N = int(sys.stdin.readline())
stack = []
for i in range(N):
    msg = sys.stdin.readline().split() #오,,, 여기서 input 쓰면 시간초과 납니다
    if msg[0] == 'push':
        stack.append(msg[1])
    elif msg[0] == 'pop':
        print(stack.pop(0)) if stack else print(-1)
    elif msg[0] == 'size':
        print(len(stack))
    elif msg[0] == 'empty':
        print(0) if stack else print(1)
    elif msg[0] == 'front':
        print(stack[0]) if stack else print(-1)
    elif msg[0] == 'back':
        print(stack[-1]) if stack else print(-1)