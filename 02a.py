def one_score(hand: str) -> int:
    return "ABC".index(hand)


def two_score(hand: str) -> int:
    return "XYZ".index(hand)


def match_score(one: str, two: str) -> int:
    if one_score(one) == (two_score(two) + 2) % 3:
        return (1 + two_score(two)) + 6
    elif one_score(one) == two_score(two):
        return (1 + two_score(two)) + 3
    else:
        return 1 + two_score(two)


with open("input.txt", "r") as input_file:
    lines = input_file.readlines()
    score = 0
    for line in lines:
        one, two = line.strip().split()
        score += match_score(one, two)
    print(score)
