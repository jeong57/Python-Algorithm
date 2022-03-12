import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())    # N: 테스트 케이스 번호
    lst = list(map(int, input().split()))

    score = [0] * 101
    for i in range(1000):
        score[lst[i]] += 1
    max_value = 0
    final_score = 0
    for i in range(101):
        if score[i] >= max_value:
            max_value = score[i]
            final_score = i
    print(f'#{tc} {final_score}')
