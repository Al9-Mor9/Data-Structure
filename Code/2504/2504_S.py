def blank(n):
    str_n_list = []
    result = 1
    answer = 0

    for i in n:
        if i == '(':
            str_n_list.append(i)
            result *= 2
            print(result, answer, str_n_list)
        elif i == ')':
            if not str_n_list or str_n_list[-1] == '[':
                return 0
            elif str_n_list[-1] == '(':
                answer += result
            result //= 2
            str_n_list.pop()
            print(result, answer, str_n_list)
        elif i == '[':
            str_n_list.append(i)
            result *= 3
            print(result, answer, str_n_list)

        elif i == ']':
            if not str_n_list or str_n_list[-1] == '(':
                return 0
            elif str_n_list[-1] == '[':
                answer += result
            result //= 3
            str_n_list.pop()
            print(result, answer, str_n_list)
    return answer
        
print(blank('(()[[]])([])')) # 28
# print(blank('()[(([]))]]')) # 

'''
2 0 ['(']
4 0 ['(', '(']
2 4 ['(']
6 4 ['(', '[']
18 4 ['(', '[', '[']
6 22 ['(', '[']
2 28 ['(']
1 30 []
2 30 ['(']
6 30 ['(', '[']
2 36 ['(']
1 38 []
38

2 0 ['(']
4 0 ['(', '(']
2 4 ['(']
6 4 ['(', '[']
18 4 ['(', '[', '[']
18 4 ['(', '[', '[']
6 22 ['(', '[']
6 22 ['(', '[']
2 22 ['(']
1 22 []
2 22 ['(']
6 22 ['(', '[']
6 22 ['(', '[']
2 28 ['(']
1 28 []
28
'''











