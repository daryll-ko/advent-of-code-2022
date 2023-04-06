DI = [0, 1, 0, -1]
DJ = [1, 0, -1, 0]

Rock = list[tuple[int, int]]

to_direction = {">": 0, "<": 2}
jet_pattern = list(map(lambda c: to_direction[c], list(input())))


def spawn_rock(left: int, bottom: int, type: int) -> Rock:
    if type == 0:
        return [
            (bottom, left),
            (bottom, left + 1),
            (bottom, left + 2),
            (bottom, left + 3),
        ]
    elif type == 1:
        return [
            (bottom + 1, left),
            (bottom + 1, left + 1),
            (bottom + 1, left + 2),
            (bottom + 2, left + 1),
            (bottom, left + 1),
        ]
    elif type == 2:
        return [
            (bottom, left),
            (bottom, left + 1),
            (bottom, left + 2),
            (bottom + 1, left + 2),
            (bottom + 2, left + 2),
        ]
    elif type == 3:
        return [
            (bottom, left),
            (bottom + 1, left),
            (bottom + 2, left),
            (bottom + 3, left),
        ]
    elif type == 4:
        return [
            (bottom, left),
            (bottom, left + 1),
            (bottom + 1, left),
            (bottom + 1, left + 1),
        ]


occupied = [set([]) for _ in range(7)]
top = 0


# (new rock, still ok)
def push_rock(rock: Rock, d: int) -> tuple[Rock, bool]:
    new_rock = []
    for i, j in rock:
        new_rock.append((i + DI[d], j + DJ[d]))
        if (
            not (1 <= i + DI[d])
            or not (0 <= j + DJ[d] < 7)
            or i + DI[d] in occupied[j + DJ[d]]
        ):
            return rock, d % 2 == 0
    return new_rock, True


tick = 0
jet_index = 0

for r in range(2022):
    rock = spawn_rock(2, top + 4, r % 5)
    ok = True
    while ok:
        if tick % 2 == 0:
            rock, ok = push_rock(rock, jet_pattern[jet_index])
            jet_index = (jet_index + 1) % len(jet_pattern)
        else:
            rock, ok = push_rock(rock, 3)
        tick ^= 1
    for i, j in rock:
        top = max(top, i)
        occupied[j].add(i)

print(top)
