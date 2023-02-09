import sys
sys.stdin = open("input.txt", "r")
arr = list(map(int, sys.stdin.readlines()))
sys.setrecursionlimit(10**4)

def postorder(l, r):
    if l > r:
        return
    mid = l + 1                         
    for i in range(l+1, r+1):
        if arr[l] < arr[i]:
            mid = i
            break
    postorder(l+1, mid-1)               
    postorder(mid, r)
    
    print(arr[l])

postorder(0, len(arr) -1)

# class Node:
#     def __init__(self, node):
#         self.node = node
#         self.left = None
#         self.right = None

# def add(n):
#     tree[n] = Node(n)
#     cur = tree[arr[0]]
#     while True:
#         if cur.node > n:
#             if cur.left != None:
#                 cur = tree[cur.left]
#             else:
#                 cur.left = n
#                 break
#         else:
#             if cur.right:
#                 cur = tree[cur.right]
#             else:
#                 cur.right = n
#                 break
# def dfs(n):
#     node = tree[n]
#     if node.left:
#         dfs(node.left)
#     if node.right:
#         dfs(node.right)
#     print(n)


# tree = {}
# tree[arr[0]] = Node(arr[0])
# for i in arr[1:]:
#     add(i)

# dfs(arr[0])
    


