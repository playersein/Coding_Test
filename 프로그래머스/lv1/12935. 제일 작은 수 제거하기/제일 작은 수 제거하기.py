def solution(arr):
    min_num = min(arr)
    for a in arr:
        if a == min_num:
            arr.remove(a)
            if len(arr) == 0:
                arr.append(-1)
            return arr
    
