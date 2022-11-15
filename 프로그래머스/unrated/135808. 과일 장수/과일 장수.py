def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    N = len(score)
    count = 0
    for i in range(N//m):
        # print(score[i*m+m-1])
        answer += (score[i*m+m-1])*m
    return answer