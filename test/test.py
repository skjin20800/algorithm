def right(x,ary):
    
    try:
        if x == 4:
            return True
        elif ary[x+1] == "X"  :
            return True
        elif ary[x+1] == "P":
            return False
        elif x == 3:
            return True
        elif ary[x+2] == "X":
            return True
        elif ary[x+2] == "P":
            return False
        return True
    except Exception as e:
        print(e)
        return True
        

def bottom(x,y,place):
    
    try:
     #   print(place,y,x)

        if y == 4:
            return True
        elif place[y+1][x] == "X":
            return True
        elif place[y+1][x] == "P":
            return False
        if y == 3:
            return True
        elif place[y+2][x] == "X":
            return True
        elif place[y+2][x] == "P":
            return False
        return True
    except Exception as e:
        print(e)
        return True
        
def bottom_right(x,y,place):
    try:    
        #우 하단 
        if place[y][x+1] == "O" and place[y+1][x+1] == "P":
            if x == 4:
                return True
            return False
        
        if place[y+1][x] == "O" and place[y+1][x+1] == "P":
            if x == 4:
                return True
            return False
        return True
    except Exception as e:
        print(e)
        return True
def bottom_left(x,y,place):
    try:    
        # 좌 하단 
        if place[y][x-1] == "O" and place[y+1][x-1] == "P":
            if x  == 0:
                return True
            return False
        
        if place[y+1][x] == "O" and place[y+1][x-1] == "P":
            if x  == 0:
                return True
            return False
        

        return True
    except Exception as e:
        print(e)
        return True
        
    
    
    

def default(place):
    is_right = True
    is_bottom = True
    is_bottom_right = True
    is_bottom_left = True
    for y, ary in enumerate(place):
        for x, P in enumerate(ary):
            if P == "P":
                print("우",right(x,ary))
                is_right = right(x,ary)
                print("바",bottom(x,y,place))
                is_bottom = bottom(x,y,place)
                print("대우",bottom_right(x,y,place))
                is_bottom_right = bottom_right(x,y,place)
                print("대좌",bottom_left(x,y,place))
                is_bottom_left = bottom_left(x,y,place)
                
                print(bottom_right(x,y,place), place, x, y)
            if is_right == False or is_bottom == False or is_bottom_right == False or is_bottom_left == False: 
                return 0
    return 1
        
    

def solution(places):
    answer = []
    for place in places:
        answer.append(default(place))
        
    return answer