def solution(absolutes, signs):
    answer = 0
    for a in range(len(signs)):
        if signs[a] is True:
            answer += absolutes[a]
        else:
            answer -= absolutes[a]                
    return answer

# 절댓값 리스트에서 a번째 원소 num을 하나씩 꺼낼 때 
# signs 리스트에서 a번째 원소가 true이면 sum에 num을 더하고,
#                         false면, sum에 num을 빼고