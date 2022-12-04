with open("input.txt", "r") as input_file:
    lines = input_file.readlines()
    answer = 0
    for line in lines:
        first_range, second_range = line.strip().split(',')
        a, b = map(int, first_range.split('-'))
        c, d = map(int, second_range.split('-'))
        if a <= c <= b or c <= a <= d:
            answer += 1
    print(answer)
