import sys
sys.stdin = open("input.txt", "r")
#------------------------------------------
import sys
s = sys.stdin.readline()

ans, tmp = 0, 1
stack = []

for i in range(len(s)):
    b = s[i]
    if b == '(':
        tmp *= 2
        stack.append(b)

    elif b == '[':
        tmp *= 3
        stack.append(b)

    elif b == ')':
        if not stack or stack[-1] == '[':
            ans = 0
            break
        else:
            if s[i-1] == '(':
                ans += tmp
            tmp //= 2
            stack.pop()
    else:
        if not stack or stack[-1] == '(':
            ans = 0
            break
        else:
            if s[i-1] == '[':
                ans += tmp
            tmp //= 3
            stack.pop()

print(ans) if not stack else print(0)