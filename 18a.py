xy_occupied = [set([]) for _ in range(50)]
yz_occupied = [set([]) for _ in range(50)]
zx_occupied = [set([]) for _ in range(50)]

l = []

with open("input.txt", "r") as input_file:
    lines = input_file.readlines()
    for line in lines:
        x, y, z = map(int, line.strip().split(","))
        l.append((x, y, z))
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
    print(answer)
