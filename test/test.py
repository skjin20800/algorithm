def solution(phone_book):
    phone_book.sort(key=len)   
    phone_dict = {}
    
    
    
    for phone_number in phone_book:
        phone_dict[phone_number] = 1
        
    for phone_number in phone_book:
        temp = ""
        
        for number in phone_number:
            temp += number
            
            if temp in phone_dict and temp != phone_number:           
                return False                                                                    
    return True   

solution(["119", "97674223", "1195524421"])