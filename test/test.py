def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i != 0 and answer[-1] == arr[i]:
            continue
            
        answer.append(arr[i])
    
    return answer