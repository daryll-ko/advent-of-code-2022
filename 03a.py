def get_priority(c: str) -> int:
    if "a" <= c <= "z":
        return 1 + (ord(c) - ord("a"))
    else:
        return 27 + (ord(c) - ord("A"))


with open("input.txt", "r") as input_file:
    lines = input_file.readlines()
    total = 0
    for line in lines:
        n = len(line.strip())
        left, right = set(line[: n // 2]), set(line[n // 2 :])
        in_both = list(left.intersection(right))[0]
        total += get_priority(in_both)
    print(total)
