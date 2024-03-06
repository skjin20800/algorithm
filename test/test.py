def solution(progresses, speeds):
    answer = []
    
    day = 0
    result = []
    for item1, speed in zip(progresses, speeds):
        
        pg_day = day
        item1 = item1 + (pg_day * speed)
        while item1 < 100:
            item1 += speed
            day += 1
        
        result.append(day)
    
    result_dic = {}
    for val in result:
        if val in result_dic:
            result_dic[val] += 1
        else:            
            result_dic[val] = 1
    answer = list(result_dic.values())
    
    
    #for val in result:
        
    
    
    return answer