def solution(n):
    answer = 0    
    n = str(n)
    answer =int(''.join(sorted(n, reverse=True)))
    return answer
    
    # for a in n:
    #     a = int(a)
    #     num.append(a)
    #     answer= ''.join(num)
    #     reversed(answer, reverse=True)
    # return answer