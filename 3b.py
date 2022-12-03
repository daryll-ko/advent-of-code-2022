def get_priority(c: str) -> int:
    if 'a' <= c <= 'z':
        return 1 + (ord(c) - ord('a'))
    else:
        return 27 + (ord(c) - ord('A'))


with open("input.txt", "r") as input_file:
    lines = list(map(lambda line: line.strip(), input_file.readlines()))
    N = len(lines)
    total = 0
    for i in range(0, N, 3):
        one, two, three = set(lines[i]), set(lines[i + 1]), set(lines[i + 2])
        in_all = list(one.intersection(two).intersection(three))[0]
        total += get_priority(in_all)
    print(total)
