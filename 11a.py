functions = [
    lambda old: old * 13,
    lambda old: old + 2,
    lambda old: old + 6,
    lambda old: old * old,
    lambda old: old + 3,
    lambda old: old * 7,
    lambda old: old + 4,
    lambda old: old + 7,
]

tests = [
    lambda worry: 3 if worry % 11 == 0 else 2,
    lambda worry: 6 if worry % 7 == 0 else 7,
    lambda worry: 3 if worry % 13 == 0 else 5,
    lambda worry: 4 if worry % 5 == 0 else 5,
    lambda worry: 1 if worry % 3 == 0 else 7,
    lambda worry: 4 if worry % 17 == 0 else 1,
    lambda worry: 2 if worry % 2 == 0 else 0,
    lambda worry: 6 if worry % 19 == 0 else 0,
]

items = [
    [57],
    [58, 93, 88, 81, 72, 73, 65],
    [65, 95],
    [58, 80, 81, 83],
    [58, 89, 90, 96, 55],
    [66, 73, 87, 58, 62, 67],
    [85, 55, 89],
    [73, 80, 54, 94, 90, 52, 69, 58],
]

inspections = [0 for _ in range(8)]

for _ in range(20):
    for i in range(8):
        for item in items[i]:
            inspections[i] += 1
            current = functions[i](item) // 3
            throw_to = tests[i](current)
            items[throw_to].append(current)
        items[i] = []

inspections.sort(reverse=True)
print(inspections[0] * inspections[1])
