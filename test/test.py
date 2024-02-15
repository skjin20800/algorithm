def solution(s):
    s = s.lower()
    text_list = s.split(" ")
    answer = ''
    for index, text in enumerate(text_list):
        if(text == ""):
            answer += " "
            continue

        upper = text[0].upper()
        text = upper + text[1:]

        if(len(answer) == 0):
            answer += text
        else:
            answer += " "+ text
    
    return answer

print(solution("a   b"))