def solution(arr1, arr2):
    answer = []
    
    
    if not len(arr1) == len(arr2):
        pass
    
    for i in range(len(arr1)):
        if not len(arr1[i]) == len(arr2[i]):
            pass
        else:
            answer1 =[]
            for a in range(len(arr1[i])):
                answer1.append(arr1[i][a] + arr2[i][a])
            answer.append(answer1)
    
    return answer