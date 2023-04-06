import sys

sys.setrecursionlimit(10**4)

Position = tuple[int, int, int]


def surface_area(l: list[Position]) -> int:
    xy_occupied = [set([]) for _ in range(50)]
    yz_occupied = [set([]) for _ in range(50)]
    zx_occupied = [set([]) for _ in range(50)]
    for x, y, z in l:
        xy_occupied[z].add((x, y))
        yz_occupied[x].add((y, z))
        zx_occupied[y].add((z, x))
        answer = 0
    for x, y, z in l:
        current = 6
        if (x, y) in xy_occupied[z - 1]:
            current -= 1
        if (x, y) in xy_occupied[z + 1]:
            current -= 1
        if (y, z) in yz_occupied[x - 1]:
            current -= 1
        if (y, z) in yz_occupied[x + 1]:
            current -= 1
        if (z, x) in zx_occupied[y - 1]:
            current -= 1
        if (z, x) in zx_occupied[y + 1]:
            current -= 1
        answer += current
    return answer


N = 20

DX = [1, -1, 0, 0, 0, 0]
DY = [0, 0, 1, -1, 0, 0]
DZ = [0, 0, 0, 0, 1, -1]

droplet = []
droplet_set = set([])
visited = set([])

with open("input.txt", "r") as input_file:
    lines = input_file.readlines()
    for line in lines:
        x, y, z = map(int, line.strip().split(","))
        droplet.append((x, y, z))
        droplet_set.add((x, y, z))


def within_bounds(current: Position) -> None:
    x, y, z = current
    return 0 <= x < N and 0 <= y < N and 0 <= z < N


def dfs(current: Position, air: bool) -> None:
    visited.add(current)
    x, y, z = current
    for d in range(6):
        x_to, y_to, z_to = x + DX[d], y + DY[d], z + DZ[d]
        if not within_bounds((x_to, y_to, z_to)):
            continue
        if air:
            if (x_to, y_to, z_to) not in droplet_set and (
                x_to,
                y_to,
                z_to,
            ) not in visited:
                dfs((x_to, y_to, z_to), air)
        else:
            if (x_to, y_to, z_to) in droplet_set and (x_to, y_to, z_to) not in visited:
                dfs((x_to, y_to, z_to), air)


for position in droplet:
    if position not in visited:
        dfs(position, False)
dfs((0, 0, 0), True)

l = []
for x in range(N):
    for y in range(N):
        for z in range(N):
            if (x, y, z) not in visited:
                l.append((x, y, z))
print(surface_area(droplet) - surface_area(l))
