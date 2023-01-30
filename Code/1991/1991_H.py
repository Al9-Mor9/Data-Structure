# import sys
#
# sys.stdin = open("input.txt", "r")

N = int(input())
arr = [list(map(str, input().split())) for _ in range(N)]


class Node(object):  # 노드 클래스 선언, 머리, 왼쪽, 오른쪽 인스턴스 변수 선언(이거 맞나?)
    def __init__(self, item):
        self.item = item
        self.left = self.right = None


class BinaryTree(object):  # 이진트리 해서 인스턴스 변수 가장 헤드만 선언
    def __init__(self):
        self.root = None

    def preorder(self):  # 전위 순회 - 자식 노드를 확인하기 전에 서브 트리의 루트를 먼저 확인한 후에 자식 노드를 확인하는 순회 방법
        def _preorder(node):  # 함수 선언 - root 받은 node 변수가 argument
            print(node.item, end='')
            if node.left:
                _preorder(node.left)  # 재귀 있음
            if node.right:
                _preorder(node.right)  # 여기도
            # 그럼 둘 다 없다면 끝나겠죵?

        _preorder(self.root)  # 함수 실행

    def inorder(self):  # 중위 순회 - 왼쪽 자식 노드, 루트 노드, 오른쪽 자식 노드 순으로 값을 확인하는 방식
        def _inorder(node):  # 함수 선언 똑같이 root 받은 node 변수가 argument
            if node.left:
                _inorder(node.left)  # 왼쪽 젤 끝으로 계속 이동하고(재귀)
            print(node.item, end='')  # 왼쪽 끝에 뭐가 더 없으면 출력
            if node.right:  # 오른쪽으로 감(재귀)
                _inorder(node.right)

        _inorder(self.root)

    def postorder(self):  # 후위 순회 - 자식 노드를 모두 확인 후 루트 노드를 확인하는 순회법
        def _postorder(node):  # 함수 선언
            if node.left:
                _postorder(node.left)  # 재귀 있슴
            if node.right:
                _postorder(node.right)
            print(node.item, end='')

        _postorder(self.root)


node = []
BT = BinaryTree()
for i in range(N):  # 먼저 N 수만큼 노드 클래스의 인스턴스들 생성, 리스트 타입으로 모아둠
    node.append(Node(arr[i][0]))
    if arr[i][1] != '.':
        node[i].left = arr[i][1]    # 일단 루트 값을 저장해둠
    if arr[i][2] != '.':
        node[i].right = arr[i][2]
BT.root = node[0]   # 루트 설정 해두고
for i in range(N):  # 이중 반복문 사용해서 node[i] 왼쪽 값(루트임 지금은)이 특정 노드의 루트와 같아 질 때
    for j in range(N):  # 왼쪽 값이 아닌 노드를 집어넣음
        if node[i].left == node[j].item:
            node[i].left = node[j]
        elif node[i].right == node[j].item: # 오른쪽도 마찬가지
            node[i].right = node[j]

BT.preorder()
print()
BT.inorder()
print()
BT.postorder()
