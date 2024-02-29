result_list = []
def dfs(current_number,numbers, target):
    
    if len(numbers) >= 1 :
        plus_number = current_number + numbers[0]
        minus_number = current_number - numbers[0]
        dfs(plus_number,numbers[1:],target) 
        dfs(minus_number,numbers[1:],target) 
    else :
        if current_number == target:
            result_list.append(current_number)
            
def solution(numbers, target):
    numbers.insert(0, 0)
    dfs(numbers[0],numbers[1:],target)      
    
    return len(result_list)