def solution(numbers):
    a = [b for b in range(0,10)]
    for i in range(0, len(numbers)):
        if numbers[i] in a:
            a.remove(numbers[i])
            
    return sum(a)
        