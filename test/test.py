def solution(numbers):
    answer = 45
    for item in numbers:
        answer = answer - item    
    return answer