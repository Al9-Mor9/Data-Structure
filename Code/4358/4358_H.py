'''
trees = {}
total_num = 0
while True:
    try:
        tree = input()
        if tree not in trees:
            trees[tree] = 1
        else:
            trees[tree] += 1
        total_num += 1
    except EOFError:
        break
'''
import sys
sys.stdin = open('input.txt','r')
#------------------------#
import sys
# sys.stdin.readline은 EOFError를 발생시키지 않고, 입력의 끝에 도달하면 빈 문자열을 반환
input = sys.stdin.readline
trees = {}
total_num = 0

while True:
    try:
        tree = input()
        if not len(tree):
            break
        tree = tree.strip('\n')
        if tree not in trees:
            trees[tree] = 1
        else:
            trees[tree] += 1
        total_num += 1
    except EOFError:
        break

trees = sorted(trees.items())
for name, num in trees:
    persentage = round(num/total_num * 100, 4)
    # 정수도 소수점 넷째자리까지 표현, 이거때문에 3시간 날림
    print(f'{name} {persentage:.4f}')