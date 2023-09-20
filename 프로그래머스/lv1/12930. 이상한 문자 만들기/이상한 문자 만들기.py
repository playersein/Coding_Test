def solution(s):
    answer = []
    blank_num = 0
    string_list = s.split(" ")

    for string in string_list:
        if string == " ":
            answer += " "
        else:
            for i in range(len(string)):
                if i % 2 == 0:
                    answer += string[i].upper()
                else:
                    answer += string[i].lower()
        if blank_num < len(string_list)-1:
            answer += " "
            blank_num += 1
        else:
            pass
    
    
    answer = ''.join(answer)
    return answer