from itertools import permutations, combinations


def solution(number):
    answer = 0
    num_list = list(combinations(number, 3))
    
    for a in num_list:
        a = list(a)
        if sum(a) == 0:
            answer += 1
            
    
    return answer