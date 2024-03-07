result = []
count = 0


def find_block(y,x,name,board,height,width,Message,y_symbol,x_symbol):
    # 우하측 심볼 y: +, x: +
    # 우상측 심볼 y: -, x: +
    # 좌하측 심볼 y: +, x: -
    # 좌상측 심볼 y: -, x: -
    try:
        if x+x_symbol < width and y+y_symbol < height and x+x_symbol >= 0 and y+y_symbol >= 0 :                 
            if board[y][x+x_symbol] == name and board[y+y_symbol][x] == name and board[y+y_symbol][x+x_symbol] == name:               
                result.append((y,x))
                return True
        return False
    except Exception as e:
        print(e,Message)
    

def calculator(height, width, board):
    # 특정 문자의 상, 하, 좌, 우 탐색후 4개면 좌표 기억하는 배열에 삽입
    
    for y, blocks in enumerate(board):
        for x, block in enumerate(blocks):
            # 같은 놈이면 찾는 연산 하기
            if block == "X":continue
            if find_block(y,x,block,board,height,width,"우하측",1,1): continue
            if find_block(y,x,block,board,height,width,"우상측",-1,1): continue
            if find_block(y,x,block,board,height,width,"좌하측",1,-1): continue
            if find_block(y,x,block,board,height,width,"좌상측",-1,-1): continue
    
    if len(result) <=0:
        return board, False
    return board, True


def sort_board(board,height):
    # 블럭 뒤집기
    board = reverse_2d_array(board)
    for y, blocks in enumerate(board):
        for x, block in enumerate(blocks):
            # X인 블럭 찾아서 위쪽 블럭과 변경
            if block == "X":
                current_y = 1
                while y+current_y < height:
                    next_y = y+current_y
                    if board[next_y][x] != "X":
                        upper_block = board[next_y][x]
                        
                        # 현재 블럭을 한층 위 블럭으로 변경 
                        temp = list(board[y])
                        temp[x] = upper_block
                        board[y] = "".join(temp)
                        
                        # 위 블럭을 X로 변경                        
                        upper_temp = list(board[next_y])
                        upper_temp[x] = "X"
                        board[next_y] = "".join(upper_temp)
                        break
                    else:
                        current_y += 1
    
    # 보드 원래 배열대로 변경
    board = reverse_2d_array(board)
  
    return board
    
    
def remove_block(board, result, height):
    
    # 모든 검사가 끝나고 좌표 기억 배열에 속한 값들은 모두 X로 변경 및 개수 찾기
    global count
    for block in result:
        y = block[0]
        x = block[1]
        temp = list(board[y])
        re = temp[x]
        temp[x] = "X"
        board[y] = "".join(temp)
        count +=1
    
    result.clear()
    return board
    
def reverse_2d_array(arr):
    # 각 행을 뒤집음
    for y, row in enumerate(arr):
        temp = list(row)
        temp.reverse()
        arr[y]= "".join(temp)    
    # 전체 배열을 뒤집음
    arr.reverse()
    
    return arr
    
def solution(m, n, board):
    """
        m: 배열 수 = height
        n: 문자열 수 = width
        borad: 배열
    """ 
    i = 0
    while True:
        # 특정 문자의 상, 하, 좌, 우 탐색후 4개면 좌표 기억하는 배열에 삽입
        board,is_process =calculator(m,n,board)
        if is_process == False:
            break
        # 모든 검사가 끝나고 좌표 기억 배열에 속한 값들은 모두 O로 변경 및 개수 찾기
        board = remove_block(board,result,m)
        # 전체 배열중 O로 변환된 놈들은 지우고 그 위에있는 값들로 대체
        board = sort_board(board,m)
    
    answer = count

    return answer