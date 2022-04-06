"""
1 2 3 4 5 6 7 8

"""
"""
8 7 6 5 4 3 2 1

"""
"""
8 1 7 2 6 3 5 4

"""

lst = list(map(int, input().split()))
ascend = list(range(1, 9))
descend = list(range(8, 0, -1))
if lst == ascend:
    print('ascending')
elif lst == descend:
    print('descending')
else:
    print('mixed')
