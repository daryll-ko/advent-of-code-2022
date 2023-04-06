from collections import defaultdict

INF = 10**18

DI = [-1, -1, -1, 1, 1, 1, 0, 0]
#     NW   N  NE  SW   S  SE   W   E
DJ = [-1, 0, 1, -1, 0, 1, -1, 1]

# which indices in DI and DJ do we access?
I = [[0, 1, 2], [3, 4, 5], [0, 6, 3], [2, 7, 5]]

i_to_d = {0: 1, 1: 4, 2: 6, 3: 7}

R = 74
C = 74
ROUNDS = 10**4

grid = [input() for _ in range(R)]
elves = []

for i in range(R):
    for j in range(C):
        if grid[i][j] == "#":
            elves.append((i, j))

i_start = 0
for round in range(ROUNDS):
    elves_set = set(elves)
    new_elves = []
    proposals = defaultdict(lambda: [])
    for i, j in elves:
        alone = True
        for d in range(8):
            i_to, j_to = i + DI[d], j + DJ[d]
            alone &= (i_to, j_to) not in elves_set
        if alone:
            new_elves.append((i, j))
        else:
            done = False
            for i_offset in range(4):
                i_index = (i_start + i_offset) % 4
                free = True
                for d in I[i_index]:
                    i_to, j_to = i + DI[d], j + DJ[d]
                    free &= (i_to, j_to) not in elves_set
                if free:
                    i_to, j_to = i + DI[i_to_d[i_index]], j + DJ[i_to_d[i_index]]
                    proposals[(i_to, j_to)].append((i, j))
                    done = True
                    break
            if not done:
                new_elves.append((i, j))
    for proposal, elf_list in proposals.items():
        if len(elf_list) == 1:
            new_elves.append(proposal)
        else:
            for i, j in elf_list:
                new_elves.append((i, j))
    assert len(elves) == len(new_elves)
    if elves == new_elves:
        print(1 + round)
        exit()
    elves = new_elves
    i_start = (i_start + 1) % 4
