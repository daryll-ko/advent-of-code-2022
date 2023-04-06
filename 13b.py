def parse_list(input: str) -> list[str]:
    if input == "[]":
        return []
    elif input[0] != "[":  # 整数
        return [input]
    else:  # リスト
        left = 0
        current = ""
        result = []
        for c in input[1:-1]:
            if c == ",":
                if left == 0:
                    result.append(current)
                    current = ""
                else:
                    current += ","
            elif c == "[":
                left += 1
                current += "["
            elif c == "]":
                left -= 1
                current += "]"
            else:
                current += c
        result.append(current)
        return result


def order(one: str, two: str) -> int:  # 0 OK, 1 NG, 2 引き分け
    one_list, two_list = parse_list(one), parse_list(two)
    N, M = len(one_list), len(two_list)
    i = 0
    while i < min(N, M):
        if one_list[i][0] != "[" and two_list[i][0] != "[":
            a, b = int(one_list[i]), int(two_list[i])
            if a < b:
                return 0
            elif a > b:
                return 1
        else:
            next_order = order(one_list[i], two_list[i])
            if next_order != 2:
                return next_order
        i += 1
    if i == N and i < M:
        return 0
    elif i < N and i == M:
        return 1
    return 2


with open("input.txt", "r") as input_file:
    lines = input_file.readlines()
    N = len(lines)
    packets = ["[[2]]", "[[6]]"]
    for i in range(0, N, 3):
        one, two = lines[i].strip(), lines[i + 1].strip()
        packets.append(one)
        packets.append(two)
    # バブルソート！
    M = len(packets)
    for _ in range(M):
        for i in range(M - 1):
            if order(packets[i], packets[i + 1]) == 1:
                packets[i], packets[i + 1] = packets[i + 1], packets[i]
    a, b = -1, -1
    for i in range(M):
        if packets[i] == "[[2]]":
            a = 1 + i
        elif packets[i] == "[[6]]":
            b = 1 + i
    print(a * b)
