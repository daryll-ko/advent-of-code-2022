from collections import deque

functions = [
    lambda old: old * 13,
    lambda old: old + 2,
    lambda old: old + 6,
    lambda old: old * old,
    lambda old: old + 3,
    lambda old: old * 7,
    lambda old: old + 4,
    lambda old: old + 7
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
    deque([57]),
    deque([58, 93, 88, 81, 72, 73, 65]),
    deque([65, 95]),
    deque([58, 80, 81, 83]),
    deque([58, 89, 90, 96, 55]),
    deque([66, 73, 87, 58, 62, 67]),
    deque([85, 55, 89]),
    deque([73, 80, 54, 94, 90, 52, 69, 58])
]

inspections = [0 for _ in range(8)]

for _ in range(10 ** 4):
    for i in range(8):
        while len(items[i]) > 0:
            item = items[i][0]
            inspections[i] += 1
            current = functions[i](item) % 9699690
            throw_to = tests[i](current)
            items[throw_to].append(current)
            items[i].popleft()

inspections.sort(reverse=True)
print(inspections[0] * inspections[1])
