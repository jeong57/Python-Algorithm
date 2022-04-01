"""
2
AAA
AAA

"""

"""
10
ABB
BB
BB
BB
BB
BB
BB
BB
BB
BB

"""

"""
2
GCF
ACDEB

"""
from sys import stdin
input = stdin.readline

N = int(input())
arr = [list(input().rstrip()) for _ in range(N)]
digits = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0,
          'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0,
          'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0,
          'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0,
          'Y': 0, 'Z': 0}

for i in range(N):
    for j in range(len(arr[i])):
        # 각 단어의 알파벳을 key로, 자릿수를 value로 하는 dictionary
        digits[arr[i][j]] += 10**(len(arr[i])-j-1)

result = []
# dictionary의 value들만 모아서 오름차순 정렬 (뒤에서부터 뺄 것)
for value in digits.values():
    if value:
        result.append(value)
result.sort()

total = 0
sup = 9     # 9부터 0까지 차례대로 자릿수에 곱하기
while result:
    num = result.pop()
    total += num * sup
    sup -= 1
print(total)
