def solution(citations):
    answer = 0
    
    result = []
    
    for i in range(1000):
        
        value = 0
        for item in citations:
            if i < item :
                value += 1
        result.append(value)
            
        
    for i, item in enumerate(result):
        print(f" i {i+1} item :{item}" )
        if (i+1) <= item:
            answer = i+1
            print(answer)
        else:
            break
            

        
    return answer