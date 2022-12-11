def one_score(hand: str) -> int:
    return "ABC".index(hand)


def match_score(one: str, two: str) -> int:
    if two == 'X':
        return (1 + (one_score(one) + 2) % 3)
    elif two == 'Y':
        return (1 + one_score(one)) + 3
    else:
        return (1 + (one_score(one) + 1) % 3) + 6


with open("input.txt", "r") as input_file:
    lines = input_file.readlines()
    score = 0
    for line in lines:
        one, two = line.strip().split()
        score += match_score(one, two)
    print(score)
