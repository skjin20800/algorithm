from queue import Queue
import copy

answer = []

# Current 클래스 정의
class Character:
    def __init__(self, x, y, count, maps):
        self.x = x
        self.y = y
        self.count = count
        self.maps = maps
        
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_count(self):
        return self.count
    
    def get_maps(self):
        return self.maps

def bfs(max_x, max_y, maps):
    queue = Queue()  # 큐 초기화
    
    init_character = Character(0, 0, 0, maps)
    queue.put(init_character)
    
    # 큐에 항목이 남아있는 동안 루프 실행
    while not queue.empty():
        item = queue.get()
        cur_x = item.get_x()    
        cur_y = item.get_y()
        count = item.get_count()
        maps = item.get_maps()
        
        # 사각형 밖으로 나갔을 때
        if cur_x < 0 or cur_y < 0 or cur_x >= max_x or cur_y >= max_y:
            continue
        # 벽으로 막혀있을 때
        if maps[cur_y][cur_x] == 0:
            continue
        # 이미 최단거리 구했을 때
        if len(answer) > 0 and count >= min(answer):
            continue
        
        # 현재 장소를 벽으로 막고 거리 카운트 +1 
        maps[cur_y][cur_x] = 0
        count = count + 1
        
        # 도착 지점이면 최단거리 저장
        if cur_x == max_x - 1 and cur_y == max_y - 1:
            answer.append(count)       
        
        # 4가지 방향으로 이동
        character1 = Character(cur_x + 1, cur_y, count, maps)
        queue.put(character1)
        
        character2 = Character(cur_x - 1, cur_y, count, maps)
        queue.put(character2)
        
        character3 = Character(cur_x, cur_y + 1, count, maps)
        queue.put(character3)
        
        character4 = Character(cur_x, cur_y - 1, count, maps)
        queue.put(character4)

    
def solution(maps):
    max_x = len(maps[0])
    max_y = len(maps)
    
    bfs(max_x, max_y, maps)
    
    if len(answer) > 0:
        return min(answer)
    return -1
