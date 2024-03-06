import copy

def solution(tickets):
    answer = []
    ticket_dic = {}
    result_dict = []
    
    for ticket in tickets:
        if ticket[0] in ticket_dic:
            ticket_dic[ticket[0]].append(ticket[1])
            ticket_dic[ticket[0]].sort()
        else:
            ticket_dic[ticket[0]] = [ticket[1]]

    max_count = len(tickets) +1
    
    
    def dfs(start,ticket_dic, result):
        try:
            if start not in ticket_dic:
                result_dict.append(result)
              #  print("끝2")
                return
            
            if len(ticket_dic[start]) == 0:
                result_dict.append(result)
              #  print("끝")
                return
            
            for ticket in ticket_dic[start]:                
                dfs_result = copy.deepcopy(result)
                dfs_dic = copy.deepcopy(ticket_dic)
                # start : 시작
                # ticket_dic[start] : 목적지 리스트
                # ticket : 도착지
                
                # 현재 시작은 동일
                # 도착지에따라 DFS 가동 
                
                
                # 도착지 저장                
                dfs_result.append(ticket)
               
                # 도착지 삭제                 
                dfs_dic[start].remove(ticket)
                
                # 출발 
                dfs(ticket,dfs_dic,dfs_result)
            
            
        except Exception as e:
          #  print("에러발생")
            print(e)

    #esult.append(tickets[0][0])
    #result.append(tickets[0][0])

    

    dfs_result = []
    dfs_result.append("ICN")
    dfs("ICN", ticket_dic,dfs_result)
        
    for item in result_dict:
        if len(item) == max_count:
            return item
        