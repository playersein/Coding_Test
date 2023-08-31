def solution(left, right):
    answer = 0
    cnt_num = 0
    
    for i in range(left, right+1):
        cnt_num = 0
        for a in range(1,i+1):
            if i % a == 0:
                cnt_num += 1
        if cnt_num % 2 == 0:
            answer += i
        else:
            answer -= i               
    return answer