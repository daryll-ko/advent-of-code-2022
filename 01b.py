with open("input.txt", "r") as input_file:
    lines = input_file.readlines()
    current = 0
    amounts = []
    for line in lines:
        if line == "\n":
            amounts.append(current)
            current = 0
        else:
            current += int(line)
    amounts.sort(reverse=True)
    print(sum(amounts[:3]))
