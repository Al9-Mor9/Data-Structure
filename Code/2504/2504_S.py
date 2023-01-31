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
        
# print(blank('(()[[]])([])')) # 28
# print(blank('()[(([]))]]')) # 
