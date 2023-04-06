with open("input.txt", "r") as input_file:
    lines = input_file.readlines()
    current, best = 0, 0
    for line in lines:
        if line == "\n":
            best = max(best, current)
            current = 0
        else:
            current += int(line)
    print(best)
