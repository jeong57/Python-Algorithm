import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    n_dict = {2:0, 3:0, 5:0, 7:0, 11:0}
    while N > 1:
        for key in n_dict.keys():
            if N % key == 0:
                n_dict[key] += 1
                N = N // key
    print(f'#{tc}', end=' ')
    for value in n_dict.values():
        print(value, end=' ')
    print()