from string import ascii_lowercase

def solution(s, n):
    answer = ''
    alphabet_list = list(ascii_lowercase)
    s_list = [string for string in s]        
    # 문장의 문자열을 하나씩 꺼내는 반복문
    for string in s_list:
        if string == " ":
            answer += " "
        elif string.islower():
            # string이 알파벳 리스트에서 몇 번째인지 알아야 함.
            if 0 <= alphabet_list.index(string)+n <= 25:
                answer += alphabet_list[alphabet_list.index(string)+n]
            else: 
                answer += alphabet_list[alphabet_list.index(string)+n - 26]
            

        else:
            if 0 <= alphabet_list.index(string.lower())+n <= 25:
                answer += alphabet_list[alphabet_list.index(string.lower())+n].upper()
            else: 
                answer += alphabet_list[alphabet_list.index(string.lower())+n - 26].upper()
            
    return answer