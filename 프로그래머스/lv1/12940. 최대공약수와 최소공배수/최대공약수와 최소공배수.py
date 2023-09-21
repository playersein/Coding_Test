def solution(n, m):
    answer = []
    max_num = []
    min_num = []

    
    for a in range(1, min(n,m)+1):
        if n % a ==0 and m % a ==0:
            max_num.append(a)
    for b in range(max(n,m),(n*m)+1):
        if b % n ==0 and b % m ==0:
            min_num.append(b)

    max_divi = max(max_num)
    min_mult = min(min_num)
    

    return [max_divi, min_mult]

