# these off-by-one errors are the end of me

with open("text-files/input.txt") as input_file:
    lines = input_file.readlines()
    l = list(map(int, lines))
    N = len(l)
    positions = [i for i in range(N)]
    for i in range(N):
        if l[i] == 0:
            continue
        # dear Arceus please make this work
        x = l[i] % (N - 1) - ((N - 1) if l[i] < 0 else 0)
        original = positions[i]
        if l[i] < 0:
            positions[i] += x
            if positions[i] <= 0:
                positions[i] = (positions[i] - 1) % N
                for j in range(N):
                    if j != i and original < positions[j] <= positions[i]:
                        positions[j] = (positions[j] - 1) % N
            else:
                for j in range(N):
                    if j != i and positions[i] <= positions[j] < original:
                        positions[j] = (positions[j] + 1) % N
        else:
            positions[i] += x
            if positions[i] >= N:
                positions[i] = (positions[i] + 1) % N
                for j in range(N):
                    if j != i and positions[i] <= positions[j] < original:
                        positions[j] = (positions[j] + 1) % N
            else:
                for j in range(N):
                    if j != i and original < positions[j] <= positions[i]:
                        positions[j] = (positions[j] - 1) % N
    l_final = [-1 for _ in range(N)]
    for i in range(N):
        l_final[positions[i]] = l[i]
    zero = l_final.index(0)
    print(
        l_final[(zero + 1000) % N]
        + l_final[(zero + 2000) % N]
        + l_final[(zero + 3000) % N]
    )
