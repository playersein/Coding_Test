def solution(s):
    result = []
    
    if len(s) == 4 or len(s) == 6:
        for a in s:
            if a in [str(i) for i in range(0,10)]:
                result.append(a)
        if len(result) == len(s):
            return True
        return False