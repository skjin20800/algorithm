import heapq

def pop(scoville, K, count):
    if  scoville[0] < K and len(scoville) > 1:
        one = heapq.heappop(scoville)
        two = heapq.heappop(scoville)
        three = one + (two *2)
        heapq.heappush(scoville, three)
        count += 1    
        count = pop(scoville, K, count)
    elif len(scoville) == 1 and scoville[0] < K:
        return -1
    elif len(scoville) == 1 and scoville[0] > K:
        return count
    else :
        return count
    return count
    

def solution(scoville, K):
    heapq.heapify(scoville)
    if scoville[0] > K:
        return -1
    
    count = 0
    result = 0
    while True:
        if  scoville[0] < K and len(scoville) > 1:            
            one = heapq.heappop(scoville)
            two = heapq.heappop(scoville)
            three = one + (two *2)
            heapq.heappush(scoville, three)
            count += 1    
        elif len(scoville) == 1 and scoville[0] < K:
            result = -1
            break
        elif len(scoville) == 1 and scoville[0] > K:
            result = count
            break
        else :
            result = count
            break

    return result
