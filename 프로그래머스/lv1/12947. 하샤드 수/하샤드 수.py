def solution(x):
    x = str(x)
    sum = 0
    for a in x:
        a = int(a)
        sum += a
    if int(x) % sum == 0:
        answer = True
    else:
        answer = False
    return answer