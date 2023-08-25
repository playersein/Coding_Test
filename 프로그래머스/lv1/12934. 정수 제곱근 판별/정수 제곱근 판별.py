import math

def solution(n):
    answer = 0
    if math.sqrt(n) % 1 == 0:
        answer = (n ** (1/2)+1)**2
    else:
        answer = -1
    return answer
    
    
    #     x == n ** (1/2)
    # if x % 1 == 0:
    #     answer =  (x+1) ** 2
    # else:
    #     answer = -1    
    
    # if n == x^2 and x > 0:
    #     answer = (x+1)^2
    #     return answer
    # else:
    #     answer = -1