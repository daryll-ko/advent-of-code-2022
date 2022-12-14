N, M = 10 ** 3, 10 ** 3

cave = [['.' for _ in range(N)] for _ in range(M)]
max_i = -123_456_789

with open("input.txt", "r") as input_file:
    lines = input_file.readlines()
    for line in lines:
        vertices = line.strip().split(" -> ")
        V = len(vertices)
        for k in range(V - 1):
            j1, i1 = map(int, vertices[k].split(','))
            j2, i2 = map(int, vertices[k + 1].split(','))
            max_i = max(max_i, i1, i2)
            if i1 == i2:
                if j1 > j2:
                    j1, j2 = j2, j1
                for j in range(j1, j2 + 1):
                    cave[i1][j] = '#'
            else:
                if i1 > i2:
                    i1, i2 = i2, i1
                for i in range(i1, i2 + 1):
                    cave[i][j1] = '#'

for j in range(M):
    cave[max_i + 2][j] = '#'

answer = 0
while not cave[0][500] == 'o':
    answer += 1
    ci, cj = 0, 500
    done = False
    while not done:
        if not (0 <= ci < N and 0 <= cj < M):
            break
        if ci == N - 1 or cave[ci + 1][cj] == '.':
            if ci == N - 1:
                break
            ci += 1
            continue
        if ci == N - 1 or cj == 0 or cave[ci + 1][cj - 1] == '.':
            if ci == N - 1 or cj == 0:
                break
            ci += 1
            cj -= 1
            continue
        if ci == N - 1 or cj == M - 1 or cave[ci + 1][cj + 1] == '.':
            if ci == N - 1 or cj == M - 1:
                break
            ci += 1
            cj += 1
            continue
        done = True
    cave[ci][cj] = 'o'
print(answer)
