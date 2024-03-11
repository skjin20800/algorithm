def solution(s):
    temp_count = 0    
    for item in s:
        if item == "(":
            temp_count += 1
        else:
            if temp_count <= 0:
                return False
            temp_count -= 1

    if temp_count != 0:
        return False
    return True