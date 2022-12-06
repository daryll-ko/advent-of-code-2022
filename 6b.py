with open("input.txt", "r") as input_file:
    line = input_file.readline()
    for i in range(len(line)):
        if i < 14:
            continue
        if len(set(list(line[i-14:i+1]))) == 14:
            print(i + 1)
            break
