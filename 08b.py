DI = [1, 0, -1, 0]
DJ = [0, 1, 0, -1]

N = 99

grid = [list(map(int, list(input()))) for _ in range(N)]


def in_grid(i: int, j: int) -> bool:
    return 0 <= i < N and 0 <= j < N


best = 0
for i in range(N):
    for j in range(N):
        score = 1
        for d in range(4):
            current = 0
            k = 1
            while in_grid(i + k * DI[d], j + k * DJ[d]) and grid[i + k * DI[d]][j + k * DJ[d]] < grid[i][j]:
                current += 1
                k += 1
            if in_grid(i + k * DI[d], j + k * DJ[d]):
                current += 1
            score *= current
        best = max(best, score)
print(best)
