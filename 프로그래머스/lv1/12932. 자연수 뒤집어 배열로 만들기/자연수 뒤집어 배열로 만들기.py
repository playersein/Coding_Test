def solution(n):
    answer = []
    n = str(n)
    for a in n:
        answer.append(int(a))
    answer = list(reversed(answer))   # answer = answer[::-1]
    return answer
