num = int(input())

for i in range(1, num+1):
    clap = str(i).count('3') + str(i).count('6') + str(i).count('9')
    if clap == 0:
        print(str(i), end = ' ')
    else:
        print('-'*clap, end = ' ')