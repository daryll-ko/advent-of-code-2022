N = 99

grid = [list(map(int, list(input()))) for _ in range(N)]
visible = [[False for _ in range(N)] for _ in range(N)]

for i in range(N):
    # from left
    current = grid[i][0]
    for j in range(N):
        if j == 0 or grid[i][j] > current:
            visible[i][j] = True
            current = grid[i][j]
    # from right
    current = grid[i][-1]
    for j in range(N - 1, -1, -1):
        if j == N - 1 or grid[i][j] > current:
            visible[i][j] = True
            current = grid[i][j]

for j in range(N):
    # from top
    current = grid[0][j]
    for i in range(N):
        if i == 0 or grid[i][j] > current:
            visible[i][j] = True
            current = grid[i][j]
    # from bottom
    current = grid[-1][j]
    for i in range(N - 1, -1, -1):
        if i == N - 1 or grid[i][j] > current:
            visible[i][j] = True
            current = grid[i][j]

answer = 0
for i in range(N):
    for j in range(N):
        if visible[i][j]:
            answer += 1
print(answer)
