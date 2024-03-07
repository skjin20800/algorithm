def solution(cacheSize, cities):
    
    # 캐시 없을때
    if cacheSize == 0:
        return len(cities)*5
    
    # 캐시 있을때
    answer = 0
    cashe = [""]*cacheSize
    
    for city in cities:
        # cashe배열에 도시있나 체크
        city = city.lower()
        if city in cashe:
            # 캐시에서 가져오기 + 캐시 업데이트
            cashe.remove(city)
            cashe.insert(0,city)
            answer += 1
        
        else:
            # 캐시에 등록 + 시간 카운트
            cashe.pop()
            cashe.insert(0,city)
            answer += 5
        
            
    return answer