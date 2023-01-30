import sys
sys.stdin = open("input.txt", "r")
#---------------------------------------------
import sys
n = int(sys.stdin.readline())

stack=[]
for i in range(n):
    order = sys.stdin.readline().split()

    if order[0] =='push':
        stack.append(order[1])

    elif order[0] =='pop': 
        print(stack.pop()) if len(stack) != 0 else print(-1)

    elif order[0] == 'size':
        print(len(stack))

    elif order[0] == 'empty':
        print(1) if len(stack) == 0 else print(0)            

    elif order[0] == 'top':
        print(stack[-1]) if len(stack) != 0 else print(-1)
            