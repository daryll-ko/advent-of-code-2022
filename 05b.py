crates = [
    ["Z", "T", "F", "R", "W", "J", "G"],
    ["G", "W", "M"],
    ["J", "N", "H", "G"],
    ["J", "R", "C", "N", "W"],
    ["W", "F", "S", "B", "G", "Q", "V", "M"],
    ["S", "R", "T", "D", "V", "W", "C"],
    ["H", "B", "N", "C", "D", "Z", "G", "V"],
    ["S", "J", "N", "M", "G", "C"],
    ["G", "P", "N", "W", "C", "J", "D", "L"],
]

with open("input.txt", "r") as input_file:
    lines = input_file.readlines()
    for line in lines:
        if len(line) >= 4 and line[:4] == "move":
            _, a, _, b, _, c = line.split()
            a, b, c = int(a), int(b), int(c)
            b -= 1
            c -= 1
            for _ in range(a):
                crate = crates[b].pop()
                crates[c].append(crate)
            crates[c][-a:] = reversed(crates[c][-a:])
    for stack in crates:
        print(stack[-1], end="")
    print()
