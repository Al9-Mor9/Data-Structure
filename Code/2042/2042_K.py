import sys
from collections import defaultdict
# sys.stdin = open('input.txt', 'r')

n, m, k = map(int,sys.stdin.readline().split())

nums = [0]
for i in range(n):
    nums.append(int(input())) # # 변동사항 계산할 때 필요 [0, 1, 2, 3, 4, 5]
partial_sum = [0] * (n + 1) # 인덱스까지의 부분합 [0, 0, 0, 0, 0, 0]
diff = defaultdict(int) # 해당 인덱스에서 변동된 양

for i in range(1, n + 1): # [0, 1, 3, 6, 10, 15]
    partial_sum[i] = partial_sum[i-1] + nums[i]

for j in range(m + k):
    a, b, c = map(int,input().split())
    if a == 1:
        diff[b] = c - nums[b] # dictionary에 b index에서의 변동량 적기 # {3: 3} /  {3: 3, 5: -3}
    else:
        diff_b, diff_c = 0 , 0
        for k in diff.keys():
            if k <= b-1: 
                diff_b += diff[k]
            if k <= c: 
                diff_c += diff[k]
        print(partial_sum[c] + diff_c - partial_sum[b-1] - diff_b)

#-------------------------------------------------------------------------------------------------------------
# Dictionary를 통해 탐색 시간을 줄이고 list slicing으로 sum 시간을 줄이고자 함(시간초과로 실패)
# for idx in range(n):
#     num_dict[idx + 1] = int(input())

# for i in range(m + k):
#     a, b, c = map(int, input().split())
#     if a == 1:
#         num_dict[b] = c
#     else: # a == 2
#         num_list = list(num_dict.values())
#         print(sum(num_list[b-1:c+1]))
