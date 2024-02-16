def solution(nums):
    set_item = set(nums)
    value = int(len(set_item))
    limit = len(nums)/2
    
    if value< limit:
        return value
    
    return limit
    