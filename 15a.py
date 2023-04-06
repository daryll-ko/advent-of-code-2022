Y = 2 * 10**6

impossible = [0 for _ in range(2 * 10**7)]

with open("input.txt", "r") as input_file:
    lines = input_file.readlines()
    for line in lines:
        args = line.strip().split()
        j1, i1 = int(args[2][2:-1]), int(args[3][2:-1])  # センサー
        j2, i2 = int(args[8][2:-1]), int(args[9][2:])  # ビーコン
        if i1 == Y:
            impossible[j1 + 10**7] = 1
        if i2 == Y:
            impossible[j2 + 10**7] = -1
        left = abs(j1 - j2) + abs(i1 - i2) - abs(i1 - Y)
        for k in range(j1 - left, j1 + left + 1):
            if impossible[k + 10**7] != -1:
                impossible[k + 10**7] = 1

answer = 0
for j in range(2 * 10**7):
    if impossible[j] == 1:
        answer += 1
print(answer)
