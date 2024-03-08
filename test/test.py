def sum_sharp(arr,sharp_arr,n):
    for y in range(n):
        for x in range(n):        
            if len(sharp_arr) > 0 and y == sharp_arr[0][0] and x == sharp_arr[0][1]:
                sharp_arr.pop(0)                
                temp = list(arr[y])
                temp[x] = "#"
                arr[y] = "".join(temp)
    return arr

def check_sharp(arr,n):
    sharp_arr = []
    for y in range(n):
        for x in range(n):
            if arr[y][x] == "#":
                sharp_arr.append([y,x])
    return sharp_arr
    

def int_ary_to_binary_ary(arr,n):
    result = []
    for num in arr:
        temp = format(num,"b")
        temp2 = list(temp)
        for x, num in enumerate(temp2):
            if num == "1":
                temp2[x] = "#"
            else:
                temp2[x] = " "
        temp2 = "".join(temp2)
        
        while len(temp2) < n:
            temp2 = " " + temp2
        result.append(temp2)
    return result
        

def solution(n, arr1, arr2):
    answer = []
    
    map1 = int_ary_to_binary_ary(arr1,n)
    map2 = int_ary_to_binary_ary(arr2,n)
    sharp_arr = check_sharp(map1,n)
    answer = sum_sharp(map2,sharp_arr,n)

    
    return answer