def dfs(root_index, computer_index, computers, visited):
    if visited[computer_index]:  # 이미 방문한 컴퓨터인 경우 종료
        return 0  # 네트워크 개수 증가 없음
    visited[computer_index] = True  # 현재 컴퓨터를 방문으로 표시
        
    network_list = computers[computer_index]
    count = 0  # 네트워크 개수를 세는 변수
    for index, value in enumerate(network_list):
        if value == 1:  # 연결된 컴퓨터가 있는 경우 재귀적으로 탐색
            count += dfs(root_index, index, computers, visited)
    
    if root_index == computer_index:  # 시작 컴퓨터와 현재 컴퓨터가 같은 경우
        return count + 1  # 네트워크 개수를 1 증가시킴
    else:
        return count  # 네트워크 개수 증가 없음

def solution(n, computers):
    answer = 0
    visited = [False] * n  # 방문 여부를 저장하는 리스트
    
    for index in range(n):
        answer += dfs(index, index, computers, visited)  # 각 컴퓨터를 시작점으로 DFS 탐색
    
    return answer
