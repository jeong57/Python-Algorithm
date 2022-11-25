x_dots = []
y_dots = []

for i in range(3):
    x, y = map(int, input().split())
    x_dots.append(x)
    y_dots.append(y)

for i in range(3):
    if x_dots.count(x_dots[i]) == 1:
        print(x_dots[i], end=' ')

for i in range(3):
    if y_dots.count(y_dots[i]) == 1:
        print(y_dots[i])