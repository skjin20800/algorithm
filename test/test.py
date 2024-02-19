def solution(A,B):
    A.sort(reverse=True)
    B.sort()
        
    value = 0
    for pair1,pair2 in zip(A, B):
        value = value + (pair1*pair2)

    return value