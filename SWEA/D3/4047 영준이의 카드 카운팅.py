import sys
sys.stdin = open('input.txt')


def card_game(numbers):
    result = ''
    for i in range(4):
        cnt = 0
        for j in range(14):
            if numbers[i][j] == 1:
                cnt += 1
            elif numbers[i][j] > 1:
                return 'ERROR'
        if cnt >= 0:
            result += str(13-cnt) + ' '
    return result


T = int(input())
for tc in range(1, T + 1):
    card_type = {'S': 0, 'D': 1, 'H': 2, 'C': 3}
    numbers = [[0]*14 for _ in range(4)]
    s = input()
    for i in range(0, len(s), 3):
        card = s[i]
        number = int(s[i + 1]) * 10 + int(s[i + 2])
        if card in card_type:
            numbers[card_type[card]][number] += 1
    print(f'#{tc} {card_game(numbers)}')
