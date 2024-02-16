def solution(seoul):
    result = 0
    for index, item in enumerate(seoul):
        if(item == "Kim"):
            result = index
    answer = f'김서방은 {result}에 있다'
    return answer