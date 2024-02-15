def solution(a, b):
    # a와 b 중 작은 값과 큰 값을 구함
    start, end = min(a,b), max(a,b)
    
    # start부터 end까지의 합을 계산
    total_sum = sum(range(start, end + 1))
    
    return total_sum

# 예제로 함수 호출 및 결과 출력
a = 3
b = 5
result = solution(a, b)
print(f"{a}부터 {b}까지의 합은 {result}입니다.")
