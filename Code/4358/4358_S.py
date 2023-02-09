import sys

cnt_trees = 0                                       # 모든 나무의 수 저장
trees_dict = {}                                     # 입력값들을 저장할 딕셔너리
while True:
    trees_word = sys.stdin.readline().rstrip()      # 입력값을 한 줄씩 가져옴
    if trees_word == '':
        break
    cnt_trees += 1                                  # 반복문이 돌면서 나무의 개수 계속 1씩 추가
    if trees_word in trees_dict:                    
        trees_dict[trees_word] += 1
    elif trees_word not in trees_dict:
        trees_dict[trees_word] = 1
    

sorted_trees_dict = dict(sorted(trees_dict.items())) # trees_dict를 key 값을 기준으로 정렬해서 새로운 딕셔너리 생성
                                                     
for i in sorted_trees_dict:                          # key 값으로 정렬된 딕셔너리를 돌면서
    tree_num = sorted_trees_dict[i]                  # 해당 나무의 개수를 가져오고
    percentage = (tree_num/cnt_trees)*100            # 그 값을 통해 비율을 구해준다
    percentage_round = round(percentage,4)           # 소수점 4째 자리까지 표시
    print(f'{i} {percentage_round}')
