from queue import Queue


queue = Queue()

class Tansform:
    def __init__(self, count,word, words):    
        self.count = count
        self.word = word
        self.words = words
    def get_item(self):
        return self
    

def bfs(begin, target,words):
    
    init_transform = Tansform(0, begin, words)
    queue.put(init_transform)   
    
    value = 0
    
    while not queue.empty():        
        item = queue.get()
        cur_word = item.word
        words = item.words
        cur_count = item.count
   
        # 타겟 검사
        if cur_word == target:
            value = cur_count
            
            break

        for word in words:            
            duplicate = 0
            for index, char in enumerate(word):
            
                # 2개 이상 다른 단어
                if duplicate == 2:
                    break
            
                # 문자 다른 단어 검사
                if char != cur_word[index]:
                    duplicate += 1
            
                if index == len(word)-1 and duplicate == 1:
                    # 큐에 넣기
                    transform = Tansform(cur_count+1, word, words)
                    queue.put(transform)
                    words.remove(word)
                     
    
    return value
        
    
    
def solution(begin, target, words):       
    return bfs(begin, target, words)