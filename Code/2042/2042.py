# 구간 합 구하기

N, M, K = map(int, (input().split()))
num_list = []

for i in range (N):
    a = int(input('숫자입력'))
    num_list.append(a)
# N개의 숫자를 입력 받아 리스트에 추가

'''
sum_num_list = [0]
for i in range (num_list):
    sum_num_list.append(i+sum_num_list)
# 초기 리스트의 숫자들을 미리 더해준 리스트 생성 
'''

for i in range(M+K):
# 교환과 덧셈을 몇 번 반복할 것인지 입력
    a, b, c = map(int, (input().split()))
    if a == 1:
        num_list[b-1] = c
    elif a == 2:
        answer = sum(num_list[b-1:c])
        print(answer)
        
