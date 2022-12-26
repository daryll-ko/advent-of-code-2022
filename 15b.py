LIMIT = 4 * 10 ** 6

possible_ranges = [[(0, LIMIT)] for _ in range(LIMIT + 1)]


def cut_range(i: int, range: tuple[int, int]) -> None:
    l1, r1 = range
    global possible_ranges
    new_ranges = []
    for l2, r2 in possible_ranges[i]:
        if r2 < l1 or r1 < l2:
            new_ranges.append((l2, r2))
            continue
        if l1 <= l2 <= r2 <= r1:
            continue
        elif l1 <= l2 <= r1:
            if r1 + 1 <= r2:
                new_ranges.append((r1 + 1, r2))
        elif l1 <= r2 <= r1:
            if l2 <= l1 - 1:
                new_ranges.append((l2, l1 - 1))
        if l2 <= l1 <= r1 <= r2:
            if l2 <= l1 - 1:
                new_ranges.append((l2, l1 - 1))
            if r1 + 1 <= r2:
                new_ranges.append((r1 + 1, r2))
        elif l2 <= l1 <= r2:
            if l2 <= l1 - 1:
                new_ranges.append((l2, l1 - 1))
        elif l2 <= r1 <= r2:
            if r1 + 1 <= r2:
                new_ranges.append((r1 + 1, r2))
    possible_ranges[i] = list(set(new_ranges))


with open("input.txt", "r") as input_file:
    lines = input_file.readlines()
    for line in lines:
        args = line.strip().split()
        j1, i1 = int(args[2][2:-1]), int(args[3][2:-1])  # センサー
        j2, i2 = int(args[8][2:-1]), int(args[9][2:])  # ビーコン
        if 0 <= j1 <= LIMIT:
            cut_range(i1, (j1, j1))
        if 0 <= j2 <= LIMIT:
            cut_range(i2, (j2, j2))
        for i in range(0, LIMIT + 1):
            left = abs(j1 - j2) + abs(i1 - i2) - abs(i1 - i)
            # (j1-left, j1+left) をカットする
            if left >= 0:
                cut_range(i, (max(0, j1 - left), min(LIMIT, j1 + left)))

for i in range(LIMIT + 1):
    if len(possible_ranges[i]) == 1:
        j, _ = possible_ranges[i][0]
        print(4 * 10 ** 6 * j + i)
        exit()
