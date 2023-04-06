NO = -(10**18)

tree = [[[], NO, "?"] for _ in range(5000)]  # [children, value, operation]
visited = [False for _ in range(5000)]

to_index = {}
index = 0


def dfs(u: int) -> None:
    global tree
    visited[u] = True
    if tree[u][1] == NO:
        assert tree[u][2] != "?"
        c1 = tree[u][0][0]
        c2 = tree[u][0][1]
        for c in [c1, c2]:
            if not visited[c]:
                dfs(c)
        if tree[u][2] == "+":
            tree[u][1] = tree[c1][1] + tree[c2][1]
        elif tree[u][2] == "-":
            tree[u][1] = tree[c1][1] - tree[c2][1]
        elif tree[u][2] == "*":
            tree[u][1] = tree[c1][1] * tree[c2][1]
        else:
            tree[u][1] = tree[c1][1] // tree[c2][1]


with open("text-files/input.txt") as input_file:
    lines = input_file.readlines()
    for line in lines:
        tokens = line.strip().split()
        name = tokens[0][:-1]
        if name not in to_index:
            to_index[name] = index
            index += 1
        if len(tokens[1:]) == 1:
            value = int(tokens[1])
            tree[to_index[name]][1] = value
        else:
            c1, op, c2 = tokens[1], tokens[2], tokens[3]
            for c in [c1, c2]:
                if c not in to_index:
                    to_index[c] = index
                    index += 1
            tree[to_index[name]][0].append(to_index[c1])
            tree[to_index[name]][0].append(to_index[c2])
            tree[to_index[name]][2] = op
    dfs(to_index["root"])
    print(tree[to_index["root"]][1])
