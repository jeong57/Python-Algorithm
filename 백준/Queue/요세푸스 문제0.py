"""
7 3

"""

N, K = map(int, input().split())
q = [i for i in range(1, N+1)]
result = []
front = rear = 0

while len(q) != 1:
    front = (rear + K - 1) % len(q)
    result.append(q.pop(front))
    rear = front

result += q
print('<', end='')
for i in range(len(result)-1):
    print(result[i], end=', ')
print(f'{result[-1]}>')
