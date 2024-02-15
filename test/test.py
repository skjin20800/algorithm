def solution(s):
    value_list = list(map(int, s.split(" ")))
    value_min = min(value_list)
    value_max = max(value_list)
    
    answer = f'{value_min} {value_max}'
    return answer

print(solution("-1 -2 -3 -4"))
