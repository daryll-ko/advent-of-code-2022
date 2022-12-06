with open("input.txt", "r") as input_file:
    line = input_file.readline()
    for i in range(len(line)):
        if i < 3:
            continue
        if len(set(list(line[i-3:i+1]))) == 4:
            print(i + 1)
            break
