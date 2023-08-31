def solution(price, money, count):
    answer = 0
    rate = 0
    for i in range(1, count+1):
        rate += price*i
    if rate > money:
        answer = rate - money
    else:
        answer = 0
    return answer