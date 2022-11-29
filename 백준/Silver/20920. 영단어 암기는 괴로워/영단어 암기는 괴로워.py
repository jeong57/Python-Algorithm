import sys
input = sys.stdin.readline

N, M = map(int, input().split())    # N: 단어 개수, M: 길이 기준
words = {}     # result = {'apple': [5, 1, 'apple'],}
for i in range(N):
    word = input().strip()
    if len(word) < M:
        continue
    else:
        if words.get(word):
            words[word][1] += 1
        else:
            words[word] = [len(word), 1, word]

result = sorted(words.items(), key=lambda x: (-x[1][1], -x[1][0], x[1][2]))
for r in result:
    print(r[0])
