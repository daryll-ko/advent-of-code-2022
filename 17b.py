from typing import List, Tuple

DI = [0, +1, 0, -1]
DJ = [1, 0, -1, 0]

Rock = List[Tuple[int, int]]

to_direction = {'>': 0, '<': 2}
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
def push_rock(rock: Rock, d: int) -> Tuple[Rock, bool]:
    new_rock = []
    for i, j in rock:
        new_rock.append((i + DI[d], j + DJ[d]))
        if not (1 <= i + DI[d]) or not (0 <= j + DJ[d] < 7) or i + DI[d] in occupied[j + DJ[d]]:
            return rock, d % 2 == 0
    return new_rock, True


to_rock_index = {}

cycle_offset = -1
cycle_length = -1
cycle_found = False


def simulate(rocks: int) -> int:  # returns height
    global occupied, top, cycle_offset, cycle_length, cycle_found
    occupied = [set([]) for _ in range(7)]
    top = 0
    tick = 0
    jet_index = 0
    for r in range(rocks):
        rock = spawn_rock(2, top + 4, r % 5)
        ok = True
        while ok:
            if tick % 2 == 0:
                rock, ok = push_rock(rock, jet_pattern[jet_index])
                jet_index = (jet_index + 1) % len(jet_pattern)
            else:
                rock, ok = push_rock(rock, 3)
            tick ^= 1
        top_10_hash = 0
        for i, j in rock:
            top = max(top, i)
            occupied[j].add(i)
            if top - i < 10:
                top_10_hash += 1 << (j * 10 + (top - i))
        full_hash = (r % 5, jet_index, top_10_hash)
        if not cycle_found and full_hash in to_rock_index and to_rock_index[full_hash] > 100:
            cycle_offset = to_rock_index[full_hash]
            cycle_length = r - to_rock_index[full_hash]
            cycle_found = True
        to_rock_index[full_hash] = r
    return top


simulate(10 ** 4)  # setup cycle values

N = 10 ** 12

A = simulate(cycle_offset)
B = (N - cycle_offset) // cycle_length * \
    (simulate(cycle_offset + cycle_length) - simulate(cycle_offset))
C = simulate(cycle_offset + (N - cycle_offset) % cycle_length) - simulate(cycle_offset)

print(A + B + C)
