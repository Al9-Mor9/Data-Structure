import sys
sys.stdin = open("input.txt", "r")
#------------------------------------
import sys
n = int(sys.stdin.readline())

class Node():
    def __init__(self, item, left, right):
        self.item = item
        self.left = left
        self.right = right
tree = {}
for _ in range(n):
    item, left, right = sys.stdin.readline().split()
    tree[item] = Node(item, left, right)


def preorder(node):
    if node == '.':
        return ''
    
    l = str(tree[node].left)
    r = str(tree[node].right)
    
    return node + preorder(l) + preorder(r)


def inorder(node):
    if node == '.':
        return ''
    
    l = str(tree[node].left)
    r = str(tree[node].right)
    
    return inorder(l) + node + inorder(r)

def postorder(node):
    if node == '.':
        return ''
    
    l = str(tree[node].left)
    r = str(tree[node].right)
    
    return postorder(l) + postorder(r) + node


print(preorder('A'))
print(inorder('A'))
print(postorder('A'))
