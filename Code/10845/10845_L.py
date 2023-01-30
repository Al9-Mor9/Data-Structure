import sys
sys.stdin = open("input.txt", "r")
#---------------------------------------------
import sys
n = int(sys.stdin.readline())

queue=[]
for i in range(n):
    order = sys.stdin.readline().split()

    if order[0] =='push':
        queue.append(order[1])

    elif order[0] =='pop': 
        print(queue.pop(0)) if len(queue) != 0 else print(-1)

    elif order[0] == 'size':
        print(len(queue))

    elif order[0] == 'empty':
        print(1) if len(queue) == 0 else print(0)            

    elif order[0] == 'front':
        print(queue[0]) if len(queue) != 0 else print(-1)

    elif order[0] == 'back':
        print(queue[-1]) if len(queue) != 0 else print(-1)
